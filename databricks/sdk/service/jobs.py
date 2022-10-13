# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List

__all__ = [
    
    'AccessControlRequest',
    'AutoScale',
    'AwsAttributes',
    'AwsAttributesAvailability',
    'AwsAttributesEbsVolumeType',
    'AzureAttributes',
    'AzureAttributesAvailability',
    'CancelAllRuns',
    'CancelRun',
    'ClusterInstance',
    'ClusterLogConf',
    'ClusterSpec',
    'ClusterTag',
    'CreateJob',
    'CreateJobFormat',
    'CronSchedule',
    'CronSchedulePauseStatus',
    'DbfsStorageInfo',
    'DeleteJob',
    'DeleteRun',
    'ExportRunOutput',
    'FileStorageInfo',
    'GcpAttributes',
    'GitSnapshot',
    'GitSource',
    'GitSourceGitProvider',
    'GroupName',
    'InitScriptInfo',
    'Job',
    'JobCluster',
    'JobEmailNotifications',
    'JobSettings',
    'JobSettingsFormat',
    'JobTaskSettings',
    'Library',
    'ListRunsResponse',
    'MavenLibrary',
    'NewCluster',
    'NotebookOutput',
    'NotebookTask',
    'PipelineParams',
    'PipelineTask',
    'PythonPyPiLibrary',
    'PythonWheelTask',
    'RCranLibrary',
    'RepairHistoryItem',
    'RepairHistoryItemType',
    'RepairRun',
    'ResetJob',
    'Run',
    'RunLifeCycleState',
    'RunNow',
    'RunNowResponse',
    'RunOutput',
    'RunParameters',
    'RunResultState',
    'RunState',
    'RunSubmitTaskSettings',
    'RunTask',
    'RunType',
    'S3StorageInfo',
    'ServicePrincipalName',
    'SparkConfPair',
    'SparkEnvPair',
    'SparkJarTask',
    'SparkPythonTask',
    'SparkSubmitTask',
    'SubmitRun',
    'SubmitRunResponse',
    'TaskDependenciesItem',
    'TaskDescription',
    'TaskKey',
    'TriggerType',
    'UpdateJob',
    'UserName',
    'ViewItem',
    'ViewType',
    'ViewsToExport',
    'CreateResponse',
    'ExportRunRequest',
    'GetRequest',
    'GetRunOutputRequest',
    'GetRunRequest',
    'ListRequest',
    'ListResponse',
    'ListRunsRequest',
    'ListRunsRunType',
    'RepairRunResponse',
    
    'Jobs',
]

# all definitions in this file are in alphabetical order

@dataclass
class AccessControlRequest:
    
    
    group_name: str = None
    
    permission_level: any /* MISSING TYPE */ = None
    
    service_principal_name: str = None
    
    user_name: str = None

    def as_request(self) -> (dict, dict):
        accessControlRequest_query, accessControlRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.group_name:
            accessControlRequest_body['group_name'] = self.group_name
        if self.permission_level:
            accessControlRequest_body['permission_level'] = self.permission_level
        if self.service_principal_name:
            accessControlRequest_body['service_principal_name'] = self.service_principal_name
        if self.user_name:
            accessControlRequest_body['user_name'] = self.user_name
        
        return accessControlRequest_query, accessControlRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AccessControlRequest':
        return cls(
            group_name=d.get('group_name', None),
            permission_level=d.get('permission_level', None),
            service_principal_name=d.get('service_principal_name', None),
            user_name=d.get('user_name', None),
        )



@dataclass
class AutoScale:
    
    # The maximum number of workers to which the cluster can scale up when
    # overloaded. max_workers must be strictly greater than min_workers.
    max_workers: int = None
    # The minimum number of workers to which the cluster can scale down when
    # underutilized. It is also the initial number of workers the cluster has
    # after creation.
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
    
    # Availability type used for all subsequent nodes past the `first_on_demand`
    # ones. **Note:** If `first_on_demand` is zero, this availability type is
    # used for the entire cluster.
    # 
    # `SPOT`: use spot instances. `ON_DEMAND`: use on-demand instances.
    # `SPOT_WITH_FALLBACK`: preferably use spot instances, but fall back to
    # on-demand instances if spot instances cannot be acquired (for example, if
    # AWS spot prices are too high).
    availability: 'AwsAttributesAvailability' = None
    # The number of volumes launched for each instance. You can choose up to 10
    # volumes. This feature is only enabled for supported node types. Legacy
    # node types cannot specify custom EBS volumes. For node types with no
    # instance store, at least one EBS volume needs to be specified; otherwise,
    # cluster creation fails.
    # 
    # These EBS volumes are mounted at `/ebs0`, `/ebs1`, and etc. Instance store
    # volumes are mounted at `/local_disk0`, `/local_disk1`, and etc.
    # 
    # If EBS volumes are attached, Databricks configures Spark to use only the
    # EBS volumes for scratch storage because heterogeneously sized scratch
    # devices can lead to inefficient disk utilization. If no EBS volumes are
    # attached, Databricks configures Spark to use instance store volumes.
    # 
    # If EBS volumes are specified, then the Spark configuration
    # `spark.local.dir` is overridden.
    ebs_volume_count: int = None
    # The number of IOPS per EBS gp3 volume.
    # 
    # This value must be between 3000 and 16000.
    # 
    # The value of IOPS and throughput is calculated based on AWS documentation
    # to match the maximum performance of a gp2 volume with the same volume
    # size.
    # 
    # For more information, see the [EBS volume limit
    # calculator](https://github.com/awslabs/aws-support-tools/tree/master/EBS/VolumeLimitCalculator).
    ebs_volume_iops: int = None
    # The size of each EBS volume (in GiB) launched for each instance. For
    # general purpose SSD, this value must be within the range 100 - 4096\. For
    # throughput optimized HDD, this value must be within the range 500 - 4096\.
    # Custom EBS volumes cannot be specified for the legacy node types
    # (_memory-optimized_ and _compute-optimized_).
    ebs_volume_size: int = None
    # The throughput per EBS gp3 volume, in MiB per second.
    # 
    # This value must be between 125 and 1000.
    ebs_volume_throughput: int = None
    # The type of EBS volume that is launched with this cluster.
    # 
    # `GENERAL_PURPOSE_SSD`: provision extra storage using AWS gp2 EBS volumes.
    # `THROUGHPUT_OPTIMIZED_HDD`: provision extra storage using AWS st1 volumes.
    ebs_volume_type: 'AwsAttributesEbsVolumeType' = None
    # The first first_on_demand nodes of the cluster are placed on on-demand
    # instances. If this value is greater than 0, the cluster driver node is
    # placed on an on-demand instance. If this value is greater than or equal to
    # the current cluster size, all nodes are placed on on-demand instances. If
    # this value is less than the current cluster size, first_on_demand nodes
    # are placed on on-demand instances and the remainder are placed on
    # `availability` instances. This value does not affect cluster size and
    # cannot be mutated over the lifetime of a cluster.
    first_on_demand: int = None
    # Nodes for this cluster are only be placed on AWS instances with this
    # instance profile. If omitted, nodes are placed on instances without an
    # instance profile. The instance profile must have previously been added to
    # the Databricks environment by an account administrator.
    # 
    # This feature may only be available to certain customer plans.
    instance_profile_arn: str = None
    # The max price for AWS spot instances, as a percentage of the corresponding
    # instance type?s on-demand price. For example, if this field is set to 50,
    # and the cluster needs a new `i3.xlarge` spot instance, then the max price
    # is half of the price of on-demand `i3.xlarge` instances. Similarly, if
    # this field is set to 200, the max price is twice the price of on-demand
    # `i3.xlarge` instances. If not specified, the default value is 100\. When
    # spot instances are requested for this cluster, only spot instances whose
    # max price percentage matches this field is considered. For safety, we
    # enforce this field to be no more than 10000.
    spot_bid_price_percent: int = None
    # Identifier for the availability zone/datacenter in which the cluster
    # resides. You have three options:
    # 
    # **Specify an availability zone as a string**, for example: ?us-west-2a?.
    # The provided availability zone must be in the same region as the
    # Databricks deployment. For example, ?us-west-2a? is not a valid zone ID if
    # the Databricks deployment resides in the ?us-east-1? region.
    # 
    # **Enable automatic availability zone selection (?Auto-AZ?)**, by setting
    # the value ?auto?. Databricks selects the AZ based on available IPs in the
    # workspace subnets and retries in other availability zones if AWS returns
    # insufficient capacity errors.
    # 
    # **Do not specify a value**. If not specified, a default zone is used.
    # 
    # The list of available zones as well as the default value can be found by
    # using the [List zones](..dev-tools/api/latest/clustershtml#list-zones)
    # API.
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
    """Availability type used for all subsequent nodes past the `first_on_demand`
    ones. **Note:** If `first_on_demand` is zero, this availability type is used
    for the entire cluster.
    
    `SPOT`: use spot instances. `ON_DEMAND`: use on-demand instances.
    `SPOT_WITH_FALLBACK`: preferably use spot instances, but fall back to
    on-demand instances if spot instances cannot be acquired (for example, if
    AWS spot prices are too high)."""
    
    ON_DEMAND = 'ON_DEMAND'
    SPOT = 'SPOT'
    SPOT_WITH_FALLBACK = 'SPOT_WITH_FALLBACK'

class AwsAttributesEbsVolumeType(Enum):
    """The type of EBS volume that is launched with this cluster.
    
    `GENERAL_PURPOSE_SSD`: provision extra storage using AWS gp2 EBS volumes.
    `THROUGHPUT_OPTIMIZED_HDD`: provision extra storage using AWS st1 volumes."""
    
    GENERAL_PURPOSE_SSD = 'GENERAL_PURPOSE_SSD'
    THROUGHPUT_OPTIMIZED_HDD = 'THROUGHPUT_OPTIMIZED_HDD'

@dataclass
class AzureAttributes:
    
    # Availability type used for all subsequent nodes past the `first_on_demand`
    # ones.
    # 
    # `SPOT_AZURE`: use spot instances. `ON_DEMAND_AZURE`: use on demand
    # instances. `SPOT_WITH_FALLBACK_AZURE`: preferably use spot instances, but
    # fall back to on-demand instances if spot instances cannot be acquired (for
    # example, if Azure spot prices are too high or out of quota). Does not
    # apply to pool availability.
    availability: 'AzureAttributesAvailability' = None
    # The first `first_on_demand` nodes of the cluster are placed on on-demand
    # instances. This value must be greater than 0, or else cluster creation
    # validation fails. If this value is greater than or equal to the current
    # cluster size, all nodes are placed on on-demand instances. If this value
    # is less than the current cluster size, `first_on_demand` nodes are placed
    # on on-demand instances and the remainder are placed on availability
    # instances. This value does not affect cluster size and cannot be mutated
    # over the lifetime of a cluster.
    first_on_demand: int = None
    # The max bid price used for Azure spot instances. You can set this to
    # greater than or equal to the current spot price. You can also set this to
    # -1 (the default), which specifies that the instance cannot be evicted on
    # the basis of price. The price for the instance is the current price for
    # spot instances or the price for a standard instance. You can view
    # historical pricing and eviction rates in the Azure portal.
    spot_bid_max_price: float = None

    def as_request(self) -> (dict, dict):
        azureAttributes_query, azureAttributes_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.availability:
            azureAttributes_body['availability'] = self.availability.value
        if self.first_on_demand:
            azureAttributes_body['first_on_demand'] = self.first_on_demand
        if self.spot_bid_max_price:
            azureAttributes_body['spot_bid_max_price'] = self.spot_bid_max_price
        
        return azureAttributes_query, azureAttributes_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AzureAttributes':
        return cls(
            availability=AzureAttributesAvailability(d['availability']) if 'availability' in d else None,
            first_on_demand=d.get('first_on_demand', None),
            spot_bid_max_price=d.get('spot_bid_max_price', None),
        )



class AzureAttributesAvailability(Enum):
    """Availability type used for all subsequent nodes past the `first_on_demand`
    ones.
    
    `SPOT_AZURE`: use spot instances. `ON_DEMAND_AZURE`: use on demand
    instances. `SPOT_WITH_FALLBACK_AZURE`: preferably use spot instances, but
    fall back to on-demand instances if spot instances cannot be acquired (for
    example, if Azure spot prices are too high or out of quota). Does not apply
    to pool availability."""
    
    ON_DEMAND_AZURE = 'ON_DEMAND_AZURE'
    SPOT_AZURE = 'SPOT_AZURE'
    SPOT_WITH_FALLBACK_AZURE = 'SPOT_WITH_FALLBACK_AZURE'

@dataclass
class CancelAllRuns:
    
    # The canonical identifier of the job to cancel all runs of. This field is
    # required.
    job_id: int

    def as_request(self) -> (dict, dict):
        cancelAllRuns_query, cancelAllRuns_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.job_id:
            cancelAllRuns_body['job_id'] = self.job_id
        
        return cancelAllRuns_query, cancelAllRuns_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CancelAllRuns':
        return cls(
            job_id=d.get('job_id', None),
        )



@dataclass
class CancelRun:
    
    # This field is required.
    run_id: int

    def as_request(self) -> (dict, dict):
        cancelRun_query, cancelRun_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.run_id:
            cancelRun_body['run_id'] = self.run_id
        
        return cancelRun_query, cancelRun_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CancelRun':
        return cls(
            run_id=d.get('run_id', None),
        )



@dataclass
class ClusterInstance:
    
    # The canonical identifier for the cluster used by a run. This field is
    # always available for runs on existing clusters. For runs on new clusters,
    # it becomes available once the cluster is created. This value can be used
    # to view logs by browsing to `/#setting/sparkui/$cluster_id/driver-logs`.
    # The logs continue to be available after the run completes.
    # 
    # The response won?t include this field if the identifier is not available
    # yet.
    cluster_id: str = None
    # The canonical identifier for the Spark context used by a run. This field
    # is filled in once the run begins execution. This value can be used to view
    # the Spark UI by browsing to
    # `/#setting/sparkui/$cluster_id/$spark_context_id`. The Spark UI continues
    # to be available after the run has completed.
    # 
    # The response won?t include this field if the identifier is not available
    # yet.
    spark_context_id: str = None

    def as_request(self) -> (dict, dict):
        clusterInstance_query, clusterInstance_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.cluster_id:
            clusterInstance_body['cluster_id'] = self.cluster_id
        if self.spark_context_id:
            clusterInstance_body['spark_context_id'] = self.spark_context_id
        
        return clusterInstance_query, clusterInstance_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterInstance':
        return cls(
            cluster_id=d.get('cluster_id', None),
            spark_context_id=d.get('spark_context_id', None),
        )



@dataclass
class ClusterLogConf:
    
    # DBFS location of cluster log. Destination must be provided. For example,
    # `{ "dbfs" : { "destination" : "dbfs:/home/cluster_log" } }`
    dbfs: 'DbfsStorageInfo' = None
    # S3 location of cluster log. `destination` and either `region` or
    # `endpoint` must be provided. For example, `{ "s3": { "destination" :
    # "s3://cluster_log_bucket/prefix", "region" : "us-west-2" } }`
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
class ClusterSpec:
    
    # If existing_cluster_id, the ID of an existing cluster that is used for all
    # runs of this job. When running jobs on an existing cluster, you may need
    # to manually restart the cluster if it stops responding. We suggest running
    # jobs on new clusters for greater reliability.
    existing_cluster_id: str = None
    # An optional list of libraries to be installed on the cluster that executes
    # the job. The default value is an empty list.
    libraries: 'List[Library]' = None
    # If new_cluster, a description of a cluster that is created for each run.
    new_cluster: 'NewCluster' = None

    def as_request(self) -> (dict, dict):
        clusterSpec_query, clusterSpec_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.existing_cluster_id:
            clusterSpec_body['existing_cluster_id'] = self.existing_cluster_id
        if self.libraries:
            clusterSpec_body['libraries'] = [v.as_request()[1] for v in self.libraries]
        if self.new_cluster:
            clusterSpec_body['new_cluster'] = self.new_cluster.as_request()[1]
        
        return clusterSpec_query, clusterSpec_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterSpec':
        return cls(
            existing_cluster_id=d.get('existing_cluster_id', None),
            libraries=[Library.from_dict(v) for v in d['libraries']] if 'libraries' in d else None,
            new_cluster=NewCluster.from_dict(d['new_cluster']) if 'new_cluster' in d else None,
        )



type ClusterTag 'Dict[str,str]'


@dataclass
class CreateJob:
    
    # List of permissions to set on the job.
    access_control_list: 'List[AccessControlRequest]' = None
    # An optional set of email addresses that is notified when runs of this job
    # begin or complete as well as when this job is deleted. The default
    # behavior is to not send any emails.
    email_notifications: 'JobEmailNotifications' = None
    # Used to tell what is the format of the job. This field is ignored in
    # Create/Update/Reset calls. When using the Jobs API 2.1 this value is
    # always set to `"MULTI_TASK"`.
    format: 'CreateJobFormat' = None
    # An optional specification for a remote repository containing the notebooks
    # used by this job's notebook tasks.
    git_source: 'GitSource' = None
    # A list of job cluster specifications that can be shared and reused by
    # tasks of this job. Libraries cannot be declared in a shared job cluster.
    # You must declare dependent libraries in task settings.
    job_clusters: 'List[JobCluster]' = None
    # An optional maximum allowed number of concurrent runs of the job.
    # 
    # Set this value if you want to be able to execute multiple runs of the same
    # job concurrently. This is useful for example if you trigger your job on a
    # frequent schedule and want to allow consecutive runs to overlap with each
    # other, or if you want to trigger multiple runs which differ by their input
    # parameters.
    # 
    # This setting affects only new runs. For example, suppose the job?s
    # concurrency is 4 and there are 4 concurrent active runs. Then setting the
    # concurrency to 3 won?t kill any of the active runs. However, from then on,
    # new runs are skipped unless there are fewer than 3 active runs.
    # 
    # This value cannot exceed 1000\. Setting this value to 0 causes all new
    # runs to be skipped. The default behavior is to allow only 1 concurrent
    # run.
    max_concurrent_runs: int = None
    # An optional name for the job.
    name: str = None
    # An optional periodic schedule for this job. The default behavior is that
    # the job only runs when triggered by clicking ?Run Now? in the Jobs UI or
    # sending an API request to `runNow`.
    schedule: 'CronSchedule' = None
    # A map of tags associated with the job. These are forwarded to the cluster
    # as cluster tags for jobs clusters, and are subject to the same limitations
    # as cluster tags. A maximum of 25 tags can be added to the job.
    tags: 'Dict[str,str]' = None
    # A list of task specifications to be executed by this job.
    tasks: 'List[JobTaskSettings]' = None
    # An optional timeout applied to each run of this job. The default behavior
    # is to have no timeout.
    timeout_seconds: int = None

    def as_request(self) -> (dict, dict):
        createJob_query, createJob_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.access_control_list:
            createJob_body['access_control_list'] = [v.as_request()[1] for v in self.access_control_list]
        if self.email_notifications:
            createJob_body['email_notifications'] = self.email_notifications.as_request()[1]
        if self.format:
            createJob_body['format'] = self.format.value
        if self.git_source:
            createJob_body['git_source'] = self.git_source.as_request()[1]
        if self.job_clusters:
            createJob_body['job_clusters'] = [v.as_request()[1] for v in self.job_clusters]
        if self.max_concurrent_runs:
            createJob_body['max_concurrent_runs'] = self.max_concurrent_runs
        if self.name:
            createJob_body['name'] = self.name
        if self.schedule:
            createJob_body['schedule'] = self.schedule.as_request()[1]
        if self.tags:
            createJob_body['tags'] = self.tags
        if self.tasks:
            createJob_body['tasks'] = [v.as_request()[1] for v in self.tasks]
        if self.timeout_seconds:
            createJob_body['timeout_seconds'] = self.timeout_seconds
        
        return createJob_query, createJob_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateJob':
        return cls(
            access_control_list=[AccessControlRequest.from_dict(v) for v in d['access_control_list']] if 'access_control_list' in d else None,
            email_notifications=JobEmailNotifications.from_dict(d['email_notifications']) if 'email_notifications' in d else None,
            format=CreateJobFormat(d['format']) if 'format' in d else None,
            git_source=GitSource.from_dict(d['git_source']) if 'git_source' in d else None,
            job_clusters=[JobCluster.from_dict(v) for v in d['job_clusters']] if 'job_clusters' in d else None,
            max_concurrent_runs=d.get('max_concurrent_runs', None),
            name=d.get('name', None),
            schedule=CronSchedule.from_dict(d['schedule']) if 'schedule' in d else None,
            tags=d.get('tags', None),
            tasks=[JobTaskSettings.from_dict(v) for v in d['tasks']] if 'tasks' in d else None,
            timeout_seconds=d.get('timeout_seconds', None),
        )



class CreateJobFormat(Enum):
    """Used to tell what is the format of the job. This field is ignored in
    Create/Update/Reset calls. When using the Jobs API 2.1 this value is always
    set to `"MULTI_TASK"`."""
    
    MULTI_TASK = 'MULTI_TASK'
    SINGLE_TASK = 'SINGLE_TASK'

@dataclass
class CronSchedule:
    
    # A Cron expression using Quartz syntax that describes the schedule for a
    # job. See [Cron
    # Trigger](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html)
    # for details. This field is required.
    quartz_cron_expression: str
    # A Java timezone ID. The schedule for a job is resolved with respect to
    # this timezone. See [Java
    # TimeZone](https://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html)
    # for details. This field is required.
    timezone_id: str
    # Indicate whether this schedule is paused or not.
    pause_status: 'CronSchedulePauseStatus' = None

    def as_request(self) -> (dict, dict):
        cronSchedule_query, cronSchedule_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.pause_status:
            cronSchedule_body['pause_status'] = self.pause_status.value
        if self.quartz_cron_expression:
            cronSchedule_body['quartz_cron_expression'] = self.quartz_cron_expression
        if self.timezone_id:
            cronSchedule_body['timezone_id'] = self.timezone_id
        
        return cronSchedule_query, cronSchedule_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CronSchedule':
        return cls(
            pause_status=CronSchedulePauseStatus(d['pause_status']) if 'pause_status' in d else None,
            quartz_cron_expression=d.get('quartz_cron_expression', None),
            timezone_id=d.get('timezone_id', None),
        )



class CronSchedulePauseStatus(Enum):
    """Indicate whether this schedule is paused or not."""
    
    PAUSED = 'PAUSED'
    UNPAUSED = 'UNPAUSED'

@dataclass
class DbfsStorageInfo:
    
    # DBFS destination. Example: `dbfs:/my/path`
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
class DeleteJob:
    
    # The canonical identifier of the job to delete. This field is required.
    job_id: int

    def as_request(self) -> (dict, dict):
        deleteJob_query, deleteJob_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.job_id:
            deleteJob_body['job_id'] = self.job_id
        
        return deleteJob_query, deleteJob_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteJob':
        return cls(
            job_id=d.get('job_id', None),
        )



@dataclass
class DeleteRun:
    
    # The canonical identifier of the run for which to retrieve the metadata.
    run_id: int = None

    def as_request(self) -> (dict, dict):
        deleteRun_query, deleteRun_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.run_id:
            deleteRun_body['run_id'] = self.run_id
        
        return deleteRun_query, deleteRun_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteRun':
        return cls(
            run_id=d.get('run_id', None),
        )



@dataclass
class ExportRunOutput:
    
    # The exported content in HTML format (one for every view item).
    views: 'List[ViewItem]' = None

    def as_request(self) -> (dict, dict):
        exportRunOutput_query, exportRunOutput_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.views:
            exportRunOutput_body['views'] = [v.as_request()[1] for v in self.views]
        
        return exportRunOutput_query, exportRunOutput_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ExportRunOutput':
        return cls(
            views=[ViewItem.from_dict(v) for v in d['views']] if 'views' in d else None,
        )



@dataclass
class FileStorageInfo:
    
    # File destination. Example: `file:/my/file.sh`
    destination: str = None

    def as_request(self) -> (dict, dict):
        fileStorageInfo_query, fileStorageInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.destination:
            fileStorageInfo_body['destination'] = self.destination
        
        return fileStorageInfo_query, fileStorageInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FileStorageInfo':
        return cls(
            destination=d.get('destination', None),
        )



@dataclass
class GcpAttributes:
    
    # Google service account email address that the cluster uses to authenticate
    # with Google Identity. This field is used for authentication with the
    # [GCS](..data/data-sources/google/gcshtml) and
    # [BigQuery](..data/data-sources/google/bigqueryhtml) data sources.
    google_service_account: str = None
    # Use preemptible executors.
    use_preemptible_executors: bool = None

    def as_request(self) -> (dict, dict):
        gcpAttributes_query, gcpAttributes_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.google_service_account:
            gcpAttributes_body['google_service_account'] = self.google_service_account
        if self.use_preemptible_executors:
            gcpAttributes_body['use_preemptible_executors'] = self.use_preemptible_executors
        
        return gcpAttributes_query, gcpAttributes_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GcpAttributes':
        return cls(
            google_service_account=d.get('google_service_account', None),
            use_preemptible_executors=d.get('use_preemptible_executors', None),
        )



@dataclass
class GitSnapshot:
    """Read-only state of the remote repository at the time the job was run. This
    field is only included on job runs."""
    # Commit that was used to execute the run. If git_branch was specified, this
    # points to the HEAD of the branch at the time of the run; if git_tag was
    # specified, this points to the commit the tag points to.
    used_commit: str = None

    def as_request(self) -> (dict, dict):
        gitSnapshot_query, gitSnapshot_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.used_commit:
            gitSnapshot_body['used_commit'] = self.used_commit
        
        return gitSnapshot_query, gitSnapshot_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GitSnapshot':
        return cls(
            used_commit=d.get('used_commit', None),
        )



@dataclass
class GitSource:
    """An optional specification for a remote repository containing the notebooks
    used by this job's notebook tasks."""
    # Unique identifier of the service used to host the Git repository. The
    # value is case insensitive.
    git_provider: 'GitSourceGitProvider'
    # URL of the repository to be cloned by this job. The maximum length is 300
    # characters.
    git_url: str
    # Name of the branch to be checked out and used by this job. This field
    # cannot be specified in conjunction with git_tag or git_commit. The maximum
    # length is 255 characters.
    git_branch: str = None
    # Commit to be checked out and used by this job. This field cannot be
    # specified in conjunction with git_branch or git_tag. The maximum length is
    # 64 characters.
    git_commit: str = None
    
    git_snapshot: 'GitSnapshot' = None
    # Name of the tag to be checked out and used by this job. This field cannot
    # be specified in conjunction with git_branch or git_commit. The maximum
    # length is 255 characters.
    git_tag: str = None

    def as_request(self) -> (dict, dict):
        gitSource_query, gitSource_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.git_branch:
            gitSource_body['git_branch'] = self.git_branch
        if self.git_commit:
            gitSource_body['git_commit'] = self.git_commit
        if self.git_provider:
            gitSource_body['git_provider'] = self.git_provider.value
        if self.git_snapshot:
            gitSource_body['git_snapshot'] = self.git_snapshot.as_request()[1]
        if self.git_tag:
            gitSource_body['git_tag'] = self.git_tag
        if self.git_url:
            gitSource_body['git_url'] = self.git_url
        
        return gitSource_query, gitSource_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GitSource':
        return cls(
            git_branch=d.get('git_branch', None),
            git_commit=d.get('git_commit', None),
            git_provider=GitSourceGitProvider(d['git_provider']) if 'git_provider' in d else None,
            git_snapshot=GitSnapshot.from_dict(d['git_snapshot']) if 'git_snapshot' in d else None,
            git_tag=d.get('git_tag', None),
            git_url=d.get('git_url', None),
        )



class GitSourceGitProvider(Enum):
    """Unique identifier of the service used to host the Git repository. The value
    is case insensitive."""
    
    awsCodeCommit = 'awsCodeCommit'
    azureDevOpsServices = 'azureDevOpsServices'
    bitbucketCloud = 'bitbucketCloud'
    bitbucketServer = 'bitbucketServer'
    gitHub = 'gitHub'
    gitHubEnterprise = 'gitHubEnterprise'
    gitLab = 'gitLab'
    gitLabEnterpriseEdition = 'gitLabEnterpriseEdition'



@dataclass
class InitScriptInfo:
    
    # S3 location of init script. Destination and either region or endpoint must
    # be provided. For example, `{ "s3": { "destination" :
    # "s3://init_script_bucket/prefix", "region" : "us-west-2" } }`
    S3: 'S3StorageInfo' = None
    # DBFS location of init script. Destination must be provided. For example,
    # `{ "dbfs" : { "destination" : "dbfs:/home/init_script" } }`
    dbfs: 'DbfsStorageInfo' = None
    # File location of init script. Destination must be provided. For example,
    # `{ "file" : { "destination" : "file:/my/local/file.sh" } }`
    file: 'FileStorageInfo' = None

    def as_request(self) -> (dict, dict):
        initScriptInfo_query, initScriptInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.S3:
            initScriptInfo_body['S3'] = self.S3.as_request()[1]
        if self.dbfs:
            initScriptInfo_body['dbfs'] = self.dbfs.as_request()[1]
        if self.file:
            initScriptInfo_body['file'] = self.file.as_request()[1]
        
        return initScriptInfo_query, initScriptInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InitScriptInfo':
        return cls(
            S3=S3StorageInfo.from_dict(d['S3']) if 'S3' in d else None,
            dbfs=DbfsStorageInfo.from_dict(d['dbfs']) if 'dbfs' in d else None,
            file=FileStorageInfo.from_dict(d['file']) if 'file' in d else None,
        )



@dataclass
class Job:
    
    # The time at which this job was created in epoch milliseconds (milliseconds
    # since 1/1/1970 UTC).
    created_time: int = None
    # The creator user name. This field won?t be included in the response if the
    # user has already been deleted.
    creator_user_name: str = None
    # The canonical identifier for this job.
    job_id: int = None
    # Settings for this job and all of its runs. These settings can be updated
    # using the `resetJob` method.
    settings: 'JobSettings' = None

    def as_request(self) -> (dict, dict):
        job_query, job_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.created_time:
            job_body['created_time'] = self.created_time
        if self.creator_user_name:
            job_body['creator_user_name'] = self.creator_user_name
        if self.job_id:
            job_body['job_id'] = self.job_id
        if self.settings:
            job_body['settings'] = self.settings.as_request()[1]
        
        return job_query, job_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Job':
        return cls(
            created_time=d.get('created_time', None),
            creator_user_name=d.get('creator_user_name', None),
            job_id=d.get('job_id', None),
            settings=JobSettings.from_dict(d['settings']) if 'settings' in d else None,
        )



@dataclass
class JobCluster:
    
    # A unique name for the job cluster. This field is required and must be
    # unique within the job. `JobTaskSettings` may refer to this field to
    # determine which cluster to launch for the task execution.
    job_cluster_key: str
    
    new_cluster: 'NewCluster' = None

    def as_request(self) -> (dict, dict):
        jobCluster_query, jobCluster_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.job_cluster_key:
            jobCluster_body['job_cluster_key'] = self.job_cluster_key
        if self.new_cluster:
            jobCluster_body['new_cluster'] = self.new_cluster.as_request()[1]
        
        return jobCluster_query, jobCluster_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobCluster':
        return cls(
            job_cluster_key=d.get('job_cluster_key', None),
            new_cluster=NewCluster.from_dict(d['new_cluster']) if 'new_cluster' in d else None,
        )



@dataclass
class JobEmailNotifications:
    
    # If true, do not send email to recipients specified in `on_failure` if the
    # run is skipped.
    no_alert_for_skipped_runs: bool = None
    # A list of email addresses to be notified when a run unsuccessfully
    # completes. A run is considered to have completed unsuccessfully if it ends
    # with an `INTERNAL_ERROR` `life_cycle_state` or a `SKIPPED`, `FAILED`, or
    # `TIMED_OUT` result_state. If this is not specified on job creation, reset,
    # or update the list is empty, and notifications are not sent.
    on_failure: 'List[str]' = None
    # A list of email addresses to be notified when a run begins. If not
    # specified on job creation, reset, or update, the list is empty, and
    # notifications are not sent.
    on_start: 'List[str]' = None
    # A list of email addresses to be notified when a run successfully
    # completes. A run is considered to have completed successfully if it ends
    # with a `TERMINATED` `life_cycle_state` and a `SUCCESSFUL` result_state. If
    # not specified on job creation, reset, or update, the list is empty, and
    # notifications are not sent.
    on_success: 'List[str]' = None

    def as_request(self) -> (dict, dict):
        jobEmailNotifications_query, jobEmailNotifications_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.no_alert_for_skipped_runs:
            jobEmailNotifications_body['no_alert_for_skipped_runs'] = self.no_alert_for_skipped_runs
        if self.on_failure:
            jobEmailNotifications_body['on_failure'] = [v for v in self.on_failure]
        if self.on_start:
            jobEmailNotifications_body['on_start'] = [v for v in self.on_start]
        if self.on_success:
            jobEmailNotifications_body['on_success'] = [v for v in self.on_success]
        
        return jobEmailNotifications_query, jobEmailNotifications_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobEmailNotifications':
        return cls(
            no_alert_for_skipped_runs=d.get('no_alert_for_skipped_runs', None),
            on_failure=d.get('on_failure', None),
            on_start=d.get('on_start', None),
            on_success=d.get('on_success', None),
        )



@dataclass
class JobSettings:
    
    # An optional set of email addresses that is notified when runs of this job
    # begin or complete as well as when this job is deleted. The default
    # behavior is to not send any emails.
    email_notifications: 'JobEmailNotifications' = None
    # Used to tell what is the format of the job. This field is ignored in
    # Create/Update/Reset calls. When using the Jobs API 2.1 this value is
    # always set to `"MULTI_TASK"`.
    format: 'JobSettingsFormat' = None
    # An optional specification for a remote repository containing the notebooks
    # used by this job's notebook tasks.
    git_source: 'GitSource' = None
    # A list of job cluster specifications that can be shared and reused by
    # tasks of this job. Libraries cannot be declared in a shared job cluster.
    # You must declare dependent libraries in task settings.
    job_clusters: 'List[JobCluster]' = None
    # An optional maximum allowed number of concurrent runs of the job.
    # 
    # Set this value if you want to be able to execute multiple runs of the same
    # job concurrently. This is useful for example if you trigger your job on a
    # frequent schedule and want to allow consecutive runs to overlap with each
    # other, or if you want to trigger multiple runs which differ by their input
    # parameters.
    # 
    # This setting affects only new runs. For example, suppose the job?s
    # concurrency is 4 and there are 4 concurrent active runs. Then setting the
    # concurrency to 3 won?t kill any of the active runs. However, from then on,
    # new runs are skipped unless there are fewer than 3 active runs.
    # 
    # This value cannot exceed 1000\. Setting this value to 0 causes all new
    # runs to be skipped. The default behavior is to allow only 1 concurrent
    # run.
    max_concurrent_runs: int = None
    # An optional name for the job.
    name: str = None
    # An optional periodic schedule for this job. The default behavior is that
    # the job only runs when triggered by clicking ?Run Now? in the Jobs UI or
    # sending an API request to `runNow`.
    schedule: 'CronSchedule' = None
    # A map of tags associated with the job. These are forwarded to the cluster
    # as cluster tags for jobs clusters, and are subject to the same limitations
    # as cluster tags. A maximum of 25 tags can be added to the job.
    tags: 'Dict[str,str]' = None
    # A list of task specifications to be executed by this job.
    tasks: 'List[JobTaskSettings]' = None
    # An optional timeout applied to each run of this job. The default behavior
    # is to have no timeout.
    timeout_seconds: int = None

    def as_request(self) -> (dict, dict):
        jobSettings_query, jobSettings_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.email_notifications:
            jobSettings_body['email_notifications'] = self.email_notifications.as_request()[1]
        if self.format:
            jobSettings_body['format'] = self.format.value
        if self.git_source:
            jobSettings_body['git_source'] = self.git_source.as_request()[1]
        if self.job_clusters:
            jobSettings_body['job_clusters'] = [v.as_request()[1] for v in self.job_clusters]
        if self.max_concurrent_runs:
            jobSettings_body['max_concurrent_runs'] = self.max_concurrent_runs
        if self.name:
            jobSettings_body['name'] = self.name
        if self.schedule:
            jobSettings_body['schedule'] = self.schedule.as_request()[1]
        if self.tags:
            jobSettings_body['tags'] = self.tags
        if self.tasks:
            jobSettings_body['tasks'] = [v.as_request()[1] for v in self.tasks]
        if self.timeout_seconds:
            jobSettings_body['timeout_seconds'] = self.timeout_seconds
        
        return jobSettings_query, jobSettings_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobSettings':
        return cls(
            email_notifications=JobEmailNotifications.from_dict(d['email_notifications']) if 'email_notifications' in d else None,
            format=JobSettingsFormat(d['format']) if 'format' in d else None,
            git_source=GitSource.from_dict(d['git_source']) if 'git_source' in d else None,
            job_clusters=[JobCluster.from_dict(v) for v in d['job_clusters']] if 'job_clusters' in d else None,
            max_concurrent_runs=d.get('max_concurrent_runs', None),
            name=d.get('name', None),
            schedule=CronSchedule.from_dict(d['schedule']) if 'schedule' in d else None,
            tags=d.get('tags', None),
            tasks=[JobTaskSettings.from_dict(v) for v in d['tasks']] if 'tasks' in d else None,
            timeout_seconds=d.get('timeout_seconds', None),
        )



class JobSettingsFormat(Enum):
    """Used to tell what is the format of the job. This field is ignored in
    Create/Update/Reset calls. When using the Jobs API 2.1 this value is always
    set to `"MULTI_TASK"`."""
    
    MULTI_TASK = 'MULTI_TASK'
    SINGLE_TASK = 'SINGLE_TASK'

@dataclass
class JobTaskSettings:
    
    
    task_key: str
    
    depends_on: 'List[TaskDependenciesItem]' = None
    
    description: str = None
    # An optional set of email addresses that is notified when runs of this task
    # begin or complete as well as when this task is deleted. The default
    # behavior is to not send any emails.
    email_notifications: 'JobEmailNotifications' = None
    # If existing_cluster_id, the ID of an existing cluster that is used for all
    # runs of this task. When running tasks on an existing cluster, you may need
    # to manually restart the cluster if it stops responding. We suggest running
    # jobs on new clusters for greater reliability.
    existing_cluster_id: str = None
    # If job_cluster_key, this task is executed reusing the cluster specified in
    # `job.settings.job_clusters`.
    job_cluster_key: str = None
    # An optional list of libraries to be installed on the cluster that executes
    # the task. The default value is an empty list.
    libraries: 'List[Library]' = None
    # An optional maximum number of times to retry an unsuccessful run. A run is
    # considered to be unsuccessful if it completes with the `FAILED`
    # result_state or `INTERNAL_ERROR` `life_cycle_state`. The value -1 means to
    # retry indefinitely and the value 0 means to never retry. The default
    # behavior is to never retry.
    max_retries: int = None
    # An optional minimal interval in milliseconds between the start of the
    # failed run and the subsequent retry run. The default behavior is that
    # unsuccessful runs are immediately retried.
    min_retry_interval_millis: int = None
    # If new_cluster, a description of a cluster that is created for each run.
    new_cluster: 'NewCluster' = None
    # If notebook_task, indicates that this task must run a notebook. This field
    # may not be specified in conjunction with spark_jar_task.
    notebook_task: 'NotebookTask' = None
    # If pipeline_task, indicates that this task must execute a Pipeline.
    pipeline_task: 'PipelineTask' = None
    # If python_wheel_task, indicates that this job must execute a PythonWheel.
    python_wheel_task: 'PythonWheelTask' = None
    # An optional policy to specify whether to retry a task when it times out.
    # The default behavior is to not retry on timeout.
    retry_on_timeout: bool = None
    # If spark_jar_task, indicates that this task must run a JAR.
    spark_jar_task: 'SparkJarTask' = None
    # If spark_python_task, indicates that this task must run a Python file.
    spark_python_task: 'SparkPythonTask' = None
    # If spark_submit_task, indicates that this task must be launched by the
    # spark submit script.
    spark_submit_task: 'SparkSubmitTask' = None
    # An optional timeout applied to each run of this job task. The default
    # behavior is to have no timeout.
    timeout_seconds: int = None

    def as_request(self) -> (dict, dict):
        jobTaskSettings_query, jobTaskSettings_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.depends_on:
            jobTaskSettings_body['depends_on'] = [v.as_request()[1] for v in self.depends_on]
        if self.description:
            jobTaskSettings_body['description'] = self.description
        if self.email_notifications:
            jobTaskSettings_body['email_notifications'] = self.email_notifications.as_request()[1]
        if self.existing_cluster_id:
            jobTaskSettings_body['existing_cluster_id'] = self.existing_cluster_id
        if self.job_cluster_key:
            jobTaskSettings_body['job_cluster_key'] = self.job_cluster_key
        if self.libraries:
            jobTaskSettings_body['libraries'] = [v.as_request()[1] for v in self.libraries]
        if self.max_retries:
            jobTaskSettings_body['max_retries'] = self.max_retries
        if self.min_retry_interval_millis:
            jobTaskSettings_body['min_retry_interval_millis'] = self.min_retry_interval_millis
        if self.new_cluster:
            jobTaskSettings_body['new_cluster'] = self.new_cluster.as_request()[1]
        if self.notebook_task:
            jobTaskSettings_body['notebook_task'] = self.notebook_task.as_request()[1]
        if self.pipeline_task:
            jobTaskSettings_body['pipeline_task'] = self.pipeline_task.as_request()[1]
        if self.python_wheel_task:
            jobTaskSettings_body['python_wheel_task'] = self.python_wheel_task.as_request()[1]
        if self.retry_on_timeout:
            jobTaskSettings_body['retry_on_timeout'] = self.retry_on_timeout
        if self.spark_jar_task:
            jobTaskSettings_body['spark_jar_task'] = self.spark_jar_task.as_request()[1]
        if self.spark_python_task:
            jobTaskSettings_body['spark_python_task'] = self.spark_python_task.as_request()[1]
        if self.spark_submit_task:
            jobTaskSettings_body['spark_submit_task'] = self.spark_submit_task.as_request()[1]
        if self.task_key:
            jobTaskSettings_body['task_key'] = self.task_key
        if self.timeout_seconds:
            jobTaskSettings_body['timeout_seconds'] = self.timeout_seconds
        
        return jobTaskSettings_query, jobTaskSettings_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobTaskSettings':
        return cls(
            depends_on=[TaskDependenciesItem.from_dict(v) for v in d['depends_on']] if 'depends_on' in d else None,
            description=d.get('description', None),
            email_notifications=JobEmailNotifications.from_dict(d['email_notifications']) if 'email_notifications' in d else None,
            existing_cluster_id=d.get('existing_cluster_id', None),
            job_cluster_key=d.get('job_cluster_key', None),
            libraries=[Library.from_dict(v) for v in d['libraries']] if 'libraries' in d else None,
            max_retries=d.get('max_retries', None),
            min_retry_interval_millis=d.get('min_retry_interval_millis', None),
            new_cluster=NewCluster.from_dict(d['new_cluster']) if 'new_cluster' in d else None,
            notebook_task=NotebookTask.from_dict(d['notebook_task']) if 'notebook_task' in d else None,
            pipeline_task=PipelineTask.from_dict(d['pipeline_task']) if 'pipeline_task' in d else None,
            python_wheel_task=PythonWheelTask.from_dict(d['python_wheel_task']) if 'python_wheel_task' in d else None,
            retry_on_timeout=d.get('retry_on_timeout', None),
            spark_jar_task=SparkJarTask.from_dict(d['spark_jar_task']) if 'spark_jar_task' in d else None,
            spark_python_task=SparkPythonTask.from_dict(d['spark_python_task']) if 'spark_python_task' in d else None,
            spark_submit_task=SparkSubmitTask.from_dict(d['spark_submit_task']) if 'spark_submit_task' in d else None,
            task_key=d.get('task_key', None),
            timeout_seconds=d.get('timeout_seconds', None),
        )



@dataclass
class Library:
    
    # If cran, specification of a CRAN library to be installed.
    cran: 'RCranLibrary' = None
    
    egg: str = None
    
    jar: str = None
    # If maven, specification of a Maven library to be installed. For example:
    # `{ "coordinates": "org.jsoup:jsoup:1.7.2" }`
    maven: 'MavenLibrary' = None
    # If pypi, specification of a PyPI library to be installed. Specifying the
    # `repo` field is optional and if not specified, the default pip index is
    # used. For example: `{ "package": "simplejson", "repo":
    # "https://my-repo.com" }`
    pypi: 'PythonPyPiLibrary' = None
    
    whl: str = None

    def as_request(self) -> (dict, dict):
        library_query, library_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.cran:
            library_body['cran'] = self.cran.as_request()[1]
        if self.egg:
            library_body['egg'] = self.egg
        if self.jar:
            library_body['jar'] = self.jar
        if self.maven:
            library_body['maven'] = self.maven.as_request()[1]
        if self.pypi:
            library_body['pypi'] = self.pypi.as_request()[1]
        if self.whl:
            library_body['whl'] = self.whl
        
        return library_query, library_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Library':
        return cls(
            cran=RCranLibrary.from_dict(d['cran']) if 'cran' in d else None,
            egg=d.get('egg', None),
            jar=d.get('jar', None),
            maven=MavenLibrary.from_dict(d['maven']) if 'maven' in d else None,
            pypi=PythonPyPiLibrary.from_dict(d['pypi']) if 'pypi' in d else None,
            whl=d.get('whl', None),
        )



@dataclass
class ListRunsResponse:
    
    # If true, additional runs matching the provided filter are available for
    # listing.
    has_more: bool = None
    # A list of runs, from most recently started to least.
    runs: 'List[Run]' = None

    def as_request(self) -> (dict, dict):
        listRunsResponse_query, listRunsResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.has_more:
            listRunsResponse_body['has_more'] = self.has_more
        if self.runs:
            listRunsResponse_body['runs'] = [v.as_request()[1] for v in self.runs]
        
        return listRunsResponse_query, listRunsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListRunsResponse':
        return cls(
            has_more=d.get('has_more', None),
            runs=[Run.from_dict(v) for v in d['runs']] if 'runs' in d else None,
        )



@dataclass
class MavenLibrary:
    
    # Gradle-style Maven coordinates. For example: `org.jsoup:jsoup:1.7.2`. This
    # field is required.
    coordinates: str
    # List of dependences to exclude. For example: `["slf4j:slf4j",
    # "*:hadoop-client"]`.
    # 
    # Maven dependency exclusions:
    # <https://maven.apache.org/guides/introduction/introduction-to-optional-and-excludes-dependencies.html>.
    exclusions: 'List[str]' = None
    # Maven repo to install the Maven package from. If omitted, both Maven
    # Central Repository and Spark Packages are searched.
    repo: str = None

    def as_request(self) -> (dict, dict):
        mavenLibrary_query, mavenLibrary_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.coordinates:
            mavenLibrary_body['coordinates'] = self.coordinates
        if self.exclusions:
            mavenLibrary_body['exclusions'] = [v for v in self.exclusions]
        if self.repo:
            mavenLibrary_body['repo'] = self.repo
        
        return mavenLibrary_query, mavenLibrary_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'MavenLibrary':
        return cls(
            coordinates=d.get('coordinates', None),
            exclusions=d.get('exclusions', None),
            repo=d.get('repo', None),
        )



@dataclass
class NewCluster:
    
    # This field encodes, through a single value, the resources available to
    # each of the Spark nodes in this cluster. For example, the Spark nodes can
    # be provisioned and optimized for memory or compute intensive workloads A
    # list of available node types can be retrieved by using the [List node
    # types](..dev-tools/api/latest/clustershtml#list-node-types) API call. This
    # field is required.
    node_type_id: str
    # The Spark version of the cluster. A list of available Spark versions can
    # be retrieved by using the [Runtime
    # versions](..dev-tools/api/latest/clustershtml#runtime-versions) API call.
    # This field is required.
    spark_version: str
    # If autoscale, the required parameters to automatically scale clusters up
    # and down based on load.
    autoscale: 'AutoScale' = None
    # Attributes related to clusters running on Amazon Web Services. If not
    # specified at cluster creation, a set of default values is used.
    aws_attributes: 'AwsAttributes' = None
    # Defines attributes such as the instance availability type, node placement,
    # and max bid price. If not specified during cluster creation, a set of
    # default values is used.
    azure_attributes: 'AzureAttributes' = None
    # The configuration for delivering Spark logs to a long-term storage
    # destination. Only one destination can be specified for one cluster. If the
    # conf is given, the logs are delivered to the destination every `5 mins`.
    # The destination of driver logs is `<destination>/<cluster-id>/driver`,
    # while the destination of executor logs is
    # `<destination>/<cluster-id>/executor`.
    cluster_log_conf: 'ClusterLogConf' = None
    
    custom_tags: 'Dict[str,str]' = None
    # The optional ID of the instance pool to use for the driver node. You must
    # also specify `instance_pool_id`. Refer to [Instance Pools
    # API](..dev-tools/api/latest/instance-poolshtml) for details.
    driver_instance_pool_id: str = None
    # The node type of the Spark driver. This field is optional; if unset, the
    # driver node type is set as the same value as `node_type_id` defined above.
    driver_node_type_id: str = None
    
    enable_elastic_disk: bool = None
    # Attributes related to clusters running on Google Cloud. If not specified
    # at cluster creation, a set of default values is used.
    gcp_attributes: 'GcpAttributes' = None
    # The configuration for storing init scripts. Any number of scripts can be
    # specified. The scripts are executed sequentially in the order provided. If
    # `cluster_log_conf` is specified, init script logs are sent to
    # `<destination>/<cluster-id>/init_scripts`.
    init_scripts: 'List[InitScriptInfo]' = None
    # The optional ID of the instance pool to use for cluster nodes. If
    # `driver_instance_pool_id` is present, `instance_pool_id` is used for
    # worker nodes only. Otherwise, it is used for both the driver node and
    # worker nodes. Refer to [Instance Pools
    # API](..dev-tools/api/latest/instance-poolshtml) for details.
    instance_pool_id: str = None
    # If num_workers, number of worker nodes that this cluster must have. A
    # cluster has one Spark driver and num_workers executors for a total of
    # num_workers + 1 Spark nodes. When reading the properties of a cluster,
    # this field reflects the desired number of workers rather than the actual
    # current number of workers. For example, if a cluster is resized from 5 to
    # 10 workers, this field immediately updates to reflect the target size of
    # 10 workers, whereas the workers listed in `spark_info` gradually increase
    # from 5 to 10 as the new nodes are provisioned.
    num_workers: int = None
    # A [cluster policy](..dev-tools/api/latest/policieshtml) ID.
    policy_id: str = None
    # An object containing a set of optional, user-specified Spark configuration
    # key-value pairs. You can also pass in a string of extra JVM options to the
    # driver and the executors via `spark.driver.extraJavaOptions` and
    # `spark.executor.extraJavaOptions` respectively.
    # 
    # Example Spark confs: `{"spark.speculation": true,
    # "spark.streaming.ui.retainedBatches": 5}` or
    # `{"spark.driver.extraJavaOptions": "-verbose:gc -XX:+PrintGCDetails"}`
    spark_conf: 'Dict[str,any /* MISSING TYPE */]' = None
    # An object containing a set of optional, user-specified environment
    # variable key-value pairs. Key-value pair of the form (X,Y) are exported as
    # is (for example, `export X='Y'`) while launching the driver and workers.
    # 
    # To specify an additional set of `SPARK_DAEMON_JAVA_OPTS`, we recommend
    # appending them to `$SPARK_DAEMON_JAVA_OPTS` as shown in the following
    # example. This ensures that all default databricks managed environmental
    # variables are included as well.
    # 
    # Example Spark environment variables: `{"SPARK_WORKER_MEMORY": "28000m",
    # "SPARK_LOCAL_DIRS": "/local_disk0"}` or `{"SPARK_DAEMON_JAVA_OPTS":
    # "$SPARK_DAEMON_JAVA_OPTS -Dspark.shuffle.service.enabled=true"}`
    spark_env_vars: 'Dict[str,any /* MISSING TYPE */]' = None
    
    ssh_public_keys: 'List[str]' = None

    def as_request(self) -> (dict, dict):
        newCluster_query, newCluster_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.autoscale:
            newCluster_body['autoscale'] = self.autoscale.as_request()[1]
        if self.aws_attributes:
            newCluster_body['aws_attributes'] = self.aws_attributes.as_request()[1]
        if self.azure_attributes:
            newCluster_body['azure_attributes'] = self.azure_attributes.as_request()[1]
        if self.cluster_log_conf:
            newCluster_body['cluster_log_conf'] = self.cluster_log_conf.as_request()[1]
        if self.custom_tags:
            newCluster_body['custom_tags'] = self.custom_tags
        if self.driver_instance_pool_id:
            newCluster_body['driver_instance_pool_id'] = self.driver_instance_pool_id
        if self.driver_node_type_id:
            newCluster_body['driver_node_type_id'] = self.driver_node_type_id
        if self.enable_elastic_disk:
            newCluster_body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.gcp_attributes:
            newCluster_body['gcp_attributes'] = self.gcp_attributes.as_request()[1]
        if self.init_scripts:
            newCluster_body['init_scripts'] = [v.as_request()[1] for v in self.init_scripts]
        if self.instance_pool_id:
            newCluster_body['instance_pool_id'] = self.instance_pool_id
        if self.node_type_id:
            newCluster_body['node_type_id'] = self.node_type_id
        if self.num_workers:
            newCluster_body['num_workers'] = self.num_workers
        if self.policy_id:
            newCluster_body['policy_id'] = self.policy_id
        if self.spark_conf:
            newCluster_body['spark_conf'] = self.spark_conf
        if self.spark_env_vars:
            newCluster_body['spark_env_vars'] = self.spark_env_vars
        if self.spark_version:
            newCluster_body['spark_version'] = self.spark_version
        if self.ssh_public_keys:
            newCluster_body['ssh_public_keys'] = [v for v in self.ssh_public_keys]
        
        return newCluster_query, newCluster_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NewCluster':
        return cls(
            autoscale=AutoScale.from_dict(d['autoscale']) if 'autoscale' in d else None,
            aws_attributes=AwsAttributes.from_dict(d['aws_attributes']) if 'aws_attributes' in d else None,
            azure_attributes=AzureAttributes.from_dict(d['azure_attributes']) if 'azure_attributes' in d else None,
            cluster_log_conf=ClusterLogConf.from_dict(d['cluster_log_conf']) if 'cluster_log_conf' in d else None,
            custom_tags=d.get('custom_tags', None),
            driver_instance_pool_id=d.get('driver_instance_pool_id', None),
            driver_node_type_id=d.get('driver_node_type_id', None),
            enable_elastic_disk=d.get('enable_elastic_disk', None),
            gcp_attributes=GcpAttributes.from_dict(d['gcp_attributes']) if 'gcp_attributes' in d else None,
            init_scripts=[InitScriptInfo.from_dict(v) for v in d['init_scripts']] if 'init_scripts' in d else None,
            instance_pool_id=d.get('instance_pool_id', None),
            node_type_id=d.get('node_type_id', None),
            num_workers=d.get('num_workers', None),
            policy_id=d.get('policy_id', None),
            spark_conf=d.get('spark_conf', None),
            spark_env_vars=d.get('spark_env_vars', None),
            spark_version=d.get('spark_version', None),
            ssh_public_keys=d.get('ssh_public_keys', None),
        )



@dataclass
class NotebookOutput:
    
    # The value passed to
    # [dbutils.notebook.exit()](..notebooks/notebook-workflowshtml#notebook-workflows-exit).
    # jobs restricts this API to return the first 5 MB of the value. For a
    # larger result, your job can store the results in a cloud storage service.
    # This field is absent if `dbutils.notebook.exit()` was never called.
    result: str = None
    # Whether or not the result was truncated.
    truncated: bool = None

    def as_request(self) -> (dict, dict):
        notebookOutput_query, notebookOutput_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.result:
            notebookOutput_body['result'] = self.result
        if self.truncated:
            notebookOutput_body['truncated'] = self.truncated
        
        return notebookOutput_query, notebookOutput_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NotebookOutput':
        return cls(
            result=d.get('result', None),
            truncated=d.get('truncated', None),
        )



@dataclass
class NotebookTask:
    
    # The path of the notebook to be run in the jobs workspace or remote
    # repository. For notebooks stored in the Databricks workspace, the path
    # must be absolute and begin with a slash. For notebooks stored in a remote
    # repository, the path must be relative. This field is required.
    notebook_path: str
    # Base parameters to be used for each run of this job. If the run is
    # initiated by a call to
    # [`run-now`](..dev-tools/api/latest/jobshtml#operation/JobsRunNow) with
    # parameters specified, the two parameters maps are merged. If the same key
    # is specified in `base_parameters` and in `run-now`, the value from
    # `run-now` is used.
    # 
    # Use [Task parameter variables](..jobshtml#parameter-variables) to set
    # parameters containing information about job runs.
    # 
    # If the notebook takes a parameter that is not specified in the job?s
    # `base_parameters` or the `run-now` override parameters, the default value
    # from the notebook is used.
    # 
    # Retrieve these parameters in a notebook using
    # [dbutils.widgets.get](..dev-tools/databricks-utilshtml#dbutils-widgets).
    base_parameters: 'Dict[str,any /* MISSING TYPE */]' = None

    def as_request(self) -> (dict, dict):
        notebookTask_query, notebookTask_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.base_parameters:
            notebookTask_body['base_parameters'] = self.base_parameters
        if self.notebook_path:
            notebookTask_body['notebook_path'] = self.notebook_path
        
        return notebookTask_query, notebookTask_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NotebookTask':
        return cls(
            base_parameters=d.get('base_parameters', None),
            notebook_path=d.get('notebook_path', None),
        )



@dataclass
class PipelineParams:
    
    # If true, triggers a full refresh on the delta live table.
    full_refresh: bool = None

    def as_request(self) -> (dict, dict):
        pipelineParams_query, pipelineParams_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.full_refresh:
            pipelineParams_body['full_refresh'] = self.full_refresh
        
        return pipelineParams_query, pipelineParams_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineParams':
        return cls(
            full_refresh=d.get('full_refresh', None),
        )



@dataclass
class PipelineTask:
    
    # If true, a full refresh will be triggered on the delta live table.
    full_refresh: bool = None
    # The full name of the pipeline task to execute.
    pipeline_id: str = None

    def as_request(self) -> (dict, dict):
        pipelineTask_query, pipelineTask_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.full_refresh:
            pipelineTask_body['full_refresh'] = self.full_refresh
        if self.pipeline_id:
            pipelineTask_body['pipeline_id'] = self.pipeline_id
        
        return pipelineTask_query, pipelineTask_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineTask':
        return cls(
            full_refresh=d.get('full_refresh', None),
            pipeline_id=d.get('pipeline_id', None),
        )



@dataclass
class PythonPyPiLibrary:
    
    # The name of the PyPI package to install. An optional exact version
    # specification is also supported. Examples: `simplejson` and
    # `simplejson==3.8.0`. This field is required.
    package: str
    # The repository where the package can be found. If not specified, the
    # default pip index is used.
    repo: str = None

    def as_request(self) -> (dict, dict):
        pythonPyPiLibrary_query, pythonPyPiLibrary_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.package:
            pythonPyPiLibrary_body['package'] = self.package
        if self.repo:
            pythonPyPiLibrary_body['repo'] = self.repo
        
        return pythonPyPiLibrary_query, pythonPyPiLibrary_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PythonPyPiLibrary':
        return cls(
            package=d.get('package', None),
            repo=d.get('repo', None),
        )



@dataclass
class PythonWheelTask:
    
    # Named entry point to use, if it does not exist in the metadata of the
    # package it executes the function from the package directly using
    # `$packageName.$entryPoint()`
    entry_point: str = None
    # Command-line parameters passed to Python wheel task in the form of
    # `["--name=task", "--data=dbfs:/path/to/data.json"]`. Leave it empty if
    # `parameters` is not null.
    named_parameters: any /* MISSING TYPE */ = None
    # Name of the package to execute
    package_name: str = None
    # Command-line parameters passed to Python wheel task. Leave it empty if
    # `named_parameters` is not null.
    parameters: 'List[str]' = None

    def as_request(self) -> (dict, dict):
        pythonWheelTask_query, pythonWheelTask_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.entry_point:
            pythonWheelTask_body['entry_point'] = self.entry_point
        if self.named_parameters:
            pythonWheelTask_body['named_parameters'] = self.named_parameters
        if self.package_name:
            pythonWheelTask_body['package_name'] = self.package_name
        if self.parameters:
            pythonWheelTask_body['parameters'] = [v for v in self.parameters]
        
        return pythonWheelTask_query, pythonWheelTask_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PythonWheelTask':
        return cls(
            entry_point=d.get('entry_point', None),
            named_parameters=d.get('named_parameters', None),
            package_name=d.get('package_name', None),
            parameters=d.get('parameters', None),
        )



@dataclass
class RCranLibrary:
    
    # The name of the CRAN package to install. This field is required.
    package: str
    # The repository where the package can be found. If not specified, the
    # default CRAN repo is used.
    repo: str = None

    def as_request(self) -> (dict, dict):
        rCranLibrary_query, rCranLibrary_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.package:
            rCranLibrary_body['package'] = self.package
        if self.repo:
            rCranLibrary_body['repo'] = self.repo
        
        return rCranLibrary_query, rCranLibrary_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RCranLibrary':
        return cls(
            package=d.get('package', None),
            repo=d.get('repo', None),
        )



@dataclass
class RepairHistoryItem:
    
    # The end time of the (repaired) run.
    end_time: int = None
    # The ID of the repair. Only returned for the items that represent a repair
    # in `repair_history`.
    id: int = None
    # The start time of the (repaired) run.
    start_time: int = None
    
    state: 'RunState' = None
    # The run IDs of the task runs that ran as part of this repair history item.
    task_run_ids: 'List[int]' = None
    # The repair history item type. Indicates whether a run is the original run
    # or a repair run.
    type: 'RepairHistoryItemType' = None

    def as_request(self) -> (dict, dict):
        repairHistoryItem_query, repairHistoryItem_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.end_time:
            repairHistoryItem_body['end_time'] = self.end_time
        if self.id:
            repairHistoryItem_body['id'] = self.id
        if self.start_time:
            repairHistoryItem_body['start_time'] = self.start_time
        if self.state:
            repairHistoryItem_body['state'] = self.state.as_request()[1]
        if self.task_run_ids:
            repairHistoryItem_body['task_run_ids'] = [v for v in self.task_run_ids]
        if self.type:
            repairHistoryItem_body['type'] = self.type.value
        
        return repairHistoryItem_query, repairHistoryItem_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RepairHistoryItem':
        return cls(
            end_time=d.get('end_time', None),
            id=d.get('id', None),
            start_time=d.get('start_time', None),
            state=RunState.from_dict(d['state']) if 'state' in d else None,
            task_run_ids=d.get('task_run_ids', None),
            type=RepairHistoryItemType(d['type']) if 'type' in d else None,
        )



class RepairHistoryItemType(Enum):
    """The repair history item type. Indicates whether a run is the original run or
    a repair run."""
    
    ORIGINAL = 'ORIGINAL'
    REPAIR = 'REPAIR'

@dataclass
class RepairRun:
    
    # A list of parameters for jobs with Spark JAR tasks, for example
    # `"jar_params": ["john doe", "35"]`. The parameters are used to invoke the
    # main function of the main class specified in the Spark JAR task. If not
    # specified upon `run-now`, it defaults to an empty list. jar_params cannot
    # be specified in conjunction with notebook_params. The JSON representation
    # of this field (for example `{"jar_params":["john doe","35"]}`) cannot
    # exceed 10,000 bytes.
    # 
    # Use [Task parameter variables](..jobshtml#parameter-variables) to set
    # parameters containing information about job runs.
    jar_params: 'List[str]' = None
    # The ID of the latest repair. This parameter is not required when repairing
    # a run for the first time, but must be provided on subsequent requests to
    # repair the same run.
    latest_repair_id: int = None
    # A map from keys to values for jobs with notebook task, for example
    # `"notebook_params": {"name": "john doe", "age": "35"}`. The map is passed
    # to the notebook and is accessible through the
    # [dbutils.widgets.get](..dev-tools/databricks-utilshtml#dbutils-widgets)
    # function.
    # 
    # If not specified upon `run-now`, the triggered run uses the job?s base
    # parameters.
    # 
    # notebook_params cannot be specified in conjunction with jar_params.
    # 
    # Use [Task parameter variables](..jobshtml#parameter-variables) to set
    # parameters containing information about job runs.
    # 
    # The JSON representation of this field (for example
    # `{"notebook_params":{"name":"john doe","age":"35"}}`) cannot exceed 10,000
    # bytes.
    notebook_params: 'Dict[str,str]' = None
    
    pipeline_params: 'PipelineParams' = None
    # A map from keys to values for jobs with Python wheel task, for example
    # `"python_named_params": {"name": "task", "data":
    # "dbfs:/path/to/data.json"}`.
    python_named_params: 'Dict[str,str]' = None
    # A list of parameters for jobs with Python tasks, for example
    # `"python_params": ["john doe", "35"]`. The parameters are passed to Python
    # file as command-line parameters. If specified upon `run-now`, it would
    # overwrite the parameters specified in job setting. The JSON representation
    # of this field (for example `{"python_params":["john doe","35"]}`) cannot
    # exceed 10,000 bytes.
    # 
    # Use [Task parameter variables](..jobshtml#parameter-variables) to set
    # parameters containing information about job runs.
    # 
    # Important
    # 
    # These parameters accept only Latin characters (ASCII character set). Using
    # non-ASCII characters returns an error. Examples of invalid, non-ASCII
    # characters are Chinese, Japanese kanjis, and emojis.
    python_params: 'List[str]' = None
    # The task keys of the task runs to repair.
    rerun_tasks: 'List[str]' = None
    # The job run ID of the run to repair. The run must not be in progress.
    run_id: int = None
    # A list of parameters for jobs with spark submit task, for example
    # `"spark_submit_params": ["--class", "org.apache.spark.examples.SparkPi"]`.
    # The parameters are passed to spark-submit script as command-line
    # parameters. If specified upon `run-now`, it would overwrite the parameters
    # specified in job setting. The JSON representation of this field (for
    # example `{"python_params":["john doe","35"]}`) cannot exceed 10,000 bytes.
    # 
    # Use [Task parameter variables](..jobshtml#parameter-variables) to set
    # parameters containing information about job runs.
    # 
    # Important
    # 
    # These parameters accept only Latin characters (ASCII character set). Using
    # non-ASCII characters returns an error. Examples of invalid, non-ASCII
    # characters are Chinese, Japanese kanjis, and emojis.
    spark_submit_params: 'List[str]' = None

    def as_request(self) -> (dict, dict):
        repairRun_query, repairRun_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.jar_params:
            repairRun_body['jar_params'] = [v for v in self.jar_params]
        if self.latest_repair_id:
            repairRun_body['latest_repair_id'] = self.latest_repair_id
        if self.notebook_params:
            repairRun_body['notebook_params'] = self.notebook_params
        if self.pipeline_params:
            repairRun_body['pipeline_params'] = self.pipeline_params.as_request()[1]
        if self.python_named_params:
            repairRun_body['python_named_params'] = self.python_named_params
        if self.python_params:
            repairRun_body['python_params'] = [v for v in self.python_params]
        if self.rerun_tasks:
            repairRun_body['rerun_tasks'] = [v for v in self.rerun_tasks]
        if self.run_id:
            repairRun_body['run_id'] = self.run_id
        if self.spark_submit_params:
            repairRun_body['spark_submit_params'] = [v for v in self.spark_submit_params]
        
        return repairRun_query, repairRun_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RepairRun':
        return cls(
            jar_params=d.get('jar_params', None),
            latest_repair_id=d.get('latest_repair_id', None),
            notebook_params=d.get('notebook_params', None),
            pipeline_params=PipelineParams.from_dict(d['pipeline_params']) if 'pipeline_params' in d else None,
            python_named_params=d.get('python_named_params', None),
            python_params=d.get('python_params', None),
            rerun_tasks=d.get('rerun_tasks', None),
            run_id=d.get('run_id', None),
            spark_submit_params=d.get('spark_submit_params', None),
        )



@dataclass
class ResetJob:
    
    # The canonical identifier of the job to reset. This field is required.
    job_id: int
    # The new settings of the job. These settings completely replace the old
    # settings.
    # 
    # Changes to the field `JobSettings.timeout_seconds` are applied to active
    # runs. Changes to other fields are applied to future runs only.
    new_settings: 'JobSettings' = None

    def as_request(self) -> (dict, dict):
        resetJob_query, resetJob_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.job_id:
            resetJob_body['job_id'] = self.job_id
        if self.new_settings:
            resetJob_body['new_settings'] = self.new_settings.as_request()[1]
        
        return resetJob_query, resetJob_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResetJob':
        return cls(
            job_id=d.get('job_id', None),
            new_settings=JobSettings.from_dict(d['new_settings']) if 'new_settings' in d else None,
        )



@dataclass
class Run:
    
    # The sequence number of this run attempt for a triggered job run. The
    # initial attempt of a run has an attempt_number of 0\. If the initial run
    # attempt fails, and the job has a retry policy (`max_retries` \> 0),
    # subsequent runs are created with an `original_attempt_run_id` of the
    # original attempt?s ID and an incrementing `attempt_number`. Runs are
    # retried only until they succeed, and the maximum `attempt_number` is the
    # same as the `max_retries` value for the job.
    attempt_number: int = None
    # The time in milliseconds it took to terminate the cluster and clean up any
    # associated artifacts. The total duration of the run is the sum of the
    # setup_duration, the execution_duration, and the cleanup_duration.
    cleanup_duration: int = None
    # The cluster used for this run. If the run is specified to use a new
    # cluster, this field is set once the Jobs service has requested a cluster
    # for the run.
    cluster_instance: 'ClusterInstance' = None
    # A snapshot of the job?s cluster specification when this run was created.
    cluster_spec: 'ClusterSpec' = None
    # The creator user name. This field won?t be included in the response if the
    # user has already been deleted.
    creator_user_name: str = None
    # The time at which this run ended in epoch milliseconds (milliseconds since
    # 1/1/1970 UTC). This field is set to 0 if the job is still running.
    end_time: int = None
    # The time in milliseconds it took to execute the commands in the JAR or
    # notebook until they completed, failed, timed out, were cancelled, or
    # encountered an unexpected error.
    execution_duration: int = None
    # An optional specification for a remote repository containing the notebooks
    # used by this job's notebook tasks.
    git_source: 'GitSource' = None
    # A list of job cluster specifications that can be shared and reused by
    # tasks of this job. Libraries cannot be declared in a shared job cluster.
    # You must declare dependent libraries in task settings.
    job_clusters: 'List[JobCluster]' = None
    # The canonical identifier of the job that contains this run.
    job_id: int = None
    # A unique identifier for this job run. This is set to the same value as
    # `run_id`.
    number_in_job: int = None
    # If this run is a retry of a prior run attempt, this field contains the
    # run_id of the original attempt; otherwise, it is the same as the run_id.
    original_attempt_run_id: int = None
    # The parameters used for this run.
    overriding_parameters: 'RunParameters' = None
    # The repair history of the run.
    repair_history: 'List[RepairHistoryItem]' = None
    # The canonical identifier of the run. This ID is unique across all runs of
    # all jobs.
    run_id: int = None
    # An optional name for the run. The maximum allowed length is 4096 bytes in
    # UTF-8 encoding.
    run_name: str = None
    # The URL to the detail page of the run.
    run_page_url: str = None
    
    run_type: 'RunType' = None
    # The cron schedule that triggered this run if it was triggered by the
    # periodic scheduler.
    schedule: 'CronSchedule' = None
    # The time it took to set up the cluster in milliseconds. For runs that run
    # on new clusters this is the cluster creation time, for runs that run on
    # existing clusters this time should be very short.
    setup_duration: int = None
    # The time at which this run was started in epoch milliseconds (milliseconds
    # since 1/1/1970 UTC). This may not be the time when the job task starts
    # executing, for example, if the job is scheduled to run on a new cluster,
    # this is the time the cluster creation call is issued.
    start_time: int = None
    # The result and lifecycle states of the run.
    state: 'RunState' = None
    # The list of tasks performed by the run. Each task has its own `run_id`
    # which you can use to call `JobsGetOutput` to retrieve the run resutls.
    tasks: 'List[RunTask]' = None
    # The type of trigger that fired this run.
    trigger: 'TriggerType' = None

    def as_request(self) -> (dict, dict):
        run_query, run_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.attempt_number:
            run_body['attempt_number'] = self.attempt_number
        if self.cleanup_duration:
            run_body['cleanup_duration'] = self.cleanup_duration
        if self.cluster_instance:
            run_body['cluster_instance'] = self.cluster_instance.as_request()[1]
        if self.cluster_spec:
            run_body['cluster_spec'] = self.cluster_spec.as_request()[1]
        if self.creator_user_name:
            run_body['creator_user_name'] = self.creator_user_name
        if self.end_time:
            run_body['end_time'] = self.end_time
        if self.execution_duration:
            run_body['execution_duration'] = self.execution_duration
        if self.git_source:
            run_body['git_source'] = self.git_source.as_request()[1]
        if self.job_clusters:
            run_body['job_clusters'] = [v.as_request()[1] for v in self.job_clusters]
        if self.job_id:
            run_body['job_id'] = self.job_id
        if self.number_in_job:
            run_body['number_in_job'] = self.number_in_job
        if self.original_attempt_run_id:
            run_body['original_attempt_run_id'] = self.original_attempt_run_id
        if self.overriding_parameters:
            run_body['overriding_parameters'] = self.overriding_parameters.as_request()[1]
        if self.repair_history:
            run_body['repair_history'] = [v.as_request()[1] for v in self.repair_history]
        if self.run_id:
            run_body['run_id'] = self.run_id
        if self.run_name:
            run_body['run_name'] = self.run_name
        if self.run_page_url:
            run_body['run_page_url'] = self.run_page_url
        if self.run_type:
            run_body['run_type'] = self.run_type.value
        if self.schedule:
            run_body['schedule'] = self.schedule.as_request()[1]
        if self.setup_duration:
            run_body['setup_duration'] = self.setup_duration
        if self.start_time:
            run_body['start_time'] = self.start_time
        if self.state:
            run_body['state'] = self.state.as_request()[1]
        if self.tasks:
            run_body['tasks'] = [v.as_request()[1] for v in self.tasks]
        if self.trigger:
            run_body['trigger'] = self.trigger.value
        
        return run_query, run_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Run':
        return cls(
            attempt_number=d.get('attempt_number', None),
            cleanup_duration=d.get('cleanup_duration', None),
            cluster_instance=ClusterInstance.from_dict(d['cluster_instance']) if 'cluster_instance' in d else None,
            cluster_spec=ClusterSpec.from_dict(d['cluster_spec']) if 'cluster_spec' in d else None,
            creator_user_name=d.get('creator_user_name', None),
            end_time=d.get('end_time', None),
            execution_duration=d.get('execution_duration', None),
            git_source=GitSource.from_dict(d['git_source']) if 'git_source' in d else None,
            job_clusters=[JobCluster.from_dict(v) for v in d['job_clusters']] if 'job_clusters' in d else None,
            job_id=d.get('job_id', None),
            number_in_job=d.get('number_in_job', None),
            original_attempt_run_id=d.get('original_attempt_run_id', None),
            overriding_parameters=RunParameters.from_dict(d['overriding_parameters']) if 'overriding_parameters' in d else None,
            repair_history=[RepairHistoryItem.from_dict(v) for v in d['repair_history']] if 'repair_history' in d else None,
            run_id=d.get('run_id', None),
            run_name=d.get('run_name', None),
            run_page_url=d.get('run_page_url', None),
            run_type=RunType(d['run_type']) if 'run_type' in d else None,
            schedule=CronSchedule.from_dict(d['schedule']) if 'schedule' in d else None,
            setup_duration=d.get('setup_duration', None),
            start_time=d.get('start_time', None),
            state=RunState.from_dict(d['state']) if 'state' in d else None,
            tasks=[RunTask.from_dict(v) for v in d['tasks']] if 'tasks' in d else None,
            trigger=TriggerType(d['trigger']) if 'trigger' in d else None,
        )



class RunLifeCycleState(Enum):
    """This describes an enum"""
    
    INTERNAL_ERROR = 'INTERNAL_ERROR'
    PENDING = 'PENDING'
    RUNNING = 'RUNNING'
    SKIPPED = 'SKIPPED'
    TERMINATED = 'TERMINATED'
    TERMINATING = 'TERMINATING'

@dataclass
class RunNow:
    
    # An optional token to guarantee the idempotency of job run requests. If a
    # run with the provided token already exists, the request does not create a
    # new run but returns the ID of the existing run instead. If a run with the
    # provided token is deleted, an error is returned.
    # 
    # If you specify the idempotency token, upon failure you can retry until the
    # request succeeds. Databricks guarantees that exactly one run is launched
    # with that idempotency token.
    # 
    # This token must have at most 64 characters.
    # 
    # For more information, see [How to ensure idempotency for
    # jobs](https://kb.databricks.com/jobs/jobs-idempotency.html).
    idempotency_token: str = None
    # A list of parameters for jobs with Spark JAR tasks, for example
    # `"jar_params": ["john doe", "35"]`. The parameters are used to invoke the
    # main function of the main class specified in the Spark JAR task. If not
    # specified upon `run-now`, it defaults to an empty list. jar_params cannot
    # be specified in conjunction with notebook_params. The JSON representation
    # of this field (for example `{"jar_params":["john doe","35"]}`) cannot
    # exceed 10,000 bytes.
    # 
    # Use [Task parameter variables](..jobshtml#parameter-variables) to set
    # parameters containing information about job runs.
    jar_params: 'List[str]' = None
    # The ID of the job to be executed
    job_id: int = None
    # A map from keys to values for jobs with notebook task, for example
    # `"notebook_params": {"name": "john doe", "age": "35"}`. The map is passed
    # to the notebook and is accessible through the
    # [dbutils.widgets.get](..dev-tools/databricks-utilshtml#dbutils-widgets)
    # function.
    # 
    # If not specified upon `run-now`, the triggered run uses the job?s base
    # parameters.
    # 
    # notebook_params cannot be specified in conjunction with jar_params.
    # 
    # Use [Task parameter variables](..jobshtml#parameter-variables) to set
    # parameters containing information about job runs.
    # 
    # The JSON representation of this field (for example
    # `{"notebook_params":{"name":"john doe","age":"35"}}`) cannot exceed 10,000
    # bytes.
    notebook_params: 'Dict[str,str]' = None
    
    pipeline_params: 'PipelineParams' = None
    # A map from keys to values for jobs with Python wheel task, for example
    # `"python_named_params": {"name": "task", "data":
    # "dbfs:/path/to/data.json"}`.
    python_named_params: 'Dict[str,str]' = None
    # A list of parameters for jobs with Python tasks, for example
    # `"python_params": ["john doe", "35"]`. The parameters are passed to Python
    # file as command-line parameters. If specified upon `run-now`, it would
    # overwrite the parameters specified in job setting. The JSON representation
    # of this field (for example `{"python_params":["john doe","35"]}`) cannot
    # exceed 10,000 bytes.
    # 
    # Use [Task parameter variables](..jobshtml#parameter-variables) to set
    # parameters containing information about job runs.
    # 
    # Important
    # 
    # These parameters accept only Latin characters (ASCII character set). Using
    # non-ASCII characters returns an error. Examples of invalid, non-ASCII
    # characters are Chinese, Japanese kanjis, and emojis.
    python_params: 'List[str]' = None
    # A list of parameters for jobs with spark submit task, for example
    # `"spark_submit_params": ["--class", "org.apache.spark.examples.SparkPi"]`.
    # The parameters are passed to spark-submit script as command-line
    # parameters. If specified upon `run-now`, it would overwrite the parameters
    # specified in job setting. The JSON representation of this field (for
    # example `{"python_params":["john doe","35"]}`) cannot exceed 10,000 bytes.
    # 
    # Use [Task parameter variables](..jobshtml#parameter-variables) to set
    # parameters containing information about job runs.
    # 
    # Important
    # 
    # These parameters accept only Latin characters (ASCII character set). Using
    # non-ASCII characters returns an error. Examples of invalid, non-ASCII
    # characters are Chinese, Japanese kanjis, and emojis.
    spark_submit_params: 'List[str]' = None

    def as_request(self) -> (dict, dict):
        runNow_query, runNow_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.idempotency_token:
            runNow_body['idempotency_token'] = self.idempotency_token
        if self.jar_params:
            runNow_body['jar_params'] = [v for v in self.jar_params]
        if self.job_id:
            runNow_body['job_id'] = self.job_id
        if self.notebook_params:
            runNow_body['notebook_params'] = self.notebook_params
        if self.pipeline_params:
            runNow_body['pipeline_params'] = self.pipeline_params.as_request()[1]
        if self.python_named_params:
            runNow_body['python_named_params'] = self.python_named_params
        if self.python_params:
            runNow_body['python_params'] = [v for v in self.python_params]
        if self.spark_submit_params:
            runNow_body['spark_submit_params'] = [v for v in self.spark_submit_params]
        
        return runNow_query, runNow_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunNow':
        return cls(
            idempotency_token=d.get('idempotency_token', None),
            jar_params=d.get('jar_params', None),
            job_id=d.get('job_id', None),
            notebook_params=d.get('notebook_params', None),
            pipeline_params=PipelineParams.from_dict(d['pipeline_params']) if 'pipeline_params' in d else None,
            python_named_params=d.get('python_named_params', None),
            python_params=d.get('python_params', None),
            spark_submit_params=d.get('spark_submit_params', None),
        )



@dataclass
class RunNowResponse:
    
    # A unique identifier for this job run. This is set to the same value as
    # `run_id`.
    number_in_job: int = None
    # The globally unique ID of the newly triggered run.
    run_id: int = None

    def as_request(self) -> (dict, dict):
        runNowResponse_query, runNowResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.number_in_job:
            runNowResponse_body['number_in_job'] = self.number_in_job
        if self.run_id:
            runNowResponse_body['run_id'] = self.run_id
        
        return runNowResponse_query, runNowResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunNowResponse':
        return cls(
            number_in_job=d.get('number_in_job', None),
            run_id=d.get('run_id', None),
        )



@dataclass
class RunOutput:
    
    # An error message indicating why a task failed or why output is not
    # available. The message is unstructured, and its exact format is subject to
    # change.
    error: str = None
    # If there was an error executing the run, this field contains any available
    # stack traces.
    error_trace: str = None
    # The output from tasks that write to standard streams (stdout/stderr) such
    # as
    # [SparkJarTask](..dev-tools/api/latest/jobshtml#/components/schemas/SparkJarTask),
    # [SparkPythonTask](..dev-tools/api/latest/jobshtml#/components/schemas/SparkPythonTask,
    # [PythonWheelTask](..dev-tools/api/latest/jobshtml#/components/schemas/PythonWheelTask.
    # It's not supported for the
    # [NotebookTask](..dev-tools/api/latest/jobshtml#/components/schemas/NotebookTask,
    # [PipelineTask](..dev-tools/api/latest/jobshtml#/components/schemas/PipelineTask,
    # or
    # [SparkSubmitTask](..dev-tools/api/latest/jobshtml#/components/schemas/SparkSubmitTask.
    # jobs restricts this API to return the last 5 MB of these logs.
    logs: str = None
    # Whether the logs are truncated.
    logs_truncated: bool = None
    # All details of the run except for its output.
    metadata: 'Run' = None
    # The output of a notebook task, if available. A notebook task that
    # terminates (either successfully or with a failure) without calling
    # `dbutils.notebook.exit()` is considered to have an empty output. This
    # field is set but its result value is empty. jobs restricts this API to
    # return the first 5 MB of the output. To return a larger result, use the
    # [ClusterLogConf](..dev-tools/api/latest/clustershtml#clusterlogconf) field
    # to configure log storage for the job cluster.
    notebook_output: 'NotebookOutput' = None

    def as_request(self) -> (dict, dict):
        runOutput_query, runOutput_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.error:
            runOutput_body['error'] = self.error
        if self.error_trace:
            runOutput_body['error_trace'] = self.error_trace
        if self.logs:
            runOutput_body['logs'] = self.logs
        if self.logs_truncated:
            runOutput_body['logs_truncated'] = self.logs_truncated
        if self.metadata:
            runOutput_body['metadata'] = self.metadata.as_request()[1]
        if self.notebook_output:
            runOutput_body['notebook_output'] = self.notebook_output.as_request()[1]
        
        return runOutput_query, runOutput_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunOutput':
        return cls(
            error=d.get('error', None),
            error_trace=d.get('error_trace', None),
            logs=d.get('logs', None),
            logs_truncated=d.get('logs_truncated', None),
            metadata=Run.from_dict(d['metadata']) if 'metadata' in d else None,
            notebook_output=NotebookOutput.from_dict(d['notebook_output']) if 'notebook_output' in d else None,
        )



@dataclass
class RunParameters:
    
    # A list of parameters for jobs with Spark JAR tasks, for example
    # `"jar_params": ["john doe", "35"]`. The parameters are used to invoke the
    # main function of the main class specified in the Spark JAR task. If not
    # specified upon `run-now`, it defaults to an empty list. jar_params cannot
    # be specified in conjunction with notebook_params. The JSON representation
    # of this field (for example `{"jar_params":["john doe","35"]}`) cannot
    # exceed 10,000 bytes.
    # 
    # Use [Task parameter variables](..jobshtml#parameter-variables) to set
    # parameters containing information about job runs.
    jar_params: 'List[str]' = None
    # A map from keys to values for jobs with notebook task, for example
    # `"notebook_params": {"name": "john doe", "age": "35"}`. The map is passed
    # to the notebook and is accessible through the
    # [dbutils.widgets.get](..dev-tools/databricks-utilshtml#dbutils-widgets)
    # function.
    # 
    # If not specified upon `run-now`, the triggered run uses the job?s base
    # parameters.
    # 
    # notebook_params cannot be specified in conjunction with jar_params.
    # 
    # Use [Task parameter variables](..jobshtml#parameter-variables) to set
    # parameters containing information about job runs.
    # 
    # The JSON representation of this field (for example
    # `{"notebook_params":{"name":"john doe","age":"35"}}`) cannot exceed 10,000
    # bytes.
    notebook_params: 'Dict[str,str]' = None
    
    pipeline_params: 'PipelineParams' = None
    # A map from keys to values for jobs with Python wheel task, for example
    # `"python_named_params": {"name": "task", "data":
    # "dbfs:/path/to/data.json"}`.
    python_named_params: 'Dict[str,str]' = None
    # A list of parameters for jobs with Python tasks, for example
    # `"python_params": ["john doe", "35"]`. The parameters are passed to Python
    # file as command-line parameters. If specified upon `run-now`, it would
    # overwrite the parameters specified in job setting. The JSON representation
    # of this field (for example `{"python_params":["john doe","35"]}`) cannot
    # exceed 10,000 bytes.
    # 
    # Use [Task parameter variables](..jobshtml#parameter-variables) to set
    # parameters containing information about job runs.
    # 
    # Important
    # 
    # These parameters accept only Latin characters (ASCII character set). Using
    # non-ASCII characters returns an error. Examples of invalid, non-ASCII
    # characters are Chinese, Japanese kanjis, and emojis.
    python_params: 'List[str]' = None
    # A list of parameters for jobs with spark submit task, for example
    # `"spark_submit_params": ["--class", "org.apache.spark.examples.SparkPi"]`.
    # The parameters are passed to spark-submit script as command-line
    # parameters. If specified upon `run-now`, it would overwrite the parameters
    # specified in job setting. The JSON representation of this field (for
    # example `{"python_params":["john doe","35"]}`) cannot exceed 10,000 bytes.
    # 
    # Use [Task parameter variables](..jobshtml#parameter-variables) to set
    # parameters containing information about job runs.
    # 
    # Important
    # 
    # These parameters accept only Latin characters (ASCII character set). Using
    # non-ASCII characters returns an error. Examples of invalid, non-ASCII
    # characters are Chinese, Japanese kanjis, and emojis.
    spark_submit_params: 'List[str]' = None

    def as_request(self) -> (dict, dict):
        runParameters_query, runParameters_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.jar_params:
            runParameters_body['jar_params'] = [v for v in self.jar_params]
        if self.notebook_params:
            runParameters_body['notebook_params'] = self.notebook_params
        if self.pipeline_params:
            runParameters_body['pipeline_params'] = self.pipeline_params.as_request()[1]
        if self.python_named_params:
            runParameters_body['python_named_params'] = self.python_named_params
        if self.python_params:
            runParameters_body['python_params'] = [v for v in self.python_params]
        if self.spark_submit_params:
            runParameters_body['spark_submit_params'] = [v for v in self.spark_submit_params]
        
        return runParameters_query, runParameters_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunParameters':
        return cls(
            jar_params=d.get('jar_params', None),
            notebook_params=d.get('notebook_params', None),
            pipeline_params=PipelineParams.from_dict(d['pipeline_params']) if 'pipeline_params' in d else None,
            python_named_params=d.get('python_named_params', None),
            python_params=d.get('python_params', None),
            spark_submit_params=d.get('spark_submit_params', None),
        )



class RunResultState(Enum):
    """This describes an enum"""
    
    CANCELED = 'CANCELED'
    FAILED = 'FAILED'
    SUCCESS = 'SUCCESS'
    TIMEDOUT = 'TIMEDOUT'

@dataclass
class RunState:
    """The result and lifecycle state of the run."""
    # A description of a run?s current location in the run lifecycle. This field
    # is always available in the response.
    life_cycle_state: 'RunLifeCycleState' = None
    
    result_state: 'RunResultState' = None
    # A descriptive message for the current state. This field is unstructured,
    # and its exact format is subject to change.
    state_message: str = None
    # Whether a run was canceled manually by a user or by the scheduler because
    # the run timed out.
    user_cancelled_or_timedout: bool = None

    def as_request(self) -> (dict, dict):
        runState_query, runState_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.life_cycle_state:
            runState_body['life_cycle_state'] = self.life_cycle_state.value
        if self.result_state:
            runState_body['result_state'] = self.result_state.value
        if self.state_message:
            runState_body['state_message'] = self.state_message
        if self.user_cancelled_or_timedout:
            runState_body['user_cancelled_or_timedout'] = self.user_cancelled_or_timedout
        
        return runState_query, runState_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunState':
        return cls(
            life_cycle_state=RunLifeCycleState(d['life_cycle_state']) if 'life_cycle_state' in d else None,
            result_state=RunResultState(d['result_state']) if 'result_state' in d else None,
            state_message=d.get('state_message', None),
            user_cancelled_or_timedout=d.get('user_cancelled_or_timedout', None),
        )



@dataclass
class RunSubmitTaskSettings:
    
    
    task_key: str
    
    depends_on: 'List[TaskDependenciesItem]' = None
    # If existing_cluster_id, the ID of an existing cluster that is used for all
    # runs of this task. When running tasks on an existing cluster, you may need
    # to manually restart the cluster if it stops responding. We suggest running
    # jobs on new clusters for greater reliability.
    existing_cluster_id: str = None
    # An optional list of libraries to be installed on the cluster that executes
    # the task. The default value is an empty list.
    libraries: 'List[Library]' = None
    # If new_cluster, a description of a cluster that is created for each run.
    new_cluster: 'NewCluster' = None
    # If notebook_task, indicates that this task must run a notebook. This field
    # may not be specified in conjunction with spark_jar_task.
    notebook_task: 'NotebookTask' = None
    # If pipeline_task, indicates that this task must execute a Pipeline.
    pipeline_task: 'PipelineTask' = None
    # If python_wheel_task, indicates that this job must execute a PythonWheel.
    python_wheel_task: 'PythonWheelTask' = None
    # If spark_jar_task, indicates that this task must run a JAR.
    spark_jar_task: 'SparkJarTask' = None
    # If spark_python_task, indicates that this task must run a Python file.
    spark_python_task: 'SparkPythonTask' = None
    # If spark_submit_task, indicates that this task must be launched by the
    # spark submit script.
    spark_submit_task: 'SparkSubmitTask' = None
    # An optional timeout applied to each run of this job task. The default
    # behavior is to have no timeout.
    timeout_seconds: int = None

    def as_request(self) -> (dict, dict):
        runSubmitTaskSettings_query, runSubmitTaskSettings_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.depends_on:
            runSubmitTaskSettings_body['depends_on'] = [v.as_request()[1] for v in self.depends_on]
        if self.existing_cluster_id:
            runSubmitTaskSettings_body['existing_cluster_id'] = self.existing_cluster_id
        if self.libraries:
            runSubmitTaskSettings_body['libraries'] = [v.as_request()[1] for v in self.libraries]
        if self.new_cluster:
            runSubmitTaskSettings_body['new_cluster'] = self.new_cluster.as_request()[1]
        if self.notebook_task:
            runSubmitTaskSettings_body['notebook_task'] = self.notebook_task.as_request()[1]
        if self.pipeline_task:
            runSubmitTaskSettings_body['pipeline_task'] = self.pipeline_task.as_request()[1]
        if self.python_wheel_task:
            runSubmitTaskSettings_body['python_wheel_task'] = self.python_wheel_task.as_request()[1]
        if self.spark_jar_task:
            runSubmitTaskSettings_body['spark_jar_task'] = self.spark_jar_task.as_request()[1]
        if self.spark_python_task:
            runSubmitTaskSettings_body['spark_python_task'] = self.spark_python_task.as_request()[1]
        if self.spark_submit_task:
            runSubmitTaskSettings_body['spark_submit_task'] = self.spark_submit_task.as_request()[1]
        if self.task_key:
            runSubmitTaskSettings_body['task_key'] = self.task_key
        if self.timeout_seconds:
            runSubmitTaskSettings_body['timeout_seconds'] = self.timeout_seconds
        
        return runSubmitTaskSettings_query, runSubmitTaskSettings_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunSubmitTaskSettings':
        return cls(
            depends_on=[TaskDependenciesItem.from_dict(v) for v in d['depends_on']] if 'depends_on' in d else None,
            existing_cluster_id=d.get('existing_cluster_id', None),
            libraries=[Library.from_dict(v) for v in d['libraries']] if 'libraries' in d else None,
            new_cluster=NewCluster.from_dict(d['new_cluster']) if 'new_cluster' in d else None,
            notebook_task=NotebookTask.from_dict(d['notebook_task']) if 'notebook_task' in d else None,
            pipeline_task=PipelineTask.from_dict(d['pipeline_task']) if 'pipeline_task' in d else None,
            python_wheel_task=PythonWheelTask.from_dict(d['python_wheel_task']) if 'python_wheel_task' in d else None,
            spark_jar_task=SparkJarTask.from_dict(d['spark_jar_task']) if 'spark_jar_task' in d else None,
            spark_python_task=SparkPythonTask.from_dict(d['spark_python_task']) if 'spark_python_task' in d else None,
            spark_submit_task=SparkSubmitTask.from_dict(d['spark_submit_task']) if 'spark_submit_task' in d else None,
            task_key=d.get('task_key', None),
            timeout_seconds=d.get('timeout_seconds', None),
        )



@dataclass
class RunTask:
    
    # The sequence number of this run attempt for a triggered job run. The
    # initial attempt of a run has an attempt_number of 0\. If the initial run
    # attempt fails, and the job has a retry policy (`max_retries` \> 0),
    # subsequent runs are created with an `original_attempt_run_id` of the
    # original attempt?s ID and an incrementing `attempt_number`. Runs are
    # retried only until they succeed, and the maximum `attempt_number` is the
    # same as the `max_retries` value for the job.
    attempt_number: int = None
    # The time in milliseconds it took to terminate the cluster and clean up any
    # associated artifacts. The total duration of the run is the sum of the
    # setup_duration, the execution_duration, and the cleanup_duration.
    cleanup_duration: int = None
    # The cluster used for this run. If the run is specified to use a new
    # cluster, this field is set once the Jobs service has requested a cluster
    # for the run.
    cluster_instance: 'ClusterInstance' = None
    
    depends_on: 'List[TaskDependenciesItem]' = None
    
    description: str = None
    # The time at which this run ended in epoch milliseconds (milliseconds since
    # 1/1/1970 UTC). This field is set to 0 if the job is still running.
    end_time: int = None
    # The time in milliseconds it took to execute the commands in the JAR or
    # notebook until they completed, failed, timed out, were cancelled, or
    # encountered an unexpected error.
    execution_duration: int = None
    # If existing_cluster_id, the ID of an existing cluster that is used for all
    # runs of this job. When running jobs on an existing cluster, you may need
    # to manually restart the cluster if it stops responding. We suggest running
    # jobs on new clusters for greater reliability.
    existing_cluster_id: str = None
    # An optional specification for a remote repository containing the notebooks
    # used by this job's notebook tasks.
    git_source: 'GitSource' = None
    # An optional list of libraries to be installed on the cluster that executes
    # the job. The default value is an empty list.
    libraries: 'List[Library]' = None
    # If new_cluster, a description of a cluster that is created for each run.
    new_cluster: 'NewCluster' = None
    # If notebook_task, indicates that this job must run a notebook. This field
    # may not be specified in conjunction with spark_jar_task.
    notebook_task: 'NotebookTask' = None
    # If pipeline_task, indicates that this job must execute a Pipeline.
    pipeline_task: 'PipelineTask' = None
    # If python_wheel_task, indicates that this job must execute a PythonWheel.
    python_wheel_task: 'PythonWheelTask' = None
    # The ID of the task run.
    run_id: int = None
    # The time it took to set up the cluster in milliseconds. For runs that run
    # on new clusters this is the cluster creation time, for runs that run on
    # existing clusters this time should be very short.
    setup_duration: int = None
    # If spark_jar_task, indicates that this job must run a JAR.
    spark_jar_task: 'SparkJarTask' = None
    # If spark_python_task, indicates that this job must run a Python file.
    spark_python_task: 'SparkPythonTask' = None
    # If spark_submit_task, indicates that this job must be launched by the
    # spark submit script.
    spark_submit_task: 'SparkSubmitTask' = None
    # The time at which this run was started in epoch milliseconds (milliseconds
    # since 1/1/1970 UTC). This may not be the time when the job task starts
    # executing, for example, if the job is scheduled to run on a new cluster,
    # this is the time the cluster creation call is issued.
    start_time: int = None
    # The result and lifecycle states of the run.
    state: 'RunState' = None
    
    task_key: str = None

    def as_request(self) -> (dict, dict):
        runTask_query, runTask_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.attempt_number:
            runTask_body['attempt_number'] = self.attempt_number
        if self.cleanup_duration:
            runTask_body['cleanup_duration'] = self.cleanup_duration
        if self.cluster_instance:
            runTask_body['cluster_instance'] = self.cluster_instance.as_request()[1]
        if self.depends_on:
            runTask_body['depends_on'] = [v.as_request()[1] for v in self.depends_on]
        if self.description:
            runTask_body['description'] = self.description
        if self.end_time:
            runTask_body['end_time'] = self.end_time
        if self.execution_duration:
            runTask_body['execution_duration'] = self.execution_duration
        if self.existing_cluster_id:
            runTask_body['existing_cluster_id'] = self.existing_cluster_id
        if self.git_source:
            runTask_body['git_source'] = self.git_source.as_request()[1]
        if self.libraries:
            runTask_body['libraries'] = [v.as_request()[1] for v in self.libraries]
        if self.new_cluster:
            runTask_body['new_cluster'] = self.new_cluster.as_request()[1]
        if self.notebook_task:
            runTask_body['notebook_task'] = self.notebook_task.as_request()[1]
        if self.pipeline_task:
            runTask_body['pipeline_task'] = self.pipeline_task.as_request()[1]
        if self.python_wheel_task:
            runTask_body['python_wheel_task'] = self.python_wheel_task.as_request()[1]
        if self.run_id:
            runTask_body['run_id'] = self.run_id
        if self.setup_duration:
            runTask_body['setup_duration'] = self.setup_duration
        if self.spark_jar_task:
            runTask_body['spark_jar_task'] = self.spark_jar_task.as_request()[1]
        if self.spark_python_task:
            runTask_body['spark_python_task'] = self.spark_python_task.as_request()[1]
        if self.spark_submit_task:
            runTask_body['spark_submit_task'] = self.spark_submit_task.as_request()[1]
        if self.start_time:
            runTask_body['start_time'] = self.start_time
        if self.state:
            runTask_body['state'] = self.state.as_request()[1]
        if self.task_key:
            runTask_body['task_key'] = self.task_key
        
        return runTask_query, runTask_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunTask':
        return cls(
            attempt_number=d.get('attempt_number', None),
            cleanup_duration=d.get('cleanup_duration', None),
            cluster_instance=ClusterInstance.from_dict(d['cluster_instance']) if 'cluster_instance' in d else None,
            depends_on=[TaskDependenciesItem.from_dict(v) for v in d['depends_on']] if 'depends_on' in d else None,
            description=d.get('description', None),
            end_time=d.get('end_time', None),
            execution_duration=d.get('execution_duration', None),
            existing_cluster_id=d.get('existing_cluster_id', None),
            git_source=GitSource.from_dict(d['git_source']) if 'git_source' in d else None,
            libraries=[Library.from_dict(v) for v in d['libraries']] if 'libraries' in d else None,
            new_cluster=NewCluster.from_dict(d['new_cluster']) if 'new_cluster' in d else None,
            notebook_task=NotebookTask.from_dict(d['notebook_task']) if 'notebook_task' in d else None,
            pipeline_task=PipelineTask.from_dict(d['pipeline_task']) if 'pipeline_task' in d else None,
            python_wheel_task=PythonWheelTask.from_dict(d['python_wheel_task']) if 'python_wheel_task' in d else None,
            run_id=d.get('run_id', None),
            setup_duration=d.get('setup_duration', None),
            spark_jar_task=SparkJarTask.from_dict(d['spark_jar_task']) if 'spark_jar_task' in d else None,
            spark_python_task=SparkPythonTask.from_dict(d['spark_python_task']) if 'spark_python_task' in d else None,
            spark_submit_task=SparkSubmitTask.from_dict(d['spark_submit_task']) if 'spark_submit_task' in d else None,
            start_time=d.get('start_time', None),
            state=RunState.from_dict(d['state']) if 'state' in d else None,
            task_key=d.get('task_key', None),
        )



class RunType(Enum):
    """The type of the run. * `JOB_RUN` \- Normal job run. A run created with [Run
    now](..dev-tools/api/latest/jobshtml#operation/JobsRunNow). * `WORKFLOW_RUN`
    \- Workflow run. A run created with
    [dbutils.notebook.run](..dev-tools/databricks-utilshtml#dbutils-workflow). *
    `SUBMIT_RUN` \- Submit run. A run created with [Run
    now](..dev-tools/api/latest/jobshtml#operation/JobsRunNow)."""
    
    JOB_RUN = 'JOB_RUN'
    SUBMIT_RUN = 'SUBMIT_RUN'
    WORKFLOW_RUN = 'WORKFLOW_RUN'

@dataclass
class S3StorageInfo:
    
    # (Optional) Set canned access control list. For example:
    # `bucket-owner-full-control`. If canned_acl is set, the cluster instance
    # profile must have `s3:PutObjectAcl` permission on the destination bucket
    # and prefix. The full list of possible canned ACLs can be found at
    # <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overviewhtml#canned-acl>.
    # By default only the object owner gets full control. If you are using cross
    # account role for writing data, you may want to set
    # `bucket-owner-full-control` to make bucket owner able to read the logs.
    canned_acl: str = None
    # S3 destination. For example: `s3://my-bucket/some-prefix` You must
    # configure the cluster with an instance profile and the instance profile
    # must have write access to the destination. You _cannot_ use AWS keys.
    destination: str = None
    # (Optional)Enable server side encryption, `false` by default.
    enable_encryption: bool = None
    # (Optional) The encryption type, it could be `sse-s3` or `sse-kms`. It is
    # used only when encryption is enabled and the default type is `sse-s3`.
    encryption_type: str = None
    # S3 endpoint. For example: `https://s3-us-west-2.amazonaws.com`. Either
    # region or endpoint must be set. If both are set, endpoint is used.
    endpoint: str = None
    # (Optional) KMS key used if encryption is enabled and encryption type is
    # set to `sse-kms`.
    kms_key: str = None
    # S3 region. For example: `us-west-2`. Either region or endpoint must be
    # set. If both are set, endpoint is used.
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





type SparkConfPair 'Dict[str,any /* MISSING TYPE */]'


type SparkEnvPair 'Dict[str,any /* MISSING TYPE */]'


@dataclass
class SparkJarTask:
    
    # Deprecated since 04/2016\. Provide a `jar` through the `libraries` field
    # instead. For an example, see
    # [Create](..dev-tools/api/latest/jobshtml#operation/JobsCreate).
    jar_uri: str = None
    # The full name of the class containing the main method to be executed. This
    # class must be contained in a JAR provided as a library.
    # 
    # The code must use `SparkContext.getOrCreate` to obtain a Spark context;
    # otherwise, runs of the job fail.
    main_class_name: str = None
    # Parameters passed to the main method.
    # 
    # Use [Task parameter variables](..jobshtml#parameter-variables) to set
    # parameters containing information about job runs.
    parameters: 'List[str]' = None

    def as_request(self) -> (dict, dict):
        sparkJarTask_query, sparkJarTask_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.jar_uri:
            sparkJarTask_body['jar_uri'] = self.jar_uri
        if self.main_class_name:
            sparkJarTask_body['main_class_name'] = self.main_class_name
        if self.parameters:
            sparkJarTask_body['parameters'] = [v for v in self.parameters]
        
        return sparkJarTask_query, sparkJarTask_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparkJarTask':
        return cls(
            jar_uri=d.get('jar_uri', None),
            main_class_name=d.get('main_class_name', None),
            parameters=d.get('parameters', None),
        )



@dataclass
class SparkPythonTask:
    
    
    python_file: str
    # Command line parameters passed to the Python file.
    # 
    # Use [Task parameter variables](..jobshtml#parameter-variables) to set
    # parameters containing information about job runs.
    parameters: 'List[str]' = None

    def as_request(self) -> (dict, dict):
        sparkPythonTask_query, sparkPythonTask_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.parameters:
            sparkPythonTask_body['parameters'] = [v for v in self.parameters]
        if self.python_file:
            sparkPythonTask_body['python_file'] = self.python_file
        
        return sparkPythonTask_query, sparkPythonTask_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparkPythonTask':
        return cls(
            parameters=d.get('parameters', None),
            python_file=d.get('python_file', None),
        )



@dataclass
class SparkSubmitTask:
    
    # Command-line parameters passed to spark submit.
    # 
    # Use [Task parameter variables](..jobshtml#parameter-variables) to set
    # parameters containing information about job runs.
    parameters: 'List[str]' = None

    def as_request(self) -> (dict, dict):
        sparkSubmitTask_query, sparkSubmitTask_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.parameters:
            sparkSubmitTask_body['parameters'] = [v for v in self.parameters]
        
        return sparkSubmitTask_query, sparkSubmitTask_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparkSubmitTask':
        return cls(
            parameters=d.get('parameters', None),
        )



@dataclass
class SubmitRun:
    
    # List of permissions to set on the job.
    access_control_list: 'List[AccessControlRequest]' = None
    # An optional specification for a remote repository containing the notebooks
    # used by this job's notebook tasks.
    git_source: 'GitSource' = None
    # An optional token that can be used to guarantee the idempotency of job run
    # requests. If a run with the provided token already exists, the request
    # does not create a new run but returns the ID of the existing run instead.
    # If a run with the provided token is deleted, an error is returned.
    # 
    # If you specify the idempotency token, upon failure you can retry until the
    # request succeeds. Databricks guarantees that exactly one run is launched
    # with that idempotency token.
    # 
    # This token must have at most 64 characters.
    # 
    # For more information, see [How to ensure idempotency for
    # jobs](https://kb.databricks.com/jobs/jobs-idempotency.html).
    idempotency_token: str = None
    # An optional name for the run. The default value is `Untitled`.
    run_name: str = None
    
    tasks: 'List[RunSubmitTaskSettings]' = None
    # An optional timeout applied to each run of this job. The default behavior
    # is to have no timeout.
    timeout_seconds: int = None

    def as_request(self) -> (dict, dict):
        submitRun_query, submitRun_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.access_control_list:
            submitRun_body['access_control_list'] = [v.as_request()[1] for v in self.access_control_list]
        if self.git_source:
            submitRun_body['git_source'] = self.git_source.as_request()[1]
        if self.idempotency_token:
            submitRun_body['idempotency_token'] = self.idempotency_token
        if self.run_name:
            submitRun_body['run_name'] = self.run_name
        if self.tasks:
            submitRun_body['tasks'] = [v.as_request()[1] for v in self.tasks]
        if self.timeout_seconds:
            submitRun_body['timeout_seconds'] = self.timeout_seconds
        
        return submitRun_query, submitRun_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SubmitRun':
        return cls(
            access_control_list=[AccessControlRequest.from_dict(v) for v in d['access_control_list']] if 'access_control_list' in d else None,
            git_source=GitSource.from_dict(d['git_source']) if 'git_source' in d else None,
            idempotency_token=d.get('idempotency_token', None),
            run_name=d.get('run_name', None),
            tasks=[RunSubmitTaskSettings.from_dict(v) for v in d['tasks']] if 'tasks' in d else None,
            timeout_seconds=d.get('timeout_seconds', None),
        )



@dataclass
class SubmitRunResponse:
    
    # The canonical identifier for the newly submitted run.
    run_id: int = None

    def as_request(self) -> (dict, dict):
        submitRunResponse_query, submitRunResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.run_id:
            submitRunResponse_body['run_id'] = self.run_id
        
        return submitRunResponse_query, submitRunResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SubmitRunResponse':
        return cls(
            run_id=d.get('run_id', None),
        )



@dataclass
class TaskDependenciesItem:
    
    
    task_key: str = None

    def as_request(self) -> (dict, dict):
        taskDependenciesItem_query, taskDependenciesItem_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.task_key:
            taskDependenciesItem_body['task_key'] = self.task_key
        
        return taskDependenciesItem_query, taskDependenciesItem_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TaskDependenciesItem':
        return cls(
            task_key=d.get('task_key', None),
        )







class TriggerType(Enum):
    """This describes an enum"""
    
    ONE_TIME = 'ONE_TIME'
    PERIODIC = 'PERIODIC'
    RETRY = 'RETRY'

@dataclass
class UpdateJob:
    
    # The canonical identifier of the job to update. This field is required.
    job_id: int
    # Remove top-level fields in the job settings. Removing nested fields is not
    # supported. This field is optional.
    fields_to_remove: 'List[str]' = None
    # The new settings for the job. Any top-level fields specified in
    # `new_settings` are completely replaced. Partially updating nested fields
    # is not supported.
    # 
    # Changes to the field `JobSettings.timeout_seconds` are applied to active
    # runs. Changes to other fields are applied to future runs only.
    new_settings: 'JobSettings' = None

    def as_request(self) -> (dict, dict):
        updateJob_query, updateJob_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.fields_to_remove:
            updateJob_body['fields_to_remove'] = [v for v in self.fields_to_remove]
        if self.job_id:
            updateJob_body['job_id'] = self.job_id
        if self.new_settings:
            updateJob_body['new_settings'] = self.new_settings.as_request()[1]
        
        return updateJob_query, updateJob_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateJob':
        return cls(
            fields_to_remove=d.get('fields_to_remove', None),
            job_id=d.get('job_id', None),
            new_settings=JobSettings.from_dict(d['new_settings']) if 'new_settings' in d else None,
        )





@dataclass
class ViewItem:
    
    # Content of the view.
    content: str = None
    # Name of the view item. In the case of code view, it would be the
    # notebook?s name. In the case of dashboard view, it would be the
    # dashboard?s name.
    name: str = None
    # Type of the view item.
    type: 'ViewType' = None

    def as_request(self) -> (dict, dict):
        viewItem_query, viewItem_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.content:
            viewItem_body['content'] = self.content
        if self.name:
            viewItem_body['name'] = self.name
        if self.type:
            viewItem_body['type'] = self.type.value
        
        return viewItem_query, viewItem_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ViewItem':
        return cls(
            content=d.get('content', None),
            name=d.get('name', None),
            type=ViewType(d['type']) if 'type' in d else None,
        )



class ViewType(Enum):
    """This describes an enum"""
    
    DASHBOARD = 'DASHBOARD'
    NOTEBOOK = 'NOTEBOOK'

class ViewsToExport(Enum):
    """This describes an enum"""
    
    ALL = 'ALL'
    CODE = 'CODE'
    DASHBOARDS = 'DASHBOARDS'

@dataclass
class CreateResponse:
    
    # The canonical identifier for the newly created job.
    job_id: int = None

    def as_request(self) -> (dict, dict):
        createResponse_query, createResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.job_id:
            createResponse_body['job_id'] = self.job_id
        
        return createResponse_query, createResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateResponse':
        return cls(
            job_id=d.get('job_id', None),
        )



@dataclass
class ExportRunRequest:
    
    # The canonical identifier for the run. This field is required.
    run_id: int # query
    # Which views to export (CODE, DASHBOARDS, or ALL). Defaults to CODE.
    views_to_export: 'ViewsToExport' = None # query

    def as_request(self) -> (dict, dict):
        exportRunRequest_query, exportRunRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.run_id:
            exportRunRequest_query['run_id'] = self.run_id
        if self.views_to_export:
            exportRunRequest_query['views_to_export'] = self.views_to_export.value
        
        return exportRunRequest_query, exportRunRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ExportRunRequest':
        return cls(
            run_id=d.get('run_id', None),
            views_to_export=ViewsToExport(d['views_to_export']) if 'views_to_export' in d else None,
        )



@dataclass
class GetRequest:
    
    # The canonical identifier of the job to retrieve information about. This
    # field is required.
    job_id: int # query

    def as_request(self) -> (dict, dict):
        getRequest_query, getRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.job_id:
            getRequest_query['job_id'] = self.job_id
        
        return getRequest_query, getRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetRequest':
        return cls(
            job_id=d.get('job_id', None),
        )



@dataclass
class GetRunOutputRequest:
    
    # The canonical identifier for the run. This field is required.
    run_id: int # query

    def as_request(self) -> (dict, dict):
        getRunOutputRequest_query, getRunOutputRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.run_id:
            getRunOutputRequest_query['run_id'] = self.run_id
        
        return getRunOutputRequest_query, getRunOutputRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetRunOutputRequest':
        return cls(
            run_id=d.get('run_id', None),
        )



@dataclass
class GetRunRequest:
    
    # The canonical identifier of the run for which to retrieve the metadata.
    # This field is required.
    run_id: int # query
    # Whether to include the repair history in the response.
    include_history: bool = None # query

    def as_request(self) -> (dict, dict):
        getRunRequest_query, getRunRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.include_history:
            getRunRequest_query['include_history'] = self.include_history
        if self.run_id:
            getRunRequest_query['run_id'] = self.run_id
        
        return getRunRequest_query, getRunRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetRunRequest':
        return cls(
            include_history=d.get('include_history', None),
            run_id=d.get('run_id', None),
        )



@dataclass
class ListRequest:
    
    # Whether to include task and cluster details in the response.
    expand_tasks: bool = None # query
    # The number of jobs to return. This value must be greater than 0 and less
    # or equal to 25. The default value is 20.
    limit: int = None # query
    # The offset of the first job to return, relative to the most recently
    # created job.
    offset: int = None # query

    def as_request(self) -> (dict, dict):
        listRequest_query, listRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.expand_tasks:
            listRequest_query['expand_tasks'] = self.expand_tasks
        if self.limit:
            listRequest_query['limit'] = self.limit
        if self.offset:
            listRequest_query['offset'] = self.offset
        
        return listRequest_query, listRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListRequest':
        return cls(
            expand_tasks=d.get('expand_tasks', None),
            limit=d.get('limit', None),
            offset=d.get('offset', None),
        )



@dataclass
class ListResponse:
    
    
    has_more: bool = None
    # The list of jobs.
    jobs: 'List[Job]' = None

    def as_request(self) -> (dict, dict):
        listResponse_query, listResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.has_more:
            listResponse_body['has_more'] = self.has_more
        if self.jobs:
            listResponse_body['jobs'] = [v.as_request()[1] for v in self.jobs]
        
        return listResponse_query, listResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListResponse':
        return cls(
            has_more=d.get('has_more', None),
            jobs=[Job.from_dict(v) for v in d['jobs']] if 'jobs' in d else None,
        )



@dataclass
class ListRunsRequest:
    
    # If active_only is `true`, only active runs are included in the results;
    # otherwise, lists both active and completed runs. An active run is a run in
    # the `PENDING`, `RUNNING`, or `TERMINATING`. This field cannot be `true`
    # when completed_only is `true`.
    active_only: bool = None # query
    # If completed_only is `true`, only completed runs are included in the
    # results; otherwise, lists both active and completed runs. This field
    # cannot be `true` when active_only is `true`.
    completed_only: bool = None # query
    # Whether to include task and cluster details in the response.
    expand_tasks: bool = None # query
    # The job for which to list runs. If omitted, the Jobs service lists runs
    # from all jobs.
    job_id: int = None # query
    # The number of runs to return. This value must be greater than 0 and less
    # than 25\. The default value is 25\. If a request specifies a limit of 0,
    # the service instead uses the maximum limit.
    limit: int = None # query
    # The offset of the first run to return, relative to the most recent run.
    offset: int = None # query
    # The type of runs to return. For a description of run types, see
    # [Run](..dev-tools/api/latest/jobshtml#operation/JobsRunsGet).
    run_type: 'ListRunsRunType' = None # query
    # Show runs that started _at or after_ this value. The value must be a UTC
    # timestamp in milliseconds. Can be combined with _start_time_to_ to filter
    # by a time range.
    start_time_from: int = None # query
    # Show runs that started _at or before_ this value. The value must be a UTC
    # timestamp in milliseconds. Can be combined with _start_time_from_ to
    # filter by a time range.
    start_time_to: int = None # query

    def as_request(self) -> (dict, dict):
        listRunsRequest_query, listRunsRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.active_only:
            listRunsRequest_query['active_only'] = self.active_only
        if self.completed_only:
            listRunsRequest_query['completed_only'] = self.completed_only
        if self.expand_tasks:
            listRunsRequest_query['expand_tasks'] = self.expand_tasks
        if self.job_id:
            listRunsRequest_query['job_id'] = self.job_id
        if self.limit:
            listRunsRequest_query['limit'] = self.limit
        if self.offset:
            listRunsRequest_query['offset'] = self.offset
        if self.run_type:
            listRunsRequest_query['run_type'] = self.run_type.value
        if self.start_time_from:
            listRunsRequest_query['start_time_from'] = self.start_time_from
        if self.start_time_to:
            listRunsRequest_query['start_time_to'] = self.start_time_to
        
        return listRunsRequest_query, listRunsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListRunsRequest':
        return cls(
            active_only=d.get('active_only', None),
            completed_only=d.get('completed_only', None),
            expand_tasks=d.get('expand_tasks', None),
            job_id=d.get('job_id', None),
            limit=d.get('limit', None),
            offset=d.get('offset', None),
            run_type=ListRunsRunType(d['run_type']) if 'run_type' in d else None,
            start_time_from=d.get('start_time_from', None),
            start_time_to=d.get('start_time_to', None),
        )



class ListRunsRunType(Enum):
    
    
    JOB_RUN = 'JOB_RUN'
    SUBMIT_RUN = 'SUBMIT_RUN'
    WORKFLOW_RUN = 'WORKFLOW_RUN'

@dataclass
class RepairRunResponse:
    
    # The ID of the repair.
    repair_id: int = None

    def as_request(self) -> (dict, dict):
        repairRunResponse_query, repairRunResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.repair_id:
            repairRunResponse_body['repair_id'] = self.repair_id
        
        return repairRunResponse_query, repairRunResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RepairRunResponse':
        return cls(
            repair_id=d.get('repair_id', None),
        )



class JobsAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def cancelAllRuns(self, request: CancelAllRuns):
        """Cancel all runs of a job
        
        Cancels all active runs of a job. The runs are canceled asynchronously,
        so it doesn't prevent new runs from being started."""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.1/jobs/runs/cancel-all', query=query, body=body)
        
    
    def cancelRun(self, request: CancelRun):
        """Cancel a job run
        
        Cancels a job run. The run is canceled asynchronously, so it may still
        be running when this request completes."""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.1/jobs/runs/cancel', query=query, body=body)
        
    
    def create(self, request: CreateJob) -> CreateResponse:
        """Create a new job
        
        Create a new job."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.1/jobs/create', query=query, body=body)
        return CreateResponse.from_dict(json)
    
    def delete(self, request: DeleteJob):
        """Delete a job
        
        Deletes a job."""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.1/jobs/delete', query=query, body=body)
        
    
    def deleteRun(self, request: DeleteRun):
        """Delete a job run
        
        Deletes a non-active run. Returns an error if the run is active."""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.1/jobs/runs/delete', query=query, body=body)
        
    
    def exportRun(self, request: ExportRunRequest) -> ExportRunOutput:
        """Export and retrieve a job run
        
        Export and retrieve the job run task."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.1/jobs/runs/export', query=query, body=body)
        return ExportRunOutput.from_dict(json)
    
    def get(self, request: GetRequest) -> Job:
        """Get a single job
        
        Retrieves the details for a single job."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.1/jobs/get', query=query, body=body)
        return Job.from_dict(json)
    
    def getRun(self, request: GetRunRequest) -> Run:
        """Get a single job run
        
        Retrieve the metadata of a run."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.1/jobs/runs/get', query=query, body=body)
        return Run.from_dict(json)
    
    def getRunOutput(self, request: GetRunOutputRequest) -> RunOutput:
        """Get the output for a single run
        
        Retrieve the output and metadata of a single task run. When a notebook
        task returns a value through the `dbutils.notebook.exit()` call, you can
        use this endpoint to retrieve that value. " + serviceName + " restricts
        this API to returning the first 5 MB of the output. To return a larger
        result, you can store job results in a cloud storage service.
        
        This endpoint validates that the __run_id__ parameter is valid and
        returns an HTTP status code 400 if the __run_id__ parameter is invalid.
        Runs are automatically removed after 60 days. If you to want to
        reference them beyond 60 days, you must save old run results before they
        expire."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.1/jobs/runs/get-output', query=query, body=body)
        return RunOutput.from_dict(json)
    
    def list(self, request: ListRequest) -> ListResponse:
        """List all jobs
        
        Retrieves a list of jobs."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.1/jobs/list', query=query, body=body)
        return ListResponse.from_dict(json)
    
    def listRuns(self, request: ListRunsRequest) -> ListRunsResponse:
        """List runs for a job
        
        List runs in descending order by start time."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.1/jobs/runs/list', query=query, body=body)
        return ListRunsResponse.from_dict(json)
    
    def repairRun(self, request: RepairRun) -> RepairRunResponse:
        """Repair a job run
        
        Re-run one or more tasks. Tasks are re-run as part of the original job
        run. They use the current job and task settings, and can be viewed in
        the history for the original job run."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.1/jobs/runs/repair', query=query, body=body)
        return RepairRunResponse.from_dict(json)
    
    def reset(self, request: ResetJob):
        """Overwrites all settings for a job
        
        Overwrites all the settings for a specific job. Use the Update endpoint
        to update job settings partially."""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.1/jobs/reset', query=query, body=body)
        
    
    def runNow(self, request: RunNow) -> RunNowResponse:
        """Trigger a new job run
        
        Run a job and return the `run_id` of the triggered run."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.1/jobs/run-now', query=query, body=body)
        return RunNowResponse.from_dict(json)
    
    def submit(self, request: SubmitRun) -> SubmitRunResponse:
        """Create and trigger a one-time run
        
        Submit a one-time run. This endpoint allows you to submit a workload
        directly without creating a job. Runs submitted using this endpoint
        don?t display in the UI. Use the `jobs/runs/get` API to check the run
        state after the job is submitted."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.1/jobs/runs/submit', query=query, body=body)
        return SubmitRunResponse.from_dict(json)
    
    def update(self, request: UpdateJob):
        """Partially updates a job
        
        Add, update, or remove specific settings of an existing job. Use the
        ResetJob to overwrite all job settings."""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.1/jobs/update', query=query, body=body)
        
    
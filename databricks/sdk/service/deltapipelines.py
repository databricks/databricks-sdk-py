# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List

__all__ = [
    
    'CreatePipelineRequest',
    'CreatePipelineResponse',
    'CronTrigger',
    'DeletePipelineRequest',
    'EditPipelineRequest',
    'Filters',
    'GetPipelineRequest',
    'GetPipelineResponse',
    'GetPipelineResponseHealth',
    'GetPipelineResponseState',
    'GetUpdateRequest',
    'GetUpdateResponse',
    'ListUpdatesRequest',
    'ListUpdatesResponse',
    'NotebookLibrary',
    'PipelineCluster',
    'PipelineLibrary',
    'PipelineSpec',
    'PipelineTrigger',
    'PipelinesAutoScale',
    'PipelinesAwsAttributes',
    'PipelinesClusterLogConf',
    'PipelinesDbfsStorageInfo',
    'PipelinesGcpAttributes',
    'PipelinesMavenLibrary',
    'PipelinesS3StorageInfo',
    'ResetPipelineRequest',
    'StartUpdateRequest',
    'StartUpdateRequestCause',
    'StartUpdateResponse',
    'StopPipelineRequest',
    'UpdateInfo',
    'UpdateInfoCause',
    'UpdateInfoState',
    'UpdateStateInfo',
    'UpdateStateInfoState',
    
    'DeltaPipelines',
]

# all definitions in this file are in alphabetical order

@dataclass
class CreatePipelineRequest:
    
    # If false, deployment will fail if name conflicts with that of another
    # pipeline.
    allow_duplicate_names: bool = None
    # Catalog in UC to add tables to. If target is specified, tables in this
    # pipeline will be published to a "target" schema inside catalog (i.e.
    # <catalog>.<target>.<table>).
    catalog: str = None
    # DLT Release Channel that specifies which version to use.
    channel: str = None
    # Cluster settings for this pipeline deployment.
    clusters: 'List[PipelineCluster]' = None
    # String-String configuration for this pipeline execution.
    configuration: 'Dict[str,str]' = None
    # Whether the pipeline is continuous or triggered. This replaces `trigger`.
    continuous: bool = None
    # Whether the pipeline is in Development mode. Defaults to false.
    development: bool = None
    
    dry_run: bool = None
    # Pipeline product edition.
    edition: str = None
    # Filters on which Pipeline packages to include in the deployed graph.
    filters: 'Filters' = None
    # Unique identifier for this pipeline.
    id: str = None
    # Libraries or code needed by this deployment.
    libraries: 'List[PipelineLibrary]' = None
    # Friendly identifier for this pipeline.
    name: str = None
    # Whether Photon is enabled for this pipeline.
    photon: bool = None
    # DBFS root directory for storing checkpoints and tables.
    storage: str = None
    # Target schema (database) to add tables in this pipeline to.
    target: str = None
    # Which pipeline trigger to use. Deprecated: Use `continuous` instead.
    trigger: 'PipelineTrigger' = None

    def as_request(self) -> (dict, dict):
        createPipelineRequest_query, createPipelineRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.allow_duplicate_names:
            createPipelineRequest_body['allow_duplicate_names'] = self.allow_duplicate_names
        if self.catalog:
            createPipelineRequest_body['catalog'] = self.catalog
        if self.channel:
            createPipelineRequest_body['channel'] = self.channel
        if self.clusters:
            createPipelineRequest_body['clusters'] = [v.as_request()[1] for v in self.clusters]
        if self.configuration:
            createPipelineRequest_body['configuration'] = self.configuration
        if self.continuous:
            createPipelineRequest_body['continuous'] = self.continuous
        if self.development:
            createPipelineRequest_body['development'] = self.development
        if self.dry_run:
            createPipelineRequest_body['dry_run'] = self.dry_run
        if self.edition:
            createPipelineRequest_body['edition'] = self.edition
        if self.filters:
            createPipelineRequest_body['filters'] = self.filters.as_request()[1]
        if self.id:
            createPipelineRequest_body['id'] = self.id
        if self.libraries:
            createPipelineRequest_body['libraries'] = [v.as_request()[1] for v in self.libraries]
        if self.name:
            createPipelineRequest_body['name'] = self.name
        if self.photon:
            createPipelineRequest_body['photon'] = self.photon
        if self.storage:
            createPipelineRequest_body['storage'] = self.storage
        if self.target:
            createPipelineRequest_body['target'] = self.target
        if self.trigger:
            createPipelineRequest_body['trigger'] = self.trigger.as_request()[1]
        
        return createPipelineRequest_query, createPipelineRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreatePipelineRequest':
        return cls(
            allow_duplicate_names=d.get('allow_duplicate_names', None),
            catalog=d.get('catalog', None),
            channel=d.get('channel', None),
            clusters=[PipelineCluster.from_dict(v) for v in d['clusters']] if 'clusters' in d else None,
            configuration=d.get('configuration', None),
            continuous=d.get('continuous', None),
            development=d.get('development', None),
            dry_run=d.get('dry_run', None),
            edition=d.get('edition', None),
            filters=Filters.from_dict(d['filters']) if 'filters' in d else None,
            id=d.get('id', None),
            libraries=[PipelineLibrary.from_dict(v) for v in d['libraries']] if 'libraries' in d else None,
            name=d.get('name', None),
            photon=d.get('photon', None),
            storage=d.get('storage', None),
            target=d.get('target', None),
            trigger=PipelineTrigger.from_dict(d['trigger']) if 'trigger' in d else None,
        )



@dataclass
class CreatePipelineResponse:
    
    # Only returned when dry_run is true
    effective_settings: 'PipelineSpec' = None
    # Only returned when dry_run is false
    pipeline_id: str = None

    def as_request(self) -> (dict, dict):
        createPipelineResponse_query, createPipelineResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.effective_settings:
            createPipelineResponse_body['effective_settings'] = self.effective_settings.as_request()[1]
        if self.pipeline_id:
            createPipelineResponse_body['pipeline_id'] = self.pipeline_id
        
        return createPipelineResponse_query, createPipelineResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreatePipelineResponse':
        return cls(
            effective_settings=PipelineSpec.from_dict(d['effective_settings']) if 'effective_settings' in d else None,
            pipeline_id=d.get('pipeline_id', None),
        )



@dataclass
class CronTrigger:
    
    
    quartz_cron_schedule: str = None
    
    timezone_id: str = None

    def as_request(self) -> (dict, dict):
        cronTrigger_query, cronTrigger_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.quartz_cron_schedule:
            cronTrigger_body['quartz_cron_schedule'] = self.quartz_cron_schedule
        if self.timezone_id:
            cronTrigger_body['timezone_id'] = self.timezone_id
        
        return cronTrigger_query, cronTrigger_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CronTrigger':
        return cls(
            quartz_cron_schedule=d.get('quartz_cron_schedule', None),
            timezone_id=d.get('timezone_id', None),
        )



@dataclass
class DeletePipelineRequest:
    
    
    pipeline_id: str # path

    def as_request(self) -> (dict, dict):
        deletePipelineRequest_query, deletePipelineRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.pipeline_id:
            deletePipelineRequest_body['pipeline_id'] = self.pipeline_id
        
        return deletePipelineRequest_query, deletePipelineRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeletePipelineRequest':
        return cls(
            pipeline_id=d.get('pipeline_id', None),
        )



@dataclass
class EditPipelineRequest:
    
    
    pipeline_id: str # path
    # If false, deployment will fail if name has changed and conflicts the name
    # of another pipeline.
    allow_duplicate_names: bool = None
    # Catalog in UC to add tables to. If target is specified, tables in this
    # pipeline will be published to a "target" schema inside catalog (i.e.
    # <catalog>.<target>.<table>).
    catalog: str = None
    # DLT Release Channel that specifies which version to use.
    channel: str = None
    # Cluster settings for this pipeline deployment.
    clusters: 'List[PipelineCluster]' = None
    # String-String configuration for this pipeline execution.
    configuration: 'Dict[str,str]' = None
    # Whether the pipeline is continuous or triggered. This replaces `trigger`.
    continuous: bool = None
    # Whether the pipeline is in Development mode. Defaults to false.
    development: bool = None
    # Pipeline product edition.
    edition: str = None
    # If present, the last-modified time of the pipeline settings before the
    # edit. If the settings were modified after that time, then the request will
    # fail with a conflict.
    expected_last_modified: int = None
    # Filters on which Pipeline packages to include in the deployed graph.
    filters: 'Filters' = None
    # Unique identifier for this pipeline.
    id: str = None
    # Libraries or code needed by this deployment.
    libraries: 'List[PipelineLibrary]' = None
    # Friendly identifier for this pipeline.
    name: str = None
    # Whether Photon is enabled for this pipeline.
    photon: bool = None
    # DBFS root directory for storing checkpoints and tables.
    storage: str = None
    # Target schema (database) to add tables in this pipeline to.
    target: str = None
    # Which pipeline trigger to use. Deprecated: Use `continuous` instead.
    trigger: 'PipelineTrigger' = None

    def as_request(self) -> (dict, dict):
        editPipelineRequest_query, editPipelineRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.allow_duplicate_names:
            editPipelineRequest_body['allow_duplicate_names'] = self.allow_duplicate_names
        if self.catalog:
            editPipelineRequest_body['catalog'] = self.catalog
        if self.channel:
            editPipelineRequest_body['channel'] = self.channel
        if self.clusters:
            editPipelineRequest_body['clusters'] = [v.as_request()[1] for v in self.clusters]
        if self.configuration:
            editPipelineRequest_body['configuration'] = self.configuration
        if self.continuous:
            editPipelineRequest_body['continuous'] = self.continuous
        if self.development:
            editPipelineRequest_body['development'] = self.development
        if self.edition:
            editPipelineRequest_body['edition'] = self.edition
        if self.expected_last_modified:
            editPipelineRequest_body['expected_last_modified'] = self.expected_last_modified
        if self.filters:
            editPipelineRequest_body['filters'] = self.filters.as_request()[1]
        if self.id:
            editPipelineRequest_body['id'] = self.id
        if self.libraries:
            editPipelineRequest_body['libraries'] = [v.as_request()[1] for v in self.libraries]
        if self.name:
            editPipelineRequest_body['name'] = self.name
        if self.photon:
            editPipelineRequest_body['photon'] = self.photon
        if self.pipeline_id:
            editPipelineRequest_body['pipeline_id'] = self.pipeline_id
        if self.storage:
            editPipelineRequest_body['storage'] = self.storage
        if self.target:
            editPipelineRequest_body['target'] = self.target
        if self.trigger:
            editPipelineRequest_body['trigger'] = self.trigger.as_request()[1]
        
        return editPipelineRequest_query, editPipelineRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EditPipelineRequest':
        return cls(
            allow_duplicate_names=d.get('allow_duplicate_names', None),
            catalog=d.get('catalog', None),
            channel=d.get('channel', None),
            clusters=[PipelineCluster.from_dict(v) for v in d['clusters']] if 'clusters' in d else None,
            configuration=d.get('configuration', None),
            continuous=d.get('continuous', None),
            development=d.get('development', None),
            edition=d.get('edition', None),
            expected_last_modified=d.get('expected_last_modified', None),
            filters=Filters.from_dict(d['filters']) if 'filters' in d else None,
            id=d.get('id', None),
            libraries=[PipelineLibrary.from_dict(v) for v in d['libraries']] if 'libraries' in d else None,
            name=d.get('name', None),
            photon=d.get('photon', None),
            pipeline_id=d.get('pipeline_id', None),
            storage=d.get('storage', None),
            target=d.get('target', None),
            trigger=PipelineTrigger.from_dict(d['trigger']) if 'trigger' in d else None,
        )



@dataclass
class Filters:
    
    # Paths to exclude.
    exclude: 'List[str]' = None
    # Paths to include.
    include: 'List[str]' = None

    def as_request(self) -> (dict, dict):
        filters_query, filters_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.exclude:
            filters_body['exclude'] = [v for v in self.exclude]
        if self.include:
            filters_body['include'] = [v for v in self.include]
        
        return filters_query, filters_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Filters':
        return cls(
            exclude=d.get('exclude', None),
            include=d.get('include', None),
        )



@dataclass
class GetPipelineRequest:
    
    
    pipeline_id: str # path

    def as_request(self) -> (dict, dict):
        getPipelineRequest_query, getPipelineRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.pipeline_id:
            getPipelineRequest_body['pipeline_id'] = self.pipeline_id
        
        return getPipelineRequest_query, getPipelineRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetPipelineRequest':
        return cls(
            pipeline_id=d.get('pipeline_id', None),
        )



@dataclass
class GetPipelineResponse:
    
    # An optional message detailing the cause of the pipeline state.
    cause: str = None
    # The ID of the cluster that the pipeline is running on.
    cluster_id: str = None
    # The username of the pipeline creator.
    creator_user_name: str = None
    # The health of a pipeline.
    health: 'GetPipelineResponseHealth' = None
    # The last time the pipeline settings were modified or created.
    last_modified: int = None
    # Status of the latest updates for the pipeline. Ordered with the newest
    # update first.
    latest_updates: 'List[UpdateStateInfo]' = None
    # A human friendly identifier for the pipeline, taken from the `spec`.
    name: str = None
    # The ID of the pipeline.
    pipeline_id: str = None
    # Username of the user that the pipeline will run on behalf of.
    run_as_user_name: str = None
    # The pipeline specification. This field is not returned when called by
    # `ListPipelines`.
    spec: 'PipelineSpec' = None
    # The pipeline state.
    state: 'GetPipelineResponseState' = None

    def as_request(self) -> (dict, dict):
        getPipelineResponse_query, getPipelineResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.cause:
            getPipelineResponse_body['cause'] = self.cause
        if self.cluster_id:
            getPipelineResponse_body['cluster_id'] = self.cluster_id
        if self.creator_user_name:
            getPipelineResponse_body['creator_user_name'] = self.creator_user_name
        if self.health:
            getPipelineResponse_body['health'] = self.health.value
        if self.last_modified:
            getPipelineResponse_body['last_modified'] = self.last_modified
        if self.latest_updates:
            getPipelineResponse_body['latest_updates'] = [v.as_request()[1] for v in self.latest_updates]
        if self.name:
            getPipelineResponse_body['name'] = self.name
        if self.pipeline_id:
            getPipelineResponse_body['pipeline_id'] = self.pipeline_id
        if self.run_as_user_name:
            getPipelineResponse_body['run_as_user_name'] = self.run_as_user_name
        if self.spec:
            getPipelineResponse_body['spec'] = self.spec.as_request()[1]
        if self.state:
            getPipelineResponse_body['state'] = self.state.value
        
        return getPipelineResponse_query, getPipelineResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetPipelineResponse':
        return cls(
            cause=d.get('cause', None),
            cluster_id=d.get('cluster_id', None),
            creator_user_name=d.get('creator_user_name', None),
            health=GetPipelineResponseHealth(d['health']) if 'health' in d else None,
            last_modified=d.get('last_modified', None),
            latest_updates=[UpdateStateInfo.from_dict(v) for v in d['latest_updates']] if 'latest_updates' in d else None,
            name=d.get('name', None),
            pipeline_id=d.get('pipeline_id', None),
            run_as_user_name=d.get('run_as_user_name', None),
            spec=PipelineSpec.from_dict(d['spec']) if 'spec' in d else None,
            state=GetPipelineResponseState(d['state']) if 'state' in d else None,
        )



class GetPipelineResponseHealth(Enum):
    """The health of a pipeline."""
    
    HEALTHY = 'HEALTHY'
    UNHEALTHY = 'UNHEALTHY'

class GetPipelineResponseState(Enum):
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
class GetUpdateRequest:
    
    # The ID of the pipeline.
    pipeline_id: str # path
    # The ID of the update.
    update_id: str # path

    def as_request(self) -> (dict, dict):
        getUpdateRequest_query, getUpdateRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.pipeline_id:
            getUpdateRequest_body['pipeline_id'] = self.pipeline_id
        if self.update_id:
            getUpdateRequest_body['update_id'] = self.update_id
        
        return getUpdateRequest_query, getUpdateRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetUpdateRequest':
        return cls(
            pipeline_id=d.get('pipeline_id', None),
            update_id=d.get('update_id', None),
        )



@dataclass
class GetUpdateResponse:
    
    # The current update info.
    update: 'UpdateInfo' = None

    def as_request(self) -> (dict, dict):
        getUpdateResponse_query, getUpdateResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.update:
            getUpdateResponse_body['update'] = self.update.as_request()[1]
        
        return getUpdateResponse_query, getUpdateResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetUpdateResponse':
        return cls(
            update=UpdateInfo.from_dict(d['update']) if 'update' in d else None,
        )



@dataclass
class ListUpdatesRequest:
    
    # The pipeline to return updates for.
    pipeline_id: str # path
    # Max number of entries to return in a single page.
    max_results: int = None # query
    # Page token returned by previous call
    page_token: str = None # query
    # If present, returns updates until and including this update_id.
    until_update_id: str = None # query

    def as_request(self) -> (dict, dict):
        listUpdatesRequest_query, listUpdatesRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.max_results:
            listUpdatesRequest_query['max_results'] = self.max_results
        if self.page_token:
            listUpdatesRequest_query['page_token'] = self.page_token
        if self.pipeline_id:
            listUpdatesRequest_body['pipeline_id'] = self.pipeline_id
        if self.until_update_id:
            listUpdatesRequest_query['until_update_id'] = self.until_update_id
        
        return listUpdatesRequest_query, listUpdatesRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListUpdatesRequest':
        return cls(
            max_results=d.get('max_results', None),
            page_token=d.get('page_token', None),
            pipeline_id=d.get('pipeline_id', None),
            until_update_id=d.get('until_update_id', None),
        )



@dataclass
class ListUpdatesResponse:
    
    # If present, then there are more results, and this a token to be used in a
    # subsequent request to fetch the next page.
    next_page_token: str = None
    # If present, then this token can be used in a subsequent request to fetch
    # the previous page.
    prev_page_token: str = None
    
    updates: 'List[UpdateInfo]' = None

    def as_request(self) -> (dict, dict):
        listUpdatesResponse_query, listUpdatesResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.next_page_token:
            listUpdatesResponse_body['next_page_token'] = self.next_page_token
        if self.prev_page_token:
            listUpdatesResponse_body['prev_page_token'] = self.prev_page_token
        if self.updates:
            listUpdatesResponse_body['updates'] = [v.as_request()[1] for v in self.updates]
        
        return listUpdatesResponse_query, listUpdatesResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListUpdatesResponse':
        return cls(
            next_page_token=d.get('next_page_token', None),
            prev_page_token=d.get('prev_page_token', None),
            updates=[UpdateInfo.from_dict(v) for v in d['updates']] if 'updates' in d else None,
        )



@dataclass
class NotebookLibrary:
    
    # The absolute path of the notebook.
    path: str = None

    def as_request(self) -> (dict, dict):
        notebookLibrary_query, notebookLibrary_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.path:
            notebookLibrary_body['path'] = self.path
        
        return notebookLibrary_query, notebookLibrary_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NotebookLibrary':
        return cls(
            path=d.get('path', None),
        )



@dataclass
class PipelineCluster:
    
    # Note: This field won't be persisted. Only API users will check this field.
    apply_policy_default_values: bool = None
    # Parameters needed in order to automatically scale clusters up and down
    # based on load. Note: autoscaling works best with DB runtime versions 3.0
    # or later.
    autoscale: 'PipelinesAutoScale' = None
    # Attributes related to clusters running on Amazon Web Services. If not
    # specified at cluster creation, a set of default values will be used.
    aws_attributes: 'PipelinesAwsAttributes' = None
    # Attributes related to clusters running on Amazon Web Services. If not
    # specified at cluster creation, a set of default values will be used.
    azure_attributes: any /* MISSING TYPE */ = None
    # The configuration for delivering spark logs to a long-term storage
    # destination. Two kinds of destinations (dbfs and s3) are supported. Only
    # one destination can be specified for one cluster. If the conf is given,
    # the logs will be delivered to the destination every ``5 mins``. The
    # destination of driver logs is ``$destination/$clusterId/driver``, while
    # the destination of executor logs is ``$destination/$clusterId/executor``.
    cluster_log_conf: 'PipelinesClusterLogConf' = None
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
    driver_node_type_id: str = None
    # Attributes related to clusters running on Google Cloud Platform. If not
    # specified at cluster creation, a set of default values will be used.
    gcp_attributes: 'PipelinesGcpAttributes' = None
    # The optional ID of the instance pool to which the cluster belongs.
    instance_pool_id: str = None
    # Cluster label
    label: str = None
    # This field encodes, through a single value, the resources available to
    # each of the Spark nodes in this cluster. For example, the Spark nodes can
    # be provisioned and optimized for memory or compute intensive workloads A
    # list of available node types can be retrieved by using the
    # :ref:`clusterClusterServicelistNodeTypes` API call.
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
    # SSH public key contents that will be added to each Spark node in this
    # cluster. The corresponding private keys can be used to login with the user
    # name ``ubuntu`` on port ``2200``. Up to 10 keys can be specified.
    ssh_public_keys: 'List[str]' = None

    def as_request(self) -> (dict, dict):
        pipelineCluster_query, pipelineCluster_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.apply_policy_default_values:
            pipelineCluster_body['apply_policy_default_values'] = self.apply_policy_default_values
        if self.autoscale:
            pipelineCluster_body['autoscale'] = self.autoscale.as_request()[1]
        if self.aws_attributes:
            pipelineCluster_body['aws_attributes'] = self.aws_attributes.as_request()[1]
        if self.azure_attributes:
            pipelineCluster_body['azure_attributes'] = self.azure_attributes
        if self.cluster_log_conf:
            pipelineCluster_body['cluster_log_conf'] = self.cluster_log_conf.as_request()[1]
        if self.custom_tags:
            pipelineCluster_body['custom_tags'] = self.custom_tags
        if self.driver_instance_pool_id:
            pipelineCluster_body['driver_instance_pool_id'] = self.driver_instance_pool_id
        if self.driver_node_type_id:
            pipelineCluster_body['driver_node_type_id'] = self.driver_node_type_id
        if self.gcp_attributes:
            pipelineCluster_body['gcp_attributes'] = self.gcp_attributes.as_request()[1]
        if self.instance_pool_id:
            pipelineCluster_body['instance_pool_id'] = self.instance_pool_id
        if self.label:
            pipelineCluster_body['label'] = self.label
        if self.node_type_id:
            pipelineCluster_body['node_type_id'] = self.node_type_id
        if self.num_workers:
            pipelineCluster_body['num_workers'] = self.num_workers
        if self.policy_id:
            pipelineCluster_body['policy_id'] = self.policy_id
        if self.spark_conf:
            pipelineCluster_body['spark_conf'] = self.spark_conf
        if self.spark_env_vars:
            pipelineCluster_body['spark_env_vars'] = self.spark_env_vars
        if self.ssh_public_keys:
            pipelineCluster_body['ssh_public_keys'] = [v for v in self.ssh_public_keys]
        
        return pipelineCluster_query, pipelineCluster_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineCluster':
        return cls(
            apply_policy_default_values=d.get('apply_policy_default_values', None),
            autoscale=PipelinesAutoScale.from_dict(d['autoscale']) if 'autoscale' in d else None,
            aws_attributes=PipelinesAwsAttributes.from_dict(d['aws_attributes']) if 'aws_attributes' in d else None,
            azure_attributes=d.get('azure_attributes', None),
            cluster_log_conf=PipelinesClusterLogConf.from_dict(d['cluster_log_conf']) if 'cluster_log_conf' in d else None,
            custom_tags=d.get('custom_tags', None),
            driver_instance_pool_id=d.get('driver_instance_pool_id', None),
            driver_node_type_id=d.get('driver_node_type_id', None),
            gcp_attributes=PipelinesGcpAttributes.from_dict(d['gcp_attributes']) if 'gcp_attributes' in d else None,
            instance_pool_id=d.get('instance_pool_id', None),
            label=d.get('label', None),
            node_type_id=d.get('node_type_id', None),
            num_workers=d.get('num_workers', None),
            policy_id=d.get('policy_id', None),
            spark_conf=d.get('spark_conf', None),
            spark_env_vars=d.get('spark_env_vars', None),
            ssh_public_keys=d.get('ssh_public_keys', None),
        )



@dataclass
class PipelineLibrary:
    
    # URI of the jar to be installed. Currently only DBFS and S3 URIs are
    # supported. For example: ``{ "jar": "dbfs:/mnt/databricks/library.jar" }``
    # or ``{ "jar": "s3://my-bucket/library.jar" }``. If S3 is used, please make
    # sure the cluster has read access on the library. You may need to launch
    # the cluster with an IAM role to access the S3 URI.
    jar: str = None
    # Specification of a maven library to be installed. For example: ``{
    # "coordinates": "org.jsoup:jsoup:1.7.2" }``
    maven: 'PipelinesMavenLibrary' = None
    # The path to a notebook that defines a pipeline and is stored in the
    # Databricks workspace. For example: ``{ "notebook" : { "path" :
    # "/my-pipeline-notebook-path" } }``. Currently, only Scala notebooks are
    # supported, and pipelines must be defined in a package cell.
    notebook: 'NotebookLibrary' = None
    # URI of the wheel to be installed. For example: ``{ "whl": "dbfs:/my/whl"
    # }`` or ``{ "whl": "s3://my-bucket/whl" }``. If S3 is used, please make
    # sure the cluster has read access on the library. You may need to launch
    # the cluster with an IAM role to access the S3 URI.
    whl: str = None

    def as_request(self) -> (dict, dict):
        pipelineLibrary_query, pipelineLibrary_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.jar:
            pipelineLibrary_body['jar'] = self.jar
        if self.maven:
            pipelineLibrary_body['maven'] = self.maven.as_request()[1]
        if self.notebook:
            pipelineLibrary_body['notebook'] = self.notebook.as_request()[1]
        if self.whl:
            pipelineLibrary_body['whl'] = self.whl
        
        return pipelineLibrary_query, pipelineLibrary_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineLibrary':
        return cls(
            jar=d.get('jar', None),
            maven=PipelinesMavenLibrary.from_dict(d['maven']) if 'maven' in d else None,
            notebook=NotebookLibrary.from_dict(d['notebook']) if 'notebook' in d else None,
            whl=d.get('whl', None),
        )



@dataclass
class PipelineSpec:
    
    # Catalog in UC to add tables to. If target is specified, tables in this
    # pipeline will be published to a "target" schema inside catalog (i.e.
    # <catalog>.<target>.<table>).
    catalog: str = None
    # DLT Release Channel that specifies which version to use.
    channel: str = None
    # Cluster settings for this pipeline deployment.
    clusters: 'List[PipelineCluster]' = None
    # String-String configuration for this pipeline execution.
    configuration: 'Dict[str,str]' = None
    # Whether the pipeline is continuous or triggered. This replaces `trigger`.
    continuous: bool = None
    # Whether the pipeline is in Development mode. Defaults to false.
    development: bool = None
    # Pipeline product edition.
    edition: str = None
    # Filters on which Pipeline packages to include in the deployed graph.
    filters: 'Filters' = None
    # Unique identifier for this pipeline.
    id: str = None
    # Libraries or code needed by this deployment.
    libraries: 'List[PipelineLibrary]' = None
    # Friendly identifier for this pipeline.
    name: str = None
    # Whether Photon is enabled for this pipeline.
    photon: bool = None
    # DBFS root directory for storing checkpoints and tables.
    storage: str = None
    # Target schema (database) to add tables in this pipeline to.
    target: str = None
    # Which pipeline trigger to use. Deprecated: Use `continuous` instead.
    trigger: 'PipelineTrigger' = None

    def as_request(self) -> (dict, dict):
        pipelineSpec_query, pipelineSpec_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog:
            pipelineSpec_body['catalog'] = self.catalog
        if self.channel:
            pipelineSpec_body['channel'] = self.channel
        if self.clusters:
            pipelineSpec_body['clusters'] = [v.as_request()[1] for v in self.clusters]
        if self.configuration:
            pipelineSpec_body['configuration'] = self.configuration
        if self.continuous:
            pipelineSpec_body['continuous'] = self.continuous
        if self.development:
            pipelineSpec_body['development'] = self.development
        if self.edition:
            pipelineSpec_body['edition'] = self.edition
        if self.filters:
            pipelineSpec_body['filters'] = self.filters.as_request()[1]
        if self.id:
            pipelineSpec_body['id'] = self.id
        if self.libraries:
            pipelineSpec_body['libraries'] = [v.as_request()[1] for v in self.libraries]
        if self.name:
            pipelineSpec_body['name'] = self.name
        if self.photon:
            pipelineSpec_body['photon'] = self.photon
        if self.storage:
            pipelineSpec_body['storage'] = self.storage
        if self.target:
            pipelineSpec_body['target'] = self.target
        if self.trigger:
            pipelineSpec_body['trigger'] = self.trigger.as_request()[1]
        
        return pipelineSpec_query, pipelineSpec_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineSpec':
        return cls(
            catalog=d.get('catalog', None),
            channel=d.get('channel', None),
            clusters=[PipelineCluster.from_dict(v) for v in d['clusters']] if 'clusters' in d else None,
            configuration=d.get('configuration', None),
            continuous=d.get('continuous', None),
            development=d.get('development', None),
            edition=d.get('edition', None),
            filters=Filters.from_dict(d['filters']) if 'filters' in d else None,
            id=d.get('id', None),
            libraries=[PipelineLibrary.from_dict(v) for v in d['libraries']] if 'libraries' in d else None,
            name=d.get('name', None),
            photon=d.get('photon', None),
            storage=d.get('storage', None),
            target=d.get('target', None),
            trigger=PipelineTrigger.from_dict(d['trigger']) if 'trigger' in d else None,
        )



@dataclass
class PipelineTrigger:
    
    
    cron: 'CronTrigger' = None
    
    manual: any /* MISSING TYPE */ = None

    def as_request(self) -> (dict, dict):
        pipelineTrigger_query, pipelineTrigger_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.cron:
            pipelineTrigger_body['cron'] = self.cron.as_request()[1]
        if self.manual:
            pipelineTrigger_body['manual'] = self.manual
        
        return pipelineTrigger_query, pipelineTrigger_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineTrigger':
        return cls(
            cron=CronTrigger.from_dict(d['cron']) if 'cron' in d else None,
            manual=d.get('manual', None),
        )



@dataclass
class PipelinesAutoScale:
    
    # The maximum number of workers to which the cluster can scale up when
    # overloaded. Note that ``max_workers`` must be strictly greater than
    # ``min_workers``.
    max_workers: int = None
    # The minimum number of workers to which the cluster can scale down when
    # underutilized. It is also the initial number of workers the cluster will
    # have after creation.
    min_workers: int = None
    # The autoscaling mode. This is an additional field available in DLT only.
    # This is used to specify the autoscaling algorithm to be used for this
    # autoscaling cluster. Decision Doc here:
    # https://docs.google.com/document/d/1Eojc1a5raIyApDz_2NYyoltDlimjXzqkTgwFwDQoGnw/edit?usp=sharing
    mode: str = None

    def as_request(self) -> (dict, dict):
        pipelinesAutoScale_query, pipelinesAutoScale_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.max_workers:
            pipelinesAutoScale_body['max_workers'] = self.max_workers
        if self.min_workers:
            pipelinesAutoScale_body['min_workers'] = self.min_workers
        if self.mode:
            pipelinesAutoScale_body['mode'] = self.mode
        
        return pipelinesAutoScale_query, pipelinesAutoScale_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelinesAutoScale':
        return cls(
            max_workers=d.get('max_workers', None),
            min_workers=d.get('min_workers', None),
            mode=d.get('mode', None),
        )



@dataclass
class PipelinesAwsAttributes:
    
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
        pipelinesAwsAttributes_query, pipelinesAwsAttributes_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.first_on_demand:
            pipelinesAwsAttributes_body['first_on_demand'] = self.first_on_demand
        if self.instance_profile_arn:
            pipelinesAwsAttributes_body['instance_profile_arn'] = self.instance_profile_arn
        if self.zone_id:
            pipelinesAwsAttributes_body['zone_id'] = self.zone_id
        
        return pipelinesAwsAttributes_query, pipelinesAwsAttributes_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelinesAwsAttributes':
        return cls(
            first_on_demand=d.get('first_on_demand', None),
            instance_profile_arn=d.get('instance_profile_arn', None),
            zone_id=d.get('zone_id', None),
        )



@dataclass
class PipelinesClusterLogConf:
    
    # destination needs to be provided. e.g. ``{ "dbfs" : { "destination" :
    # "dbfs:/home/cluster_log" } }``
    dbfs: 'PipelinesDbfsStorageInfo' = None
    # destination and either region or endpoint should also be provided. e.g.
    # ``{ "s3": { "destination" : "s3://cluster_log_bucket/prefix", "region" :
    # "us-west-2" } }`` Cluster iam role is used to access s3, please make sure
    # the cluster iam role in ``instance_profile_arn`` has permission to write
    # data to the s3 destination.
    s3: 'PipelinesS3StorageInfo' = None

    def as_request(self) -> (dict, dict):
        pipelinesClusterLogConf_query, pipelinesClusterLogConf_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.dbfs:
            pipelinesClusterLogConf_body['dbfs'] = self.dbfs.as_request()[1]
        if self.s3:
            pipelinesClusterLogConf_body['s3'] = self.s3.as_request()[1]
        
        return pipelinesClusterLogConf_query, pipelinesClusterLogConf_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelinesClusterLogConf':
        return cls(
            dbfs=PipelinesDbfsStorageInfo.from_dict(d['dbfs']) if 'dbfs' in d else None,
            s3=PipelinesS3StorageInfo.from_dict(d['s3']) if 's3' in d else None,
        )



@dataclass
class PipelinesDbfsStorageInfo:
    
    # dbfs destination, e.g. ``dbfs:/my/path``
    destination: str = None

    def as_request(self) -> (dict, dict):
        pipelinesDbfsStorageInfo_query, pipelinesDbfsStorageInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.destination:
            pipelinesDbfsStorageInfo_body['destination'] = self.destination
        
        return pipelinesDbfsStorageInfo_query, pipelinesDbfsStorageInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelinesDbfsStorageInfo':
        return cls(
            destination=d.get('destination', None),
        )



@dataclass
class PipelinesGcpAttributes:
    
    # If provided, the cluster will impersonate the google service account when
    # accessing gcloud services (like GCS). The google service account must have
    # previously been added to the Databricks environment by an account
    # administrator.
    google_service_account: str = None

    def as_request(self) -> (dict, dict):
        pipelinesGcpAttributes_query, pipelinesGcpAttributes_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.google_service_account:
            pipelinesGcpAttributes_body['google_service_account'] = self.google_service_account
        
        return pipelinesGcpAttributes_query, pipelinesGcpAttributes_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelinesGcpAttributes':
        return cls(
            google_service_account=d.get('google_service_account', None),
        )



@dataclass
class PipelinesMavenLibrary:
    
    # Gradle-style maven coordinates. For example: "org.jsoup:jsoup:1.7.2".
    coordinates: str
    # List of dependences to exclude. For example: ``["slf4j:slf4j",
    # "*:hadoop-client"]``.
    # 
    # Maven dependency exclusions:
    # https://maven.apache.org/guides/introduction/introduction-to-optional-and-excludes-dependencies.html.
    exclusions: 'List[str]' = None
    # Maven repo to install the Maven package from. If omitted, both Maven
    # Central Repository and Spark Packages are searched.
    repo: str = None

    def as_request(self) -> (dict, dict):
        pipelinesMavenLibrary_query, pipelinesMavenLibrary_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.coordinates:
            pipelinesMavenLibrary_body['coordinates'] = self.coordinates
        if self.exclusions:
            pipelinesMavenLibrary_body['exclusions'] = [v for v in self.exclusions]
        if self.repo:
            pipelinesMavenLibrary_body['repo'] = self.repo
        
        return pipelinesMavenLibrary_query, pipelinesMavenLibrary_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelinesMavenLibrary':
        return cls(
            coordinates=d.get('coordinates', None),
            exclusions=d.get('exclusions', None),
            repo=d.get('repo', None),
        )



@dataclass
class PipelinesS3StorageInfo:
    
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
        pipelinesS3StorageInfo_query, pipelinesS3StorageInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.canned_acl:
            pipelinesS3StorageInfo_body['canned_acl'] = self.canned_acl
        if self.destination:
            pipelinesS3StorageInfo_body['destination'] = self.destination
        if self.enable_encryption:
            pipelinesS3StorageInfo_body['enable_encryption'] = self.enable_encryption
        if self.encryption_type:
            pipelinesS3StorageInfo_body['encryption_type'] = self.encryption_type
        if self.endpoint:
            pipelinesS3StorageInfo_body['endpoint'] = self.endpoint
        if self.kms_key:
            pipelinesS3StorageInfo_body['kms_key'] = self.kms_key
        if self.region:
            pipelinesS3StorageInfo_body['region'] = self.region
        
        return pipelinesS3StorageInfo_query, pipelinesS3StorageInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelinesS3StorageInfo':
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
class ResetPipelineRequest:
    
    
    pipeline_id: str # path

    def as_request(self) -> (dict, dict):
        resetPipelineRequest_query, resetPipelineRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.pipeline_id:
            resetPipelineRequest_body['pipeline_id'] = self.pipeline_id
        
        return resetPipelineRequest_query, resetPipelineRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResetPipelineRequest':
        return cls(
            pipeline_id=d.get('pipeline_id', None),
        )



@dataclass
class StartUpdateRequest:
    
    
    pipeline_id: str # path
    
    cause: 'StartUpdateRequestCause' = None
    # If true, this update will reset all tables before running.
    full_refresh: bool = None
    # A list of tables to update with fullRefresh. If both refresh_selection and
    # full_refresh_selection are empty, this is a full graph update. Full
    # Refresh on a table means that the states of the table will be reset before
    # the refresh.
    full_refresh_selection: 'List[str]' = None
    # A list of tables to update without fullRefresh. If both refresh_selection
    # and full_refresh_selection are empty, this is a full graph update. Full
    # Refresh on a table means that the states of the table will be reset before
    # the refresh.
    refresh_selection: 'List[str]' = None

    def as_request(self) -> (dict, dict):
        startUpdateRequest_query, startUpdateRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.cause:
            startUpdateRequest_body['cause'] = self.cause.value
        if self.full_refresh:
            startUpdateRequest_body['full_refresh'] = self.full_refresh
        if self.full_refresh_selection:
            startUpdateRequest_body['full_refresh_selection'] = [v for v in self.full_refresh_selection]
        if self.pipeline_id:
            startUpdateRequest_body['pipeline_id'] = self.pipeline_id
        if self.refresh_selection:
            startUpdateRequest_body['refresh_selection'] = [v for v in self.refresh_selection]
        
        return startUpdateRequest_query, startUpdateRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StartUpdateRequest':
        return cls(
            cause=StartUpdateRequestCause(d['cause']) if 'cause' in d else None,
            full_refresh=d.get('full_refresh', None),
            full_refresh_selection=d.get('full_refresh_selection', None),
            pipeline_id=d.get('pipeline_id', None),
            refresh_selection=d.get('refresh_selection', None),
        )



class StartUpdateRequestCause(Enum):
    
    
    API_CALL = 'API_CALL'
    JOB_TASK = 'JOB_TASK'
    RETRY_ON_FAILURE = 'RETRY_ON_FAILURE'
    SCHEMA_CHANGE = 'SCHEMA_CHANGE'
    SERVICE_UPGRADE = 'SERVICE_UPGRADE'
    USER_ACTION = 'USER_ACTION'

@dataclass
class StartUpdateResponse:
    
    
    update_id: str = None

    def as_request(self) -> (dict, dict):
        startUpdateResponse_query, startUpdateResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.update_id:
            startUpdateResponse_body['update_id'] = self.update_id
        
        return startUpdateResponse_query, startUpdateResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StartUpdateResponse':
        return cls(
            update_id=d.get('update_id', None),
        )



@dataclass
class StopPipelineRequest:
    
    
    pipeline_id: str # path

    def as_request(self) -> (dict, dict):
        stopPipelineRequest_query, stopPipelineRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.pipeline_id:
            stopPipelineRequest_body['pipeline_id'] = self.pipeline_id
        
        return stopPipelineRequest_query, stopPipelineRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StopPipelineRequest':
        return cls(
            pipeline_id=d.get('pipeline_id', None),
        )



@dataclass
class UpdateInfo:
    
    # What triggered this update.
    cause: 'UpdateInfoCause' = None
    # The ID of the cluster that the update is running on.
    cluster_id: str = None
    # The pipeline configuration with system defaults applied where unspecified
    # by the user. Not returned by ListUpdates.
    config: 'PipelineSpec' = None
    # The time when this update was created.
    creation_time: int = None
    # If true, this update will reset all tables before running.
    full_refresh: bool = None
    # A list of tables to update with fullRefresh. If both refresh_selection and
    # full_refresh_selection are empty, this is a full graph update. Full
    # Refresh on a table means that the states of the table will be reset before
    # the refresh.
    full_refresh_selection: 'List[str]' = None
    # The ID of the pipeline.
    pipeline_id: str = None
    # A list of tables to update without fullRefresh. If both refresh_selection
    # and full_refresh_selection are empty, this is a full graph update. Full
    # Refresh on a table means that the states of the table will be reset before
    # the refresh.
    refresh_selection: 'List[str]' = None
    # The update state.
    state: 'UpdateInfoState' = None
    # The ID of this update.
    update_id: str = None

    def as_request(self) -> (dict, dict):
        updateInfo_query, updateInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.cause:
            updateInfo_body['cause'] = self.cause.value
        if self.cluster_id:
            updateInfo_body['cluster_id'] = self.cluster_id
        if self.config:
            updateInfo_body['config'] = self.config.as_request()[1]
        if self.creation_time:
            updateInfo_body['creation_time'] = self.creation_time
        if self.full_refresh:
            updateInfo_body['full_refresh'] = self.full_refresh
        if self.full_refresh_selection:
            updateInfo_body['full_refresh_selection'] = [v for v in self.full_refresh_selection]
        if self.pipeline_id:
            updateInfo_body['pipeline_id'] = self.pipeline_id
        if self.refresh_selection:
            updateInfo_body['refresh_selection'] = [v for v in self.refresh_selection]
        if self.state:
            updateInfo_body['state'] = self.state.value
        if self.update_id:
            updateInfo_body['update_id'] = self.update_id
        
        return updateInfo_query, updateInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateInfo':
        return cls(
            cause=UpdateInfoCause(d['cause']) if 'cause' in d else None,
            cluster_id=d.get('cluster_id', None),
            config=PipelineSpec.from_dict(d['config']) if 'config' in d else None,
            creation_time=d.get('creation_time', None),
            full_refresh=d.get('full_refresh', None),
            full_refresh_selection=d.get('full_refresh_selection', None),
            pipeline_id=d.get('pipeline_id', None),
            refresh_selection=d.get('refresh_selection', None),
            state=UpdateInfoState(d['state']) if 'state' in d else None,
            update_id=d.get('update_id', None),
        )



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

    def as_request(self) -> (dict, dict):
        updateStateInfo_query, updateStateInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.creation_time:
            updateStateInfo_body['creation_time'] = self.creation_time
        if self.state:
            updateStateInfo_body['state'] = self.state.value
        if self.update_id:
            updateStateInfo_body['update_id'] = self.update_id
        
        return updateStateInfo_query, updateStateInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateStateInfo':
        return cls(
            creation_time=d.get('creation_time', None),
            state=UpdateStateInfoState(d['state']) if 'state' in d else None,
            update_id=d.get('update_id', None),
        )



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

class DeltaPipelinesAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def createPipeline(self, request: CreatePipelineRequest) -> CreatePipelineResponse:
        
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.0/pipelines', query=query, body=body)
        return CreatePipelineResponse.from_dict(json)
    
    def deletePipeline(self, request: DeletePipelineRequest):
        
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.0/pipelines/{request.pipeline_id}', query=query, body=body)
        
    
    def editPipeline(self, request: EditPipelineRequest):
        
        query, body = request.as_request()
        self._api.do('PUT', f'/api/2.0/pipelines/{request.pipeline_id}', query=query, body=body)
        
    
    def getPipeline(self, request: GetPipelineRequest) -> GetPipelineResponse:
        
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.0/pipelines/{request.pipeline_id}', query=query, body=body)
        return GetPipelineResponse.from_dict(json)
    
    def getUpdate(self, request: GetUpdateRequest) -> GetUpdateResponse:
        
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.0/pipelines/{request.pipeline_id}/updates/{request.update_id}', query=query, body=body)
        return GetUpdateResponse.from_dict(json)
    
    def listUpdates(self, request: ListUpdatesRequest) -> ListUpdatesResponse:
        
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.0/pipelines/{request.pipeline_id}/updates', query=query, body=body)
        return ListUpdatesResponse.from_dict(json)
    
    def resetPipeline(self, request: ResetPipelineRequest):
        
        query, body = request.as_request()
        self._api.do('POST', f'/api/2.0/pipelines/{request.pipeline_id}/reset', query=query, body=body)
        
    
    def startUpdate(self, request: StartUpdateRequest) -> StartUpdateResponse:
        """* Starts or queues a pipeline update."""
        query, body = request.as_request()
        json = self._api.do('POST', f'/api/2.0/pipelines/{request.pipeline_id}/updates', query=query, body=body)
        return StartUpdateResponse.from_dict(json)
    
    def stopPipeline(self, request: StopPipelineRequest):
        
        query, body = request.as_request()
        self._api.do('POST', f'/api/2.0/pipelines/{request.pipeline_id}/stop', query=query, body=body)
        
    
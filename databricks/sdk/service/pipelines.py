# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


from .clusters import AutoScale
from .clusters import AwsAttributes
from .clusters import AzureAttributes
from .clusters import ClusterLogConf
from .clusters import GcpAttributes
from .libraries import MavenLibrary

# all definitions in this file are in alphabetical order


@dataclass
class CreatePipeline:

    # If false, deployment will fail if name conflicts with that of another
    # pipeline.
    allow_duplicate_names: bool
    # Catalog in UC to add tables to. If target is specified, tables in this
    # pipeline will be published to a "target" schema inside catalog (i.e.
    # <catalog>.<target>.<table>).
    catalog: str
    # DLT Release Channel that specifies which version to use.
    channel: str
    # Cluster settings for this pipeline deployment.
    clusters: "List[PipelineCluster]"
    # String-String configuration for this pipeline execution.
    configuration: "Dict[str,str]"
    # Whether the pipeline is continuous or triggered. This replaces `trigger`.
    continuous: bool
    # Whether the pipeline is in Development mode. Defaults to false.
    development: bool

    dry_run: bool
    # Pipeline product edition.
    edition: str
    # Filters on which Pipeline packages to include in the deployed graph.
    filters: "Filters"
    # Unique identifier for this pipeline.
    id: str
    # Libraries or code needed by this deployment.
    libraries: "List[PipelineLibrary]"
    # Friendly identifier for this pipeline.
    name: str
    # Whether Photon is enabled for this pipeline.
    photon: bool
    # DBFS root directory for storing checkpoints and tables.
    storage: str
    # Target schema (database) to add tables in this pipeline to.
    target: str
    # Which pipeline trigger to use. Deprecated: Use `continuous` instead.
    trigger: "PipelineTrigger"

    def as_request(self) -> (dict, dict):
        createPipeline_query, createPipeline_body = {}, {}
        if self.allow_duplicate_names:
            createPipeline_body["allow_duplicate_names"] = self.allow_duplicate_names
        if self.catalog:
            createPipeline_body["catalog"] = self.catalog
        if self.channel:
            createPipeline_body["channel"] = self.channel
        if self.clusters:
            createPipeline_body["clusters"] = [v.as_request()[1] for v in self.clusters]
        if self.configuration:
            createPipeline_body["configuration"] = self.configuration
        if self.continuous:
            createPipeline_body["continuous"] = self.continuous
        if self.development:
            createPipeline_body["development"] = self.development
        if self.dry_run:
            createPipeline_body["dry_run"] = self.dry_run
        if self.edition:
            createPipeline_body["edition"] = self.edition
        if self.filters:
            createPipeline_body["filters"] = self.filters.as_request()[1]
        if self.id:
            createPipeline_body["id"] = self.id
        if self.libraries:
            createPipeline_body["libraries"] = [
                v.as_request()[1] for v in self.libraries
            ]
        if self.name:
            createPipeline_body["name"] = self.name
        if self.photon:
            createPipeline_body["photon"] = self.photon
        if self.storage:
            createPipeline_body["storage"] = self.storage
        if self.target:
            createPipeline_body["target"] = self.target
        if self.trigger:
            createPipeline_body["trigger"] = self.trigger.as_request()[1]

        return createPipeline_query, createPipeline_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreatePipeline":
        return cls(
            allow_duplicate_names=d.get("allow_duplicate_names", None),
            catalog=d.get("catalog", None),
            channel=d.get("channel", None),
            clusters=[PipelineCluster.from_dict(v) for v in d["clusters"]]
            if "clusters" in d
            else None,
            configuration=d.get("configuration", None),
            continuous=d.get("continuous", None),
            development=d.get("development", None),
            dry_run=d.get("dry_run", None),
            edition=d.get("edition", None),
            filters=Filters.from_dict(d["filters"]) if "filters" in d else None,
            id=d.get("id", None),
            libraries=[PipelineLibrary.from_dict(v) for v in d["libraries"]]
            if "libraries" in d
            else None,
            name=d.get("name", None),
            photon=d.get("photon", None),
            storage=d.get("storage", None),
            target=d.get("target", None),
            trigger=PipelineTrigger.from_dict(d["trigger"]) if "trigger" in d else None,
        )


@dataclass
class CreatePipelineResponse:

    # Only returned when dry_run is true
    effective_settings: "PipelineSpec"
    # Only returned when dry_run is false
    pipeline_id: str

    def as_request(self) -> (dict, dict):
        createPipelineResponse_query, createPipelineResponse_body = {}, {}
        if self.effective_settings:
            createPipelineResponse_body[
                "effective_settings"
            ] = self.effective_settings.as_request()[1]
        if self.pipeline_id:
            createPipelineResponse_body["pipeline_id"] = self.pipeline_id

        return createPipelineResponse_query, createPipelineResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreatePipelineResponse":
        return cls(
            effective_settings=PipelineSpec.from_dict(d["effective_settings"])
            if "effective_settings" in d
            else None,
            pipeline_id=d.get("pipeline_id", None),
        )


@dataclass
class CronTrigger:

    quartz_cron_schedule: str

    timezone_id: str

    def as_request(self) -> (dict, dict):
        cronTrigger_query, cronTrigger_body = {}, {}
        if self.quartz_cron_schedule:
            cronTrigger_body["quartz_cron_schedule"] = self.quartz_cron_schedule
        if self.timezone_id:
            cronTrigger_body["timezone_id"] = self.timezone_id

        return cronTrigger_query, cronTrigger_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CronTrigger":
        return cls(
            quartz_cron_schedule=d.get("quartz_cron_schedule", None),
            timezone_id=d.get("timezone_id", None),
        )


@dataclass
class Delete:
    """Delete a pipeline"""

    pipeline_id: str  # path

    def as_request(self) -> (dict, dict):
        delete_query, delete_body = {}, {}
        if self.pipeline_id:
            delete_body["pipeline_id"] = self.pipeline_id

        return delete_query, delete_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Delete":
        return cls(
            pipeline_id=d.get("pipeline_id", None),
        )


@dataclass
class EditPipeline:

    # If false, deployment will fail if name has changed and conflicts the name
    # of another pipeline.
    allow_duplicate_names: bool
    # Catalog in UC to add tables to. If target is specified, tables in this
    # pipeline will be published to a "target" schema inside catalog (i.e.
    # <catalog>.<target>.<table>).
    catalog: str
    # DLT Release Channel that specifies which version to use.
    channel: str
    # Cluster settings for this pipeline deployment.
    clusters: "List[PipelineCluster]"
    # String-String configuration for this pipeline execution.
    configuration: "Dict[str,str]"
    # Whether the pipeline is continuous or triggered. This replaces `trigger`.
    continuous: bool
    # Whether the pipeline is in Development mode. Defaults to false.
    development: bool
    # Pipeline product edition.
    edition: str
    # If present, the last-modified time of the pipeline settings before the
    # edit. If the settings were modified after that time, then the request will
    # fail with a conflict.
    expected_last_modified: int
    # Filters on which Pipeline packages to include in the deployed graph.
    filters: "Filters"
    # Unique identifier for this pipeline.
    id: str
    # Libraries or code needed by this deployment.
    libraries: "List[PipelineLibrary]"
    # Friendly identifier for this pipeline.
    name: str
    # Whether Photon is enabled for this pipeline.
    photon: bool
    # Unique identifier for this pipeline.
    pipeline_id: str  # path
    # DBFS root directory for storing checkpoints and tables.
    storage: str
    # Target schema (database) to add tables in this pipeline to.
    target: str
    # Which pipeline trigger to use. Deprecated: Use `continuous` instead.
    trigger: "PipelineTrigger"

    def as_request(self) -> (dict, dict):
        editPipeline_query, editPipeline_body = {}, {}
        if self.allow_duplicate_names:
            editPipeline_body["allow_duplicate_names"] = self.allow_duplicate_names
        if self.catalog:
            editPipeline_body["catalog"] = self.catalog
        if self.channel:
            editPipeline_body["channel"] = self.channel
        if self.clusters:
            editPipeline_body["clusters"] = [v.as_request()[1] for v in self.clusters]
        if self.configuration:
            editPipeline_body["configuration"] = self.configuration
        if self.continuous:
            editPipeline_body["continuous"] = self.continuous
        if self.development:
            editPipeline_body["development"] = self.development
        if self.edition:
            editPipeline_body["edition"] = self.edition
        if self.expected_last_modified:
            editPipeline_body["expected_last_modified"] = self.expected_last_modified
        if self.filters:
            editPipeline_body["filters"] = self.filters.as_request()[1]
        if self.id:
            editPipeline_body["id"] = self.id
        if self.libraries:
            editPipeline_body["libraries"] = [v.as_request()[1] for v in self.libraries]
        if self.name:
            editPipeline_body["name"] = self.name
        if self.photon:
            editPipeline_body["photon"] = self.photon
        if self.pipeline_id:
            editPipeline_body["pipeline_id"] = self.pipeline_id
        if self.storage:
            editPipeline_body["storage"] = self.storage
        if self.target:
            editPipeline_body["target"] = self.target
        if self.trigger:
            editPipeline_body["trigger"] = self.trigger.as_request()[1]

        return editPipeline_query, editPipeline_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "EditPipeline":
        return cls(
            allow_duplicate_names=d.get("allow_duplicate_names", None),
            catalog=d.get("catalog", None),
            channel=d.get("channel", None),
            clusters=[PipelineCluster.from_dict(v) for v in d["clusters"]]
            if "clusters" in d
            else None,
            configuration=d.get("configuration", None),
            continuous=d.get("continuous", None),
            development=d.get("development", None),
            edition=d.get("edition", None),
            expected_last_modified=d.get("expected_last_modified", None),
            filters=Filters.from_dict(d["filters"]) if "filters" in d else None,
            id=d.get("id", None),
            libraries=[PipelineLibrary.from_dict(v) for v in d["libraries"]]
            if "libraries" in d
            else None,
            name=d.get("name", None),
            photon=d.get("photon", None),
            pipeline_id=d.get("pipeline_id", None),
            storage=d.get("storage", None),
            target=d.get("target", None),
            trigger=PipelineTrigger.from_dict(d["trigger"]) if "trigger" in d else None,
        )


@dataclass
class Filters:

    # Paths to exclude.
    exclude: "List[str]"
    # Paths to include.
    include: "List[str]"

    def as_request(self) -> (dict, dict):
        filters_query, filters_body = {}, {}
        if self.exclude:
            filters_body["exclude"] = [v for v in self.exclude]
        if self.include:
            filters_body["include"] = [v for v in self.include]

        return filters_query, filters_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Filters":
        return cls(
            exclude=d.get("exclude", None),
            include=d.get("include", None),
        )


@dataclass
class Get:
    """Get a pipeline"""

    pipeline_id: str  # path

    def as_request(self) -> (dict, dict):
        get_query, get_body = {}, {}
        if self.pipeline_id:
            get_body["pipeline_id"] = self.pipeline_id

        return get_query, get_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Get":
        return cls(
            pipeline_id=d.get("pipeline_id", None),
        )


@dataclass
class GetPipelineResponse:

    # An optional message detailing the cause of the pipeline state.
    cause: str
    # The ID of the cluster that the pipeline is running on.
    cluster_id: str
    # The username of the pipeline creator.
    creator_user_name: str
    # The health of a pipeline.
    health: "GetPipelineResponseHealth"
    # The last time the pipeline settings were modified or created.
    last_modified: int
    # Status of the latest updates for the pipeline. Ordered with the newest
    # update first.
    latest_updates: "List[UpdateStateInfo]"
    # A human friendly identifier for the pipeline, taken from the `spec`.
    name: str
    # The ID of the pipeline.
    pipeline_id: str
    # Username of the user that the pipeline will run on behalf of.
    run_as_user_name: str
    # The pipeline specification. This field is not returned when called by
    # `ListPipelines`.
    spec: "PipelineSpec"
    # The pipeline state.
    state: "PipelineState"

    def as_request(self) -> (dict, dict):
        getPipelineResponse_query, getPipelineResponse_body = {}, {}
        if self.cause:
            getPipelineResponse_body["cause"] = self.cause
        if self.cluster_id:
            getPipelineResponse_body["cluster_id"] = self.cluster_id
        if self.creator_user_name:
            getPipelineResponse_body["creator_user_name"] = self.creator_user_name
        if self.health:
            getPipelineResponse_body["health"] = self.health.value
        if self.last_modified:
            getPipelineResponse_body["last_modified"] = self.last_modified
        if self.latest_updates:
            getPipelineResponse_body["latest_updates"] = [
                v.as_request()[1] for v in self.latest_updates
            ]
        if self.name:
            getPipelineResponse_body["name"] = self.name
        if self.pipeline_id:
            getPipelineResponse_body["pipeline_id"] = self.pipeline_id
        if self.run_as_user_name:
            getPipelineResponse_body["run_as_user_name"] = self.run_as_user_name
        if self.spec:
            getPipelineResponse_body["spec"] = self.spec.as_request()[1]
        if self.state:
            getPipelineResponse_body["state"] = self.state.value

        return getPipelineResponse_query, getPipelineResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetPipelineResponse":
        return cls(
            cause=d.get("cause", None),
            cluster_id=d.get("cluster_id", None),
            creator_user_name=d.get("creator_user_name", None),
            health=GetPipelineResponseHealth(d["health"]) if "health" in d else None,
            last_modified=d.get("last_modified", None),
            latest_updates=[UpdateStateInfo.from_dict(v) for v in d["latest_updates"]]
            if "latest_updates" in d
            else None,
            name=d.get("name", None),
            pipeline_id=d.get("pipeline_id", None),
            run_as_user_name=d.get("run_as_user_name", None),
            spec=PipelineSpec.from_dict(d["spec"]) if "spec" in d else None,
            state=PipelineState(d["state"]) if "state" in d else None,
        )


class GetPipelineResponseHealth(Enum):
    """The health of a pipeline."""

    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"


@dataclass
class GetUpdate:
    """Get a pipeline update"""

    # The ID of the pipeline.
    pipeline_id: str  # path
    # The ID of the update.
    update_id: str  # path

    def as_request(self) -> (dict, dict):
        getUpdate_query, getUpdate_body = {}, {}
        if self.pipeline_id:
            getUpdate_body["pipeline_id"] = self.pipeline_id
        if self.update_id:
            getUpdate_body["update_id"] = self.update_id

        return getUpdate_query, getUpdate_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetUpdate":
        return cls(
            pipeline_id=d.get("pipeline_id", None),
            update_id=d.get("update_id", None),
        )


@dataclass
class GetUpdateResponse:

    # The current update info.
    update: "UpdateInfo"

    def as_request(self) -> (dict, dict):
        getUpdateResponse_query, getUpdateResponse_body = {}, {}
        if self.update:
            getUpdateResponse_body["update"] = self.update.as_request()[1]

        return getUpdateResponse_query, getUpdateResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetUpdateResponse":
        return cls(
            update=UpdateInfo.from_dict(d["update"]) if "update" in d else None,
        )


@dataclass
class ListPipelines:
    """List pipelines"""

    # Select a subset of results based on the specified criteria. The supported
    # filters are:
    #
    # * `notebook='<path>'` to select pipelines that reference the provided
    # notebook path. * `name LIKE '[pattern]'` to select pipelines with a name
    # that matches pattern. Wildcards are supported, for example: `name LIKE
    # '%shopping%'`
    #
    # Composite filters are not supported. This field is optional.
    filter: str  # query
    # The maximum number of entries to return in a single page. The system may
    # return fewer than max_results events in a response, even if there are more
    # events available. This field is optional. The default value is 25. The
    # maximum value is 100. An error is returned if the value of max_results is
    # greater than 100.
    max_results: int  # query
    # A list of strings specifying the order of results. Supported order_by
    # fields are id and name. The default is id asc. This field is optional.
    order_by: "List[str]"  # query
    # Page token returned by previous call
    page_token: str  # query

    def as_request(self) -> (dict, dict):
        listPipelines_query, listPipelines_body = {}, {}
        if self.filter:
            listPipelines_query["filter"] = self.filter
        if self.max_results:
            listPipelines_query["max_results"] = self.max_results
        if self.order_by:
            listPipelines_query["order_by"] = [v for v in self.order_by]
        if self.page_token:
            listPipelines_query["page_token"] = self.page_token

        return listPipelines_query, listPipelines_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListPipelines":
        return cls(
            filter=d.get("filter", None),
            max_results=d.get("max_results", None),
            order_by=d.get("order_by", None),
            page_token=d.get("page_token", None),
        )


@dataclass
class ListPipelinesResponse:

    # If present, a token to fetch the next page of events.
    next_page_token: str
    # The list of events matching the request criteria.
    statuses: "List[PipelineStateInfo]"

    def as_request(self) -> (dict, dict):
        listPipelinesResponse_query, listPipelinesResponse_body = {}, {}
        if self.next_page_token:
            listPipelinesResponse_body["next_page_token"] = self.next_page_token
        if self.statuses:
            listPipelinesResponse_body["statuses"] = [
                v.as_request()[1] for v in self.statuses
            ]

        return listPipelinesResponse_query, listPipelinesResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListPipelinesResponse":
        return cls(
            next_page_token=d.get("next_page_token", None),
            statuses=[PipelineStateInfo.from_dict(v) for v in d["statuses"]]
            if "statuses" in d
            else None,
        )


@dataclass
class ListUpdates:
    """List pipeline updates"""

    # Max number of entries to return in a single page.
    max_results: int  # query
    # Page token returned by previous call
    page_token: str  # query
    # The pipeline to return updates for.
    pipeline_id: str  # path
    # If present, returns updates until and including this update_id.
    until_update_id: str  # query

    def as_request(self) -> (dict, dict):
        listUpdates_query, listUpdates_body = {}, {}
        if self.max_results:
            listUpdates_query["max_results"] = self.max_results
        if self.page_token:
            listUpdates_query["page_token"] = self.page_token
        if self.pipeline_id:
            listUpdates_body["pipeline_id"] = self.pipeline_id
        if self.until_update_id:
            listUpdates_query["until_update_id"] = self.until_update_id

        return listUpdates_query, listUpdates_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListUpdates":
        return cls(
            max_results=d.get("max_results", None),
            page_token=d.get("page_token", None),
            pipeline_id=d.get("pipeline_id", None),
            until_update_id=d.get("until_update_id", None),
        )


@dataclass
class ListUpdatesResponse:

    # If present, then there are more results, and this a token to be used in a
    # subsequent request to fetch the next page.
    next_page_token: str
    # If present, then this token can be used in a subsequent request to fetch
    # the previous page.
    prev_page_token: str

    updates: "List[UpdateInfo]"

    def as_request(self) -> (dict, dict):
        listUpdatesResponse_query, listUpdatesResponse_body = {}, {}
        if self.next_page_token:
            listUpdatesResponse_body["next_page_token"] = self.next_page_token
        if self.prev_page_token:
            listUpdatesResponse_body["prev_page_token"] = self.prev_page_token
        if self.updates:
            listUpdatesResponse_body["updates"] = [
                v.as_request()[1] for v in self.updates
            ]

        return listUpdatesResponse_query, listUpdatesResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListUpdatesResponse":
        return cls(
            next_page_token=d.get("next_page_token", None),
            prev_page_token=d.get("prev_page_token", None),
            updates=[UpdateInfo.from_dict(v) for v in d["updates"]]
            if "updates" in d
            else None,
        )


@dataclass
class NotebookLibrary:

    # The absolute path of the notebook.
    path: str

    def as_request(self) -> (dict, dict):
        notebookLibrary_query, notebookLibrary_body = {}, {}
        if self.path:
            notebookLibrary_body["path"] = self.path

        return notebookLibrary_query, notebookLibrary_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "NotebookLibrary":
        return cls(
            path=d.get("path", None),
        )


@dataclass
class PipelineCluster:

    # Note: This field won't be persisted. Only API users will check this field.
    apply_policy_default_values: bool
    # Parameters needed in order to automatically scale clusters up and down
    # based on load. Note: autoscaling works best with DB runtime versions 3.0
    # or later.
    autoscale: "AutoScale"
    # Attributes related to clusters running on Amazon Web Services. If not
    # specified at cluster creation, a set of default values will be used.
    aws_attributes: "AwsAttributes"
    # Attributes related to clusters running on Amazon Web Services. If not
    # specified at cluster creation, a set of default values will be used.
    azure_attributes: "AzureAttributes"
    # The configuration for delivering spark logs to a long-term storage
    # destination. Two kinds of destinations (dbfs and s3) are supported. Only
    # one destination can be specified for one cluster. If the conf is given,
    # the logs will be delivered to the destination every `5 mins`. The
    # destination of driver logs is `$destination/$clusterId/driver`, while the
    # destination of executor logs is `$destination/$clusterId/executor`.
    cluster_log_conf: "ClusterLogConf"
    # Additional tags for cluster resources. Databricks will tag all cluster
    # resources (e.g., AWS instances and EBS volumes) with these tags in
    # addition to `default_tags`. Notes:
    #
    # - Currently, Databricks allows at most 45 custom tags
    #
    # - Clusters can only reuse cloud resources if the resources' tags are a
    # subset of the cluster tags
    custom_tags: "Dict[str,str]"
    # The optional ID of the instance pool for the driver of the cluster
    # belongs. The pool cluster uses the instance pool with id
    # (instance_pool_id) if the driver pool is not assigned.
    driver_instance_pool_id: str
    # The node type of the Spark driver. Note that this field is optional; if
    # unset, the driver node type will be set as the same value as
    # `node_type_id` defined above.
    driver_node_type_id: str
    # Attributes related to clusters running on Google Cloud Platform. If not
    # specified at cluster creation, a set of default values will be used.
    gcp_attributes: "GcpAttributes"
    # The optional ID of the instance pool to which the cluster belongs.
    instance_pool_id: str
    # Cluster label
    label: str
    # This field encodes, through a single value, the resources available to
    # each of the Spark nodes in this cluster. For example, the Spark nodes can
    # be provisioned and optimized for memory or compute intensive workloads. A
    # list of available node types can be retrieved by using the
    # :method:clusters/listNodeTypes API call.
    node_type_id: str
    # Number of worker nodes that this cluster should have. A cluster has one
    # Spark Driver and `num_workers` Executors for a total of `num_workers` + 1
    # Spark nodes.
    #
    # Note: When reading the properties of a cluster, this field reflects the
    # desired number of workers rather than the actual current number of
    # workers. For instance, if a cluster is resized from 5 to 10 workers, this
    # field will immediately be updated to reflect the target size of 10
    # workers, whereas the workers listed in `spark_info` will gradually
    # increase from 5 to 10 as the new nodes are provisioned.
    num_workers: int
    # The ID of the cluster policy used to create the cluster if applicable.
    policy_id: str
    # An object containing a set of optional, user-specified Spark configuration
    # key-value pairs. See :method:clusters/create for more details.
    spark_conf: "Dict[str,str]"
    # An object containing a set of optional, user-specified environment
    # variable key-value pairs. Please note that key-value pair of the form
    # (X,Y) will be exported as is (i.e., `export X='Y'`) while launching the
    # driver and workers.
    #
    # In order to specify an additional set of `SPARK_DAEMON_JAVA_OPTS`, we
    # recommend appending them to `$SPARK_DAEMON_JAVA_OPTS` as shown in the
    # example below. This ensures that all default databricks managed
    # environmental variables are included as well.
    #
    # Example Spark environment variables: `{"SPARK_WORKER_MEMORY": "28000m",
    # "SPARK_LOCAL_DIRS": "/local_disk0"}` or `{"SPARK_DAEMON_JAVA_OPTS":
    # "$SPARK_DAEMON_JAVA_OPTS -Dspark.shuffle.service.enabled=true"}`
    spark_env_vars: "Dict[str,str]"
    # SSH public key contents that will be added to each Spark node in this
    # cluster. The corresponding private keys can be used to login with the user
    # name `ubuntu` on port `2200`. Up to 10 keys can be specified.
    ssh_public_keys: "List[str]"

    def as_request(self) -> (dict, dict):
        pipelineCluster_query, pipelineCluster_body = {}, {}
        if self.apply_policy_default_values:
            pipelineCluster_body[
                "apply_policy_default_values"
            ] = self.apply_policy_default_values
        if self.autoscale:
            pipelineCluster_body["autoscale"] = self.autoscale
        if self.aws_attributes:
            pipelineCluster_body["aws_attributes"] = self.aws_attributes
        if self.azure_attributes:
            pipelineCluster_body["azure_attributes"] = self.azure_attributes
        if self.cluster_log_conf:
            pipelineCluster_body["cluster_log_conf"] = self.cluster_log_conf
        if self.custom_tags:
            pipelineCluster_body["custom_tags"] = self.custom_tags
        if self.driver_instance_pool_id:
            pipelineCluster_body[
                "driver_instance_pool_id"
            ] = self.driver_instance_pool_id
        if self.driver_node_type_id:
            pipelineCluster_body["driver_node_type_id"] = self.driver_node_type_id
        if self.gcp_attributes:
            pipelineCluster_body["gcp_attributes"] = self.gcp_attributes
        if self.instance_pool_id:
            pipelineCluster_body["instance_pool_id"] = self.instance_pool_id
        if self.label:
            pipelineCluster_body["label"] = self.label
        if self.node_type_id:
            pipelineCluster_body["node_type_id"] = self.node_type_id
        if self.num_workers:
            pipelineCluster_body["num_workers"] = self.num_workers
        if self.policy_id:
            pipelineCluster_body["policy_id"] = self.policy_id
        if self.spark_conf:
            pipelineCluster_body["spark_conf"] = self.spark_conf
        if self.spark_env_vars:
            pipelineCluster_body["spark_env_vars"] = self.spark_env_vars
        if self.ssh_public_keys:
            pipelineCluster_body["ssh_public_keys"] = [v for v in self.ssh_public_keys]

        return pipelineCluster_query, pipelineCluster_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PipelineCluster":
        return cls(
            apply_policy_default_values=d.get("apply_policy_default_values", None),
            autoscale=AutoScale.from_dict(d["autoscale"]) if "autoscale" in d else None,
            aws_attributes=AwsAttributes.from_dict(d["aws_attributes"])
            if "aws_attributes" in d
            else None,
            azure_attributes=AzureAttributes.from_dict(d["azure_attributes"])
            if "azure_attributes" in d
            else None,
            cluster_log_conf=ClusterLogConf.from_dict(d["cluster_log_conf"])
            if "cluster_log_conf" in d
            else None,
            custom_tags=d.get("custom_tags", None),
            driver_instance_pool_id=d.get("driver_instance_pool_id", None),
            driver_node_type_id=d.get("driver_node_type_id", None),
            gcp_attributes=GcpAttributes.from_dict(d["gcp_attributes"])
            if "gcp_attributes" in d
            else None,
            instance_pool_id=d.get("instance_pool_id", None),
            label=d.get("label", None),
            node_type_id=d.get("node_type_id", None),
            num_workers=d.get("num_workers", None),
            policy_id=d.get("policy_id", None),
            spark_conf=d.get("spark_conf", None),
            spark_env_vars=d.get("spark_env_vars", None),
            ssh_public_keys=d.get("ssh_public_keys", None),
        )


@dataclass
class PipelineLibrary:

    # URI of the jar to be installed. Currently only DBFS and S3 URIs are
    # supported. For example: `{ "jar": "dbfs:/mnt/databricks/library.jar" }` or
    # `{ "jar": "s3://my-bucket/library.jar" }`. If S3 is used, please make sure
    # the cluster has read access on the library. You may need to launch the
    # cluster with an IAM role to access the S3 URI.
    jar: str
    # Specification of a maven library to be installed. For example: `{
    # "coordinates": "org.jsoup:jsoup:1.7.2" }`
    maven: "MavenLibrary"
    # The path to a notebook that defines a pipeline and is stored in the
    # Databricks workspace. For example: `{ "notebook" : { "path" :
    # "/my-pipeline-notebook-path" } }`. Currently, only Scala notebooks are
    # supported, and pipelines must be defined in a package cell.
    notebook: "NotebookLibrary"
    # URI of the wheel to be installed. For example: `{ "whl": "dbfs:/my/whl" }`
    # or `{ "whl": "s3://my-bucket/whl" }`. If S3 is used, please make sure the
    # cluster has read access on the library. You may need to launch the cluster
    # with an IAM role to access the S3 URI.
    whl: str

    def as_request(self) -> (dict, dict):
        pipelineLibrary_query, pipelineLibrary_body = {}, {}
        if self.jar:
            pipelineLibrary_body["jar"] = self.jar
        if self.maven:
            pipelineLibrary_body["maven"] = self.maven
        if self.notebook:
            pipelineLibrary_body["notebook"] = self.notebook.as_request()[1]
        if self.whl:
            pipelineLibrary_body["whl"] = self.whl

        return pipelineLibrary_query, pipelineLibrary_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PipelineLibrary":
        return cls(
            jar=d.get("jar", None),
            maven=MavenLibrary.from_dict(d["maven"]) if "maven" in d else None,
            notebook=NotebookLibrary.from_dict(d["notebook"])
            if "notebook" in d
            else None,
            whl=d.get("whl", None),
        )


@dataclass
class PipelineSpec:

    # Catalog in UC to add tables to. If target is specified, tables in this
    # pipeline will be published to a "target" schema inside catalog (i.e.
    # <catalog>.<target>.<table>).
    catalog: str
    # DLT Release Channel that specifies which version to use.
    channel: str
    # Cluster settings for this pipeline deployment.
    clusters: "List[PipelineCluster]"
    # String-String configuration for this pipeline execution.
    configuration: "Dict[str,str]"
    # Whether the pipeline is continuous or triggered. This replaces `trigger`.
    continuous: bool
    # Whether the pipeline is in Development mode. Defaults to false.
    development: bool
    # Pipeline product edition.
    edition: str
    # Filters on which Pipeline packages to include in the deployed graph.
    filters: "Filters"
    # Unique identifier for this pipeline.
    id: str
    # Libraries or code needed by this deployment.
    libraries: "List[PipelineLibrary]"
    # Friendly identifier for this pipeline.
    name: str
    # Whether Photon is enabled for this pipeline.
    photon: bool
    # DBFS root directory for storing checkpoints and tables.
    storage: str
    # Target schema (database) to add tables in this pipeline to.
    target: str
    # Which pipeline trigger to use. Deprecated: Use `continuous` instead.
    trigger: "PipelineTrigger"

    def as_request(self) -> (dict, dict):
        pipelineSpec_query, pipelineSpec_body = {}, {}
        if self.catalog:
            pipelineSpec_body["catalog"] = self.catalog
        if self.channel:
            pipelineSpec_body["channel"] = self.channel
        if self.clusters:
            pipelineSpec_body["clusters"] = [v.as_request()[1] for v in self.clusters]
        if self.configuration:
            pipelineSpec_body["configuration"] = self.configuration
        if self.continuous:
            pipelineSpec_body["continuous"] = self.continuous
        if self.development:
            pipelineSpec_body["development"] = self.development
        if self.edition:
            pipelineSpec_body["edition"] = self.edition
        if self.filters:
            pipelineSpec_body["filters"] = self.filters.as_request()[1]
        if self.id:
            pipelineSpec_body["id"] = self.id
        if self.libraries:
            pipelineSpec_body["libraries"] = [v.as_request()[1] for v in self.libraries]
        if self.name:
            pipelineSpec_body["name"] = self.name
        if self.photon:
            pipelineSpec_body["photon"] = self.photon
        if self.storage:
            pipelineSpec_body["storage"] = self.storage
        if self.target:
            pipelineSpec_body["target"] = self.target
        if self.trigger:
            pipelineSpec_body["trigger"] = self.trigger.as_request()[1]

        return pipelineSpec_query, pipelineSpec_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PipelineSpec":
        return cls(
            catalog=d.get("catalog", None),
            channel=d.get("channel", None),
            clusters=[PipelineCluster.from_dict(v) for v in d["clusters"]]
            if "clusters" in d
            else None,
            configuration=d.get("configuration", None),
            continuous=d.get("continuous", None),
            development=d.get("development", None),
            edition=d.get("edition", None),
            filters=Filters.from_dict(d["filters"]) if "filters" in d else None,
            id=d.get("id", None),
            libraries=[PipelineLibrary.from_dict(v) for v in d["libraries"]]
            if "libraries" in d
            else None,
            name=d.get("name", None),
            photon=d.get("photon", None),
            storage=d.get("storage", None),
            target=d.get("target", None),
            trigger=PipelineTrigger.from_dict(d["trigger"]) if "trigger" in d else None,
        )


class PipelineState(Enum):
    """The pipeline state."""

    DELETED = "DELETED"
    DEPLOYING = "DEPLOYING"
    FAILED = "FAILED"
    IDLE = "IDLE"
    RECOVERING = "RECOVERING"
    RESETTING = "RESETTING"
    RUNNING = "RUNNING"
    STARTING = "STARTING"
    STOPPING = "STOPPING"


@dataclass
class PipelineStateInfo:

    # The unique identifier of the cluster running the pipeline.
    cluster_id: str
    # The username of the pipeline creator.
    creator_user_name: str
    # Status of the latest updates for the pipeline. Ordered with the newest
    # update first.
    latest_updates: "List[UpdateStateInfo]"
    # The user-friendly name of the pipeline.
    name: str
    # The unique identifier of the pipeline.
    pipeline_id: str
    # The username that the pipeline runs as. This is a read only value derived
    # from the pipeline owner.
    run_as_user_name: str
    # The pipeline state.
    state: "PipelineState"

    def as_request(self) -> (dict, dict):
        pipelineStateInfo_query, pipelineStateInfo_body = {}, {}
        if self.cluster_id:
            pipelineStateInfo_body["cluster_id"] = self.cluster_id
        if self.creator_user_name:
            pipelineStateInfo_body["creator_user_name"] = self.creator_user_name
        if self.latest_updates:
            pipelineStateInfo_body["latest_updates"] = [
                v.as_request()[1] for v in self.latest_updates
            ]
        if self.name:
            pipelineStateInfo_body["name"] = self.name
        if self.pipeline_id:
            pipelineStateInfo_body["pipeline_id"] = self.pipeline_id
        if self.run_as_user_name:
            pipelineStateInfo_body["run_as_user_name"] = self.run_as_user_name
        if self.state:
            pipelineStateInfo_body["state"] = self.state.value

        return pipelineStateInfo_query, pipelineStateInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PipelineStateInfo":
        return cls(
            cluster_id=d.get("cluster_id", None),
            creator_user_name=d.get("creator_user_name", None),
            latest_updates=[UpdateStateInfo.from_dict(v) for v in d["latest_updates"]]
            if "latest_updates" in d
            else None,
            name=d.get("name", None),
            pipeline_id=d.get("pipeline_id", None),
            run_as_user_name=d.get("run_as_user_name", None),
            state=PipelineState(d["state"]) if "state" in d else None,
        )


@dataclass
class PipelineTrigger:

    cron: "CronTrigger"

    manual: Any

    def as_request(self) -> (dict, dict):
        pipelineTrigger_query, pipelineTrigger_body = {}, {}
        if self.cron:
            pipelineTrigger_body["cron"] = self.cron.as_request()[1]
        if self.manual:
            pipelineTrigger_body["manual"] = self.manual

        return pipelineTrigger_query, pipelineTrigger_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PipelineTrigger":
        return cls(
            cron=CronTrigger.from_dict(d["cron"]) if "cron" in d else None,
            manual=d.get("manual", None),
        )


@dataclass
class Reset:
    """Reset a pipeline"""

    pipeline_id: str  # path

    def as_request(self) -> (dict, dict):
        reset_query, reset_body = {}, {}
        if self.pipeline_id:
            reset_body["pipeline_id"] = self.pipeline_id

        return reset_query, reset_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Reset":
        return cls(
            pipeline_id=d.get("pipeline_id", None),
        )


@dataclass
class StartUpdate:

    cause: "StartUpdateCause"
    # If true, this update will reset all tables before running.
    full_refresh: bool
    # A list of tables to update with fullRefresh. If both refresh_selection and
    # full_refresh_selection are empty, this is a full graph update. Full
    # Refresh on a table means that the states of the table will be reset before
    # the refresh.
    full_refresh_selection: "List[str]"

    pipeline_id: str  # path
    # A list of tables to update without fullRefresh. If both refresh_selection
    # and full_refresh_selection are empty, this is a full graph update. Full
    # Refresh on a table means that the states of the table will be reset before
    # the refresh.
    refresh_selection: "List[str]"

    def as_request(self) -> (dict, dict):
        startUpdate_query, startUpdate_body = {}, {}
        if self.cause:
            startUpdate_body["cause"] = self.cause.value
        if self.full_refresh:
            startUpdate_body["full_refresh"] = self.full_refresh
        if self.full_refresh_selection:
            startUpdate_body["full_refresh_selection"] = [
                v for v in self.full_refresh_selection
            ]
        if self.pipeline_id:
            startUpdate_body["pipeline_id"] = self.pipeline_id
        if self.refresh_selection:
            startUpdate_body["refresh_selection"] = [v for v in self.refresh_selection]

        return startUpdate_query, startUpdate_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "StartUpdate":
        return cls(
            cause=StartUpdateCause(d["cause"]) if "cause" in d else None,
            full_refresh=d.get("full_refresh", None),
            full_refresh_selection=d.get("full_refresh_selection", None),
            pipeline_id=d.get("pipeline_id", None),
            refresh_selection=d.get("refresh_selection", None),
        )


class StartUpdateCause(Enum):

    API_CALL = "API_CALL"
    JOB_TASK = "JOB_TASK"
    RETRY_ON_FAILURE = "RETRY_ON_FAILURE"
    SCHEMA_CHANGE = "SCHEMA_CHANGE"
    SERVICE_UPGRADE = "SERVICE_UPGRADE"
    USER_ACTION = "USER_ACTION"


@dataclass
class StartUpdateResponse:

    update_id: str

    def as_request(self) -> (dict, dict):
        startUpdateResponse_query, startUpdateResponse_body = {}, {}
        if self.update_id:
            startUpdateResponse_body["update_id"] = self.update_id

        return startUpdateResponse_query, startUpdateResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "StartUpdateResponse":
        return cls(
            update_id=d.get("update_id", None),
        )


@dataclass
class Stop:
    """Stop a pipeline"""

    pipeline_id: str  # path

    def as_request(self) -> (dict, dict):
        stop_query, stop_body = {}, {}
        if self.pipeline_id:
            stop_body["pipeline_id"] = self.pipeline_id

        return stop_query, stop_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Stop":
        return cls(
            pipeline_id=d.get("pipeline_id", None),
        )


@dataclass
class UpdateInfo:

    # What triggered this update.
    cause: "UpdateInfoCause"
    # The ID of the cluster that the update is running on.
    cluster_id: str
    # The pipeline configuration with system defaults applied where unspecified
    # by the user. Not returned by ListUpdates.
    config: "PipelineSpec"
    # The time when this update was created.
    creation_time: int
    # If true, this update will reset all tables before running.
    full_refresh: bool
    # A list of tables to update with fullRefresh. If both refresh_selection and
    # full_refresh_selection are empty, this is a full graph update. Full
    # Refresh on a table means that the states of the table will be reset before
    # the refresh.
    full_refresh_selection: "List[str]"
    # The ID of the pipeline.
    pipeline_id: str
    # A list of tables to update without fullRefresh. If both refresh_selection
    # and full_refresh_selection are empty, this is a full graph update. Full
    # Refresh on a table means that the states of the table will be reset before
    # the refresh.
    refresh_selection: "List[str]"
    # The update state.
    state: "UpdateInfoState"
    # The ID of this update.
    update_id: str

    def as_request(self) -> (dict, dict):
        updateInfo_query, updateInfo_body = {}, {}
        if self.cause:
            updateInfo_body["cause"] = self.cause.value
        if self.cluster_id:
            updateInfo_body["cluster_id"] = self.cluster_id
        if self.config:
            updateInfo_body["config"] = self.config.as_request()[1]
        if self.creation_time:
            updateInfo_body["creation_time"] = self.creation_time
        if self.full_refresh:
            updateInfo_body["full_refresh"] = self.full_refresh
        if self.full_refresh_selection:
            updateInfo_body["full_refresh_selection"] = [
                v for v in self.full_refresh_selection
            ]
        if self.pipeline_id:
            updateInfo_body["pipeline_id"] = self.pipeline_id
        if self.refresh_selection:
            updateInfo_body["refresh_selection"] = [v for v in self.refresh_selection]
        if self.state:
            updateInfo_body["state"] = self.state.value
        if self.update_id:
            updateInfo_body["update_id"] = self.update_id

        return updateInfo_query, updateInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateInfo":
        return cls(
            cause=UpdateInfoCause(d["cause"]) if "cause" in d else None,
            cluster_id=d.get("cluster_id", None),
            config=PipelineSpec.from_dict(d["config"]) if "config" in d else None,
            creation_time=d.get("creation_time", None),
            full_refresh=d.get("full_refresh", None),
            full_refresh_selection=d.get("full_refresh_selection", None),
            pipeline_id=d.get("pipeline_id", None),
            refresh_selection=d.get("refresh_selection", None),
            state=UpdateInfoState(d["state"]) if "state" in d else None,
            update_id=d.get("update_id", None),
        )


class UpdateInfoCause(Enum):
    """What triggered this update."""

    API_CALL = "API_CALL"
    JOB_TASK = "JOB_TASK"
    RETRY_ON_FAILURE = "RETRY_ON_FAILURE"
    SCHEMA_CHANGE = "SCHEMA_CHANGE"
    SERVICE_UPGRADE = "SERVICE_UPGRADE"
    USER_ACTION = "USER_ACTION"


class UpdateInfoState(Enum):
    """The update state."""

    CANCELED = "CANCELED"
    COMPLETED = "COMPLETED"
    CREATED = "CREATED"
    FAILED = "FAILED"
    INITIALIZING = "INITIALIZING"
    QUEUED = "QUEUED"
    RESETTING = "RESETTING"
    RUNNING = "RUNNING"
    SETTING_UP_TABLES = "SETTING_UP_TABLES"
    STOPPING = "STOPPING"
    WAITING_FOR_RESOURCES = "WAITING_FOR_RESOURCES"


@dataclass
class UpdateStateInfo:

    creation_time: str

    state: "UpdateStateInfoState"

    update_id: str

    def as_request(self) -> (dict, dict):
        updateStateInfo_query, updateStateInfo_body = {}, {}
        if self.creation_time:
            updateStateInfo_body["creation_time"] = self.creation_time
        if self.state:
            updateStateInfo_body["state"] = self.state.value
        if self.update_id:
            updateStateInfo_body["update_id"] = self.update_id

        return updateStateInfo_query, updateStateInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateStateInfo":
        return cls(
            creation_time=d.get("creation_time", None),
            state=UpdateStateInfoState(d["state"]) if "state" in d else None,
            update_id=d.get("update_id", None),
        )


class UpdateStateInfoState(Enum):

    CANCELED = "CANCELED"
    COMPLETED = "COMPLETED"
    CREATED = "CREATED"
    FAILED = "FAILED"
    INITIALIZING = "INITIALIZING"
    QUEUED = "QUEUED"
    RESETTING = "RESETTING"
    RUNNING = "RUNNING"
    SETTING_UP_TABLES = "SETTING_UP_TABLES"
    STOPPING = "STOPPING"
    WAITING_FOR_RESOURCES = "WAITING_FOR_RESOURCES"


class PipelinesAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreatePipeline) -> CreatePipelineResponse:
        """Create a pipeline.

        Creates a new data processing pipeline based on the requested
        configuration. If successful, this method returns the ID of the new
        pipeline."""
        query, body = request.as_request()
        json = self._api.do("POST", "/api/2.0/pipelines", query=query, body=body)
        return CreatePipelineResponse.from_dict(json)

    def delete(self, request: Delete):
        """Delete a pipeline.

        Deletes a pipeline."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/pipelines/{request.pipeline_id}",
            query=query,
            body=body,
        )

    def get(self, request: Get) -> GetPipelineResponse:
        """Get a pipeline."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", f"/api/2.0/pipelines/{request.pipeline_id}", query=query, body=body
        )
        return GetPipelineResponse.from_dict(json)

    def get_update(self, request: GetUpdate) -> GetUpdateResponse:
        """Get a pipeline update.

        Gets an update from an active pipeline."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/pipelines/{request.pipeline_id}/updates/{request.update_id}",
            query=query,
            body=body,
        )
        return GetUpdateResponse.from_dict(json)

    def list_pipelines(self, request: ListPipelines) -> ListPipelinesResponse:
        """List pipelines.

        Lists pipelines defined in the Delta Live Tables system."""
        query, body = request.as_request()
        json = self._api.do("GET", "/api/2.0/pipelines", query=query, body=body)
        return ListPipelinesResponse.from_dict(json)

    def list_updates(self, request: ListUpdates) -> ListUpdatesResponse:
        """List pipeline updates.

        List updates for an active pipeline."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/pipelines/{request.pipeline_id}/updates",
            query=query,
            body=body,
        )
        return ListUpdatesResponse.from_dict(json)

    def reset(self, request: Reset):
        """Reset a pipeline.

        Resets a pipeline."""
        query, body = request.as_request()
        self._api.do(
            "POST",
            f"/api/2.0/pipelines/{request.pipeline_id}/reset",
            query=query,
            body=body,
        )

    def start_update(self, request: StartUpdate) -> StartUpdateResponse:
        """Queue a pipeline update.

        Starts or queues a pipeline update."""
        query, body = request.as_request()
        json = self._api.do(
            "POST",
            f"/api/2.0/pipelines/{request.pipeline_id}/updates",
            query=query,
            body=body,
        )
        return StartUpdateResponse.from_dict(json)

    def stop(self, request: Stop):
        """Stop a pipeline.

        Stops a pipeline."""
        query, body = request.as_request()
        self._api.do(
            "POST",
            f"/api/2.0/pipelines/{request.pipeline_id}/stop",
            query=query,
            body=body,
        )

    def update(self, request: EditPipeline):
        """Edit a pipeline.

        Updates a pipeline with the supplied configuration."""
        query, body = request.as_request()
        self._api.do(
            "PUT", f"/api/2.0/pipelines/{request.pipeline_id}", query=query, body=body
        )

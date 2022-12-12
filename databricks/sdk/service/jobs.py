# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


from .clusters import CreateCluster
from .libraries import Library
from .permissions import AccessControlRequest

# all definitions in this file are in alphabetical order


@dataclass
class CancelAllRuns:

    # The canonical identifier of the job to cancel all runs of. This field is
    # required.
    job_id: int

    def as_request(self) -> (dict, dict):
        cancelAllRuns_query, cancelAllRuns_body = {}, {}
        if self.job_id:
            cancelAllRuns_body["job_id"] = self.job_id

        return cancelAllRuns_query, cancelAllRuns_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CancelAllRuns":
        return cls(
            job_id=d.get("job_id", None),
        )


@dataclass
class CancelRun:

    # This field is required.
    run_id: int

    def as_request(self) -> (dict, dict):
        cancelRun_query, cancelRun_body = {}, {}
        if self.run_id:
            cancelRun_body["run_id"] = self.run_id

        return cancelRun_query, cancelRun_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CancelRun":
        return cls(
            run_id=d.get("run_id", None),
        )


@dataclass
class ClusterInstance:

    # The canonical identifier for the cluster used by a run. This field is
    # always available for runs on existing clusters. For runs on new clusters,
    # it becomes available once the cluster is created. This value can be used
    # to view logs by browsing to `/#setting/sparkui/$cluster_id/driver-logs`.
    # The logs continue to be available after the run completes.
    #
    # The response won’t include this field if the identifier is not available
    # yet.
    cluster_id: str
    # The canonical identifier for the Spark context used by a run. This field
    # is filled in once the run begins execution. This value can be used to view
    # the Spark UI by browsing to
    # `/#setting/sparkui/$cluster_id/$spark_context_id`. The Spark UI continues
    # to be available after the run has completed.
    #
    # The response won’t include this field if the identifier is not available
    # yet.
    spark_context_id: str

    def as_request(self) -> (dict, dict):
        clusterInstance_query, clusterInstance_body = {}, {}
        if self.cluster_id:
            clusterInstance_body["cluster_id"] = self.cluster_id
        if self.spark_context_id:
            clusterInstance_body["spark_context_id"] = self.spark_context_id

        return clusterInstance_query, clusterInstance_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ClusterInstance":
        return cls(
            cluster_id=d.get("cluster_id", None),
            spark_context_id=d.get("spark_context_id", None),
        )


@dataclass
class ClusterSpec:

    # If existing_cluster_id, the ID of an existing cluster that is used for all
    # runs of this job. When running jobs on an existing cluster, you may need
    # to manually restart the cluster if it stops responding. We suggest running
    # jobs on new clusters for greater reliability
    existing_cluster_id: str
    # An optional list of libraries to be installed on the cluster that executes
    # the job. The default value is an empty list.
    libraries: "List[Library]"
    # If new_cluster, a description of a cluster that is created for each run.
    new_cluster: "CreateCluster"

    def as_request(self) -> (dict, dict):
        clusterSpec_query, clusterSpec_body = {}, {}
        if self.existing_cluster_id:
            clusterSpec_body["existing_cluster_id"] = self.existing_cluster_id
        if self.libraries:
            clusterSpec_body["libraries"] = [v for v in self.libraries]
        if self.new_cluster:
            clusterSpec_body["new_cluster"] = self.new_cluster

        return clusterSpec_query, clusterSpec_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ClusterSpec":
        return cls(
            existing_cluster_id=d.get("existing_cluster_id", None),
            libraries=d.get("libraries", None),
            new_cluster=CreateCluster.from_dict(d["new_cluster"])
            if "new_cluster" in d
            else None,
        )


@dataclass
class CreateJob:

    # List of permissions to set on the job.
    access_control_list: "List[AccessControlRequest]"
    # An optional set of email addresses that is notified when runs of this job
    # begin or complete as well as when this job is deleted. The default
    # behavior is to not send any emails.
    email_notifications: "JobEmailNotifications"
    # Used to tell what is the format of the job. This field is ignored in
    # Create/Update/Reset calls. When using the Jobs API 2.1 this value is
    # always set to `"MULTI_TASK"`.
    format: "CreateJobFormat"
    # An optional specification for a remote repository containing the notebooks
    # used by this job's notebook tasks.
    git_source: "GitSource"
    # A list of job cluster specifications that can be shared and reused by
    # tasks of this job. Libraries cannot be declared in a shared job cluster.
    # You must declare dependent libraries in task settings.
    job_clusters: "List[JobCluster]"
    # An optional maximum allowed number of concurrent runs of the job.
    #
    # Set this value if you want to be able to execute multiple runs of the same
    # job concurrently. This is useful for example if you trigger your job on a
    # frequent schedule and want to allow consecutive runs to overlap with each
    # other, or if you want to trigger multiple runs which differ by their input
    # parameters.
    #
    # This setting affects only new runs. For example, suppose the job’s
    # concurrency is 4 and there are 4 concurrent active runs. Then setting the
    # concurrency to 3 won’t kill any of the active runs. However, from then
    # on, new runs are skipped unless there are fewer than 3 active runs.
    #
    # This value cannot exceed 1000\. Setting this value to 0 causes all new
    # runs to be skipped. The default behavior is to allow only 1 concurrent
    # run.
    max_concurrent_runs: int
    # An optional name for the job.
    name: str
    # An optional periodic schedule for this job. The default behavior is that
    # the job only runs when triggered by clicking “Run Now” in the Jobs UI
    # or sending an API request to `runNow`.
    schedule: "CronSchedule"
    # A map of tags associated with the job. These are forwarded to the cluster
    # as cluster tags for jobs clusters, and are subject to the same limitations
    # as cluster tags. A maximum of 25 tags can be added to the job.
    tags: "Dict[str,str]"
    # A list of task specifications to be executed by this job.
    tasks: "List[JobTaskSettings]"
    # An optional timeout applied to each run of this job. The default behavior
    # is to have no timeout.
    timeout_seconds: int
    # A collection of system notification IDs to notify when the run begins or
    # completes. The default behavior is to not send any system notifications.
    webhook_notifications: "JobWebhookNotifications"

    def as_request(self) -> (dict, dict):
        createJob_query, createJob_body = {}, {}
        if self.access_control_list:
            createJob_body["access_control_list"] = [
                v for v in self.access_control_list
            ]
        if self.email_notifications:
            createJob_body[
                "email_notifications"
            ] = self.email_notifications.as_request()[1]
        if self.format:
            createJob_body["format"] = self.format.value
        if self.git_source:
            createJob_body["git_source"] = self.git_source.as_request()[1]
        if self.job_clusters:
            createJob_body["job_clusters"] = [
                v.as_request()[1] for v in self.job_clusters
            ]
        if self.max_concurrent_runs:
            createJob_body["max_concurrent_runs"] = self.max_concurrent_runs
        if self.name:
            createJob_body["name"] = self.name
        if self.schedule:
            createJob_body["schedule"] = self.schedule.as_request()[1]
        if self.tags:
            createJob_body["tags"] = self.tags
        if self.tasks:
            createJob_body["tasks"] = [v.as_request()[1] for v in self.tasks]
        if self.timeout_seconds:
            createJob_body["timeout_seconds"] = self.timeout_seconds
        if self.webhook_notifications:
            createJob_body[
                "webhook_notifications"
            ] = self.webhook_notifications.as_request()[1]

        return createJob_query, createJob_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateJob":
        return cls(
            access_control_list=d.get("access_control_list", None),
            email_notifications=JobEmailNotifications.from_dict(
                d["email_notifications"]
            )
            if "email_notifications" in d
            else None,
            format=CreateJobFormat(d["format"]) if "format" in d else None,
            git_source=GitSource.from_dict(d["git_source"])
            if "git_source" in d
            else None,
            job_clusters=[JobCluster.from_dict(v) for v in d["job_clusters"]]
            if "job_clusters" in d
            else None,
            max_concurrent_runs=d.get("max_concurrent_runs", None),
            name=d.get("name", None),
            schedule=CronSchedule.from_dict(d["schedule"]) if "schedule" in d else None,
            tags=d.get("tags", None),
            tasks=[JobTaskSettings.from_dict(v) for v in d["tasks"]]
            if "tasks" in d
            else None,
            timeout_seconds=d.get("timeout_seconds", None),
            webhook_notifications=JobWebhookNotifications.from_dict(
                d["webhook_notifications"]
            )
            if "webhook_notifications" in d
            else None,
        )


class CreateJobFormat(Enum):
    """Used to tell what is the format of the job. This field is ignored in
    Create/Update/Reset calls. When using the Jobs API 2.1 this value is always
    set to `"MULTI_TASK"`."""

    MULTI_TASK = "MULTI_TASK"
    SINGLE_TASK = "SINGLE_TASK"


@dataclass
class CreateResponse:

    # The canonical identifier for the newly created job.
    job_id: int

    def as_request(self) -> (dict, dict):
        createResponse_query, createResponse_body = {}, {}
        if self.job_id:
            createResponse_body["job_id"] = self.job_id

        return createResponse_query, createResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateResponse":
        return cls(
            job_id=d.get("job_id", None),
        )


@dataclass
class CronSchedule:

    # Indicate whether this schedule is paused or not.
    pause_status: "CronSchedulePauseStatus"
    # A Cron expression using Quartz syntax that describes the schedule for a
    # job. See [Cron Trigger] for details. This field is required."
    #
    # [Cron Trigger]: http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html
    quartz_cron_expression: str
    # A Java timezone ID. The schedule for a job is resolved with respect to
    # this timezone. See [Java TimeZone] for details. This field is required.
    #
    # [Java TimeZone]: https://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html
    timezone_id: str

    def as_request(self) -> (dict, dict):
        cronSchedule_query, cronSchedule_body = {}, {}
        if self.pause_status:
            cronSchedule_body["pause_status"] = self.pause_status.value
        if self.quartz_cron_expression:
            cronSchedule_body["quartz_cron_expression"] = self.quartz_cron_expression
        if self.timezone_id:
            cronSchedule_body["timezone_id"] = self.timezone_id

        return cronSchedule_query, cronSchedule_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CronSchedule":
        return cls(
            pause_status=CronSchedulePauseStatus(d["pause_status"])
            if "pause_status" in d
            else None,
            quartz_cron_expression=d.get("quartz_cron_expression", None),
            timezone_id=d.get("timezone_id", None),
        )


class CronSchedulePauseStatus(Enum):
    """Indicate whether this schedule is paused or not."""

    PAUSED = "PAUSED"
    UNPAUSED = "UNPAUSED"


@dataclass
class DbtOutput:

    # An optional map of headers to send when retrieving the artifact from the
    # `artifacts_link`.
    artifacts_headers: Any
    # A pre-signed URL to download the (compressed) dbt artifacts. This link is
    # valid for a limited time (30 minutes). This information is only available
    # after the run has finished.
    artifacts_link: str

    def as_request(self) -> (dict, dict):
        dbtOutput_query, dbtOutput_body = {}, {}
        if self.artifacts_headers:
            dbtOutput_body["artifacts_headers"] = self.artifacts_headers
        if self.artifacts_link:
            dbtOutput_body["artifacts_link"] = self.artifacts_link

        return dbtOutput_query, dbtOutput_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DbtOutput":
        return cls(
            artifacts_headers=d.get("artifacts_headers", None),
            artifacts_link=d.get("artifacts_link", None),
        )


@dataclass
class DbtTask:

    # A list of dbt commands to execute. All commands must start with `dbt`.
    # This parameter must not be empty. A maximum of up to 10 commands can be
    # provided.
    commands: "List[str]"
    # Optional (relative) path to the profiles directory. Can only be specified
    # if no warehouse_id is specified. If no warehouse_id is specified and this
    # folder is unset, the root directory is used.
    profiles_directory: str
    # Optional (relative) path to the project directory, if no value is
    # provided, the root of the git repository is used.
    project_directory: str
    # Optional schema to write to. This parameter is only used when a
    # warehouse_id is also provided. If not provided, the `default` schema is
    # used.
    schema: str
    # ID of the SQL warehouse to connect to. If provided, we automatically
    # generate and provide the profile and connection details to dbt. It can be
    # overridden on a per-command basis by using the `--profiles-dir` command
    # line argument.
    warehouse_id: str

    def as_request(self) -> (dict, dict):
        dbtTask_query, dbtTask_body = {}, {}
        if self.commands:
            dbtTask_body["commands"] = [v for v in self.commands]
        if self.profiles_directory:
            dbtTask_body["profiles_directory"] = self.profiles_directory
        if self.project_directory:
            dbtTask_body["project_directory"] = self.project_directory
        if self.schema:
            dbtTask_body["schema"] = self.schema
        if self.warehouse_id:
            dbtTask_body["warehouse_id"] = self.warehouse_id

        return dbtTask_query, dbtTask_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DbtTask":
        return cls(
            commands=d.get("commands", None),
            profiles_directory=d.get("profiles_directory", None),
            project_directory=d.get("project_directory", None),
            schema=d.get("schema", None),
            warehouse_id=d.get("warehouse_id", None),
        )


@dataclass
class DeleteJob:

    # The canonical identifier of the job to delete. This field is required.
    job_id: int

    def as_request(self) -> (dict, dict):
        deleteJob_query, deleteJob_body = {}, {}
        if self.job_id:
            deleteJob_body["job_id"] = self.job_id

        return deleteJob_query, deleteJob_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteJob":
        return cls(
            job_id=d.get("job_id", None),
        )


@dataclass
class DeleteRun:

    # The canonical identifier of the run for which to retrieve the metadata.
    run_id: int

    def as_request(self) -> (dict, dict):
        deleteRun_query, deleteRun_body = {}, {}
        if self.run_id:
            deleteRun_body["run_id"] = self.run_id

        return deleteRun_query, deleteRun_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteRun":
        return cls(
            run_id=d.get("run_id", None),
        )


@dataclass
class ExportRun:
    """Export and retrieve a job run"""

    # The canonical identifier for the run. This field is required.
    run_id: int  # query
    # Which views to export (CODE, DASHBOARDS, or ALL). Defaults to CODE.
    views_to_export: "ViewsToExport"  # query

    def as_request(self) -> (dict, dict):
        exportRun_query, exportRun_body = {}, {}
        if self.run_id:
            exportRun_query["run_id"] = self.run_id
        if self.views_to_export:
            exportRun_query["views_to_export"] = self.views_to_export.value

        return exportRun_query, exportRun_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ExportRun":
        return cls(
            run_id=d.get("run_id", None),
            views_to_export=ViewsToExport(d["views_to_export"])
            if "views_to_export" in d
            else None,
        )


@dataclass
class ExportRunOutput:

    # The exported content in HTML format (one for every view item).
    views: "List[ViewItem]"

    def as_request(self) -> (dict, dict):
        exportRunOutput_query, exportRunOutput_body = {}, {}
        if self.views:
            exportRunOutput_body["views"] = [v.as_request()[1] for v in self.views]

        return exportRunOutput_query, exportRunOutput_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ExportRunOutput":
        return cls(
            views=[ViewItem.from_dict(v) for v in d["views"]] if "views" in d else None,
        )


@dataclass
class Get:
    """Get a single job"""

    # The canonical identifier of the job to retrieve information about. This
    # field is required.
    job_id: int  # query

    def as_request(self) -> (dict, dict):
        get_query, get_body = {}, {}
        if self.job_id:
            get_query["job_id"] = self.job_id

        return get_query, get_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Get":
        return cls(
            job_id=d.get("job_id", None),
        )


@dataclass
class GetRun:
    """Get a single job run"""

    # Whether to include the repair history in the response.
    include_history: bool  # query
    # The canonical identifier of the run for which to retrieve the metadata.
    # This field is required.
    run_id: int  # query

    def as_request(self) -> (dict, dict):
        getRun_query, getRun_body = {}, {}
        if self.include_history:
            getRun_query["include_history"] = self.include_history
        if self.run_id:
            getRun_query["run_id"] = self.run_id

        return getRun_query, getRun_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetRun":
        return cls(
            include_history=d.get("include_history", None),
            run_id=d.get("run_id", None),
        )


@dataclass
class GetRunOutput:
    """Get the output for a single run"""

    # The canonical identifier for the run. This field is required.
    run_id: int  # query

    def as_request(self) -> (dict, dict):
        getRunOutput_query, getRunOutput_body = {}, {}
        if self.run_id:
            getRunOutput_query["run_id"] = self.run_id

        return getRunOutput_query, getRunOutput_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetRunOutput":
        return cls(
            run_id=d.get("run_id", None),
        )


@dataclass
class GitSnapshot:
    """Read-only state of the remote repository at the time the job was run. This
    field is only included on job runs."""

    # Commit that was used to execute the run. If git_branch was specified, this
    # points to the HEAD of the branch at the time of the run; if git_tag was
    # specified, this points to the commit the tag points to.
    used_commit: str

    def as_request(self) -> (dict, dict):
        gitSnapshot_query, gitSnapshot_body = {}, {}
        if self.used_commit:
            gitSnapshot_body["used_commit"] = self.used_commit

        return gitSnapshot_query, gitSnapshot_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GitSnapshot":
        return cls(
            used_commit=d.get("used_commit", None),
        )


@dataclass
class GitSource:
    """An optional specification for a remote repository containing the notebooks
    used by this job's notebook tasks."""

    # Name of the branch to be checked out and used by this job. This field
    # cannot be specified in conjunction with git_tag or git_commit.
    #
    # The maximum length is 255 characters.
    git_branch: str
    # Commit to be checked out and used by this job. This field cannot be
    # specified in conjunction with git_branch or git_tag. The maximum length is
    # 64 characters.
    git_commit: str
    # Unique identifier of the service used to host the Git repository. The
    # value is case insensitive.
    git_provider: "GitSourceGitProvider"
    # Read-only state of the remote repository at the time the job was run. This
    # field is only included on job runs.
    git_snapshot: "GitSnapshot"
    # Name of the tag to be checked out and used by this job. This field cannot
    # be specified in conjunction with git_branch or git_commit.
    #
    # The maximum length is 255 characters.
    git_tag: str
    # URL of the repository to be cloned by this job. The maximum length is 300
    # characters.
    git_url: str

    def as_request(self) -> (dict, dict):
        gitSource_query, gitSource_body = {}, {}
        if self.git_branch:
            gitSource_body["git_branch"] = self.git_branch
        if self.git_commit:
            gitSource_body["git_commit"] = self.git_commit
        if self.git_provider:
            gitSource_body["git_provider"] = self.git_provider.value
        if self.git_snapshot:
            gitSource_body["git_snapshot"] = self.git_snapshot.as_request()[1]
        if self.git_tag:
            gitSource_body["git_tag"] = self.git_tag
        if self.git_url:
            gitSource_body["git_url"] = self.git_url

        return gitSource_query, gitSource_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GitSource":
        return cls(
            git_branch=d.get("git_branch", None),
            git_commit=d.get("git_commit", None),
            git_provider=GitSourceGitProvider(d["git_provider"])
            if "git_provider" in d
            else None,
            git_snapshot=GitSnapshot.from_dict(d["git_snapshot"])
            if "git_snapshot" in d
            else None,
            git_tag=d.get("git_tag", None),
            git_url=d.get("git_url", None),
        )


class GitSourceGitProvider(Enum):
    """Unique identifier of the service used to host the Git repository. The value
    is case insensitive."""

    awsCodeCommit = "awsCodeCommit"
    azureDevOpsServices = "azureDevOpsServices"
    bitbucketCloud = "bitbucketCloud"
    bitbucketServer = "bitbucketServer"
    gitHub = "gitHub"
    gitHubEnterprise = "gitHubEnterprise"
    gitLab = "gitLab"
    gitLabEnterpriseEdition = "gitLabEnterpriseEdition"


@dataclass
class Job:

    # The time at which this job was created in epoch milliseconds (milliseconds
    # since 1/1/1970 UTC).
    created_time: int
    # The creator user name. This field won’t be included in the response if
    # the user has already been deleted.
    creator_user_name: str
    # The canonical identifier for this job.
    job_id: int
    # The user name that the job runs as. `run_as_user_name` is based on the
    # current job settings, and is set to the creator of the job if job access
    # control is disabled, or the `is_owner` permission if job access control is
    # enabled.
    run_as_user_name: str
    # Settings for this job and all of its runs. These settings can be updated
    # using the `resetJob` method.
    settings: "JobSettings"

    def as_request(self) -> (dict, dict):
        job_query, job_body = {}, {}
        if self.created_time:
            job_body["created_time"] = self.created_time
        if self.creator_user_name:
            job_body["creator_user_name"] = self.creator_user_name
        if self.job_id:
            job_body["job_id"] = self.job_id
        if self.run_as_user_name:
            job_body["run_as_user_name"] = self.run_as_user_name
        if self.settings:
            job_body["settings"] = self.settings.as_request()[1]

        return job_query, job_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Job":
        return cls(
            created_time=d.get("created_time", None),
            creator_user_name=d.get("creator_user_name", None),
            job_id=d.get("job_id", None),
            run_as_user_name=d.get("run_as_user_name", None),
            settings=JobSettings.from_dict(d["settings"]) if "settings" in d else None,
        )


@dataclass
class JobCluster:

    # A unique name for the job cluster. This field is required and must be
    # unique within the job. `JobTaskSettings` may refer to this field to
    # determine which cluster to launch for the task execution.
    job_cluster_key: str

    new_cluster: "CreateCluster"

    def as_request(self) -> (dict, dict):
        jobCluster_query, jobCluster_body = {}, {}
        if self.job_cluster_key:
            jobCluster_body["job_cluster_key"] = self.job_cluster_key
        if self.new_cluster:
            jobCluster_body["new_cluster"] = self.new_cluster

        return jobCluster_query, jobCluster_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "JobCluster":
        return cls(
            job_cluster_key=d.get("job_cluster_key", None),
            new_cluster=CreateCluster.from_dict(d["new_cluster"])
            if "new_cluster" in d
            else None,
        )


@dataclass
class JobEmailNotifications:

    # If true, do not send email to recipients specified in `on_failure` if the
    # run is skipped.
    no_alert_for_skipped_runs: bool
    # A list of email addresses to be notified when a run unsuccessfully
    # completes. A run is considered to have completed unsuccessfully if it ends
    # with an `INTERNAL_ERROR` `life_cycle_state` or a `SKIPPED`, `FAILED`, or
    # `TIMED_OUT` result_state. If this is not specified on job creation, reset,
    # or update the list is empty, and notifications are not sent.
    on_failure: "List[str]"
    # A list of email addresses to be notified when a run begins. If not
    # specified on job creation, reset, or update, the list is empty, and
    # notifications are not sent.
    on_start: "List[str]"
    # A list of email addresses to be notified when a run successfully
    # completes. A run is considered to have completed successfully if it ends
    # with a `TERMINATED` `life_cycle_state` and a `SUCCESSFUL` result_state. If
    # not specified on job creation, reset, or update, the list is empty, and
    # notifications are not sent.
    on_success: "List[str]"

    def as_request(self) -> (dict, dict):
        jobEmailNotifications_query, jobEmailNotifications_body = {}, {}
        if self.no_alert_for_skipped_runs:
            jobEmailNotifications_body[
                "no_alert_for_skipped_runs"
            ] = self.no_alert_for_skipped_runs
        if self.on_failure:
            jobEmailNotifications_body["on_failure"] = [v for v in self.on_failure]
        if self.on_start:
            jobEmailNotifications_body["on_start"] = [v for v in self.on_start]
        if self.on_success:
            jobEmailNotifications_body["on_success"] = [v for v in self.on_success]

        return jobEmailNotifications_query, jobEmailNotifications_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "JobEmailNotifications":
        return cls(
            no_alert_for_skipped_runs=d.get("no_alert_for_skipped_runs", None),
            on_failure=d.get("on_failure", None),
            on_start=d.get("on_start", None),
            on_success=d.get("on_success", None),
        )


@dataclass
class JobSettings:

    # An optional set of email addresses that is notified when runs of this job
    # begin or complete as well as when this job is deleted. The default
    # behavior is to not send any emails.
    email_notifications: "JobEmailNotifications"
    # Used to tell what is the format of the job. This field is ignored in
    # Create/Update/Reset calls. When using the Jobs API 2.1 this value is
    # always set to `"MULTI_TASK"`.
    format: "JobSettingsFormat"
    # An optional specification for a remote repository containing the notebooks
    # used by this job's notebook tasks.
    git_source: "GitSource"
    # A list of job cluster specifications that can be shared and reused by
    # tasks of this job. Libraries cannot be declared in a shared job cluster.
    # You must declare dependent libraries in task settings.
    job_clusters: "List[JobCluster]"
    # An optional maximum allowed number of concurrent runs of the job.
    #
    # Set this value if you want to be able to execute multiple runs of the same
    # job concurrently. This is useful for example if you trigger your job on a
    # frequent schedule and want to allow consecutive runs to overlap with each
    # other, or if you want to trigger multiple runs which differ by their input
    # parameters.
    #
    # This setting affects only new runs. For example, suppose the job’s
    # concurrency is 4 and there are 4 concurrent active runs. Then setting the
    # concurrency to 3 won’t kill any of the active runs. However, from then
    # on, new runs are skipped unless there are fewer than 3 active runs.
    #
    # This value cannot exceed 1000\. Setting this value to 0 causes all new
    # runs to be skipped. The default behavior is to allow only 1 concurrent
    # run.
    max_concurrent_runs: int
    # An optional name for the job.
    name: str
    # An optional periodic schedule for this job. The default behavior is that
    # the job only runs when triggered by clicking “Run Now” in the Jobs UI
    # or sending an API request to `runNow`.
    schedule: "CronSchedule"
    # A map of tags associated with the job. These are forwarded to the cluster
    # as cluster tags for jobs clusters, and are subject to the same limitations
    # as cluster tags. A maximum of 25 tags can be added to the job.
    tags: "Dict[str,str]"
    # A list of task specifications to be executed by this job.
    tasks: "List[JobTaskSettings]"
    # An optional timeout applied to each run of this job. The default behavior
    # is to have no timeout.
    timeout_seconds: int
    # A collection of system notification IDs to notify when the run begins or
    # completes. The default behavior is to not send any system notifications.
    webhook_notifications: "JobWebhookNotifications"

    def as_request(self) -> (dict, dict):
        jobSettings_query, jobSettings_body = {}, {}
        if self.email_notifications:
            jobSettings_body[
                "email_notifications"
            ] = self.email_notifications.as_request()[1]
        if self.format:
            jobSettings_body["format"] = self.format.value
        if self.git_source:
            jobSettings_body["git_source"] = self.git_source.as_request()[1]
        if self.job_clusters:
            jobSettings_body["job_clusters"] = [
                v.as_request()[1] for v in self.job_clusters
            ]
        if self.max_concurrent_runs:
            jobSettings_body["max_concurrent_runs"] = self.max_concurrent_runs
        if self.name:
            jobSettings_body["name"] = self.name
        if self.schedule:
            jobSettings_body["schedule"] = self.schedule.as_request()[1]
        if self.tags:
            jobSettings_body["tags"] = self.tags
        if self.tasks:
            jobSettings_body["tasks"] = [v.as_request()[1] for v in self.tasks]
        if self.timeout_seconds:
            jobSettings_body["timeout_seconds"] = self.timeout_seconds
        if self.webhook_notifications:
            jobSettings_body[
                "webhook_notifications"
            ] = self.webhook_notifications.as_request()[1]

        return jobSettings_query, jobSettings_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "JobSettings":
        return cls(
            email_notifications=JobEmailNotifications.from_dict(
                d["email_notifications"]
            )
            if "email_notifications" in d
            else None,
            format=JobSettingsFormat(d["format"]) if "format" in d else None,
            git_source=GitSource.from_dict(d["git_source"])
            if "git_source" in d
            else None,
            job_clusters=[JobCluster.from_dict(v) for v in d["job_clusters"]]
            if "job_clusters" in d
            else None,
            max_concurrent_runs=d.get("max_concurrent_runs", None),
            name=d.get("name", None),
            schedule=CronSchedule.from_dict(d["schedule"]) if "schedule" in d else None,
            tags=d.get("tags", None),
            tasks=[JobTaskSettings.from_dict(v) for v in d["tasks"]]
            if "tasks" in d
            else None,
            timeout_seconds=d.get("timeout_seconds", None),
            webhook_notifications=JobWebhookNotifications.from_dict(
                d["webhook_notifications"]
            )
            if "webhook_notifications" in d
            else None,
        )


class JobSettingsFormat(Enum):
    """Used to tell what is the format of the job. This field is ignored in
    Create/Update/Reset calls. When using the Jobs API 2.1 this value is always
    set to `"MULTI_TASK"`."""

    MULTI_TASK = "MULTI_TASK"
    SINGLE_TASK = "SINGLE_TASK"


@dataclass
class JobTaskSettings:

    # If dbt_task, indicates that this must execute a dbt task. It requires both
    # Databricks SQL and the ability to use a serverless or a pro SQL warehouse.
    dbt_task: "DbtTask"
    # An optional array of objects specifying the dependency graph of the task.
    # All tasks specified in this field must complete successfully before
    # executing this task. The key is `task_key`, and the value is the name
    # assigned to the dependent task. This field is required when a job consists
    # of more than one task.
    depends_on: "List[TaskDependenciesItem]"
    # An optional description for this task. The maximum length is 4096 bytes.
    description: str
    # An optional set of email addresses that is notified when runs of this task
    # begin or complete as well as when this task is deleted. The default
    # behavior is to not send any emails.
    email_notifications: "JobEmailNotifications"
    # If existing_cluster_id, the ID of an existing cluster that is used for all
    # runs of this task. When running tasks on an existing cluster, you may need
    # to manually restart the cluster if it stops responding. We suggest running
    # jobs on new clusters for greater reliability.
    existing_cluster_id: str
    # If job_cluster_key, this task is executed reusing the cluster specified in
    # `job.settings.job_clusters`.
    job_cluster_key: str
    # An optional list of libraries to be installed on the cluster that executes
    # the task. The default value is an empty list.
    libraries: "List[Library]"
    # An optional maximum number of times to retry an unsuccessful run. A run is
    # considered to be unsuccessful if it completes with the `FAILED`
    # result_state or `INTERNAL_ERROR` `life_cycle_state`. The value -1 means to
    # retry indefinitely and the value 0 means to never retry. The default
    # behavior is to never retry.
    max_retries: int
    # An optional minimal interval in milliseconds between the start of the
    # failed run and the subsequent retry run. The default behavior is that
    # unsuccessful runs are immediately retried.
    min_retry_interval_millis: int
    # If new_cluster, a description of a cluster that is created for each run.
    new_cluster: "CreateCluster"
    # If notebook_task, indicates that this task must run a notebook. This field
    # may not be specified in conjunction with spark_jar_task.
    notebook_task: "NotebookTask"
    # If pipeline_task, indicates that this task must execute a Pipeline.
    pipeline_task: "PipelineTask"
    # If python_wheel_task, indicates that this job must execute a PythonWheel.
    python_wheel_task: "PythonWheelTask"
    # An optional policy to specify whether to retry a task when it times out.
    # The default behavior is to not retry on timeout.
    retry_on_timeout: bool
    # If spark_jar_task, indicates that this task must run a JAR.
    spark_jar_task: "SparkJarTask"
    # If spark_python_task, indicates that this task must run a Python file.
    spark_python_task: "SparkPythonTask"
    # If spark_submit_task, indicates that this task must be launched by the
    # spark submit script.
    spark_submit_task: "SparkSubmitTask"
    # If sql_task, indicates that this job must execute a SQL task.
    sql_task: "SqlTask"
    # A unique name for the task. This field is used to refer to this task from
    # other tasks. This field is required and must be unique within its parent
    # job. On Update or Reset, this field is used to reference the tasks to be
    # updated or reset. The maximum length is 100 characters.
    task_key: str
    # An optional timeout applied to each run of this job task. The default
    # behavior is to have no timeout.
    timeout_seconds: int

    def as_request(self) -> (dict, dict):
        jobTaskSettings_query, jobTaskSettings_body = {}, {}
        if self.dbt_task:
            jobTaskSettings_body["dbt_task"] = self.dbt_task.as_request()[1]
        if self.depends_on:
            jobTaskSettings_body["depends_on"] = [
                v.as_request()[1] for v in self.depends_on
            ]
        if self.description:
            jobTaskSettings_body["description"] = self.description
        if self.email_notifications:
            jobTaskSettings_body[
                "email_notifications"
            ] = self.email_notifications.as_request()[1]
        if self.existing_cluster_id:
            jobTaskSettings_body["existing_cluster_id"] = self.existing_cluster_id
        if self.job_cluster_key:
            jobTaskSettings_body["job_cluster_key"] = self.job_cluster_key
        if self.libraries:
            jobTaskSettings_body["libraries"] = [v for v in self.libraries]
        if self.max_retries:
            jobTaskSettings_body["max_retries"] = self.max_retries
        if self.min_retry_interval_millis:
            jobTaskSettings_body[
                "min_retry_interval_millis"
            ] = self.min_retry_interval_millis
        if self.new_cluster:
            jobTaskSettings_body["new_cluster"] = self.new_cluster
        if self.notebook_task:
            jobTaskSettings_body["notebook_task"] = self.notebook_task.as_request()[1]
        if self.pipeline_task:
            jobTaskSettings_body["pipeline_task"] = self.pipeline_task.as_request()[1]
        if self.python_wheel_task:
            jobTaskSettings_body[
                "python_wheel_task"
            ] = self.python_wheel_task.as_request()[1]
        if self.retry_on_timeout:
            jobTaskSettings_body["retry_on_timeout"] = self.retry_on_timeout
        if self.spark_jar_task:
            jobTaskSettings_body["spark_jar_task"] = self.spark_jar_task.as_request()[1]
        if self.spark_python_task:
            jobTaskSettings_body[
                "spark_python_task"
            ] = self.spark_python_task.as_request()[1]
        if self.spark_submit_task:
            jobTaskSettings_body[
                "spark_submit_task"
            ] = self.spark_submit_task.as_request()[1]
        if self.sql_task:
            jobTaskSettings_body["sql_task"] = self.sql_task.as_request()[1]
        if self.task_key:
            jobTaskSettings_body["task_key"] = self.task_key
        if self.timeout_seconds:
            jobTaskSettings_body["timeout_seconds"] = self.timeout_seconds

        return jobTaskSettings_query, jobTaskSettings_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "JobTaskSettings":
        return cls(
            dbt_task=DbtTask.from_dict(d["dbt_task"]) if "dbt_task" in d else None,
            depends_on=[TaskDependenciesItem.from_dict(v) for v in d["depends_on"]]
            if "depends_on" in d
            else None,
            description=d.get("description", None),
            email_notifications=JobEmailNotifications.from_dict(
                d["email_notifications"]
            )
            if "email_notifications" in d
            else None,
            existing_cluster_id=d.get("existing_cluster_id", None),
            job_cluster_key=d.get("job_cluster_key", None),
            libraries=d.get("libraries", None),
            max_retries=d.get("max_retries", None),
            min_retry_interval_millis=d.get("min_retry_interval_millis", None),
            new_cluster=CreateCluster.from_dict(d["new_cluster"])
            if "new_cluster" in d
            else None,
            notebook_task=NotebookTask.from_dict(d["notebook_task"])
            if "notebook_task" in d
            else None,
            pipeline_task=PipelineTask.from_dict(d["pipeline_task"])
            if "pipeline_task" in d
            else None,
            python_wheel_task=PythonWheelTask.from_dict(d["python_wheel_task"])
            if "python_wheel_task" in d
            else None,
            retry_on_timeout=d.get("retry_on_timeout", None),
            spark_jar_task=SparkJarTask.from_dict(d["spark_jar_task"])
            if "spark_jar_task" in d
            else None,
            spark_python_task=SparkPythonTask.from_dict(d["spark_python_task"])
            if "spark_python_task" in d
            else None,
            spark_submit_task=SparkSubmitTask.from_dict(d["spark_submit_task"])
            if "spark_submit_task" in d
            else None,
            sql_task=SqlTask.from_dict(d["sql_task"]) if "sql_task" in d else None,
            task_key=d.get("task_key", None),
            timeout_seconds=d.get("timeout_seconds", None),
        )


@dataclass
class JobWebhookNotifications:

    # An optional list of system notification IDs to call when the run fails. A
    # maximum of 3 destinations can be specified for the `on_failure` property.
    on_failure: "List[JobWebhookNotificationsOnFailureItem]"
    # An optional list of system notification IDs to call when the run starts. A
    # maximum of 3 destinations can be specified for the `on_start` property.
    on_start: "List[JobWebhookNotificationsOnStartItem]"
    # An optional list of system notification IDs to call when the run completes
    # successfully. A maximum of 3 destinations can be specified for the
    # `on_success` property.
    on_success: "List[JobWebhookNotificationsOnSuccessItem]"

    def as_request(self) -> (dict, dict):
        jobWebhookNotifications_query, jobWebhookNotifications_body = {}, {}
        if self.on_failure:
            jobWebhookNotifications_body["on_failure"] = [
                v.as_request()[1] for v in self.on_failure
            ]
        if self.on_start:
            jobWebhookNotifications_body["on_start"] = [
                v.as_request()[1] for v in self.on_start
            ]
        if self.on_success:
            jobWebhookNotifications_body["on_success"] = [
                v.as_request()[1] for v in self.on_success
            ]

        return jobWebhookNotifications_query, jobWebhookNotifications_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "JobWebhookNotifications":
        return cls(
            on_failure=[
                JobWebhookNotificationsOnFailureItem.from_dict(v)
                for v in d["on_failure"]
            ]
            if "on_failure" in d
            else None,
            on_start=[
                JobWebhookNotificationsOnStartItem.from_dict(v) for v in d["on_start"]
            ]
            if "on_start" in d
            else None,
            on_success=[
                JobWebhookNotificationsOnSuccessItem.from_dict(v)
                for v in d["on_success"]
            ]
            if "on_success" in d
            else None,
        )


@dataclass
class JobWebhookNotificationsOnFailureItem:

    id: str

    def as_request(self) -> (dict, dict):
        (
            jobWebhookNotificationsOnFailureItem_query,
            jobWebhookNotificationsOnFailureItem_body,
        ) = ({}, {})
        if self.id:
            jobWebhookNotificationsOnFailureItem_body["id"] = self.id

        return (
            jobWebhookNotificationsOnFailureItem_query,
            jobWebhookNotificationsOnFailureItem_body,
        )

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "JobWebhookNotificationsOnFailureItem":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class JobWebhookNotificationsOnStartItem:

    id: str

    def as_request(self) -> (dict, dict):
        (
            jobWebhookNotificationsOnStartItem_query,
            jobWebhookNotificationsOnStartItem_body,
        ) = ({}, {})
        if self.id:
            jobWebhookNotificationsOnStartItem_body["id"] = self.id

        return (
            jobWebhookNotificationsOnStartItem_query,
            jobWebhookNotificationsOnStartItem_body,
        )

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "JobWebhookNotificationsOnStartItem":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class JobWebhookNotificationsOnSuccessItem:

    id: str

    def as_request(self) -> (dict, dict):
        (
            jobWebhookNotificationsOnSuccessItem_query,
            jobWebhookNotificationsOnSuccessItem_body,
        ) = ({}, {})
        if self.id:
            jobWebhookNotificationsOnSuccessItem_body["id"] = self.id

        return (
            jobWebhookNotificationsOnSuccessItem_query,
            jobWebhookNotificationsOnSuccessItem_body,
        )

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "JobWebhookNotificationsOnSuccessItem":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class List:
    """List all jobs"""

    # Whether to include task and cluster details in the response.
    expand_tasks: bool  # query
    # The number of jobs to return. This value must be greater than 0 and less
    # or equal to 25. The default value is 20.
    limit: int  # query
    # A filter on the list based on the exact (case insensitive) job name.
    name: str  # query
    # The offset of the first job to return, relative to the most recently
    # created job.
    offset: int  # query

    def as_request(self) -> (dict, dict):
        list_query, list_body = {}, {}
        if self.expand_tasks:
            list_query["expand_tasks"] = self.expand_tasks
        if self.limit:
            list_query["limit"] = self.limit
        if self.name:
            list_query["name"] = self.name
        if self.offset:
            list_query["offset"] = self.offset

        return list_query, list_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "List":
        return cls(
            expand_tasks=d.get("expand_tasks", None),
            limit=d.get("limit", None),
            name=d.get("name", None),
            offset=d.get("offset", None),
        )


@dataclass
class ListJobsResponse:

    has_more: bool
    # The list of jobs.
    jobs: "List[Job]"

    def as_request(self) -> (dict, dict):
        listJobsResponse_query, listJobsResponse_body = {}, {}
        if self.has_more:
            listJobsResponse_body["has_more"] = self.has_more
        if self.jobs:
            listJobsResponse_body["jobs"] = [v.as_request()[1] for v in self.jobs]

        return listJobsResponse_query, listJobsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListJobsResponse":
        return cls(
            has_more=d.get("has_more", None),
            jobs=[Job.from_dict(v) for v in d["jobs"]] if "jobs" in d else None,
        )


@dataclass
class ListRuns:
    """List runs for a job"""

    # If active_only is `true`, only active runs are included in the results;
    # otherwise, lists both active and completed runs. An active run is a run in
    # the `PENDING`, `RUNNING`, or `TERMINATING`. This field cannot be `true`
    # when completed_only is `true`.
    active_only: bool  # query
    # If completed_only is `true`, only completed runs are included in the
    # results; otherwise, lists both active and completed runs. This field
    # cannot be `true` when active_only is `true`.
    completed_only: bool  # query
    # Whether to include task and cluster details in the response.
    expand_tasks: bool  # query
    # The job for which to list runs. If omitted, the Jobs service lists runs
    # from all jobs.
    job_id: int  # query
    # The number of runs to return. This value must be greater than 0 and less
    # than 25. The default value is 25. If a request specifies a limit of 0, the
    # service instead uses the maximum limit.
    limit: int  # query
    # The offset of the first run to return, relative to the most recent run.
    offset: int  # query
    # The type of runs to return. For a description of run types, see
    # :method:getRun.
    run_type: "ListRunsRunType"  # query
    # Show runs that started _at or after_ this value. The value must be a UTC
    # timestamp in milliseconds. Can be combined with _start_time_to_ to filter
    # by a time range.
    start_time_from: int  # query
    # Show runs that started _at or before_ this value. The value must be a UTC
    # timestamp in milliseconds. Can be combined with _start_time_from_ to
    # filter by a time range.
    start_time_to: int  # query

    def as_request(self) -> (dict, dict):
        listRuns_query, listRuns_body = {}, {}
        if self.active_only:
            listRuns_query["active_only"] = self.active_only
        if self.completed_only:
            listRuns_query["completed_only"] = self.completed_only
        if self.expand_tasks:
            listRuns_query["expand_tasks"] = self.expand_tasks
        if self.job_id:
            listRuns_query["job_id"] = self.job_id
        if self.limit:
            listRuns_query["limit"] = self.limit
        if self.offset:
            listRuns_query["offset"] = self.offset
        if self.run_type:
            listRuns_query["run_type"] = self.run_type.value
        if self.start_time_from:
            listRuns_query["start_time_from"] = self.start_time_from
        if self.start_time_to:
            listRuns_query["start_time_to"] = self.start_time_to

        return listRuns_query, listRuns_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListRuns":
        return cls(
            active_only=d.get("active_only", None),
            completed_only=d.get("completed_only", None),
            expand_tasks=d.get("expand_tasks", None),
            job_id=d.get("job_id", None),
            limit=d.get("limit", None),
            offset=d.get("offset", None),
            run_type=ListRunsRunType(d["run_type"]) if "run_type" in d else None,
            start_time_from=d.get("start_time_from", None),
            start_time_to=d.get("start_time_to", None),
        )


@dataclass
class ListRunsResponse:

    # If true, additional runs matching the provided filter are available for
    # listing.
    has_more: bool
    # A list of runs, from most recently started to least.
    runs: "List[Run]"

    def as_request(self) -> (dict, dict):
        listRunsResponse_query, listRunsResponse_body = {}, {}
        if self.has_more:
            listRunsResponse_body["has_more"] = self.has_more
        if self.runs:
            listRunsResponse_body["runs"] = [v.as_request()[1] for v in self.runs]

        return listRunsResponse_query, listRunsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListRunsResponse":
        return cls(
            has_more=d.get("has_more", None),
            runs=[Run.from_dict(v) for v in d["runs"]] if "runs" in d else None,
        )


class ListRunsRunType(Enum):
    """This describes an enum"""

    JOB_RUN = "JOB_RUN"
    SUBMIT_RUN = "SUBMIT_RUN"
    WORKFLOW_RUN = "WORKFLOW_RUN"


@dataclass
class NotebookOutput:

    # The value passed to
    # [dbutils.notebook.exit()](/notebooks/notebook-workflows.html#notebook-workflows-exit).
    # Databricks restricts this API to return the first 5 MB of the value. For a
    # larger result, your job can store the results in a cloud storage service.
    # This field is absent if `dbutils.notebook.exit()` was never called.
    result: str
    # Whether or not the result was truncated.
    truncated: bool

    def as_request(self) -> (dict, dict):
        notebookOutput_query, notebookOutput_body = {}, {}
        if self.result:
            notebookOutput_body["result"] = self.result
        if self.truncated:
            notebookOutput_body["truncated"] = self.truncated

        return notebookOutput_query, notebookOutput_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "NotebookOutput":
        return cls(
            result=d.get("result", None),
            truncated=d.get("truncated", None),
        )


@dataclass
class NotebookTask:

    # Base parameters to be used for each run of this job. If the run is
    # initiated by a call to :method:runNow with parameters specified, the two
    # parameters maps are merged. If the same key is specified in
    # `base_parameters` and in `run-now`, the value from `run-now` is used.
    #
    # Use [Task parameter variables] to set parameters containing information
    # about job runs.
    #
    # If the notebook takes a parameter that is not specified in the job’s
    # `base_parameters` or the `run-now` override parameters, the default value
    # from the notebook is used.
    #
    # Retrieve these parameters in a notebook using [dbutils.widgets.get].
    #
    # [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
    # [dbutils.widgets.get]: https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-widgets
    base_parameters: "Dict[str,Any]"
    # The path of the notebook to be run in the Databricks workspace or remote
    # repository. For notebooks stored in the Databricks workspace, the path
    # must be absolute and begin with a slash. For notebooks stored in a remote
    # repository, the path must be relative. This field is required.
    notebook_path: str
    # This describes an enum
    source: "NotebookTaskSource"

    def as_request(self) -> (dict, dict):
        notebookTask_query, notebookTask_body = {}, {}
        if self.base_parameters:
            notebookTask_body["base_parameters"] = self.base_parameters
        if self.notebook_path:
            notebookTask_body["notebook_path"] = self.notebook_path
        if self.source:
            notebookTask_body["source"] = self.source.value

        return notebookTask_query, notebookTask_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "NotebookTask":
        return cls(
            base_parameters=d.get("base_parameters", None),
            notebook_path=d.get("notebook_path", None),
            source=NotebookTaskSource(d["source"]) if "source" in d else None,
        )


class NotebookTaskSource(Enum):
    """This describes an enum"""

    GIT = "GIT"
    WORKSPACE = "WORKSPACE"


@dataclass
class PipelineParams:

    # If true, triggers a full refresh on the delta live table.
    full_refresh: bool

    def as_request(self) -> (dict, dict):
        pipelineParams_query, pipelineParams_body = {}, {}
        if self.full_refresh:
            pipelineParams_body["full_refresh"] = self.full_refresh

        return pipelineParams_query, pipelineParams_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PipelineParams":
        return cls(
            full_refresh=d.get("full_refresh", None),
        )


@dataclass
class PipelineTask:

    # If true, a full refresh will be triggered on the delta live table.
    full_refresh: bool
    # The full name of the pipeline task to execute.
    pipeline_id: str

    def as_request(self) -> (dict, dict):
        pipelineTask_query, pipelineTask_body = {}, {}
        if self.full_refresh:
            pipelineTask_body["full_refresh"] = self.full_refresh
        if self.pipeline_id:
            pipelineTask_body["pipeline_id"] = self.pipeline_id

        return pipelineTask_query, pipelineTask_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PipelineTask":
        return cls(
            full_refresh=d.get("full_refresh", None),
            pipeline_id=d.get("pipeline_id", None),
        )


@dataclass
class PythonWheelTask:

    # Named entry point to use, if it does not exist in the metadata of the
    # package it executes the function from the package directly using
    # `$packageName.$entryPoint()`
    entry_point: str
    # Command-line parameters passed to Python wheel task in the form of
    # `["--name=task", "--data=dbfs:/path/to/data.json"]`. Leave it empty if
    # `parameters` is not null.
    named_parameters: Any
    # Name of the package to execute
    package_name: str
    # Command-line parameters passed to Python wheel task. Leave it empty if
    # `named_parameters` is not null.
    parameters: "List[str]"

    def as_request(self) -> (dict, dict):
        pythonWheelTask_query, pythonWheelTask_body = {}, {}
        if self.entry_point:
            pythonWheelTask_body["entry_point"] = self.entry_point
        if self.named_parameters:
            pythonWheelTask_body["named_parameters"] = self.named_parameters
        if self.package_name:
            pythonWheelTask_body["package_name"] = self.package_name
        if self.parameters:
            pythonWheelTask_body["parameters"] = [v for v in self.parameters]

        return pythonWheelTask_query, pythonWheelTask_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PythonWheelTask":
        return cls(
            entry_point=d.get("entry_point", None),
            named_parameters=d.get("named_parameters", None),
            package_name=d.get("package_name", None),
            parameters=d.get("parameters", None),
        )


@dataclass
class RepairHistoryItem:

    # The end time of the (repaired) run.
    end_time: int
    # The ID of the repair. Only returned for the items that represent a repair
    # in `repair_history`.
    id: int
    # The start time of the (repaired) run.
    start_time: int
    # The result and lifecycle state of the run.
    state: "RunState"
    # The run IDs of the task runs that ran as part of this repair history item.
    task_run_ids: "List[int]"
    # The repair history item type. Indicates whether a run is the original run
    # or a repair run.
    type: "RepairHistoryItemType"

    def as_request(self) -> (dict, dict):
        repairHistoryItem_query, repairHistoryItem_body = {}, {}
        if self.end_time:
            repairHistoryItem_body["end_time"] = self.end_time
        if self.id:
            repairHistoryItem_body["id"] = self.id
        if self.start_time:
            repairHistoryItem_body["start_time"] = self.start_time
        if self.state:
            repairHistoryItem_body["state"] = self.state.as_request()[1]
        if self.task_run_ids:
            repairHistoryItem_body["task_run_ids"] = [v for v in self.task_run_ids]
        if self.type:
            repairHistoryItem_body["type"] = self.type.value

        return repairHistoryItem_query, repairHistoryItem_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RepairHistoryItem":
        return cls(
            end_time=d.get("end_time", None),
            id=d.get("id", None),
            start_time=d.get("start_time", None),
            state=RunState.from_dict(d["state"]) if "state" in d else None,
            task_run_ids=d.get("task_run_ids", None),
            type=RepairHistoryItemType(d["type"]) if "type" in d else None,
        )


class RepairHistoryItemType(Enum):
    """The repair history item type. Indicates whether a run is the original run or
    a repair run."""

    ORIGINAL = "ORIGINAL"
    REPAIR = "REPAIR"


@dataclass
class RepairRun:

    # An array of commands to execute for jobs with the dbt task, for example
    # `"dbt_commands": ["dbt deps", "dbt seed", "dbt run"]`
    dbt_commands: "List[str]"
    # A list of parameters for jobs with Spark JAR tasks, for example
    # `\"jar_params\": [\"john doe\", \"35\"]`. The parameters are used to
    # invoke the main function of the main class specified in the Spark JAR
    # task. If not specified upon `run-now`, it defaults to an empty list.
    # jar_params cannot be specified in conjunction with notebook_params. The
    # JSON representation of this field (for example `{\"jar_params\":[\"john
    # doe\",\"35\"]}`) cannot exceed 10,000 bytes.
    #
    # Use [Task parameter variables](/jobs.html"#parameter-variables") to set
    # parameters containing information about job runs.
    jar_params: "List[str]"
    # The ID of the latest repair. This parameter is not required when repairing
    # a run for the first time, but must be provided on subsequent requests to
    # repair the same run.
    latest_repair_id: int
    # A map from keys to values for jobs with notebook task, for example
    # `\"notebook_params\": {\"name\": \"john doe\", \"age\": \"35\"}`. The map
    # is passed to the notebook and is accessible through the
    # [dbutils.widgets.get] function.
    #
    # If not specified upon `run-now`, the triggered run uses the job’s base
    # parameters.
    #
    # notebook_params cannot be specified in conjunction with jar_params.
    #
    # Use [Task parameter variables] to set parameters containing information
    # about job runs.
    #
    # The JSON representation of this field (for example
    # `{\"notebook_params\":{\"name\":\"john doe\",\"age\":\"35\"}}`) cannot
    # exceed 10,000 bytes.
    #
    # [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
    # [dbutils.widgets.get]: https://docs.databricks.com/dev-tools/databricks-utils.html
    notebook_params: "Dict[str,str]"

    pipeline_params: "PipelineParams"
    # A map from keys to values for jobs with Python wheel task, for example
    # `"python_named_params": {"name": "task", "data":
    # "dbfs:/path/to/data.json"}`.
    python_named_params: "Dict[str,str]"
    # A list of parameters for jobs with Python tasks, for example
    # `\"python_params\": [\"john doe\", \"35\"]`. The parameters are passed to
    # Python file as command-line parameters. If specified upon `run-now`, it
    # would overwrite the parameters specified in job setting. The JSON
    # representation of this field (for example `{\"python_params\":[\"john
    # doe\",\"35\"]}`) cannot exceed 10,000 bytes.
    #
    # Use [Task parameter variables] to set parameters containing information
    # about job runs.
    #
    # Important
    #
    # These parameters accept only Latin characters (ASCII character set). Using
    # non-ASCII characters returns an error. Examples of invalid, non-ASCII
    # characters are Chinese, Japanese kanjis, and emojis.
    #
    # [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
    python_params: "List[str]"
    # If true, repair all failed tasks. Only one of rerun_tasks or
    # rerun_all_failed_tasks can be used.
    rerun_all_failed_tasks: bool
    # The task keys of the task runs to repair.
    rerun_tasks: "List[str]"
    # The job run ID of the run to repair. The run must not be in progress.
    run_id: int
    # A list of parameters for jobs with spark submit task, for example
    # `\"spark_submit_params\": [\"--class\",
    # \"org.apache.spark.examples.SparkPi\"]`. The parameters are passed to
    # spark-submit script as command-line parameters. If specified upon
    # `run-now`, it would overwrite the parameters specified in job setting. The
    # JSON representation of this field (for example `{\"python_params\":[\"john
    # doe\",\"35\"]}`) cannot exceed 10,000 bytes.
    #
    # Use [Task parameter variables] to set parameters containing information
    # about job runs
    #
    # Important
    #
    # These parameters accept only Latin characters (ASCII character set). Using
    # non-ASCII characters returns an error. Examples of invalid, non-ASCII
    # characters are Chinese, Japanese kanjis, and emojis.
    #
    # [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
    spark_submit_params: "List[str]"
    # A map from keys to values for jobs with SQL task, for example
    # `"sql_params": {"name": "john doe", "age": "35"}`. The SQL alert task does
    # not support custom parameters.
    sql_params: "Dict[str,str]"

    def as_request(self) -> (dict, dict):
        repairRun_query, repairRun_body = {}, {}
        if self.dbt_commands:
            repairRun_body["dbt_commands"] = [v for v in self.dbt_commands]
        if self.jar_params:
            repairRun_body["jar_params"] = [v for v in self.jar_params]
        if self.latest_repair_id:
            repairRun_body["latest_repair_id"] = self.latest_repair_id
        if self.notebook_params:
            repairRun_body["notebook_params"] = self.notebook_params
        if self.pipeline_params:
            repairRun_body["pipeline_params"] = self.pipeline_params.as_request()[1]
        if self.python_named_params:
            repairRun_body["python_named_params"] = self.python_named_params
        if self.python_params:
            repairRun_body["python_params"] = [v for v in self.python_params]
        if self.rerun_all_failed_tasks:
            repairRun_body["rerun_all_failed_tasks"] = self.rerun_all_failed_tasks
        if self.rerun_tasks:
            repairRun_body["rerun_tasks"] = [v for v in self.rerun_tasks]
        if self.run_id:
            repairRun_body["run_id"] = self.run_id
        if self.spark_submit_params:
            repairRun_body["spark_submit_params"] = [
                v for v in self.spark_submit_params
            ]
        if self.sql_params:
            repairRun_body["sql_params"] = self.sql_params

        return repairRun_query, repairRun_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RepairRun":
        return cls(
            dbt_commands=d.get("dbt_commands", None),
            jar_params=d.get("jar_params", None),
            latest_repair_id=d.get("latest_repair_id", None),
            notebook_params=d.get("notebook_params", None),
            pipeline_params=PipelineParams.from_dict(d["pipeline_params"])
            if "pipeline_params" in d
            else None,
            python_named_params=d.get("python_named_params", None),
            python_params=d.get("python_params", None),
            rerun_all_failed_tasks=d.get("rerun_all_failed_tasks", None),
            rerun_tasks=d.get("rerun_tasks", None),
            run_id=d.get("run_id", None),
            spark_submit_params=d.get("spark_submit_params", None),
            sql_params=d.get("sql_params", None),
        )


@dataclass
class RepairRunResponse:

    # The ID of the repair.
    repair_id: int

    def as_request(self) -> (dict, dict):
        repairRunResponse_query, repairRunResponse_body = {}, {}
        if self.repair_id:
            repairRunResponse_body["repair_id"] = self.repair_id

        return repairRunResponse_query, repairRunResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RepairRunResponse":
        return cls(
            repair_id=d.get("repair_id", None),
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
    new_settings: "JobSettings"

    def as_request(self) -> (dict, dict):
        resetJob_query, resetJob_body = {}, {}
        if self.job_id:
            resetJob_body["job_id"] = self.job_id
        if self.new_settings:
            resetJob_body["new_settings"] = self.new_settings.as_request()[1]

        return resetJob_query, resetJob_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ResetJob":
        return cls(
            job_id=d.get("job_id", None),
            new_settings=JobSettings.from_dict(d["new_settings"])
            if "new_settings" in d
            else None,
        )


@dataclass
class Run:

    # The sequence number of this run attempt for a triggered job run. The
    # initial attempt of a run has an attempt_number of 0\. If the initial run
    # attempt fails, and the job has a retry policy (`max_retries` \> 0),
    # subsequent runs are created with an `original_attempt_run_id` of the
    # original attempt’s ID and an incrementing `attempt_number`. Runs are
    # retried only until they succeed, and the maximum `attempt_number` is the
    # same as the `max_retries` value for the job.
    attempt_number: int
    # The time in milliseconds it took to terminate the cluster and clean up any
    # associated artifacts. The total duration of the run is the sum of the
    # setup_duration, the execution_duration, and the cleanup_duration.
    cleanup_duration: int
    # The cluster used for this run. If the run is specified to use a new
    # cluster, this field is set once the Jobs service has requested a cluster
    # for the run.
    cluster_instance: "ClusterInstance"
    # A snapshot of the job’s cluster specification when this run was created.
    cluster_spec: "ClusterSpec"
    # The creator user name. This field won’t be included in the response if
    # the user has already been deleted.
    creator_user_name: str
    # The time at which this run ended in epoch milliseconds (milliseconds since
    # 1/1/1970 UTC). This field is set to 0 if the job is still running.
    end_time: int
    # The time in milliseconds it took to execute the commands in the JAR or
    # notebook until they completed, failed, timed out, were cancelled, or
    # encountered an unexpected error.
    execution_duration: int
    # An optional specification for a remote repository containing the notebooks
    # used by this job's notebook tasks.
    git_source: "GitSource"
    # A list of job cluster specifications that can be shared and reused by
    # tasks of this job. Libraries cannot be declared in a shared job cluster.
    # You must declare dependent libraries in task settings.
    job_clusters: "List[JobCluster]"
    # The canonical identifier of the job that contains this run.
    job_id: int
    # A unique identifier for this job run. This is set to the same value as
    # `run_id`.
    number_in_job: int
    # If this run is a retry of a prior run attempt, this field contains the
    # run_id of the original attempt; otherwise, it is the same as the run_id.
    original_attempt_run_id: int
    # The parameters used for this run.
    overriding_parameters: "RunParameters"
    # The repair history of the run.
    repair_history: "List[RepairHistoryItem]"
    # The canonical identifier of the run. This ID is unique across all runs of
    # all jobs.
    run_id: int
    # An optional name for the run. The maximum allowed length is 4096 bytes in
    # UTF-8 encoding.
    run_name: str
    # The URL to the detail page of the run.
    run_page_url: str
    # This describes an enum
    run_type: "RunType"
    # The cron schedule that triggered this run if it was triggered by the
    # periodic scheduler.
    schedule: "CronSchedule"
    # The time it took to set up the cluster in milliseconds. For runs that run
    # on new clusters this is the cluster creation time, for runs that run on
    # existing clusters this time should be very short.
    setup_duration: int
    # The time at which this run was started in epoch milliseconds (milliseconds
    # since 1/1/1970 UTC). This may not be the time when the job task starts
    # executing, for example, if the job is scheduled to run on a new cluster,
    # this is the time the cluster creation call is issued.
    start_time: int
    # The result and lifecycle states of the run.
    state: "RunState"
    # The list of tasks performed by the run. Each task has its own `run_id`
    # which you can use to call `JobsGetOutput` to retrieve the run resutls.
    tasks: "List[RunTask]"
    # The type of trigger that fired this run.
    trigger: "TriggerType"

    def as_request(self) -> (dict, dict):
        run_query, run_body = {}, {}
        if self.attempt_number:
            run_body["attempt_number"] = self.attempt_number
        if self.cleanup_duration:
            run_body["cleanup_duration"] = self.cleanup_duration
        if self.cluster_instance:
            run_body["cluster_instance"] = self.cluster_instance.as_request()[1]
        if self.cluster_spec:
            run_body["cluster_spec"] = self.cluster_spec.as_request()[1]
        if self.creator_user_name:
            run_body["creator_user_name"] = self.creator_user_name
        if self.end_time:
            run_body["end_time"] = self.end_time
        if self.execution_duration:
            run_body["execution_duration"] = self.execution_duration
        if self.git_source:
            run_body["git_source"] = self.git_source.as_request()[1]
        if self.job_clusters:
            run_body["job_clusters"] = [v.as_request()[1] for v in self.job_clusters]
        if self.job_id:
            run_body["job_id"] = self.job_id
        if self.number_in_job:
            run_body["number_in_job"] = self.number_in_job
        if self.original_attempt_run_id:
            run_body["original_attempt_run_id"] = self.original_attempt_run_id
        if self.overriding_parameters:
            run_body["overriding_parameters"] = self.overriding_parameters.as_request()[
                1
            ]
        if self.repair_history:
            run_body["repair_history"] = [
                v.as_request()[1] for v in self.repair_history
            ]
        if self.run_id:
            run_body["run_id"] = self.run_id
        if self.run_name:
            run_body["run_name"] = self.run_name
        if self.run_page_url:
            run_body["run_page_url"] = self.run_page_url
        if self.run_type:
            run_body["run_type"] = self.run_type.value
        if self.schedule:
            run_body["schedule"] = self.schedule.as_request()[1]
        if self.setup_duration:
            run_body["setup_duration"] = self.setup_duration
        if self.start_time:
            run_body["start_time"] = self.start_time
        if self.state:
            run_body["state"] = self.state.as_request()[1]
        if self.tasks:
            run_body["tasks"] = [v.as_request()[1] for v in self.tasks]
        if self.trigger:
            run_body["trigger"] = self.trigger.value

        return run_query, run_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Run":
        return cls(
            attempt_number=d.get("attempt_number", None),
            cleanup_duration=d.get("cleanup_duration", None),
            cluster_instance=ClusterInstance.from_dict(d["cluster_instance"])
            if "cluster_instance" in d
            else None,
            cluster_spec=ClusterSpec.from_dict(d["cluster_spec"])
            if "cluster_spec" in d
            else None,
            creator_user_name=d.get("creator_user_name", None),
            end_time=d.get("end_time", None),
            execution_duration=d.get("execution_duration", None),
            git_source=GitSource.from_dict(d["git_source"])
            if "git_source" in d
            else None,
            job_clusters=[JobCluster.from_dict(v) for v in d["job_clusters"]]
            if "job_clusters" in d
            else None,
            job_id=d.get("job_id", None),
            number_in_job=d.get("number_in_job", None),
            original_attempt_run_id=d.get("original_attempt_run_id", None),
            overriding_parameters=RunParameters.from_dict(d["overriding_parameters"])
            if "overriding_parameters" in d
            else None,
            repair_history=[RepairHistoryItem.from_dict(v) for v in d["repair_history"]]
            if "repair_history" in d
            else None,
            run_id=d.get("run_id", None),
            run_name=d.get("run_name", None),
            run_page_url=d.get("run_page_url", None),
            run_type=RunType(d["run_type"]) if "run_type" in d else None,
            schedule=CronSchedule.from_dict(d["schedule"]) if "schedule" in d else None,
            setup_duration=d.get("setup_duration", None),
            start_time=d.get("start_time", None),
            state=RunState.from_dict(d["state"]) if "state" in d else None,
            tasks=[RunTask.from_dict(v) for v in d["tasks"]] if "tasks" in d else None,
            trigger=TriggerType(d["trigger"]) if "trigger" in d else None,
        )


class RunLifeCycleState(Enum):
    """This describes an enum"""

    BLOCKED = "BLOCKED"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SKIPPED = "SKIPPED"
    TERMINATED = "TERMINATED"
    TERMINATING = "TERMINATING"
    WAITING_FOR_RETRY = "WAITING_FOR_RETRY"


@dataclass
class RunNow:

    # An array of commands to execute for jobs with the dbt task, for example
    # `"dbt_commands": ["dbt deps", "dbt seed", "dbt run"]`
    dbt_commands: "List[str]"
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
    # For more information, see [How to ensure idempotency for jobs].
    #
    # [How to ensure idempotency for jobs]: https://kb.databricks.com/jobs/jobs-idempotency.html
    idempotency_token: str
    # A list of parameters for jobs with Spark JAR tasks, for example
    # `\"jar_params\": [\"john doe\", \"35\"]`. The parameters are used to
    # invoke the main function of the main class specified in the Spark JAR
    # task. If not specified upon `run-now`, it defaults to an empty list.
    # jar_params cannot be specified in conjunction with notebook_params. The
    # JSON representation of this field (for example `{\"jar_params\":[\"john
    # doe\",\"35\"]}`) cannot exceed 10,000 bytes.
    #
    # Use [Task parameter variables](/jobs.html"#parameter-variables") to set
    # parameters containing information about job runs.
    jar_params: "List[str]"
    # The ID of the job to be executed
    job_id: int
    # A map from keys to values for jobs with notebook task, for example
    # `\"notebook_params\": {\"name\": \"john doe\", \"age\": \"35\"}`. The map
    # is passed to the notebook and is accessible through the
    # [dbutils.widgets.get] function.
    #
    # If not specified upon `run-now`, the triggered run uses the job’s base
    # parameters.
    #
    # notebook_params cannot be specified in conjunction with jar_params.
    #
    # Use [Task parameter variables] to set parameters containing information
    # about job runs.
    #
    # The JSON representation of this field (for example
    # `{\"notebook_params\":{\"name\":\"john doe\",\"age\":\"35\"}}`) cannot
    # exceed 10,000 bytes.
    #
    # [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
    # [dbutils.widgets.get]: https://docs.databricks.com/dev-tools/databricks-utils.html
    notebook_params: "Dict[str,str]"

    pipeline_params: "PipelineParams"
    # A map from keys to values for jobs with Python wheel task, for example
    # `"python_named_params": {"name": "task", "data":
    # "dbfs:/path/to/data.json"}`.
    python_named_params: "Dict[str,str]"
    # A list of parameters for jobs with Python tasks, for example
    # `\"python_params\": [\"john doe\", \"35\"]`. The parameters are passed to
    # Python file as command-line parameters. If specified upon `run-now`, it
    # would overwrite the parameters specified in job setting. The JSON
    # representation of this field (for example `{\"python_params\":[\"john
    # doe\",\"35\"]}`) cannot exceed 10,000 bytes.
    #
    # Use [Task parameter variables] to set parameters containing information
    # about job runs.
    #
    # Important
    #
    # These parameters accept only Latin characters (ASCII character set). Using
    # non-ASCII characters returns an error. Examples of invalid, non-ASCII
    # characters are Chinese, Japanese kanjis, and emojis.
    #
    # [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
    python_params: "List[str]"
    # A list of parameters for jobs with spark submit task, for example
    # `\"spark_submit_params\": [\"--class\",
    # \"org.apache.spark.examples.SparkPi\"]`. The parameters are passed to
    # spark-submit script as command-line parameters. If specified upon
    # `run-now`, it would overwrite the parameters specified in job setting. The
    # JSON representation of this field (for example `{\"python_params\":[\"john
    # doe\",\"35\"]}`) cannot exceed 10,000 bytes.
    #
    # Use [Task parameter variables] to set parameters containing information
    # about job runs
    #
    # Important
    #
    # These parameters accept only Latin characters (ASCII character set). Using
    # non-ASCII characters returns an error. Examples of invalid, non-ASCII
    # characters are Chinese, Japanese kanjis, and emojis.
    #
    # [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
    spark_submit_params: "List[str]"
    # A map from keys to values for jobs with SQL task, for example
    # `"sql_params": {"name": "john doe", "age": "35"}`. The SQL alert task does
    # not support custom parameters.
    sql_params: "Dict[str,str]"

    def as_request(self) -> (dict, dict):
        runNow_query, runNow_body = {}, {}
        if self.dbt_commands:
            runNow_body["dbt_commands"] = [v for v in self.dbt_commands]
        if self.idempotency_token:
            runNow_body["idempotency_token"] = self.idempotency_token
        if self.jar_params:
            runNow_body["jar_params"] = [v for v in self.jar_params]
        if self.job_id:
            runNow_body["job_id"] = self.job_id
        if self.notebook_params:
            runNow_body["notebook_params"] = self.notebook_params
        if self.pipeline_params:
            runNow_body["pipeline_params"] = self.pipeline_params.as_request()[1]
        if self.python_named_params:
            runNow_body["python_named_params"] = self.python_named_params
        if self.python_params:
            runNow_body["python_params"] = [v for v in self.python_params]
        if self.spark_submit_params:
            runNow_body["spark_submit_params"] = [v for v in self.spark_submit_params]
        if self.sql_params:
            runNow_body["sql_params"] = self.sql_params

        return runNow_query, runNow_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RunNow":
        return cls(
            dbt_commands=d.get("dbt_commands", None),
            idempotency_token=d.get("idempotency_token", None),
            jar_params=d.get("jar_params", None),
            job_id=d.get("job_id", None),
            notebook_params=d.get("notebook_params", None),
            pipeline_params=PipelineParams.from_dict(d["pipeline_params"])
            if "pipeline_params" in d
            else None,
            python_named_params=d.get("python_named_params", None),
            python_params=d.get("python_params", None),
            spark_submit_params=d.get("spark_submit_params", None),
            sql_params=d.get("sql_params", None),
        )


@dataclass
class RunNowResponse:

    # A unique identifier for this job run. This is set to the same value as
    # `run_id`.
    number_in_job: int
    # The globally unique ID of the newly triggered run.
    run_id: int

    def as_request(self) -> (dict, dict):
        runNowResponse_query, runNowResponse_body = {}, {}
        if self.number_in_job:
            runNowResponse_body["number_in_job"] = self.number_in_job
        if self.run_id:
            runNowResponse_body["run_id"] = self.run_id

        return runNowResponse_query, runNowResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RunNowResponse":
        return cls(
            number_in_job=d.get("number_in_job", None),
            run_id=d.get("run_id", None),
        )


@dataclass
class RunOutput:

    # The output of a dbt task, if available.
    dbt_output: "DbtOutput"
    # An error message indicating why a task failed or why output is not
    # available. The message is unstructured, and its exact format is subject to
    # change.
    error: str
    # If there was an error executing the run, this field contains any available
    # stack traces.
    error_trace: str
    # The output from tasks that write to standard streams (stdout/stderr) such
    # as :schema:sparkjartask, :schema:sparkpythontask, :schema:pythonwheeltask.
    #
    # It's not supported for the :schema:notebooktask, :schema:pipelinetask or
    # :schema:sparksubmittask.
    #
    # Databricks restricts this API to return the last 5 MB of these logs.
    logs: str
    # Whether the logs are truncated.
    logs_truncated: bool
    # All details of the run except for its output.
    metadata: "Run"
    # The output of a notebook task, if available. A notebook task that
    # terminates (either successfully or with a failure) without calling
    # `dbutils.notebook.exit()` is considered to have an empty output. This
    # field is set but its result value is empty. <Databricks> restricts this
    # API to return the first 5 MB of the output. To return a larger result, use
    # the [ClusterLogConf](/dev-tools/api/latest/clusters.html#clusterlogconf)
    # field to configure log storage for the job cluster.
    notebook_output: "NotebookOutput"
    # The output of a SQL task, if available.
    sql_output: "SqlOutput"

    def as_request(self) -> (dict, dict):
        runOutput_query, runOutput_body = {}, {}
        if self.dbt_output:
            runOutput_body["dbt_output"] = self.dbt_output.as_request()[1]
        if self.error:
            runOutput_body["error"] = self.error
        if self.error_trace:
            runOutput_body["error_trace"] = self.error_trace
        if self.logs:
            runOutput_body["logs"] = self.logs
        if self.logs_truncated:
            runOutput_body["logs_truncated"] = self.logs_truncated
        if self.metadata:
            runOutput_body["metadata"] = self.metadata.as_request()[1]
        if self.notebook_output:
            runOutput_body["notebook_output"] = self.notebook_output.as_request()[1]
        if self.sql_output:
            runOutput_body["sql_output"] = self.sql_output.as_request()[1]

        return runOutput_query, runOutput_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RunOutput":
        return cls(
            dbt_output=DbtOutput.from_dict(d["dbt_output"])
            if "dbt_output" in d
            else None,
            error=d.get("error", None),
            error_trace=d.get("error_trace", None),
            logs=d.get("logs", None),
            logs_truncated=d.get("logs_truncated", None),
            metadata=Run.from_dict(d["metadata"]) if "metadata" in d else None,
            notebook_output=NotebookOutput.from_dict(d["notebook_output"])
            if "notebook_output" in d
            else None,
            sql_output=SqlOutput.from_dict(d["sql_output"])
            if "sql_output" in d
            else None,
        )


@dataclass
class RunParameters:

    # An array of commands to execute for jobs with the dbt task, for example
    # `"dbt_commands": ["dbt deps", "dbt seed", "dbt run"]`
    dbt_commands: "List[str]"
    # A list of parameters for jobs with Spark JAR tasks, for example
    # `\"jar_params\": [\"john doe\", \"35\"]`. The parameters are used to
    # invoke the main function of the main class specified in the Spark JAR
    # task. If not specified upon `run-now`, it defaults to an empty list.
    # jar_params cannot be specified in conjunction with notebook_params. The
    # JSON representation of this field (for example `{\"jar_params\":[\"john
    # doe\",\"35\"]}`) cannot exceed 10,000 bytes.
    #
    # Use [Task parameter variables](/jobs.html"#parameter-variables") to set
    # parameters containing information about job runs.
    jar_params: "List[str]"
    # A map from keys to values for jobs with notebook task, for example
    # `\"notebook_params\": {\"name\": \"john doe\", \"age\": \"35\"}`. The map
    # is passed to the notebook and is accessible through the
    # [dbutils.widgets.get] function.
    #
    # If not specified upon `run-now`, the triggered run uses the job’s base
    # parameters.
    #
    # notebook_params cannot be specified in conjunction with jar_params.
    #
    # Use [Task parameter variables] to set parameters containing information
    # about job runs.
    #
    # The JSON representation of this field (for example
    # `{\"notebook_params\":{\"name\":\"john doe\",\"age\":\"35\"}}`) cannot
    # exceed 10,000 bytes.
    #
    # [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
    # [dbutils.widgets.get]: https://docs.databricks.com/dev-tools/databricks-utils.html
    notebook_params: "Dict[str,str]"

    pipeline_params: "PipelineParams"
    # A map from keys to values for jobs with Python wheel task, for example
    # `"python_named_params": {"name": "task", "data":
    # "dbfs:/path/to/data.json"}`.
    python_named_params: "Dict[str,str]"
    # A list of parameters for jobs with Python tasks, for example
    # `\"python_params\": [\"john doe\", \"35\"]`. The parameters are passed to
    # Python file as command-line parameters. If specified upon `run-now`, it
    # would overwrite the parameters specified in job setting. The JSON
    # representation of this field (for example `{\"python_params\":[\"john
    # doe\",\"35\"]}`) cannot exceed 10,000 bytes.
    #
    # Use [Task parameter variables] to set parameters containing information
    # about job runs.
    #
    # Important
    #
    # These parameters accept only Latin characters (ASCII character set). Using
    # non-ASCII characters returns an error. Examples of invalid, non-ASCII
    # characters are Chinese, Japanese kanjis, and emojis.
    #
    # [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
    python_params: "List[str]"
    # A list of parameters for jobs with spark submit task, for example
    # `\"spark_submit_params\": [\"--class\",
    # \"org.apache.spark.examples.SparkPi\"]`. The parameters are passed to
    # spark-submit script as command-line parameters. If specified upon
    # `run-now`, it would overwrite the parameters specified in job setting. The
    # JSON representation of this field (for example `{\"python_params\":[\"john
    # doe\",\"35\"]}`) cannot exceed 10,000 bytes.
    #
    # Use [Task parameter variables] to set parameters containing information
    # about job runs
    #
    # Important
    #
    # These parameters accept only Latin characters (ASCII character set). Using
    # non-ASCII characters returns an error. Examples of invalid, non-ASCII
    # characters are Chinese, Japanese kanjis, and emojis.
    #
    # [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
    spark_submit_params: "List[str]"
    # A map from keys to values for jobs with SQL task, for example
    # `"sql_params": {"name": "john doe", "age": "35"}`. The SQL alert task does
    # not support custom parameters.
    sql_params: "Dict[str,str]"

    def as_request(self) -> (dict, dict):
        runParameters_query, runParameters_body = {}, {}
        if self.dbt_commands:
            runParameters_body["dbt_commands"] = [v for v in self.dbt_commands]
        if self.jar_params:
            runParameters_body["jar_params"] = [v for v in self.jar_params]
        if self.notebook_params:
            runParameters_body["notebook_params"] = self.notebook_params
        if self.pipeline_params:
            runParameters_body["pipeline_params"] = self.pipeline_params.as_request()[1]
        if self.python_named_params:
            runParameters_body["python_named_params"] = self.python_named_params
        if self.python_params:
            runParameters_body["python_params"] = [v for v in self.python_params]
        if self.spark_submit_params:
            runParameters_body["spark_submit_params"] = [
                v for v in self.spark_submit_params
            ]
        if self.sql_params:
            runParameters_body["sql_params"] = self.sql_params

        return runParameters_query, runParameters_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RunParameters":
        return cls(
            dbt_commands=d.get("dbt_commands", None),
            jar_params=d.get("jar_params", None),
            notebook_params=d.get("notebook_params", None),
            pipeline_params=PipelineParams.from_dict(d["pipeline_params"])
            if "pipeline_params" in d
            else None,
            python_named_params=d.get("python_named_params", None),
            python_params=d.get("python_params", None),
            spark_submit_params=d.get("spark_submit_params", None),
            sql_params=d.get("sql_params", None),
        )


class RunResultState(Enum):
    """This describes an enum"""

    CANCELED = "CANCELED"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"
    TIMEDOUT = "TIMEDOUT"


@dataclass
class RunState:
    """The result and lifecycle state of the run."""

    # A description of a run’s current location in the run lifecycle. This
    # field is always available in the response.
    life_cycle_state: "RunLifeCycleState"
    # This describes an enum
    result_state: "RunResultState"
    # A descriptive message for the current state. This field is unstructured,
    # and its exact format is subject to change.
    state_message: str
    # Whether a run was canceled manually by a user or by the scheduler because
    # the run timed out.
    user_cancelled_or_timedout: bool

    def as_request(self) -> (dict, dict):
        runState_query, runState_body = {}, {}
        if self.life_cycle_state:
            runState_body["life_cycle_state"] = self.life_cycle_state.value
        if self.result_state:
            runState_body["result_state"] = self.result_state.value
        if self.state_message:
            runState_body["state_message"] = self.state_message
        if self.user_cancelled_or_timedout:
            runState_body[
                "user_cancelled_or_timedout"
            ] = self.user_cancelled_or_timedout

        return runState_query, runState_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RunState":
        return cls(
            life_cycle_state=RunLifeCycleState(d["life_cycle_state"])
            if "life_cycle_state" in d
            else None,
            result_state=RunResultState(d["result_state"])
            if "result_state" in d
            else None,
            state_message=d.get("state_message", None),
            user_cancelled_or_timedout=d.get("user_cancelled_or_timedout", None),
        )


@dataclass
class RunSubmitTaskSettings:

    # An optional array of objects specifying the dependency graph of the task.
    # All tasks specified in this field must complete successfully before
    # executing this task. The key is `task_key`, and the value is the name
    # assigned to the dependent task. This field is required when a job consists
    # of more than one task.
    depends_on: "List[TaskDependenciesItem]"
    # If existing_cluster_id, the ID of an existing cluster that is used for all
    # runs of this task. When running tasks on an existing cluster, you may need
    # to manually restart the cluster if it stops responding. We suggest running
    # jobs on new clusters for greater reliability.
    existing_cluster_id: str
    # An optional list of libraries to be installed on the cluster that executes
    # the task. The default value is an empty list.
    libraries: "List[Library]"
    # If new_cluster, a description of a cluster that is created for each run.
    new_cluster: "CreateCluster"
    # If notebook_task, indicates that this task must run a notebook. This field
    # may not be specified in conjunction with spark_jar_task.
    notebook_task: "NotebookTask"
    # If pipeline_task, indicates that this task must execute a Pipeline.
    pipeline_task: "PipelineTask"
    # If python_wheel_task, indicates that this job must execute a PythonWheel.
    python_wheel_task: "PythonWheelTask"
    # If spark_jar_task, indicates that this task must run a JAR.
    spark_jar_task: "SparkJarTask"
    # If spark_python_task, indicates that this task must run a Python file.
    spark_python_task: "SparkPythonTask"
    # If spark_submit_task, indicates that this task must be launched by the
    # spark submit script.
    spark_submit_task: "SparkSubmitTask"
    # A unique name for the task. This field is used to refer to this task from
    # other tasks. This field is required and must be unique within its parent
    # job. On Update or Reset, this field is used to reference the tasks to be
    # updated or reset. The maximum length is 100 characters.
    task_key: str
    # An optional timeout applied to each run of this job task. The default
    # behavior is to have no timeout.
    timeout_seconds: int

    def as_request(self) -> (dict, dict):
        runSubmitTaskSettings_query, runSubmitTaskSettings_body = {}, {}
        if self.depends_on:
            runSubmitTaskSettings_body["depends_on"] = [
                v.as_request()[1] for v in self.depends_on
            ]
        if self.existing_cluster_id:
            runSubmitTaskSettings_body["existing_cluster_id"] = self.existing_cluster_id
        if self.libraries:
            runSubmitTaskSettings_body["libraries"] = [v for v in self.libraries]
        if self.new_cluster:
            runSubmitTaskSettings_body["new_cluster"] = self.new_cluster
        if self.notebook_task:
            runSubmitTaskSettings_body[
                "notebook_task"
            ] = self.notebook_task.as_request()[1]
        if self.pipeline_task:
            runSubmitTaskSettings_body[
                "pipeline_task"
            ] = self.pipeline_task.as_request()[1]
        if self.python_wheel_task:
            runSubmitTaskSettings_body[
                "python_wheel_task"
            ] = self.python_wheel_task.as_request()[1]
        if self.spark_jar_task:
            runSubmitTaskSettings_body[
                "spark_jar_task"
            ] = self.spark_jar_task.as_request()[1]
        if self.spark_python_task:
            runSubmitTaskSettings_body[
                "spark_python_task"
            ] = self.spark_python_task.as_request()[1]
        if self.spark_submit_task:
            runSubmitTaskSettings_body[
                "spark_submit_task"
            ] = self.spark_submit_task.as_request()[1]
        if self.task_key:
            runSubmitTaskSettings_body["task_key"] = self.task_key
        if self.timeout_seconds:
            runSubmitTaskSettings_body["timeout_seconds"] = self.timeout_seconds

        return runSubmitTaskSettings_query, runSubmitTaskSettings_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RunSubmitTaskSettings":
        return cls(
            depends_on=[TaskDependenciesItem.from_dict(v) for v in d["depends_on"]]
            if "depends_on" in d
            else None,
            existing_cluster_id=d.get("existing_cluster_id", None),
            libraries=d.get("libraries", None),
            new_cluster=CreateCluster.from_dict(d["new_cluster"])
            if "new_cluster" in d
            else None,
            notebook_task=NotebookTask.from_dict(d["notebook_task"])
            if "notebook_task" in d
            else None,
            pipeline_task=PipelineTask.from_dict(d["pipeline_task"])
            if "pipeline_task" in d
            else None,
            python_wheel_task=PythonWheelTask.from_dict(d["python_wheel_task"])
            if "python_wheel_task" in d
            else None,
            spark_jar_task=SparkJarTask.from_dict(d["spark_jar_task"])
            if "spark_jar_task" in d
            else None,
            spark_python_task=SparkPythonTask.from_dict(d["spark_python_task"])
            if "spark_python_task" in d
            else None,
            spark_submit_task=SparkSubmitTask.from_dict(d["spark_submit_task"])
            if "spark_submit_task" in d
            else None,
            task_key=d.get("task_key", None),
            timeout_seconds=d.get("timeout_seconds", None),
        )


@dataclass
class RunTask:

    # The sequence number of this run attempt for a triggered job run. The
    # initial attempt of a run has an attempt_number of 0\. If the initial run
    # attempt fails, and the job has a retry policy (`max_retries` \> 0),
    # subsequent runs are created with an `original_attempt_run_id` of the
    # original attempt’s ID and an incrementing `attempt_number`. Runs are
    # retried only until they succeed, and the maximum `attempt_number` is the
    # same as the `max_retries` value for the job.
    attempt_number: int
    # The time in milliseconds it took to terminate the cluster and clean up any
    # associated artifacts. The total duration of the run is the sum of the
    # setup_duration, the execution_duration, and the cleanup_duration.
    cleanup_duration: int
    # The cluster used for this run. If the run is specified to use a new
    # cluster, this field is set once the Jobs service has requested a cluster
    # for the run.
    cluster_instance: "ClusterInstance"
    # If dbt_task, indicates that this must execute a dbt task. It requires both
    # Databricks SQL and the ability to use a serverless or a pro SQL warehouse.
    dbt_task: "DbtTask"
    # An optional array of objects specifying the dependency graph of the task.
    # All tasks specified in this field must complete successfully before
    # executing this task. The key is `task_key`, and the value is the name
    # assigned to the dependent task. This field is required when a job consists
    # of more than one task.
    depends_on: "List[TaskDependenciesItem]"
    # An optional description for this task. The maximum length is 4096 bytes.
    description: str
    # The time at which this run ended in epoch milliseconds (milliseconds since
    # 1/1/1970 UTC). This field is set to 0 if the job is still running.
    end_time: int
    # The time in milliseconds it took to execute the commands in the JAR or
    # notebook until they completed, failed, timed out, were cancelled, or
    # encountered an unexpected error.
    execution_duration: int
    # If existing_cluster_id, the ID of an existing cluster that is used for all
    # runs of this job. When running jobs on an existing cluster, you may need
    # to manually restart the cluster if it stops responding. We suggest running
    # jobs on new clusters for greater reliability.
    existing_cluster_id: str
    # An optional specification for a remote repository containing the notebooks
    # used by this job's notebook tasks.
    git_source: "GitSource"
    # An optional list of libraries to be installed on the cluster that executes
    # the job. The default value is an empty list.
    libraries: "List[Library]"
    # If new_cluster, a description of a cluster that is created for each run.
    new_cluster: "CreateCluster"
    # If notebook_task, indicates that this job must run a notebook. This field
    # may not be specified in conjunction with spark_jar_task.
    notebook_task: "NotebookTask"
    # If pipeline_task, indicates that this job must execute a Pipeline.
    pipeline_task: "PipelineTask"
    # If python_wheel_task, indicates that this job must execute a PythonWheel.
    python_wheel_task: "PythonWheelTask"
    # The ID of the task run.
    run_id: int
    # The time it took to set up the cluster in milliseconds. For runs that run
    # on new clusters this is the cluster creation time, for runs that run on
    # existing clusters this time should be very short.
    setup_duration: int
    # If spark_jar_task, indicates that this job must run a JAR.
    spark_jar_task: "SparkJarTask"
    # If spark_python_task, indicates that this job must run a Python file.
    spark_python_task: "SparkPythonTask"
    # If spark_submit_task, indicates that this job must be launched by the
    # spark submit script.
    spark_submit_task: "SparkSubmitTask"
    # If sql_task, indicates that this job must execute a SQL.
    sql_task: "SqlTask"
    # The time at which this run was started in epoch milliseconds (milliseconds
    # since 1/1/1970 UTC). This may not be the time when the job task starts
    # executing, for example, if the job is scheduled to run on a new cluster,
    # this is the time the cluster creation call is issued.
    start_time: int
    # The result and lifecycle states of the run.
    state: "RunState"
    # A unique name for the task. This field is used to refer to this task from
    # other tasks. This field is required and must be unique within its parent
    # job. On Update or Reset, this field is used to reference the tasks to be
    # updated or reset. The maximum length is 100 characters.
    task_key: str

    def as_request(self) -> (dict, dict):
        runTask_query, runTask_body = {}, {}
        if self.attempt_number:
            runTask_body["attempt_number"] = self.attempt_number
        if self.cleanup_duration:
            runTask_body["cleanup_duration"] = self.cleanup_duration
        if self.cluster_instance:
            runTask_body["cluster_instance"] = self.cluster_instance.as_request()[1]
        if self.dbt_task:
            runTask_body["dbt_task"] = self.dbt_task.as_request()[1]
        if self.depends_on:
            runTask_body["depends_on"] = [v.as_request()[1] for v in self.depends_on]
        if self.description:
            runTask_body["description"] = self.description
        if self.end_time:
            runTask_body["end_time"] = self.end_time
        if self.execution_duration:
            runTask_body["execution_duration"] = self.execution_duration
        if self.existing_cluster_id:
            runTask_body["existing_cluster_id"] = self.existing_cluster_id
        if self.git_source:
            runTask_body["git_source"] = self.git_source.as_request()[1]
        if self.libraries:
            runTask_body["libraries"] = [v for v in self.libraries]
        if self.new_cluster:
            runTask_body["new_cluster"] = self.new_cluster
        if self.notebook_task:
            runTask_body["notebook_task"] = self.notebook_task.as_request()[1]
        if self.pipeline_task:
            runTask_body["pipeline_task"] = self.pipeline_task.as_request()[1]
        if self.python_wheel_task:
            runTask_body["python_wheel_task"] = self.python_wheel_task.as_request()[1]
        if self.run_id:
            runTask_body["run_id"] = self.run_id
        if self.setup_duration:
            runTask_body["setup_duration"] = self.setup_duration
        if self.spark_jar_task:
            runTask_body["spark_jar_task"] = self.spark_jar_task.as_request()[1]
        if self.spark_python_task:
            runTask_body["spark_python_task"] = self.spark_python_task.as_request()[1]
        if self.spark_submit_task:
            runTask_body["spark_submit_task"] = self.spark_submit_task.as_request()[1]
        if self.sql_task:
            runTask_body["sql_task"] = self.sql_task.as_request()[1]
        if self.start_time:
            runTask_body["start_time"] = self.start_time
        if self.state:
            runTask_body["state"] = self.state.as_request()[1]
        if self.task_key:
            runTask_body["task_key"] = self.task_key

        return runTask_query, runTask_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RunTask":
        return cls(
            attempt_number=d.get("attempt_number", None),
            cleanup_duration=d.get("cleanup_duration", None),
            cluster_instance=ClusterInstance.from_dict(d["cluster_instance"])
            if "cluster_instance" in d
            else None,
            dbt_task=DbtTask.from_dict(d["dbt_task"]) if "dbt_task" in d else None,
            depends_on=[TaskDependenciesItem.from_dict(v) for v in d["depends_on"]]
            if "depends_on" in d
            else None,
            description=d.get("description", None),
            end_time=d.get("end_time", None),
            execution_duration=d.get("execution_duration", None),
            existing_cluster_id=d.get("existing_cluster_id", None),
            git_source=GitSource.from_dict(d["git_source"])
            if "git_source" in d
            else None,
            libraries=d.get("libraries", None),
            new_cluster=CreateCluster.from_dict(d["new_cluster"])
            if "new_cluster" in d
            else None,
            notebook_task=NotebookTask.from_dict(d["notebook_task"])
            if "notebook_task" in d
            else None,
            pipeline_task=PipelineTask.from_dict(d["pipeline_task"])
            if "pipeline_task" in d
            else None,
            python_wheel_task=PythonWheelTask.from_dict(d["python_wheel_task"])
            if "python_wheel_task" in d
            else None,
            run_id=d.get("run_id", None),
            setup_duration=d.get("setup_duration", None),
            spark_jar_task=SparkJarTask.from_dict(d["spark_jar_task"])
            if "spark_jar_task" in d
            else None,
            spark_python_task=SparkPythonTask.from_dict(d["spark_python_task"])
            if "spark_python_task" in d
            else None,
            spark_submit_task=SparkSubmitTask.from_dict(d["spark_submit_task"])
            if "spark_submit_task" in d
            else None,
            sql_task=SqlTask.from_dict(d["sql_task"]) if "sql_task" in d else None,
            start_time=d.get("start_time", None),
            state=RunState.from_dict(d["state"]) if "state" in d else None,
            task_key=d.get("task_key", None),
        )


class RunType(Enum):
    """This describes an enum"""

    JOB_RUN = "JOB_RUN"
    SUBMIT_RUN = "SUBMIT_RUN"
    WORKFLOW_RUN = "WORKFLOW_RUN"


@dataclass
class SparkJarTask:

    # Deprecated since 04/2016\\. Provide a `jar` through the `libraries` field
    # instead. For an example, see :method:create.
    jar_uri: str
    # The full name of the class containing the main method to be executed. This
    # class must be contained in a JAR provided as a library.
    #
    # The code must use `SparkContext.getOrCreate` to obtain a Spark context;
    # otherwise, runs of the job fail.
    main_class_name: str
    # Parameters passed to the main method.
    #
    # Use [Task parameter variables] to set parameters containing information
    # about job runs.
    #
    # [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
    parameters: "List[str]"

    def as_request(self) -> (dict, dict):
        sparkJarTask_query, sparkJarTask_body = {}, {}
        if self.jar_uri:
            sparkJarTask_body["jar_uri"] = self.jar_uri
        if self.main_class_name:
            sparkJarTask_body["main_class_name"] = self.main_class_name
        if self.parameters:
            sparkJarTask_body["parameters"] = [v for v in self.parameters]

        return sparkJarTask_query, sparkJarTask_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SparkJarTask":
        return cls(
            jar_uri=d.get("jar_uri", None),
            main_class_name=d.get("main_class_name", None),
            parameters=d.get("parameters", None),
        )


@dataclass
class SparkPythonTask:

    # Command line parameters passed to the Python file.
    #
    # Use [Task parameter variables] to set parameters containing information
    # about job runs.
    #
    # [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
    parameters: "List[str]"

    python_file: str

    def as_request(self) -> (dict, dict):
        sparkPythonTask_query, sparkPythonTask_body = {}, {}
        if self.parameters:
            sparkPythonTask_body["parameters"] = [v for v in self.parameters]
        if self.python_file:
            sparkPythonTask_body["python_file"] = self.python_file

        return sparkPythonTask_query, sparkPythonTask_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SparkPythonTask":
        return cls(
            parameters=d.get("parameters", None),
            python_file=d.get("python_file", None),
        )


@dataclass
class SparkSubmitTask:

    # Command-line parameters passed to spark submit.
    #
    # Use [Task parameter variables] to set parameters containing information
    # about job runs.
    #
    # [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
    parameters: "List[str]"

    def as_request(self) -> (dict, dict):
        sparkSubmitTask_query, sparkSubmitTask_body = {}, {}
        if self.parameters:
            sparkSubmitTask_body["parameters"] = [v for v in self.parameters]

        return sparkSubmitTask_query, sparkSubmitTask_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SparkSubmitTask":
        return cls(
            parameters=d.get("parameters", None),
        )


@dataclass
class SqlAlertOutput:

    # The link to find the output results.
    output_link: str
    # The text of the SQL query. Can Run permission of the SQL query associated
    # with the SQL alert is required to view this field.
    query_text: str
    # Information about SQL statements executed in the run.
    sql_statements: "SqlStatementOutput"
    # The canonical identifier of the SQL warehouse.
    warehouse_id: str

    def as_request(self) -> (dict, dict):
        sqlAlertOutput_query, sqlAlertOutput_body = {}, {}
        if self.output_link:
            sqlAlertOutput_body["output_link"] = self.output_link
        if self.query_text:
            sqlAlertOutput_body["query_text"] = self.query_text
        if self.sql_statements:
            sqlAlertOutput_body["sql_statements"] = self.sql_statements.as_request()[1]
        if self.warehouse_id:
            sqlAlertOutput_body["warehouse_id"] = self.warehouse_id

        return sqlAlertOutput_query, sqlAlertOutput_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SqlAlertOutput":
        return cls(
            output_link=d.get("output_link", None),
            query_text=d.get("query_text", None),
            sql_statements=SqlStatementOutput.from_dict(d["sql_statements"])
            if "sql_statements" in d
            else None,
            warehouse_id=d.get("warehouse_id", None),
        )


@dataclass
class SqlDashboardOutput:

    # Widgets executed in the run. Only SQL query based widgets are listed.
    widgets: "SqlDashboardWidgetOutput"

    def as_request(self) -> (dict, dict):
        sqlDashboardOutput_query, sqlDashboardOutput_body = {}, {}
        if self.widgets:
            sqlDashboardOutput_body["widgets"] = self.widgets.as_request()[1]

        return sqlDashboardOutput_query, sqlDashboardOutput_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SqlDashboardOutput":
        return cls(
            widgets=SqlDashboardWidgetOutput.from_dict(d["widgets"])
            if "widgets" in d
            else None,
        )


@dataclass
class SqlDashboardWidgetOutput:

    # Time (in epoch milliseconds) when execution of the SQL widget ends.
    end_time: int
    # The information about the error when execution fails.
    error: "SqlOutputError"
    # The link to find the output results.
    output_link: str
    # Time (in epoch milliseconds) when execution of the SQL widget starts.
    start_time: int
    # The execution status of the SQL widget.
    status: "SqlDashboardWidgetOutputStatus"
    # The canonical identifier of the SQL widget.
    widget_id: str
    # The title of the SQL widget.
    widget_title: str

    def as_request(self) -> (dict, dict):
        sqlDashboardWidgetOutput_query, sqlDashboardWidgetOutput_body = {}, {}
        if self.end_time:
            sqlDashboardWidgetOutput_body["end_time"] = self.end_time
        if self.error:
            sqlDashboardWidgetOutput_body["error"] = self.error.as_request()[1]
        if self.output_link:
            sqlDashboardWidgetOutput_body["output_link"] = self.output_link
        if self.start_time:
            sqlDashboardWidgetOutput_body["start_time"] = self.start_time
        if self.status:
            sqlDashboardWidgetOutput_body["status"] = self.status.value
        if self.widget_id:
            sqlDashboardWidgetOutput_body["widget_id"] = self.widget_id
        if self.widget_title:
            sqlDashboardWidgetOutput_body["widget_title"] = self.widget_title

        return sqlDashboardWidgetOutput_query, sqlDashboardWidgetOutput_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SqlDashboardWidgetOutput":
        return cls(
            end_time=d.get("end_time", None),
            error=SqlOutputError.from_dict(d["error"]) if "error" in d else None,
            output_link=d.get("output_link", None),
            start_time=d.get("start_time", None),
            status=SqlDashboardWidgetOutputStatus(d["status"])
            if "status" in d
            else None,
            widget_id=d.get("widget_id", None),
            widget_title=d.get("widget_title", None),
        )


class SqlDashboardWidgetOutputStatus(Enum):
    """The execution status of the SQL widget."""

    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"


@dataclass
class SqlOutput:

    # The output of a SQL alert task, if available.
    alert_output: "SqlAlertOutput"
    # The output of a SQL dashboard task, if available.
    dashboard_output: "SqlDashboardOutput"
    # The output of a SQL query task, if available.
    query_output: "SqlQueryOutput"

    def as_request(self) -> (dict, dict):
        sqlOutput_query, sqlOutput_body = {}, {}
        if self.alert_output:
            sqlOutput_body["alert_output"] = self.alert_output.as_request()[1]
        if self.dashboard_output:
            sqlOutput_body["dashboard_output"] = self.dashboard_output.as_request()[1]
        if self.query_output:
            sqlOutput_body["query_output"] = self.query_output.as_request()[1]

        return sqlOutput_query, sqlOutput_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SqlOutput":
        return cls(
            alert_output=SqlAlertOutput.from_dict(d["alert_output"])
            if "alert_output" in d
            else None,
            dashboard_output=SqlDashboardOutput.from_dict(d["dashboard_output"])
            if "dashboard_output" in d
            else None,
            query_output=SqlQueryOutput.from_dict(d["query_output"])
            if "query_output" in d
            else None,
        )


@dataclass
class SqlOutputError:

    # The error message when execution fails.
    message: str

    def as_request(self) -> (dict, dict):
        sqlOutputError_query, sqlOutputError_body = {}, {}
        if self.message:
            sqlOutputError_body["message"] = self.message

        return sqlOutputError_query, sqlOutputError_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SqlOutputError":
        return cls(
            message=d.get("message", None),
        )


@dataclass
class SqlQueryOutput:

    # The link to find the output results.
    output_link: str
    # The text of the SQL query. Can Run permission of the SQL query is required
    # to view this field.
    query_text: str
    # Information about SQL statements executed in the run.
    sql_statements: "SqlStatementOutput"
    # The canonical identifier of the SQL warehouse.
    warehouse_id: str

    def as_request(self) -> (dict, dict):
        sqlQueryOutput_query, sqlQueryOutput_body = {}, {}
        if self.output_link:
            sqlQueryOutput_body["output_link"] = self.output_link
        if self.query_text:
            sqlQueryOutput_body["query_text"] = self.query_text
        if self.sql_statements:
            sqlQueryOutput_body["sql_statements"] = self.sql_statements.as_request()[1]
        if self.warehouse_id:
            sqlQueryOutput_body["warehouse_id"] = self.warehouse_id

        return sqlQueryOutput_query, sqlQueryOutput_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SqlQueryOutput":
        return cls(
            output_link=d.get("output_link", None),
            query_text=d.get("query_text", None),
            sql_statements=SqlStatementOutput.from_dict(d["sql_statements"])
            if "sql_statements" in d
            else None,
            warehouse_id=d.get("warehouse_id", None),
        )


@dataclass
class SqlStatementOutput:

    # A key that can be used to look up query details.
    lookup_key: str

    def as_request(self) -> (dict, dict):
        sqlStatementOutput_query, sqlStatementOutput_body = {}, {}
        if self.lookup_key:
            sqlStatementOutput_body["lookup_key"] = self.lookup_key

        return sqlStatementOutput_query, sqlStatementOutput_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SqlStatementOutput":
        return cls(
            lookup_key=d.get("lookup_key", None),
        )


@dataclass
class SqlTask:

    # If alert, indicates that this job must refresh a SQL alert.
    alert: "SqlTaskAlert"
    # If dashboard, indicates that this job must refresh a SQL dashboard.
    dashboard: "SqlTaskDashboard"
    # Parameters to be used for each run of this job. The SQL alert task does
    # not support custom parameters.
    parameters: Any
    # If query, indicates that this job must execute a SQL query.
    query: "SqlTaskQuery"
    # The canonical identifier of the SQL warehouse. Only serverless and pro SQL
    # warehouses are supported.
    warehouse_id: str

    def as_request(self) -> (dict, dict):
        sqlTask_query, sqlTask_body = {}, {}
        if self.alert:
            sqlTask_body["alert"] = self.alert.as_request()[1]
        if self.dashboard:
            sqlTask_body["dashboard"] = self.dashboard.as_request()[1]
        if self.parameters:
            sqlTask_body["parameters"] = self.parameters
        if self.query:
            sqlTask_body["query"] = self.query.as_request()[1]
        if self.warehouse_id:
            sqlTask_body["warehouse_id"] = self.warehouse_id

        return sqlTask_query, sqlTask_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SqlTask":
        return cls(
            alert=SqlTaskAlert.from_dict(d["alert"]) if "alert" in d else None,
            dashboard=SqlTaskDashboard.from_dict(d["dashboard"])
            if "dashboard" in d
            else None,
            parameters=d.get("parameters", None),
            query=SqlTaskQuery.from_dict(d["query"]) if "query" in d else None,
            warehouse_id=d.get("warehouse_id", None),
        )


@dataclass
class SqlTaskAlert:

    # The canonical identifier of the SQL alert.
    alert_id: str

    def as_request(self) -> (dict, dict):
        sqlTaskAlert_query, sqlTaskAlert_body = {}, {}
        if self.alert_id:
            sqlTaskAlert_body["alert_id"] = self.alert_id

        return sqlTaskAlert_query, sqlTaskAlert_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SqlTaskAlert":
        return cls(
            alert_id=d.get("alert_id", None),
        )


@dataclass
class SqlTaskDashboard:

    # The canonical identifier of the SQL dashboard.
    dashboard_id: str

    def as_request(self) -> (dict, dict):
        sqlTaskDashboard_query, sqlTaskDashboard_body = {}, {}
        if self.dashboard_id:
            sqlTaskDashboard_body["dashboard_id"] = self.dashboard_id

        return sqlTaskDashboard_query, sqlTaskDashboard_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SqlTaskDashboard":
        return cls(
            dashboard_id=d.get("dashboard_id", None),
        )


@dataclass
class SqlTaskQuery:

    # The canonical identifier of the SQL query.
    query_id: str

    def as_request(self) -> (dict, dict):
        sqlTaskQuery_query, sqlTaskQuery_body = {}, {}
        if self.query_id:
            sqlTaskQuery_body["query_id"] = self.query_id

        return sqlTaskQuery_query, sqlTaskQuery_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SqlTaskQuery":
        return cls(
            query_id=d.get("query_id", None),
        )


@dataclass
class SubmitRun:

    # List of permissions to set on the job.
    access_control_list: "List[AccessControlRequest]"
    # An optional specification for a remote repository containing the notebooks
    # used by this job's notebook tasks.
    git_source: "GitSource"
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
    # For more information, see [How to ensure idempotency for jobs].
    #
    # [How to ensure idempotency for jobs]: https://kb.databricks.com/jobs/jobs-idempotency.html
    idempotency_token: str
    # An optional name for the run. The default value is `Untitled`.
    run_name: str

    tasks: "List[RunSubmitTaskSettings]"
    # An optional timeout applied to each run of this job. The default behavior
    # is to have no timeout.
    timeout_seconds: int
    # A collection of system notification IDs to notify when the run begins or
    # completes. The default behavior is to not send any system notifications.
    webhook_notifications: "JobWebhookNotifications"

    def as_request(self) -> (dict, dict):
        submitRun_query, submitRun_body = {}, {}
        if self.access_control_list:
            submitRun_body["access_control_list"] = [
                v for v in self.access_control_list
            ]
        if self.git_source:
            submitRun_body["git_source"] = self.git_source.as_request()[1]
        if self.idempotency_token:
            submitRun_body["idempotency_token"] = self.idempotency_token
        if self.run_name:
            submitRun_body["run_name"] = self.run_name
        if self.tasks:
            submitRun_body["tasks"] = [v.as_request()[1] for v in self.tasks]
        if self.timeout_seconds:
            submitRun_body["timeout_seconds"] = self.timeout_seconds
        if self.webhook_notifications:
            submitRun_body[
                "webhook_notifications"
            ] = self.webhook_notifications.as_request()[1]

        return submitRun_query, submitRun_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SubmitRun":
        return cls(
            access_control_list=d.get("access_control_list", None),
            git_source=GitSource.from_dict(d["git_source"])
            if "git_source" in d
            else None,
            idempotency_token=d.get("idempotency_token", None),
            run_name=d.get("run_name", None),
            tasks=[RunSubmitTaskSettings.from_dict(v) for v in d["tasks"]]
            if "tasks" in d
            else None,
            timeout_seconds=d.get("timeout_seconds", None),
            webhook_notifications=JobWebhookNotifications.from_dict(
                d["webhook_notifications"]
            )
            if "webhook_notifications" in d
            else None,
        )


@dataclass
class SubmitRunResponse:

    # The canonical identifier for the newly submitted run.
    run_id: int

    def as_request(self) -> (dict, dict):
        submitRunResponse_query, submitRunResponse_body = {}, {}
        if self.run_id:
            submitRunResponse_body["run_id"] = self.run_id

        return submitRunResponse_query, submitRunResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SubmitRunResponse":
        return cls(
            run_id=d.get("run_id", None),
        )


@dataclass
class TaskDependenciesItem:

    task_key: str

    def as_request(self) -> (dict, dict):
        taskDependenciesItem_query, taskDependenciesItem_body = {}, {}
        if self.task_key:
            taskDependenciesItem_body["task_key"] = self.task_key

        return taskDependenciesItem_query, taskDependenciesItem_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "TaskDependenciesItem":
        return cls(
            task_key=d.get("task_key", None),
        )


class TriggerType(Enum):
    """This describes an enum"""

    ONE_TIME = "ONE_TIME"
    PERIODIC = "PERIODIC"
    RETRY = "RETRY"


@dataclass
class UpdateJob:

    # Remove top-level fields in the job settings. Removing nested fields is not
    # supported. This field is optional.
    fields_to_remove: "List[str]"
    # The canonical identifier of the job to update. This field is required.
    job_id: int
    # The new settings for the job. Any top-level fields specified in
    # `new_settings` are completely replaced. Partially updating nested fields
    # is not supported.
    #
    # Changes to the field `JobSettings.timeout_seconds` are applied to active
    # runs. Changes to other fields are applied to future runs only.
    new_settings: "JobSettings"

    def as_request(self) -> (dict, dict):
        updateJob_query, updateJob_body = {}, {}
        if self.fields_to_remove:
            updateJob_body["fields_to_remove"] = [v for v in self.fields_to_remove]
        if self.job_id:
            updateJob_body["job_id"] = self.job_id
        if self.new_settings:
            updateJob_body["new_settings"] = self.new_settings.as_request()[1]

        return updateJob_query, updateJob_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateJob":
        return cls(
            fields_to_remove=d.get("fields_to_remove", None),
            job_id=d.get("job_id", None),
            new_settings=JobSettings.from_dict(d["new_settings"])
            if "new_settings" in d
            else None,
        )


@dataclass
class ViewItem:

    # Content of the view.
    content: str
    # Name of the view item. In the case of code view, it would be the
    # notebook’s name. In the case of dashboard view, it would be the
    # dashboard’s name.
    name: str
    # Type of the view item.
    type: "ViewType"

    def as_request(self) -> (dict, dict):
        viewItem_query, viewItem_body = {}, {}
        if self.content:
            viewItem_body["content"] = self.content
        if self.name:
            viewItem_body["name"] = self.name
        if self.type:
            viewItem_body["type"] = self.type.value

        return viewItem_query, viewItem_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ViewItem":
        return cls(
            content=d.get("content", None),
            name=d.get("name", None),
            type=ViewType(d["type"]) if "type" in d else None,
        )


class ViewType(Enum):
    """This describes an enum"""

    DASHBOARD = "DASHBOARD"
    NOTEBOOK = "NOTEBOOK"


class ViewsToExport(Enum):
    """This describes an enum"""

    ALL = "ALL"
    CODE = "CODE"
    DASHBOARDS = "DASHBOARDS"


class JobsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def cancel_all_runs(self, request: CancelAllRuns):
        """Cancel all runs of a job.

        Cancels all active runs of a job. The runs are canceled asynchronously,
        so it doesn't prevent new runs from being started."""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.1/jobs/runs/cancel-all", query=query, body=body)

    def cancel_run(self, request: CancelRun):
        """Cancel a job run.

        Cancels a job run. The run is canceled asynchronously, so it may still
        be running when this request completes."""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.1/jobs/runs/cancel", query=query, body=body)

    def create(self, request: CreateJob) -> CreateResponse:
        """Create a new job.

        Create a new job."""
        query, body = request.as_request()
        json = self._api.do("POST", "/api/2.1/jobs/create", query=query, body=body)
        return CreateResponse.from_dict(json)

    def delete(self, request: DeleteJob):
        """Delete a job.

        Deletes a job."""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.1/jobs/delete", query=query, body=body)

    def delete_run(self, request: DeleteRun):
        """Delete a job run.

        Deletes a non-active run. Returns an error if the run is active."""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.1/jobs/runs/delete", query=query, body=body)

    def export_run(self, request: ExportRun) -> ExportRunOutput:
        """Export and retrieve a job run.

        Export and retrieve the job run task."""
        query, body = request.as_request()
        json = self._api.do("GET", "/api/2.1/jobs/runs/export", query=query, body=body)
        return ExportRunOutput.from_dict(json)

    def get(self, request: Get) -> Job:
        """Get a single job.

        Retrieves the details for a single job."""
        query, body = request.as_request()
        json = self._api.do("GET", "/api/2.1/jobs/get", query=query, body=body)
        return Job.from_dict(json)

    def get_run(self, request: GetRun) -> Run:
        """Get a single job run.

        Retrieve the metadata of a run."""
        query, body = request.as_request()
        json = self._api.do("GET", "/api/2.1/jobs/runs/get", query=query, body=body)
        return Run.from_dict(json)

    def get_run_output(self, request: GetRunOutput) -> RunOutput:
        """Get the output for a single run.

        Retrieve the output and metadata of a single task run. When a notebook
        task returns a value through the `dbutils.notebook.exit()` call, you can
        use this endpoint to retrieve that value. Databricks restricts this API
        to returning the first 5 MB of the output. To return a larger result,
        you can store job results in a cloud storage service.

        This endpoint validates that the __run_id__ parameter is valid and
        returns an HTTP status code 400 if the __run_id__ parameter is invalid.
        Runs are automatically removed after 60 days. If you to want to
        reference them beyond 60 days, you must save old run results before they
        expire."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.1/jobs/runs/get-output", query=query, body=body
        )
        return RunOutput.from_dict(json)

    def list(self, request: List) -> ListJobsResponse:
        """List all jobs.

        Retrieves a list of jobs."""
        query, body = request.as_request()
        json = self._api.do("GET", "/api/2.1/jobs/list", query=query, body=body)
        return ListJobsResponse.from_dict(json)

    def list_runs(self, request: ListRuns) -> ListRunsResponse:
        """List runs for a job.

        List runs in descending order by start time."""
        query, body = request.as_request()
        json = self._api.do("GET", "/api/2.1/jobs/runs/list", query=query, body=body)
        return ListRunsResponse.from_dict(json)

    def repair_run(self, request: RepairRun) -> RepairRunResponse:
        """Repair a job run.

        Re-run one or more tasks. Tasks are re-run as part of the original job
        run. They use the current job and task settings, and can be viewed in
        the history for the original job run."""
        query, body = request.as_request()
        json = self._api.do("POST", "/api/2.1/jobs/runs/repair", query=query, body=body)
        return RepairRunResponse.from_dict(json)

    def reset(self, request: ResetJob):
        """Overwrites all settings for a job.

        Overwrites all the settings for a specific job. Use the Update endpoint
        to update job settings partially."""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.1/jobs/reset", query=query, body=body)

    def run_now(self, request: RunNow) -> RunNowResponse:
        """Trigger a new job run.

        Run a job and return the `run_id` of the triggered run."""
        query, body = request.as_request()
        json = self._api.do("POST", "/api/2.1/jobs/run-now", query=query, body=body)
        return RunNowResponse.from_dict(json)

    def submit(self, request: SubmitRun) -> SubmitRunResponse:
        """Create and trigger a one-time run.

        Submit a one-time run. This endpoint allows you to submit a workload
        directly without creating a job. Runs submitted using this endpoint
        don’t display in the UI. Use the `jobs/runs/get` API to check the run
        state after the job is submitted."""
        query, body = request.as_request()
        json = self._api.do("POST", "/api/2.1/jobs/runs/submit", query=query, body=body)
        return SubmitRunResponse.from_dict(json)

    def update(self, request: UpdateJob):
        """Partially updates a job.

        Add, update, or remove specific settings of an existing job. Use the
        ResetJob to overwrite all job settings."""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.1/jobs/update", query=query, body=body)

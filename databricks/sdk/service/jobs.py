# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
import random
import time
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Any, Callable, Dict, Iterator, List, Optional

from ..core import ApiClient
from ..errors import OperationFailed
from ._internal import Wait, _enum, _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

from .compute import BaseClusterInfo, Library
from .iam import AccessControlRequest

# all definitions in this file are in alphabetical order


@dataclass
class BaseJob:
    created_time: Optional[int] = None
    creator_user_name: Optional[str] = None
    job_id: Optional[int] = None
    settings: Optional['JobSettings'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.created_time: body['created_time'] = self.created_time
        if self.creator_user_name: body['creator_user_name'] = self.creator_user_name
        if self.job_id: body['job_id'] = self.job_id
        if self.settings: body['settings'] = self.settings.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'BaseJob':
        return cls(created_time=d.get('created_time', None),
                   creator_user_name=d.get('creator_user_name', None),
                   job_id=d.get('job_id', None),
                   settings=_from_dict(d, 'settings', JobSettings))


@dataclass
class BaseRun:
    attempt_number: Optional[int] = None
    cleanup_duration: Optional[int] = None
    cluster_instance: Optional['ClusterInstance'] = None
    cluster_spec: Optional['ClusterSpec'] = None
    continuous: Optional['Continuous'] = None
    creator_user_name: Optional[str] = None
    end_time: Optional[int] = None
    execution_duration: Optional[int] = None
    git_source: Optional['GitSource'] = None
    job_clusters: Optional['List[JobCluster]'] = None
    job_id: Optional[int] = None
    number_in_job: Optional[int] = None
    original_attempt_run_id: Optional[int] = None
    overriding_parameters: Optional['RunParameters'] = None
    run_duration: Optional[int] = None
    run_id: Optional[int] = None
    run_name: Optional[str] = None
    run_page_url: Optional[str] = None
    run_type: Optional['RunType'] = None
    schedule: Optional['CronSchedule'] = None
    setup_duration: Optional[int] = None
    start_time: Optional[int] = None
    state: Optional['RunState'] = None
    tasks: Optional['List[RunTask]'] = None
    trigger: Optional['TriggerType'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.attempt_number: body['attempt_number'] = self.attempt_number
        if self.cleanup_duration: body['cleanup_duration'] = self.cleanup_duration
        if self.cluster_instance: body['cluster_instance'] = self.cluster_instance.as_dict()
        if self.cluster_spec: body['cluster_spec'] = self.cluster_spec.as_dict()
        if self.continuous: body['continuous'] = self.continuous.as_dict()
        if self.creator_user_name: body['creator_user_name'] = self.creator_user_name
        if self.end_time: body['end_time'] = self.end_time
        if self.execution_duration: body['execution_duration'] = self.execution_duration
        if self.git_source: body['git_source'] = self.git_source.as_dict()
        if self.job_clusters: body['job_clusters'] = [v.as_dict() for v in self.job_clusters]
        if self.job_id: body['job_id'] = self.job_id
        if self.number_in_job: body['number_in_job'] = self.number_in_job
        if self.original_attempt_run_id: body['original_attempt_run_id'] = self.original_attempt_run_id
        if self.overriding_parameters: body['overriding_parameters'] = self.overriding_parameters.as_dict()
        if self.run_duration: body['run_duration'] = self.run_duration
        if self.run_id: body['run_id'] = self.run_id
        if self.run_name: body['run_name'] = self.run_name
        if self.run_page_url: body['run_page_url'] = self.run_page_url
        if self.run_type: body['run_type'] = self.run_type.value
        if self.schedule: body['schedule'] = self.schedule.as_dict()
        if self.setup_duration: body['setup_duration'] = self.setup_duration
        if self.start_time: body['start_time'] = self.start_time
        if self.state: body['state'] = self.state.as_dict()
        if self.tasks: body['tasks'] = [v.as_dict() for v in self.tasks]
        if self.trigger: body['trigger'] = self.trigger.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'BaseRun':
        return cls(attempt_number=d.get('attempt_number', None),
                   cleanup_duration=d.get('cleanup_duration', None),
                   cluster_instance=_from_dict(d, 'cluster_instance', ClusterInstance),
                   cluster_spec=_from_dict(d, 'cluster_spec', ClusterSpec),
                   continuous=_from_dict(d, 'continuous', Continuous),
                   creator_user_name=d.get('creator_user_name', None),
                   end_time=d.get('end_time', None),
                   execution_duration=d.get('execution_duration', None),
                   git_source=_from_dict(d, 'git_source', GitSource),
                   job_clusters=_repeated(d, 'job_clusters', JobCluster),
                   job_id=d.get('job_id', None),
                   number_in_job=d.get('number_in_job', None),
                   original_attempt_run_id=d.get('original_attempt_run_id', None),
                   overriding_parameters=_from_dict(d, 'overriding_parameters', RunParameters),
                   run_duration=d.get('run_duration', None),
                   run_id=d.get('run_id', None),
                   run_name=d.get('run_name', None),
                   run_page_url=d.get('run_page_url', None),
                   run_type=_enum(d, 'run_type', RunType),
                   schedule=_from_dict(d, 'schedule', CronSchedule),
                   setup_duration=d.get('setup_duration', None),
                   start_time=d.get('start_time', None),
                   state=_from_dict(d, 'state', RunState),
                   tasks=_repeated(d, 'tasks', RunTask),
                   trigger=_enum(d, 'trigger', TriggerType))


@dataclass
class CancelAllRuns:
    job_id: int

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.job_id: body['job_id'] = self.job_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'CancelAllRuns':
        return cls(job_id=d.get('job_id', None))


@dataclass
class CancelRun:
    run_id: int

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.run_id: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'CancelRun':
        return cls(run_id=d.get('run_id', None))


@dataclass
class ClusterInstance:
    cluster_id: Optional[str] = None
    spark_context_id: Optional[str] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.spark_context_id: body['spark_context_id'] = self.spark_context_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'ClusterInstance':
        return cls(cluster_id=d.get('cluster_id', None), spark_context_id=d.get('spark_context_id', None))


@dataclass
class ClusterSpec:
    existing_cluster_id: Optional[str] = None
    libraries: Optional['List[Library]'] = None
    new_cluster: Optional['BaseClusterInfo'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.existing_cluster_id: body['existing_cluster_id'] = self.existing_cluster_id
        if self.libraries: body['libraries'] = [v for v in self.libraries]
        if self.new_cluster: body['new_cluster'] = self.new_cluster.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'ClusterSpec':
        return cls(existing_cluster_id=d.get('existing_cluster_id', None),
                   libraries=d.get('libraries', None),
                   new_cluster=_from_dict(d, 'new_cluster', BaseClusterInfo))


@dataclass
class Continuous:
    pause_status: Optional['ContinuousPauseStatus'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.pause_status: body['pause_status'] = self.pause_status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'Continuous':
        return cls(pause_status=_enum(d, 'pause_status', ContinuousPauseStatus))


class ContinuousPauseStatus(Enum):
    """Indicate whether the continuous execution of the job is paused or not. Defaults to UNPAUSED."""

    PAUSED = 'PAUSED'
    UNPAUSED = 'UNPAUSED'


@dataclass
class CreateJob:
    access_control_list: Optional['List[AccessControlRequest]'] = None
    continuous: Optional['Continuous'] = None
    email_notifications: Optional['JobEmailNotifications'] = None
    format: Optional['CreateJobFormat'] = None
    git_source: Optional['GitSource'] = None
    job_clusters: Optional['List[JobCluster]'] = None
    max_concurrent_runs: Optional[int] = None
    name: Optional[str] = None
    schedule: Optional['CronSchedule'] = None
    tags: Optional['Dict[str,str]'] = None
    tasks: Optional['List[JobTaskSettings]'] = None
    timeout_seconds: Optional[int] = None
    trigger: Optional['TriggerSettings'] = None
    webhook_notifications: Optional['JobWebhookNotifications'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.access_control_list: body['access_control_list'] = [v for v in self.access_control_list]
        if self.continuous: body['continuous'] = self.continuous.as_dict()
        if self.email_notifications: body['email_notifications'] = self.email_notifications.as_dict()
        if self.format: body['format'] = self.format.value
        if self.git_source: body['git_source'] = self.git_source.as_dict()
        if self.job_clusters: body['job_clusters'] = [v.as_dict() for v in self.job_clusters]
        if self.max_concurrent_runs: body['max_concurrent_runs'] = self.max_concurrent_runs
        if self.name: body['name'] = self.name
        if self.schedule: body['schedule'] = self.schedule.as_dict()
        if self.tags: body['tags'] = self.tags
        if self.tasks: body['tasks'] = [v.as_dict() for v in self.tasks]
        if self.timeout_seconds: body['timeout_seconds'] = self.timeout_seconds
        if self.trigger: body['trigger'] = self.trigger.as_dict()
        if self.webhook_notifications: body['webhook_notifications'] = self.webhook_notifications.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'CreateJob':
        return cls(access_control_list=d.get('access_control_list', None),
                   continuous=_from_dict(d, 'continuous', Continuous),
                   email_notifications=_from_dict(d, 'email_notifications', JobEmailNotifications),
                   format=_enum(d, 'format', CreateJobFormat),
                   git_source=_from_dict(d, 'git_source', GitSource),
                   job_clusters=_repeated(d, 'job_clusters', JobCluster),
                   max_concurrent_runs=d.get('max_concurrent_runs', None),
                   name=d.get('name', None),
                   schedule=_from_dict(d, 'schedule', CronSchedule),
                   tags=d.get('tags', None),
                   tasks=_repeated(d, 'tasks', JobTaskSettings),
                   timeout_seconds=d.get('timeout_seconds', None),
                   trigger=_from_dict(d, 'trigger', TriggerSettings),
                   webhook_notifications=_from_dict(d, 'webhook_notifications', JobWebhookNotifications))


class CreateJobFormat(Enum):
    """Used to tell what is the format of the job. This field is ignored in Create/Update/Reset calls.
    When using the Jobs API 2.1 this value is always set to `"MULTI_TASK"`."""

    MULTI_TASK = 'MULTI_TASK'
    SINGLE_TASK = 'SINGLE_TASK'


@dataclass
class CreateResponse:
    job_id: Optional[int] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.job_id: body['job_id'] = self.job_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'CreateResponse':
        return cls(job_id=d.get('job_id', None))


@dataclass
class CronSchedule:
    quartz_cron_expression: str
    timezone_id: str
    pause_status: Optional['CronSchedulePauseStatus'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.pause_status: body['pause_status'] = self.pause_status.value
        if self.quartz_cron_expression: body['quartz_cron_expression'] = self.quartz_cron_expression
        if self.timezone_id: body['timezone_id'] = self.timezone_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'CronSchedule':
        return cls(pause_status=_enum(d, 'pause_status', CronSchedulePauseStatus),
                   quartz_cron_expression=d.get('quartz_cron_expression', None),
                   timezone_id=d.get('timezone_id', None))


class CronSchedulePauseStatus(Enum):
    """Indicate whether this schedule is paused or not."""

    PAUSED = 'PAUSED'
    UNPAUSED = 'UNPAUSED'


@dataclass
class DbtOutput:
    artifacts_headers: Optional['Dict[str,str]'] = None
    artifacts_link: Optional[str] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.artifacts_headers: body['artifacts_headers'] = self.artifacts_headers
        if self.artifacts_link: body['artifacts_link'] = self.artifacts_link
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'DbtOutput':
        return cls(artifacts_headers=d.get('artifacts_headers', None),
                   artifacts_link=d.get('artifacts_link', None))


@dataclass
class DbtTask:
    commands: 'List[str]'
    catalog: Optional[str] = None
    profiles_directory: Optional[str] = None
    project_directory: Optional[str] = None
    schema: Optional[str] = None
    warehouse_id: Optional[str] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.catalog: body['catalog'] = self.catalog
        if self.commands: body['commands'] = [v for v in self.commands]
        if self.profiles_directory: body['profiles_directory'] = self.profiles_directory
        if self.project_directory: body['project_directory'] = self.project_directory
        if self.schema: body['schema'] = self.schema
        if self.warehouse_id: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'DbtTask':
        return cls(catalog=d.get('catalog', None),
                   commands=d.get('commands', None),
                   profiles_directory=d.get('profiles_directory', None),
                   project_directory=d.get('project_directory', None),
                   schema=d.get('schema', None),
                   warehouse_id=d.get('warehouse_id', None))


@dataclass
class DeleteJob:
    job_id: int

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.job_id: body['job_id'] = self.job_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'DeleteJob':
        return cls(job_id=d.get('job_id', None))


@dataclass
class DeleteRun:
    run_id: int

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.run_id: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'DeleteRun':
        return cls(run_id=d.get('run_id', None))


@dataclass
class ExportRunOutput:
    views: Optional['List[ViewItem]'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.views: body['views'] = [v.as_dict() for v in self.views]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'ExportRunOutput':
        return cls(views=_repeated(d, 'views', ViewItem))


@dataclass
class ExportRunRequest:
    """Export and retrieve a job run"""

    run_id: int
    views_to_export: Optional['ViewsToExport'] = None


@dataclass
class FileArrivalTriggerSettings:
    min_time_between_trigger_seconds: Optional[int] = None
    url: Optional[str] = None
    wait_after_last_change_seconds: Optional[int] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.min_time_between_trigger_seconds:
            body['min_time_between_trigger_seconds'] = self.min_time_between_trigger_seconds
        if self.url: body['url'] = self.url
        if self.wait_after_last_change_seconds:
            body['wait_after_last_change_seconds'] = self.wait_after_last_change_seconds
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'FileArrivalTriggerSettings':
        return cls(min_time_between_trigger_seconds=d.get('min_time_between_trigger_seconds', None),
                   url=d.get('url', None),
                   wait_after_last_change_seconds=d.get('wait_after_last_change_seconds', None))


@dataclass
class GetJobRequest:
    """Get a single job"""

    job_id: int


@dataclass
class GetRunOutputRequest:
    """Get the output for a single run"""

    run_id: int


@dataclass
class GetRunRequest:
    """Get a single job run"""

    run_id: int
    include_history: Optional[bool] = None


@dataclass
class GitSnapshot:
    """Read-only state of the remote repository at the time the job was run. This field is only
    included on job runs."""

    used_commit: Optional[str] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.used_commit: body['used_commit'] = self.used_commit
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'GitSnapshot':
        return cls(used_commit=d.get('used_commit', None))


@dataclass
class GitSource:
    """An optional specification for a remote repository containing the notebooks used by this job's
    notebook tasks."""

    git_url: str
    git_provider: 'GitSourceGitProvider'
    git_branch: Optional[str] = None
    git_commit: Optional[str] = None
    git_snapshot: Optional['GitSnapshot'] = None
    git_tag: Optional[str] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.git_branch: body['git_branch'] = self.git_branch
        if self.git_commit: body['git_commit'] = self.git_commit
        if self.git_provider: body['git_provider'] = self.git_provider.value
        if self.git_snapshot: body['git_snapshot'] = self.git_snapshot.as_dict()
        if self.git_tag: body['git_tag'] = self.git_tag
        if self.git_url: body['git_url'] = self.git_url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'GitSource':
        return cls(git_branch=d.get('git_branch', None),
                   git_commit=d.get('git_commit', None),
                   git_provider=_enum(d, 'git_provider', GitSourceGitProvider),
                   git_snapshot=_from_dict(d, 'git_snapshot', GitSnapshot),
                   git_tag=d.get('git_tag', None),
                   git_url=d.get('git_url', None))


class GitSourceGitProvider(Enum):
    """Unique identifier of the service used to host the Git repository. The value is case insensitive."""

    awsCodeCommit = 'awsCodeCommit'
    azureDevOpsServices = 'azureDevOpsServices'
    bitbucketCloud = 'bitbucketCloud'
    bitbucketServer = 'bitbucketServer'
    gitHub = 'gitHub'
    gitHubEnterprise = 'gitHubEnterprise'
    gitLab = 'gitLab'
    gitLabEnterpriseEdition = 'gitLabEnterpriseEdition'


@dataclass
class Job:
    created_time: Optional[int] = None
    creator_user_name: Optional[str] = None
    job_id: Optional[int] = None
    run_as_user_name: Optional[str] = None
    settings: Optional['JobSettings'] = None
    trigger_history: Optional['TriggerHistory'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.created_time: body['created_time'] = self.created_time
        if self.creator_user_name: body['creator_user_name'] = self.creator_user_name
        if self.job_id: body['job_id'] = self.job_id
        if self.run_as_user_name: body['run_as_user_name'] = self.run_as_user_name
        if self.settings: body['settings'] = self.settings.as_dict()
        if self.trigger_history: body['trigger_history'] = self.trigger_history.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'Job':
        return cls(created_time=d.get('created_time', None),
                   creator_user_name=d.get('creator_user_name', None),
                   job_id=d.get('job_id', None),
                   run_as_user_name=d.get('run_as_user_name', None),
                   settings=_from_dict(d, 'settings', JobSettings),
                   trigger_history=_from_dict(d, 'trigger_history', TriggerHistory))


@dataclass
class JobCluster:
    job_cluster_key: str
    new_cluster: Optional['BaseClusterInfo'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.job_cluster_key: body['job_cluster_key'] = self.job_cluster_key
        if self.new_cluster: body['new_cluster'] = self.new_cluster.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'JobCluster':
        return cls(job_cluster_key=d.get('job_cluster_key', None),
                   new_cluster=_from_dict(d, 'new_cluster', BaseClusterInfo))


@dataclass
class JobEmailNotifications:
    no_alert_for_skipped_runs: Optional[bool] = None
    on_failure: Optional['List[str]'] = None
    on_start: Optional['List[str]'] = None
    on_success: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.no_alert_for_skipped_runs: body['no_alert_for_skipped_runs'] = self.no_alert_for_skipped_runs
        if self.on_failure: body['on_failure'] = [v for v in self.on_failure]
        if self.on_start: body['on_start'] = [v for v in self.on_start]
        if self.on_success: body['on_success'] = [v for v in self.on_success]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'JobEmailNotifications':
        return cls(no_alert_for_skipped_runs=d.get('no_alert_for_skipped_runs', None),
                   on_failure=d.get('on_failure', None),
                   on_start=d.get('on_start', None),
                   on_success=d.get('on_success', None))


@dataclass
class JobSettings:
    continuous: Optional['Continuous'] = None
    email_notifications: Optional['JobEmailNotifications'] = None
    format: Optional['JobSettingsFormat'] = None
    git_source: Optional['GitSource'] = None
    job_clusters: Optional['List[JobCluster]'] = None
    max_concurrent_runs: Optional[int] = None
    name: Optional[str] = None
    schedule: Optional['CronSchedule'] = None
    tags: Optional['Dict[str,str]'] = None
    tasks: Optional['List[JobTaskSettings]'] = None
    timeout_seconds: Optional[int] = None
    trigger: Optional['TriggerSettings'] = None
    webhook_notifications: Optional['JobWebhookNotifications'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.continuous: body['continuous'] = self.continuous.as_dict()
        if self.email_notifications: body['email_notifications'] = self.email_notifications.as_dict()
        if self.format: body['format'] = self.format.value
        if self.git_source: body['git_source'] = self.git_source.as_dict()
        if self.job_clusters: body['job_clusters'] = [v.as_dict() for v in self.job_clusters]
        if self.max_concurrent_runs: body['max_concurrent_runs'] = self.max_concurrent_runs
        if self.name: body['name'] = self.name
        if self.schedule: body['schedule'] = self.schedule.as_dict()
        if self.tags: body['tags'] = self.tags
        if self.tasks: body['tasks'] = [v.as_dict() for v in self.tasks]
        if self.timeout_seconds: body['timeout_seconds'] = self.timeout_seconds
        if self.trigger: body['trigger'] = self.trigger.as_dict()
        if self.webhook_notifications: body['webhook_notifications'] = self.webhook_notifications.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'JobSettings':
        return cls(continuous=_from_dict(d, 'continuous', Continuous),
                   email_notifications=_from_dict(d, 'email_notifications', JobEmailNotifications),
                   format=_enum(d, 'format', JobSettingsFormat),
                   git_source=_from_dict(d, 'git_source', GitSource),
                   job_clusters=_repeated(d, 'job_clusters', JobCluster),
                   max_concurrent_runs=d.get('max_concurrent_runs', None),
                   name=d.get('name', None),
                   schedule=_from_dict(d, 'schedule', CronSchedule),
                   tags=d.get('tags', None),
                   tasks=_repeated(d, 'tasks', JobTaskSettings),
                   timeout_seconds=d.get('timeout_seconds', None),
                   trigger=_from_dict(d, 'trigger', TriggerSettings),
                   webhook_notifications=_from_dict(d, 'webhook_notifications', JobWebhookNotifications))


class JobSettingsFormat(Enum):
    """Used to tell what is the format of the job. This field is ignored in Create/Update/Reset calls.
    When using the Jobs API 2.1 this value is always set to `"MULTI_TASK"`."""

    MULTI_TASK = 'MULTI_TASK'
    SINGLE_TASK = 'SINGLE_TASK'


@dataclass
class JobTaskSettings:
    task_key: str
    dbt_task: Optional['DbtTask'] = None
    depends_on: Optional['List[TaskDependenciesItem]'] = None
    description: Optional[str] = None
    email_notifications: Optional['JobEmailNotifications'] = None
    existing_cluster_id: Optional[str] = None
    job_cluster_key: Optional[str] = None
    libraries: Optional['List[Library]'] = None
    max_retries: Optional[int] = None
    min_retry_interval_millis: Optional[int] = None
    new_cluster: Optional['BaseClusterInfo'] = None
    notebook_task: Optional['NotebookTask'] = None
    pipeline_task: Optional['PipelineTask'] = None
    python_wheel_task: Optional['PythonWheelTask'] = None
    retry_on_timeout: Optional[bool] = None
    spark_jar_task: Optional['SparkJarTask'] = None
    spark_python_task: Optional['SparkPythonTask'] = None
    spark_submit_task: Optional['SparkSubmitTask'] = None
    sql_task: Optional['SqlTask'] = None
    timeout_seconds: Optional[int] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.dbt_task: body['dbt_task'] = self.dbt_task.as_dict()
        if self.depends_on: body['depends_on'] = [v.as_dict() for v in self.depends_on]
        if self.description: body['description'] = self.description
        if self.email_notifications: body['email_notifications'] = self.email_notifications.as_dict()
        if self.existing_cluster_id: body['existing_cluster_id'] = self.existing_cluster_id
        if self.job_cluster_key: body['job_cluster_key'] = self.job_cluster_key
        if self.libraries: body['libraries'] = [v for v in self.libraries]
        if self.max_retries: body['max_retries'] = self.max_retries
        if self.min_retry_interval_millis: body['min_retry_interval_millis'] = self.min_retry_interval_millis
        if self.new_cluster: body['new_cluster'] = self.new_cluster.as_dict()
        if self.notebook_task: body['notebook_task'] = self.notebook_task.as_dict()
        if self.pipeline_task: body['pipeline_task'] = self.pipeline_task.as_dict()
        if self.python_wheel_task: body['python_wheel_task'] = self.python_wheel_task.as_dict()
        if self.retry_on_timeout: body['retry_on_timeout'] = self.retry_on_timeout
        if self.spark_jar_task: body['spark_jar_task'] = self.spark_jar_task.as_dict()
        if self.spark_python_task: body['spark_python_task'] = self.spark_python_task.as_dict()
        if self.spark_submit_task: body['spark_submit_task'] = self.spark_submit_task.as_dict()
        if self.sql_task: body['sql_task'] = self.sql_task.as_dict()
        if self.task_key: body['task_key'] = self.task_key
        if self.timeout_seconds: body['timeout_seconds'] = self.timeout_seconds
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'JobTaskSettings':
        return cls(dbt_task=_from_dict(d, 'dbt_task', DbtTask),
                   depends_on=_repeated(d, 'depends_on', TaskDependenciesItem),
                   description=d.get('description', None),
                   email_notifications=_from_dict(d, 'email_notifications', JobEmailNotifications),
                   existing_cluster_id=d.get('existing_cluster_id', None),
                   job_cluster_key=d.get('job_cluster_key', None),
                   libraries=d.get('libraries', None),
                   max_retries=d.get('max_retries', None),
                   min_retry_interval_millis=d.get('min_retry_interval_millis', None),
                   new_cluster=_from_dict(d, 'new_cluster', BaseClusterInfo),
                   notebook_task=_from_dict(d, 'notebook_task', NotebookTask),
                   pipeline_task=_from_dict(d, 'pipeline_task', PipelineTask),
                   python_wheel_task=_from_dict(d, 'python_wheel_task', PythonWheelTask),
                   retry_on_timeout=d.get('retry_on_timeout', None),
                   spark_jar_task=_from_dict(d, 'spark_jar_task', SparkJarTask),
                   spark_python_task=_from_dict(d, 'spark_python_task', SparkPythonTask),
                   spark_submit_task=_from_dict(d, 'spark_submit_task', SparkSubmitTask),
                   sql_task=_from_dict(d, 'sql_task', SqlTask),
                   task_key=d.get('task_key', None),
                   timeout_seconds=d.get('timeout_seconds', None))


@dataclass
class JobWebhookNotifications:
    on_failure: Optional['List[JobWebhookNotificationsOnFailureItem]'] = None
    on_start: Optional['List[JobWebhookNotificationsOnStartItem]'] = None
    on_success: Optional['List[JobWebhookNotificationsOnSuccessItem]'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.on_failure: body['on_failure'] = [v.as_dict() for v in self.on_failure]
        if self.on_start: body['on_start'] = [v.as_dict() for v in self.on_start]
        if self.on_success: body['on_success'] = [v.as_dict() for v in self.on_success]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'JobWebhookNotifications':
        return cls(on_failure=_repeated(d, 'on_failure', JobWebhookNotificationsOnFailureItem),
                   on_start=_repeated(d, 'on_start', JobWebhookNotificationsOnStartItem),
                   on_success=_repeated(d, 'on_success', JobWebhookNotificationsOnSuccessItem))


@dataclass
class JobWebhookNotificationsOnFailureItem:
    id: Optional[str] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.id: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'JobWebhookNotificationsOnFailureItem':
        return cls(id=d.get('id', None))


@dataclass
class JobWebhookNotificationsOnStartItem:
    id: Optional[str] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.id: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'JobWebhookNotificationsOnStartItem':
        return cls(id=d.get('id', None))


@dataclass
class JobWebhookNotificationsOnSuccessItem:
    id: Optional[str] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.id: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'JobWebhookNotificationsOnSuccessItem':
        return cls(id=d.get('id', None))


@dataclass
class ListJobsRequest:
    """List all jobs"""

    expand_tasks: Optional[bool] = None
    limit: Optional[int] = None
    name: Optional[str] = None
    offset: Optional[int] = None


@dataclass
class ListJobsResponse:
    has_more: Optional[bool] = None
    jobs: Optional['List[BaseJob]'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.has_more: body['has_more'] = self.has_more
        if self.jobs: body['jobs'] = [v.as_dict() for v in self.jobs]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'ListJobsResponse':
        return cls(has_more=d.get('has_more', None), jobs=_repeated(d, 'jobs', BaseJob))


@dataclass
class ListRunsRequest:
    """List runs for a job"""

    active_only: Optional[bool] = None
    completed_only: Optional[bool] = None
    expand_tasks: Optional[bool] = None
    job_id: Optional[int] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    run_type: Optional['ListRunsRunType'] = None
    start_time_from: Optional[int] = None
    start_time_to: Optional[int] = None


@dataclass
class ListRunsResponse:
    has_more: Optional[bool] = None
    runs: Optional['List[BaseRun]'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.has_more: body['has_more'] = self.has_more
        if self.runs: body['runs'] = [v.as_dict() for v in self.runs]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'ListRunsResponse':
        return cls(has_more=d.get('has_more', None), runs=_repeated(d, 'runs', BaseRun))


class ListRunsRunType(Enum):
    """This describes an enum"""

    JOB_RUN = 'JOB_RUN'
    SUBMIT_RUN = 'SUBMIT_RUN'
    WORKFLOW_RUN = 'WORKFLOW_RUN'


@dataclass
class NotebookOutput:
    result: Optional[str] = None
    truncated: Optional[bool] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.result: body['result'] = self.result
        if self.truncated: body['truncated'] = self.truncated
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'NotebookOutput':
        return cls(result=d.get('result', None), truncated=d.get('truncated', None))


@dataclass
class NotebookTask:
    notebook_path: str
    base_parameters: Optional['Dict[str,str]'] = None
    source: Optional['NotebookTaskSource'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.base_parameters: body['base_parameters'] = self.base_parameters
        if self.notebook_path: body['notebook_path'] = self.notebook_path
        if self.source: body['source'] = self.source.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'NotebookTask':
        return cls(base_parameters=d.get('base_parameters', None),
                   notebook_path=d.get('notebook_path', None),
                   source=_enum(d, 'source', NotebookTaskSource))


class NotebookTaskSource(Enum):
    """This describes an enum"""

    GIT = 'GIT'
    WORKSPACE = 'WORKSPACE'


@dataclass
class PipelineParams:
    full_refresh: Optional[bool] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.full_refresh: body['full_refresh'] = self.full_refresh
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'PipelineParams':
        return cls(full_refresh=d.get('full_refresh', None))


@dataclass
class PipelineTask:
    full_refresh: Optional[bool] = None
    pipeline_id: Optional[str] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.full_refresh: body['full_refresh'] = self.full_refresh
        if self.pipeline_id: body['pipeline_id'] = self.pipeline_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'PipelineTask':
        return cls(full_refresh=d.get('full_refresh', None), pipeline_id=d.get('pipeline_id', None))


@dataclass
class PythonWheelTask:
    entry_point: Optional[str] = None
    named_parameters: Optional['Dict[str,str]'] = None
    package_name: Optional[str] = None
    parameters: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.entry_point: body['entry_point'] = self.entry_point
        if self.named_parameters: body['named_parameters'] = self.named_parameters
        if self.package_name: body['package_name'] = self.package_name
        if self.parameters: body['parameters'] = [v for v in self.parameters]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'PythonWheelTask':
        return cls(entry_point=d.get('entry_point', None),
                   named_parameters=d.get('named_parameters', None),
                   package_name=d.get('package_name', None),
                   parameters=d.get('parameters', None))


@dataclass
class RepairHistoryItem:
    end_time: Optional[int] = None
    id: Optional[int] = None
    start_time: Optional[int] = None
    state: Optional['RunState'] = None
    task_run_ids: Optional['List[int]'] = None
    type: Optional['RepairHistoryItemType'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.end_time: body['end_time'] = self.end_time
        if self.id: body['id'] = self.id
        if self.start_time: body['start_time'] = self.start_time
        if self.state: body['state'] = self.state.as_dict()
        if self.task_run_ids: body['task_run_ids'] = [v for v in self.task_run_ids]
        if self.type: body['type'] = self.type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'RepairHistoryItem':
        return cls(end_time=d.get('end_time', None),
                   id=d.get('id', None),
                   start_time=d.get('start_time', None),
                   state=_from_dict(d, 'state', RunState),
                   task_run_ids=d.get('task_run_ids', None),
                   type=_enum(d, 'type', RepairHistoryItemType))


class RepairHistoryItemType(Enum):
    """The repair history item type. Indicates whether a run is the original run or a repair run."""

    ORIGINAL = 'ORIGINAL'
    REPAIR = 'REPAIR'


@dataclass
class RepairRun:
    run_id: int
    dbt_commands: Optional['List[str]'] = None
    jar_params: Optional['List[str]'] = None
    latest_repair_id: Optional[int] = None
    notebook_params: Optional['Dict[str,str]'] = None
    pipeline_params: Optional['PipelineParams'] = None
    python_named_params: Optional['Dict[str,str]'] = None
    python_params: Optional['List[str]'] = None
    rerun_all_failed_tasks: Optional[bool] = None
    rerun_tasks: Optional['List[str]'] = None
    spark_submit_params: Optional['List[str]'] = None
    sql_params: Optional['Dict[str,str]'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.dbt_commands: body['dbt_commands'] = [v for v in self.dbt_commands]
        if self.jar_params: body['jar_params'] = [v for v in self.jar_params]
        if self.latest_repair_id: body['latest_repair_id'] = self.latest_repair_id
        if self.notebook_params: body['notebook_params'] = self.notebook_params
        if self.pipeline_params: body['pipeline_params'] = self.pipeline_params.as_dict()
        if self.python_named_params: body['python_named_params'] = self.python_named_params
        if self.python_params: body['python_params'] = [v for v in self.python_params]
        if self.rerun_all_failed_tasks: body['rerun_all_failed_tasks'] = self.rerun_all_failed_tasks
        if self.rerun_tasks: body['rerun_tasks'] = [v for v in self.rerun_tasks]
        if self.run_id: body['run_id'] = self.run_id
        if self.spark_submit_params: body['spark_submit_params'] = [v for v in self.spark_submit_params]
        if self.sql_params: body['sql_params'] = self.sql_params
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'RepairRun':
        return cls(dbt_commands=d.get('dbt_commands', None),
                   jar_params=d.get('jar_params', None),
                   latest_repair_id=d.get('latest_repair_id', None),
                   notebook_params=d.get('notebook_params', None),
                   pipeline_params=_from_dict(d, 'pipeline_params', PipelineParams),
                   python_named_params=d.get('python_named_params', None),
                   python_params=d.get('python_params', None),
                   rerun_all_failed_tasks=d.get('rerun_all_failed_tasks', None),
                   rerun_tasks=d.get('rerun_tasks', None),
                   run_id=d.get('run_id', None),
                   spark_submit_params=d.get('spark_submit_params', None),
                   sql_params=d.get('sql_params', None))


@dataclass
class RepairRunResponse:
    repair_id: Optional[int] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.repair_id: body['repair_id'] = self.repair_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'RepairRunResponse':
        return cls(repair_id=d.get('repair_id', None))


@dataclass
class ResetJob:
    job_id: int
    new_settings: 'JobSettings'

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.job_id: body['job_id'] = self.job_id
        if self.new_settings: body['new_settings'] = self.new_settings.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'ResetJob':
        return cls(job_id=d.get('job_id', None), new_settings=_from_dict(d, 'new_settings', JobSettings))


@dataclass
class Run:
    attempt_number: Optional[int] = None
    cleanup_duration: Optional[int] = None
    cluster_instance: Optional['ClusterInstance'] = None
    cluster_spec: Optional['ClusterSpec'] = None
    continuous: Optional['Continuous'] = None
    creator_user_name: Optional[str] = None
    end_time: Optional[int] = None
    execution_duration: Optional[int] = None
    git_source: Optional['GitSource'] = None
    job_clusters: Optional['List[JobCluster]'] = None
    job_id: Optional[int] = None
    number_in_job: Optional[int] = None
    original_attempt_run_id: Optional[int] = None
    overriding_parameters: Optional['RunParameters'] = None
    repair_history: Optional['List[RepairHistoryItem]'] = None
    run_duration: Optional[int] = None
    run_id: Optional[int] = None
    run_name: Optional[str] = None
    run_page_url: Optional[str] = None
    run_type: Optional['RunType'] = None
    schedule: Optional['CronSchedule'] = None
    setup_duration: Optional[int] = None
    start_time: Optional[int] = None
    state: Optional['RunState'] = None
    tasks: Optional['List[RunTask]'] = None
    trigger: Optional['TriggerType'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.attempt_number: body['attempt_number'] = self.attempt_number
        if self.cleanup_duration: body['cleanup_duration'] = self.cleanup_duration
        if self.cluster_instance: body['cluster_instance'] = self.cluster_instance.as_dict()
        if self.cluster_spec: body['cluster_spec'] = self.cluster_spec.as_dict()
        if self.continuous: body['continuous'] = self.continuous.as_dict()
        if self.creator_user_name: body['creator_user_name'] = self.creator_user_name
        if self.end_time: body['end_time'] = self.end_time
        if self.execution_duration: body['execution_duration'] = self.execution_duration
        if self.git_source: body['git_source'] = self.git_source.as_dict()
        if self.job_clusters: body['job_clusters'] = [v.as_dict() for v in self.job_clusters]
        if self.job_id: body['job_id'] = self.job_id
        if self.number_in_job: body['number_in_job'] = self.number_in_job
        if self.original_attempt_run_id: body['original_attempt_run_id'] = self.original_attempt_run_id
        if self.overriding_parameters: body['overriding_parameters'] = self.overriding_parameters.as_dict()
        if self.repair_history: body['repair_history'] = [v.as_dict() for v in self.repair_history]
        if self.run_duration: body['run_duration'] = self.run_duration
        if self.run_id: body['run_id'] = self.run_id
        if self.run_name: body['run_name'] = self.run_name
        if self.run_page_url: body['run_page_url'] = self.run_page_url
        if self.run_type: body['run_type'] = self.run_type.value
        if self.schedule: body['schedule'] = self.schedule.as_dict()
        if self.setup_duration: body['setup_duration'] = self.setup_duration
        if self.start_time: body['start_time'] = self.start_time
        if self.state: body['state'] = self.state.as_dict()
        if self.tasks: body['tasks'] = [v.as_dict() for v in self.tasks]
        if self.trigger: body['trigger'] = self.trigger.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'Run':
        return cls(attempt_number=d.get('attempt_number', None),
                   cleanup_duration=d.get('cleanup_duration', None),
                   cluster_instance=_from_dict(d, 'cluster_instance', ClusterInstance),
                   cluster_spec=_from_dict(d, 'cluster_spec', ClusterSpec),
                   continuous=_from_dict(d, 'continuous', Continuous),
                   creator_user_name=d.get('creator_user_name', None),
                   end_time=d.get('end_time', None),
                   execution_duration=d.get('execution_duration', None),
                   git_source=_from_dict(d, 'git_source', GitSource),
                   job_clusters=_repeated(d, 'job_clusters', JobCluster),
                   job_id=d.get('job_id', None),
                   number_in_job=d.get('number_in_job', None),
                   original_attempt_run_id=d.get('original_attempt_run_id', None),
                   overriding_parameters=_from_dict(d, 'overriding_parameters', RunParameters),
                   repair_history=_repeated(d, 'repair_history', RepairHistoryItem),
                   run_duration=d.get('run_duration', None),
                   run_id=d.get('run_id', None),
                   run_name=d.get('run_name', None),
                   run_page_url=d.get('run_page_url', None),
                   run_type=_enum(d, 'run_type', RunType),
                   schedule=_from_dict(d, 'schedule', CronSchedule),
                   setup_duration=d.get('setup_duration', None),
                   start_time=d.get('start_time', None),
                   state=_from_dict(d, 'state', RunState),
                   tasks=_repeated(d, 'tasks', RunTask),
                   trigger=_enum(d, 'trigger', TriggerType))


class RunLifeCycleState(Enum):
    """This describes an enum"""

    BLOCKED = 'BLOCKED'
    INTERNAL_ERROR = 'INTERNAL_ERROR'
    PENDING = 'PENDING'
    RUNNING = 'RUNNING'
    SKIPPED = 'SKIPPED'
    TERMINATED = 'TERMINATED'
    TERMINATING = 'TERMINATING'
    WAITING_FOR_RETRY = 'WAITING_FOR_RETRY'


@dataclass
class RunNow:
    job_id: int
    dbt_commands: Optional['List[str]'] = None
    idempotency_token: Optional[str] = None
    jar_params: Optional['List[str]'] = None
    notebook_params: Optional['Dict[str,str]'] = None
    pipeline_params: Optional['PipelineParams'] = None
    python_named_params: Optional['Dict[str,str]'] = None
    python_params: Optional['List[str]'] = None
    spark_submit_params: Optional['List[str]'] = None
    sql_params: Optional['Dict[str,str]'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.dbt_commands: body['dbt_commands'] = [v for v in self.dbt_commands]
        if self.idempotency_token: body['idempotency_token'] = self.idempotency_token
        if self.jar_params: body['jar_params'] = [v for v in self.jar_params]
        if self.job_id: body['job_id'] = self.job_id
        if self.notebook_params: body['notebook_params'] = self.notebook_params
        if self.pipeline_params: body['pipeline_params'] = self.pipeline_params.as_dict()
        if self.python_named_params: body['python_named_params'] = self.python_named_params
        if self.python_params: body['python_params'] = [v for v in self.python_params]
        if self.spark_submit_params: body['spark_submit_params'] = [v for v in self.spark_submit_params]
        if self.sql_params: body['sql_params'] = self.sql_params
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'RunNow':
        return cls(dbt_commands=d.get('dbt_commands', None),
                   idempotency_token=d.get('idempotency_token', None),
                   jar_params=d.get('jar_params', None),
                   job_id=d.get('job_id', None),
                   notebook_params=d.get('notebook_params', None),
                   pipeline_params=_from_dict(d, 'pipeline_params', PipelineParams),
                   python_named_params=d.get('python_named_params', None),
                   python_params=d.get('python_params', None),
                   spark_submit_params=d.get('spark_submit_params', None),
                   sql_params=d.get('sql_params', None))


@dataclass
class RunNowResponse:
    number_in_job: Optional[int] = None
    run_id: Optional[int] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.number_in_job: body['number_in_job'] = self.number_in_job
        if self.run_id: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'RunNowResponse':
        return cls(number_in_job=d.get('number_in_job', None), run_id=d.get('run_id', None))


@dataclass
class RunOutput:
    dbt_output: Optional['DbtOutput'] = None
    error: Optional[str] = None
    error_trace: Optional[str] = None
    logs: Optional[str] = None
    logs_truncated: Optional[bool] = None
    metadata: Optional['Run'] = None
    notebook_output: Optional['NotebookOutput'] = None
    sql_output: Optional['SqlOutput'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.dbt_output: body['dbt_output'] = self.dbt_output.as_dict()
        if self.error: body['error'] = self.error
        if self.error_trace: body['error_trace'] = self.error_trace
        if self.logs: body['logs'] = self.logs
        if self.logs_truncated: body['logs_truncated'] = self.logs_truncated
        if self.metadata: body['metadata'] = self.metadata.as_dict()
        if self.notebook_output: body['notebook_output'] = self.notebook_output.as_dict()
        if self.sql_output: body['sql_output'] = self.sql_output.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'RunOutput':
        return cls(dbt_output=_from_dict(d, 'dbt_output', DbtOutput),
                   error=d.get('error', None),
                   error_trace=d.get('error_trace', None),
                   logs=d.get('logs', None),
                   logs_truncated=d.get('logs_truncated', None),
                   metadata=_from_dict(d, 'metadata', Run),
                   notebook_output=_from_dict(d, 'notebook_output', NotebookOutput),
                   sql_output=_from_dict(d, 'sql_output', SqlOutput))


@dataclass
class RunParameters:
    dbt_commands: Optional['List[str]'] = None
    jar_params: Optional['List[str]'] = None
    notebook_params: Optional['Dict[str,str]'] = None
    pipeline_params: Optional['PipelineParams'] = None
    python_named_params: Optional['Dict[str,str]'] = None
    python_params: Optional['List[str]'] = None
    spark_submit_params: Optional['List[str]'] = None
    sql_params: Optional['Dict[str,str]'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.dbt_commands: body['dbt_commands'] = [v for v in self.dbt_commands]
        if self.jar_params: body['jar_params'] = [v for v in self.jar_params]
        if self.notebook_params: body['notebook_params'] = self.notebook_params
        if self.pipeline_params: body['pipeline_params'] = self.pipeline_params.as_dict()
        if self.python_named_params: body['python_named_params'] = self.python_named_params
        if self.python_params: body['python_params'] = [v for v in self.python_params]
        if self.spark_submit_params: body['spark_submit_params'] = [v for v in self.spark_submit_params]
        if self.sql_params: body['sql_params'] = self.sql_params
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'RunParameters':
        return cls(dbt_commands=d.get('dbt_commands', None),
                   jar_params=d.get('jar_params', None),
                   notebook_params=d.get('notebook_params', None),
                   pipeline_params=_from_dict(d, 'pipeline_params', PipelineParams),
                   python_named_params=d.get('python_named_params', None),
                   python_params=d.get('python_params', None),
                   spark_submit_params=d.get('spark_submit_params', None),
                   sql_params=d.get('sql_params', None))


class RunResultState(Enum):
    """This describes an enum"""

    CANCELED = 'CANCELED'
    FAILED = 'FAILED'
    SUCCESS = 'SUCCESS'
    TIMEDOUT = 'TIMEDOUT'


@dataclass
class RunState:
    """The result and lifecycle state of the run."""

    life_cycle_state: Optional['RunLifeCycleState'] = None
    result_state: Optional['RunResultState'] = None
    state_message: Optional[str] = None
    user_cancelled_or_timedout: Optional[bool] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.life_cycle_state: body['life_cycle_state'] = self.life_cycle_state.value
        if self.result_state: body['result_state'] = self.result_state.value
        if self.state_message: body['state_message'] = self.state_message
        if self.user_cancelled_or_timedout:
            body['user_cancelled_or_timedout'] = self.user_cancelled_or_timedout
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'RunState':
        return cls(life_cycle_state=_enum(d, 'life_cycle_state', RunLifeCycleState),
                   result_state=_enum(d, 'result_state', RunResultState),
                   state_message=d.get('state_message', None),
                   user_cancelled_or_timedout=d.get('user_cancelled_or_timedout', None))


@dataclass
class RunSubmitTaskSettings:
    task_key: str
    depends_on: Optional['List[TaskDependenciesItem]'] = None
    existing_cluster_id: Optional[str] = None
    libraries: Optional['List[Library]'] = None
    new_cluster: Optional['BaseClusterInfo'] = None
    notebook_task: Optional['NotebookTask'] = None
    pipeline_task: Optional['PipelineTask'] = None
    python_wheel_task: Optional['PythonWheelTask'] = None
    spark_jar_task: Optional['SparkJarTask'] = None
    spark_python_task: Optional['SparkPythonTask'] = None
    spark_submit_task: Optional['SparkSubmitTask'] = None
    timeout_seconds: Optional[int] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.depends_on: body['depends_on'] = [v.as_dict() for v in self.depends_on]
        if self.existing_cluster_id: body['existing_cluster_id'] = self.existing_cluster_id
        if self.libraries: body['libraries'] = [v for v in self.libraries]
        if self.new_cluster: body['new_cluster'] = self.new_cluster.as_dict()
        if self.notebook_task: body['notebook_task'] = self.notebook_task.as_dict()
        if self.pipeline_task: body['pipeline_task'] = self.pipeline_task.as_dict()
        if self.python_wheel_task: body['python_wheel_task'] = self.python_wheel_task.as_dict()
        if self.spark_jar_task: body['spark_jar_task'] = self.spark_jar_task.as_dict()
        if self.spark_python_task: body['spark_python_task'] = self.spark_python_task.as_dict()
        if self.spark_submit_task: body['spark_submit_task'] = self.spark_submit_task.as_dict()
        if self.task_key: body['task_key'] = self.task_key
        if self.timeout_seconds: body['timeout_seconds'] = self.timeout_seconds
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'RunSubmitTaskSettings':
        return cls(depends_on=_repeated(d, 'depends_on', TaskDependenciesItem),
                   existing_cluster_id=d.get('existing_cluster_id', None),
                   libraries=d.get('libraries', None),
                   new_cluster=_from_dict(d, 'new_cluster', BaseClusterInfo),
                   notebook_task=_from_dict(d, 'notebook_task', NotebookTask),
                   pipeline_task=_from_dict(d, 'pipeline_task', PipelineTask),
                   python_wheel_task=_from_dict(d, 'python_wheel_task', PythonWheelTask),
                   spark_jar_task=_from_dict(d, 'spark_jar_task', SparkJarTask),
                   spark_python_task=_from_dict(d, 'spark_python_task', SparkPythonTask),
                   spark_submit_task=_from_dict(d, 'spark_submit_task', SparkSubmitTask),
                   task_key=d.get('task_key', None),
                   timeout_seconds=d.get('timeout_seconds', None))


@dataclass
class RunTask:
    attempt_number: Optional[int] = None
    cleanup_duration: Optional[int] = None
    cluster_instance: Optional['ClusterInstance'] = None
    dbt_task: Optional['DbtTask'] = None
    depends_on: Optional['List[TaskDependenciesItem]'] = None
    description: Optional[str] = None
    end_time: Optional[int] = None
    execution_duration: Optional[int] = None
    existing_cluster_id: Optional[str] = None
    git_source: Optional['GitSource'] = None
    libraries: Optional['List[Library]'] = None
    new_cluster: Optional['BaseClusterInfo'] = None
    notebook_task: Optional['NotebookTask'] = None
    pipeline_task: Optional['PipelineTask'] = None
    python_wheel_task: Optional['PythonWheelTask'] = None
    run_id: Optional[int] = None
    setup_duration: Optional[int] = None
    spark_jar_task: Optional['SparkJarTask'] = None
    spark_python_task: Optional['SparkPythonTask'] = None
    spark_submit_task: Optional['SparkSubmitTask'] = None
    sql_task: Optional['SqlTask'] = None
    start_time: Optional[int] = None
    state: Optional['RunState'] = None
    task_key: Optional[str] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.attempt_number: body['attempt_number'] = self.attempt_number
        if self.cleanup_duration: body['cleanup_duration'] = self.cleanup_duration
        if self.cluster_instance: body['cluster_instance'] = self.cluster_instance.as_dict()
        if self.dbt_task: body['dbt_task'] = self.dbt_task.as_dict()
        if self.depends_on: body['depends_on'] = [v.as_dict() for v in self.depends_on]
        if self.description: body['description'] = self.description
        if self.end_time: body['end_time'] = self.end_time
        if self.execution_duration: body['execution_duration'] = self.execution_duration
        if self.existing_cluster_id: body['existing_cluster_id'] = self.existing_cluster_id
        if self.git_source: body['git_source'] = self.git_source.as_dict()
        if self.libraries: body['libraries'] = [v for v in self.libraries]
        if self.new_cluster: body['new_cluster'] = self.new_cluster.as_dict()
        if self.notebook_task: body['notebook_task'] = self.notebook_task.as_dict()
        if self.pipeline_task: body['pipeline_task'] = self.pipeline_task.as_dict()
        if self.python_wheel_task: body['python_wheel_task'] = self.python_wheel_task.as_dict()
        if self.run_id: body['run_id'] = self.run_id
        if self.setup_duration: body['setup_duration'] = self.setup_duration
        if self.spark_jar_task: body['spark_jar_task'] = self.spark_jar_task.as_dict()
        if self.spark_python_task: body['spark_python_task'] = self.spark_python_task.as_dict()
        if self.spark_submit_task: body['spark_submit_task'] = self.spark_submit_task.as_dict()
        if self.sql_task: body['sql_task'] = self.sql_task.as_dict()
        if self.start_time: body['start_time'] = self.start_time
        if self.state: body['state'] = self.state.as_dict()
        if self.task_key: body['task_key'] = self.task_key
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'RunTask':
        return cls(attempt_number=d.get('attempt_number', None),
                   cleanup_duration=d.get('cleanup_duration', None),
                   cluster_instance=_from_dict(d, 'cluster_instance', ClusterInstance),
                   dbt_task=_from_dict(d, 'dbt_task', DbtTask),
                   depends_on=_repeated(d, 'depends_on', TaskDependenciesItem),
                   description=d.get('description', None),
                   end_time=d.get('end_time', None),
                   execution_duration=d.get('execution_duration', None),
                   existing_cluster_id=d.get('existing_cluster_id', None),
                   git_source=_from_dict(d, 'git_source', GitSource),
                   libraries=d.get('libraries', None),
                   new_cluster=_from_dict(d, 'new_cluster', BaseClusterInfo),
                   notebook_task=_from_dict(d, 'notebook_task', NotebookTask),
                   pipeline_task=_from_dict(d, 'pipeline_task', PipelineTask),
                   python_wheel_task=_from_dict(d, 'python_wheel_task', PythonWheelTask),
                   run_id=d.get('run_id', None),
                   setup_duration=d.get('setup_duration', None),
                   spark_jar_task=_from_dict(d, 'spark_jar_task', SparkJarTask),
                   spark_python_task=_from_dict(d, 'spark_python_task', SparkPythonTask),
                   spark_submit_task=_from_dict(d, 'spark_submit_task', SparkSubmitTask),
                   sql_task=_from_dict(d, 'sql_task', SqlTask),
                   start_time=d.get('start_time', None),
                   state=_from_dict(d, 'state', RunState),
                   task_key=d.get('task_key', None))


class RunType(Enum):
    """This describes an enum"""

    JOB_RUN = 'JOB_RUN'
    SUBMIT_RUN = 'SUBMIT_RUN'
    WORKFLOW_RUN = 'WORKFLOW_RUN'


@dataclass
class SparkJarTask:
    jar_uri: Optional[str] = None
    main_class_name: Optional[str] = None
    parameters: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.jar_uri: body['jar_uri'] = self.jar_uri
        if self.main_class_name: body['main_class_name'] = self.main_class_name
        if self.parameters: body['parameters'] = [v for v in self.parameters]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'SparkJarTask':
        return cls(jar_uri=d.get('jar_uri', None),
                   main_class_name=d.get('main_class_name', None),
                   parameters=d.get('parameters', None))


@dataclass
class SparkPythonTask:
    python_file: str
    parameters: Optional['List[str]'] = None
    source: Optional['SparkPythonTaskSource'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.parameters: body['parameters'] = [v for v in self.parameters]
        if self.python_file: body['python_file'] = self.python_file
        if self.source: body['source'] = self.source.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'SparkPythonTask':
        return cls(parameters=d.get('parameters', None),
                   python_file=d.get('python_file', None),
                   source=_enum(d, 'source', SparkPythonTaskSource))


class SparkPythonTaskSource(Enum):
    """This describes an enum"""

    GIT = 'GIT'
    WORKSPACE = 'WORKSPACE'


@dataclass
class SparkSubmitTask:
    parameters: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.parameters: body['parameters'] = [v for v in self.parameters]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'SparkSubmitTask':
        return cls(parameters=d.get('parameters', None))


@dataclass
class SqlAlertOutput:
    alert_state: Optional['SqlAlertState'] = None
    output_link: Optional[str] = None
    query_text: Optional[str] = None
    sql_statements: Optional['List[SqlStatementOutput]'] = None
    warehouse_id: Optional[str] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.alert_state: body['alert_state'] = self.alert_state.value
        if self.output_link: body['output_link'] = self.output_link
        if self.query_text: body['query_text'] = self.query_text
        if self.sql_statements: body['sql_statements'] = [v.as_dict() for v in self.sql_statements]
        if self.warehouse_id: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'SqlAlertOutput':
        return cls(alert_state=_enum(d, 'alert_state', SqlAlertState),
                   output_link=d.get('output_link', None),
                   query_text=d.get('query_text', None),
                   sql_statements=_repeated(d, 'sql_statements', SqlStatementOutput),
                   warehouse_id=d.get('warehouse_id', None))


class SqlAlertState(Enum):
    """The state of the SQL alert.
    
    * UNKNOWN: alert yet to be evaluated * OK: alert evaluated and did not fulfill trigger
    conditions * TRIGGERED: alert evaluated and fulfilled trigger conditions"""

    OK = 'OK'
    TRIGGERED = 'TRIGGERED'
    UNKNOWN = 'UNKNOWN'


@dataclass
class SqlDashboardOutput:
    warehouse_id: Optional[str] = None
    widgets: Optional['SqlDashboardWidgetOutput'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.warehouse_id: body['warehouse_id'] = self.warehouse_id
        if self.widgets: body['widgets'] = self.widgets.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'SqlDashboardOutput':
        return cls(warehouse_id=d.get('warehouse_id', None),
                   widgets=_from_dict(d, 'widgets', SqlDashboardWidgetOutput))


@dataclass
class SqlDashboardWidgetOutput:
    end_time: Optional[int] = None
    error: Optional['SqlOutputError'] = None
    output_link: Optional[str] = None
    start_time: Optional[int] = None
    status: Optional['SqlDashboardWidgetOutputStatus'] = None
    widget_id: Optional[str] = None
    widget_title: Optional[str] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.end_time: body['end_time'] = self.end_time
        if self.error: body['error'] = self.error.as_dict()
        if self.output_link: body['output_link'] = self.output_link
        if self.start_time: body['start_time'] = self.start_time
        if self.status: body['status'] = self.status.value
        if self.widget_id: body['widget_id'] = self.widget_id
        if self.widget_title: body['widget_title'] = self.widget_title
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'SqlDashboardWidgetOutput':
        return cls(end_time=d.get('end_time', None),
                   error=_from_dict(d, 'error', SqlOutputError),
                   output_link=d.get('output_link', None),
                   start_time=d.get('start_time', None),
                   status=_enum(d, 'status', SqlDashboardWidgetOutputStatus),
                   widget_id=d.get('widget_id', None),
                   widget_title=d.get('widget_title', None))


class SqlDashboardWidgetOutputStatus(Enum):
    """The execution status of the SQL widget."""

    CANCELLED = 'CANCELLED'
    FAILED = 'FAILED'
    PENDING = 'PENDING'
    RUNNING = 'RUNNING'
    SUCCESS = 'SUCCESS'


@dataclass
class SqlOutput:
    alert_output: Optional['SqlAlertOutput'] = None
    dashboard_output: Optional['SqlDashboardOutput'] = None
    query_output: Optional['SqlQueryOutput'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.alert_output: body['alert_output'] = self.alert_output.as_dict()
        if self.dashboard_output: body['dashboard_output'] = self.dashboard_output.as_dict()
        if self.query_output: body['query_output'] = self.query_output.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'SqlOutput':
        return cls(alert_output=_from_dict(d, 'alert_output', SqlAlertOutput),
                   dashboard_output=_from_dict(d, 'dashboard_output', SqlDashboardOutput),
                   query_output=_from_dict(d, 'query_output', SqlQueryOutput))


@dataclass
class SqlOutputError:
    message: Optional[str] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.message: body['message'] = self.message
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'SqlOutputError':
        return cls(message=d.get('message', None))


@dataclass
class SqlQueryOutput:
    output_link: Optional[str] = None
    query_text: Optional[str] = None
    sql_statements: Optional['List[SqlStatementOutput]'] = None
    warehouse_id: Optional[str] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.output_link: body['output_link'] = self.output_link
        if self.query_text: body['query_text'] = self.query_text
        if self.sql_statements: body['sql_statements'] = [v.as_dict() for v in self.sql_statements]
        if self.warehouse_id: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'SqlQueryOutput':
        return cls(output_link=d.get('output_link', None),
                   query_text=d.get('query_text', None),
                   sql_statements=_repeated(d, 'sql_statements', SqlStatementOutput),
                   warehouse_id=d.get('warehouse_id', None))


@dataclass
class SqlStatementOutput:
    lookup_key: Optional[str] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.lookup_key: body['lookup_key'] = self.lookup_key
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'SqlStatementOutput':
        return cls(lookup_key=d.get('lookup_key', None))


@dataclass
class SqlTask:
    warehouse_id: str
    alert: Optional['SqlTaskAlert'] = None
    dashboard: Optional['SqlTaskDashboard'] = None
    parameters: Optional['Dict[str,str]'] = None
    query: Optional['SqlTaskQuery'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.alert: body['alert'] = self.alert.as_dict()
        if self.dashboard: body['dashboard'] = self.dashboard.as_dict()
        if self.parameters: body['parameters'] = self.parameters
        if self.query: body['query'] = self.query.as_dict()
        if self.warehouse_id: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'SqlTask':
        return cls(alert=_from_dict(d, 'alert', SqlTaskAlert),
                   dashboard=_from_dict(d, 'dashboard', SqlTaskDashboard),
                   parameters=d.get('parameters', None),
                   query=_from_dict(d, 'query', SqlTaskQuery),
                   warehouse_id=d.get('warehouse_id', None))


@dataclass
class SqlTaskAlert:
    alert_id: str
    pause_subscriptions: Optional[bool] = None
    subscriptions: Optional['List[SqlTaskSubscription]'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.alert_id: body['alert_id'] = self.alert_id
        if self.pause_subscriptions: body['pause_subscriptions'] = self.pause_subscriptions
        if self.subscriptions: body['subscriptions'] = [v.as_dict() for v in self.subscriptions]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'SqlTaskAlert':
        return cls(alert_id=d.get('alert_id', None),
                   pause_subscriptions=d.get('pause_subscriptions', None),
                   subscriptions=_repeated(d, 'subscriptions', SqlTaskSubscription))


@dataclass
class SqlTaskDashboard:
    dashboard_id: str
    custom_subject: Optional[str] = None
    pause_subscriptions: Optional[bool] = None
    subscriptions: Optional['List[SqlTaskSubscription]'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.custom_subject: body['custom_subject'] = self.custom_subject
        if self.dashboard_id: body['dashboard_id'] = self.dashboard_id
        if self.pause_subscriptions: body['pause_subscriptions'] = self.pause_subscriptions
        if self.subscriptions: body['subscriptions'] = [v.as_dict() for v in self.subscriptions]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'SqlTaskDashboard':
        return cls(custom_subject=d.get('custom_subject', None),
                   dashboard_id=d.get('dashboard_id', None),
                   pause_subscriptions=d.get('pause_subscriptions', None),
                   subscriptions=_repeated(d, 'subscriptions', SqlTaskSubscription))


@dataclass
class SqlTaskQuery:
    query_id: str

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.query_id: body['query_id'] = self.query_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'SqlTaskQuery':
        return cls(query_id=d.get('query_id', None))


@dataclass
class SqlTaskSubscription:
    destination_id: Optional[str] = None
    user_name: Optional[str] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.destination_id: body['destination_id'] = self.destination_id
        if self.user_name: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'SqlTaskSubscription':
        return cls(destination_id=d.get('destination_id', None), user_name=d.get('user_name', None))


@dataclass
class SubmitRun:
    access_control_list: Optional['List[AccessControlRequest]'] = None
    git_source: Optional['GitSource'] = None
    idempotency_token: Optional[str] = None
    run_name: Optional[str] = None
    tasks: Optional['List[RunSubmitTaskSettings]'] = None
    timeout_seconds: Optional[int] = None
    webhook_notifications: Optional['JobWebhookNotifications'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.access_control_list: body['access_control_list'] = [v for v in self.access_control_list]
        if self.git_source: body['git_source'] = self.git_source.as_dict()
        if self.idempotency_token: body['idempotency_token'] = self.idempotency_token
        if self.run_name: body['run_name'] = self.run_name
        if self.tasks: body['tasks'] = [v.as_dict() for v in self.tasks]
        if self.timeout_seconds: body['timeout_seconds'] = self.timeout_seconds
        if self.webhook_notifications: body['webhook_notifications'] = self.webhook_notifications.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'SubmitRun':
        return cls(access_control_list=d.get('access_control_list', None),
                   git_source=_from_dict(d, 'git_source', GitSource),
                   idempotency_token=d.get('idempotency_token', None),
                   run_name=d.get('run_name', None),
                   tasks=_repeated(d, 'tasks', RunSubmitTaskSettings),
                   timeout_seconds=d.get('timeout_seconds', None),
                   webhook_notifications=_from_dict(d, 'webhook_notifications', JobWebhookNotifications))


@dataclass
class SubmitRunResponse:
    run_id: Optional[int] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.run_id: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'SubmitRunResponse':
        return cls(run_id=d.get('run_id', None))


@dataclass
class TaskDependenciesItem:
    task_key: Optional[str] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.task_key: body['task_key'] = self.task_key
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'TaskDependenciesItem':
        return cls(task_key=d.get('task_key', None))


@dataclass
class TriggerEvaluation:
    description: Optional[str] = None
    run_id: Optional[int] = None
    timestamp: Optional[int] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.description: body['description'] = self.description
        if self.run_id: body['run_id'] = self.run_id
        if self.timestamp: body['timestamp'] = self.timestamp
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'TriggerEvaluation':
        return cls(description=d.get('description', None),
                   run_id=d.get('run_id', None),
                   timestamp=d.get('timestamp', None))


@dataclass
class TriggerHistory:
    last_failed: Optional['TriggerEvaluation'] = None
    last_not_triggered: Optional['TriggerEvaluation'] = None
    last_triggered: Optional['TriggerEvaluation'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.last_failed: body['last_failed'] = self.last_failed.as_dict()
        if self.last_not_triggered: body['last_not_triggered'] = self.last_not_triggered.as_dict()
        if self.last_triggered: body['last_triggered'] = self.last_triggered.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'TriggerHistory':
        return cls(last_failed=_from_dict(d, 'last_failed', TriggerEvaluation),
                   last_not_triggered=_from_dict(d, 'last_not_triggered', TriggerEvaluation),
                   last_triggered=_from_dict(d, 'last_triggered', TriggerEvaluation))


@dataclass
class TriggerSettings:
    file_arrival: Optional['FileArrivalTriggerSettings'] = None
    pause_status: Optional['TriggerSettingsPauseStatus'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.file_arrival: body['file_arrival'] = self.file_arrival.as_dict()
        if self.pause_status: body['pause_status'] = self.pause_status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'TriggerSettings':
        return cls(file_arrival=_from_dict(d, 'file_arrival', FileArrivalTriggerSettings),
                   pause_status=_enum(d, 'pause_status', TriggerSettingsPauseStatus))


class TriggerSettingsPauseStatus(Enum):
    """Whether this trigger is paused or not."""

    PAUSED = 'PAUSED'
    UNPAUSED = 'UNPAUSED'


class TriggerType(Enum):
    """This describes an enum"""

    FILE_ARRIVAL = 'FILE_ARRIVAL'
    ONE_TIME = 'ONE_TIME'
    PERIODIC = 'PERIODIC'
    RETRY = 'RETRY'


@dataclass
class UpdateJob:
    job_id: int
    fields_to_remove: Optional['List[str]'] = None
    new_settings: Optional['JobSettings'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.fields_to_remove: body['fields_to_remove'] = [v for v in self.fields_to_remove]
        if self.job_id: body['job_id'] = self.job_id
        if self.new_settings: body['new_settings'] = self.new_settings.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'UpdateJob':
        return cls(fields_to_remove=d.get('fields_to_remove', None),
                   job_id=d.get('job_id', None),
                   new_settings=_from_dict(d, 'new_settings', JobSettings))


@dataclass
class ViewItem:
    content: Optional[str] = None
    name: Optional[str] = None
    type: Optional['ViewType'] = None

    def as_dict(self) -> dict:
        body: Dict[str, Any] = {}
        if self.content: body['content'] = self.content
        if self.name: body['name'] = self.name
        if self.type: body['type'] = self.type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'ViewItem':
        return cls(content=d.get('content', None), name=d.get('name', None), type=_enum(d, 'type', ViewType))


class ViewType(Enum):
    """This describes an enum"""

    DASHBOARD = 'DASHBOARD'
    NOTEBOOK = 'NOTEBOOK'


class ViewsToExport(Enum):
    """This describes an enum"""

    ALL = 'ALL'
    CODE = 'CODE'
    DASHBOARDS = 'DASHBOARDS'


class JobsAPI:
    """The Jobs API allows you to create, edit, and delete jobs.
    
    You can use a Databricks job to run a data processing or data analysis task in a Databricks cluster with
    scalable resources. Your job can consist of a single task or can be a large, multi-task workflow with
    complex dependencies. Databricks manages the task orchestration, cluster management, monitoring, and error
    reporting for all of your jobs. You can run your jobs immediately or periodically through an easy-to-use
    scheduling system. You can implement job tasks using notebooks, JARS, Delta Live Tables pipelines, or
    Python, Scala, Spark submit, and Java applications.
    
    You should never hard code secrets or store them in plain text. Use the :service:secrets to manage secrets
    in the [Databricks CLI]. Use the [Secrets utility] to reference secrets in notebooks and jobs.
    
    [Databricks CLI]: https://docs.databricks.com/dev-tools/cli/index.html
    [Secrets utility]: https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-secrets"""

    def __init__(self, api_client: ApiClient):
        self._api = api_client

    def wait_get_run_job_terminated_or_skipped(self,
                                               run_id: int,
                                               timeout=timedelta(minutes=20),
                                               callback: Optional[Callable[[Run], None]] = None) -> Run:
        deadline = time.time() + timeout.total_seconds()
        target_states = (RunLifeCycleState.TERMINATED, RunLifeCycleState.SKIPPED, )
        failure_states = (RunLifeCycleState.INTERNAL_ERROR, )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.get_run(run_id=run_id)
            status = poll.state.life_cycle_state
            status_message = f'current status: {status}'
            if poll.state is not None:
                status_message = poll.state.state_message
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f'failed to reach TERMINATED or SKIPPED, got {status}: {status_message}'
                raise OperationFailed(msg)
            prefix = f"run_id={run_id}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f'timed out after {timeout}: {status_message}')

    def cancel_all_runs(self, job_id: int, **kwargs: dict):
        """Cancel all runs of a job.
        
        Cancels all active runs of a job. The runs are canceled asynchronously, so it doesn't prevent new runs
        from being started."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CancelAllRuns(job_id=job_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.1/jobs/runs/cancel-all', body=body)

    def cancel_run(self, run_id: int, **kwargs: dict) -> Wait[Run]:
        """Cancel a job run.
        
        Cancels a job run. The run is canceled asynchronously, so it may still be running when this request
        completes."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CancelRun(run_id=run_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.1/jobs/runs/cancel', body=body)
        return Wait(self.wait_get_run_job_terminated_or_skipped, run_id=request.run_id)

    def cancel_run_and_wait(self, run_id: int, timeout=timedelta(minutes=20)) -> Run:
        return self.cancel_run(run_id=run_id).result(timeout=timeout)

    def create(self,
               *,
               access_control_list: Optional[List[AccessControlRequest]] = None,
               continuous: Optional[Continuous] = None,
               email_notifications: Optional[JobEmailNotifications] = None,
               format: Optional[CreateJobFormat] = None,
               git_source: Optional[GitSource] = None,
               job_clusters: Optional[List[JobCluster]] = None,
               max_concurrent_runs: Optional[int] = None,
               name: Optional[str] = None,
               schedule: Optional[CronSchedule] = None,
               tags: Optional[Dict[str, str]] = None,
               tasks: Optional[List[JobTaskSettings]] = None,
               timeout_seconds: Optional[int] = None,
               trigger: Optional[TriggerSettings] = None,
               webhook_notifications: Optional[JobWebhookNotifications] = None,
               **kwargs: dict) -> CreateResponse:
        """Create a new job.
        
        Create a new job."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateJob(access_control_list=access_control_list,
                                continuous=continuous,
                                email_notifications=email_notifications,
                                format=format,
                                git_source=git_source,
                                job_clusters=job_clusters,
                                max_concurrent_runs=max_concurrent_runs,
                                name=name,
                                schedule=schedule,
                                tags=tags,
                                tasks=tasks,
                                timeout_seconds=timeout_seconds,
                                trigger=trigger,
                                webhook_notifications=webhook_notifications)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.1/jobs/create', body=body)
        return CreateResponse.from_dict(json)

    def delete(self, job_id: int, **kwargs: dict):
        """Delete a job.
        
        Deletes a job."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteJob(job_id=job_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.1/jobs/delete', body=body)

    def delete_run(self, run_id: int, **kwargs: dict):
        """Delete a job run.
        
        Deletes a non-active run. Returns an error if the run is active."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteRun(run_id=run_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.1/jobs/runs/delete', body=body)

    def export_run(self,
                   run_id: int,
                   *,
                   views_to_export: Optional[ViewsToExport] = None,
                   **kwargs: dict) -> ExportRunOutput:
        """Export and retrieve a job run.
        
        Export and retrieve the job run task."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ExportRunRequest(run_id=run_id, views_to_export=views_to_export)

        query = {}
        if run_id: query['run_id'] = request.run_id
        if views_to_export: query['views_to_export'] = request.views_to_export.value

        json = self._api.do('GET', '/api/2.1/jobs/runs/export', query=query)
        return ExportRunOutput.from_dict(json)

    def get(self, job_id: int, **kwargs: dict) -> Job:
        """Get a single job.
        
        Retrieves the details for a single job."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetJobRequest(job_id=job_id)

        query = {}
        if job_id: query['job_id'] = request.job_id

        json = self._api.do('GET', '/api/2.1/jobs/get', query=query)
        return Job.from_dict(json)

    def get_run(self, run_id: int, *, include_history: Optional[bool] = None, **kwargs: dict) -> Run:
        """Get a single job run.
        
        Retrieve the metadata of a run."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetRunRequest(include_history=include_history, run_id=run_id)

        query = {}
        if include_history: query['include_history'] = request.include_history
        if run_id: query['run_id'] = request.run_id

        json = self._api.do('GET', '/api/2.1/jobs/runs/get', query=query)
        return Run.from_dict(json)

    def get_run_output(self, run_id: int, **kwargs: dict) -> RunOutput:
        """Get the output for a single run.
        
        Retrieve the output and metadata of a single task run. When a notebook task returns a value through
        the `dbutils.notebook.exit()` call, you can use this endpoint to retrieve that value. Databricks
        restricts this API to returning the first 5 MB of the output. To return a larger result, you can store
        job results in a cloud storage service.
        
        This endpoint validates that the __run_id__ parameter is valid and returns an HTTP status code 400 if
        the __run_id__ parameter is invalid. Runs are automatically removed after 60 days. If you to want to
        reference them beyond 60 days, you must save old run results before they expire."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetRunOutputRequest(run_id=run_id)

        query = {}
        if run_id: query['run_id'] = request.run_id

        json = self._api.do('GET', '/api/2.1/jobs/runs/get-output', query=query)
        return RunOutput.from_dict(json)

    def list(self,
             *,
             expand_tasks: Optional[bool] = None,
             limit: Optional[int] = None,
             name: Optional[str] = None,
             offset: Optional[int] = None,
             **kwargs: dict) -> Iterator[BaseJob]:
        """List all jobs.
        
        Retrieves a list of jobs."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListJobsRequest(expand_tasks=expand_tasks, limit=limit, name=name, offset=offset)

        query = {}
        if expand_tasks: query['expand_tasks'] = request.expand_tasks
        if limit: query['limit'] = request.limit
        if name: query['name'] = request.name
        if offset: query['offset'] = request.offset

        # deduplicate items that may have been added during iteration
        seen = set()
        query['offset'] = 0
        while True:
            json = self._api.do('GET', '/api/2.1/jobs/list', query=query)
            if 'jobs' not in json or not json['jobs']:
                return
            for v in json['jobs']:
                i = v['job_id']
                if i in seen:
                    continue
                seen.add(i)
                yield BaseJob.from_dict(v)
            query['offset'] += len(json['jobs'])

    def list_runs(self,
                  *,
                  active_only: Optional[bool] = None,
                  completed_only: Optional[bool] = None,
                  expand_tasks: Optional[bool] = None,
                  job_id: Optional[int] = None,
                  limit: Optional[int] = None,
                  offset: Optional[int] = None,
                  run_type: Optional[ListRunsRunType] = None,
                  start_time_from: Optional[int] = None,
                  start_time_to: Optional[int] = None,
                  **kwargs: dict) -> Iterator[BaseRun]:
        """List runs for a job.
        
        List runs in descending order by start time."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListRunsRequest(active_only=active_only,
                                      completed_only=completed_only,
                                      expand_tasks=expand_tasks,
                                      job_id=job_id,
                                      limit=limit,
                                      offset=offset,
                                      run_type=run_type,
                                      start_time_from=start_time_from,
                                      start_time_to=start_time_to)

        query = {}
        if active_only: query['active_only'] = request.active_only
        if completed_only: query['completed_only'] = request.completed_only
        if expand_tasks: query['expand_tasks'] = request.expand_tasks
        if job_id: query['job_id'] = request.job_id
        if limit: query['limit'] = request.limit
        if offset: query['offset'] = request.offset
        if run_type: query['run_type'] = request.run_type.value
        if start_time_from: query['start_time_from'] = request.start_time_from
        if start_time_to: query['start_time_to'] = request.start_time_to

        # deduplicate items that may have been added during iteration
        seen = set()
        query['offset'] = 0
        while True:
            json = self._api.do('GET', '/api/2.1/jobs/runs/list', query=query)
            if 'runs' not in json or not json['runs']:
                return
            for v in json['runs']:
                i = v['run_id']
                if i in seen:
                    continue
                seen.add(i)
                yield BaseRun.from_dict(v)
            query['offset'] += len(json['runs'])

    def repair_run(self,
                   run_id: int,
                   *,
                   dbt_commands: Optional[List[str]] = None,
                   jar_params: Optional[List[str]] = None,
                   latest_repair_id: Optional[int] = None,
                   notebook_params: Optional[Dict[str, str]] = None,
                   pipeline_params: Optional[PipelineParams] = None,
                   python_named_params: Optional[Dict[str, str]] = None,
                   python_params: Optional[List[str]] = None,
                   rerun_all_failed_tasks: Optional[bool] = None,
                   rerun_tasks: Optional[List[str]] = None,
                   spark_submit_params: Optional[List[str]] = None,
                   sql_params: Optional[Dict[str, str]] = None,
                   **kwargs: dict) -> Wait[Run]:
        """Repair a job run.
        
        Re-run one or more tasks. Tasks are re-run as part of the original job run. They use the current job
        and task settings, and can be viewed in the history for the original job run."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = RepairRun(dbt_commands=dbt_commands,
                                jar_params=jar_params,
                                latest_repair_id=latest_repair_id,
                                notebook_params=notebook_params,
                                pipeline_params=pipeline_params,
                                python_named_params=python_named_params,
                                python_params=python_params,
                                rerun_all_failed_tasks=rerun_all_failed_tasks,
                                rerun_tasks=rerun_tasks,
                                run_id=run_id,
                                spark_submit_params=spark_submit_params,
                                sql_params=sql_params)
        body = request.as_dict()
        op_response = self._api.do('POST', '/api/2.1/jobs/runs/repair', body=body)
        return Wait(self.wait_get_run_job_terminated_or_skipped,
                    response=RepairRunResponse.from_dict(op_response),
                    run_id=request.run_id)

    def repair_run_and_wait(
        self,
        run_id: int,
        *,
        dbt_commands: Optional[List[str]] = None,
        jar_params: Optional[List[str]] = None,
        latest_repair_id: Optional[int] = None,
        notebook_params: Optional[Dict[str, str]] = None,
        pipeline_params: Optional[PipelineParams] = None,
        python_named_params: Optional[Dict[str, str]] = None,
        python_params: Optional[List[str]] = None,
        rerun_all_failed_tasks: Optional[bool] = None,
        rerun_tasks: Optional[List[str]] = None,
        spark_submit_params: Optional[List[str]] = None,
        sql_params: Optional[Dict[str, str]] = None,
        timeout=timedelta(minutes=20)) -> Run:
        return self.repair_run(dbt_commands=dbt_commands,
                               jar_params=jar_params,
                               latest_repair_id=latest_repair_id,
                               notebook_params=notebook_params,
                               pipeline_params=pipeline_params,
                               python_named_params=python_named_params,
                               python_params=python_params,
                               rerun_all_failed_tasks=rerun_all_failed_tasks,
                               rerun_tasks=rerun_tasks,
                               run_id=run_id,
                               spark_submit_params=spark_submit_params,
                               sql_params=sql_params).result(timeout=timeout)

    def reset(self, job_id: int, new_settings: JobSettings, **kwargs: dict):
        """Overwrites all settings for a job.
        
        Overwrites all the settings for a specific job. Use the Update endpoint to update job settings
        partially."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ResetJob(job_id=job_id, new_settings=new_settings)
        body = request.as_dict()
        self._api.do('POST', '/api/2.1/jobs/reset', body=body)

    def run_now(self,
                job_id: int,
                *,
                dbt_commands: Optional[List[str]] = None,
                idempotency_token: Optional[str] = None,
                jar_params: Optional[List[str]] = None,
                notebook_params: Optional[Dict[str, str]] = None,
                pipeline_params: Optional[PipelineParams] = None,
                python_named_params: Optional[Dict[str, str]] = None,
                python_params: Optional[List[str]] = None,
                spark_submit_params: Optional[List[str]] = None,
                sql_params: Optional[Dict[str, str]] = None,
                **kwargs: dict) -> Wait[Run]:
        """Trigger a new job run.
        
        Run a job and return the `run_id` of the triggered run."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = RunNow(dbt_commands=dbt_commands,
                             idempotency_token=idempotency_token,
                             jar_params=jar_params,
                             job_id=job_id,
                             notebook_params=notebook_params,
                             pipeline_params=pipeline_params,
                             python_named_params=python_named_params,
                             python_params=python_params,
                             spark_submit_params=spark_submit_params,
                             sql_params=sql_params)
        body = request.as_dict()
        op_response = self._api.do('POST', '/api/2.1/jobs/run-now', body=body)
        return Wait(self.wait_get_run_job_terminated_or_skipped,
                    response=RunNowResponse.from_dict(op_response),
                    run_id=op_response['run_id'])

    def run_now_and_wait(self,
                         job_id: int,
                         *,
                         dbt_commands: Optional[List[str]] = None,
                         idempotency_token: Optional[str] = None,
                         jar_params: Optional[List[str]] = None,
                         notebook_params: Optional[Dict[str, str]] = None,
                         pipeline_params: Optional[PipelineParams] = None,
                         python_named_params: Optional[Dict[str, str]] = None,
                         python_params: Optional[List[str]] = None,
                         spark_submit_params: Optional[List[str]] = None,
                         sql_params: Optional[Dict[str, str]] = None,
                         timeout=timedelta(minutes=20)) -> Run:
        return self.run_now(dbt_commands=dbt_commands,
                            idempotency_token=idempotency_token,
                            jar_params=jar_params,
                            job_id=job_id,
                            notebook_params=notebook_params,
                            pipeline_params=pipeline_params,
                            python_named_params=python_named_params,
                            python_params=python_params,
                            spark_submit_params=spark_submit_params,
                            sql_params=sql_params).result(timeout=timeout)

    def submit(self,
               *,
               access_control_list: Optional[List[AccessControlRequest]] = None,
               git_source: Optional[GitSource] = None,
               idempotency_token: Optional[str] = None,
               run_name: Optional[str] = None,
               tasks: Optional[List[RunSubmitTaskSettings]] = None,
               timeout_seconds: Optional[int] = None,
               webhook_notifications: Optional[JobWebhookNotifications] = None,
               **kwargs: dict) -> Wait[Run]:
        """Create and trigger a one-time run.
        
        Submit a one-time run. This endpoint allows you to submit a workload directly without creating a job.
        Runs submitted using this endpoint don’t display in the UI. Use the `jobs/runs/get` API to check the
        run state after the job is submitted."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SubmitRun(access_control_list=access_control_list,
                                git_source=git_source,
                                idempotency_token=idempotency_token,
                                run_name=run_name,
                                tasks=tasks,
                                timeout_seconds=timeout_seconds,
                                webhook_notifications=webhook_notifications)
        body = request.as_dict()
        op_response = self._api.do('POST', '/api/2.1/jobs/runs/submit', body=body)
        return Wait(self.wait_get_run_job_terminated_or_skipped,
                    response=SubmitRunResponse.from_dict(op_response),
                    run_id=op_response['run_id'])

    def submit_and_wait(
        self,
        *,
        access_control_list: Optional[List[AccessControlRequest]] = None,
        git_source: Optional[GitSource] = None,
        idempotency_token: Optional[str] = None,
        run_name: Optional[str] = None,
        tasks: Optional[List[RunSubmitTaskSettings]] = None,
        timeout_seconds: Optional[int] = None,
        webhook_notifications: Optional[JobWebhookNotifications] = None,
        timeout=timedelta(minutes=20)) -> Run:
        return self.submit(access_control_list=access_control_list,
                           git_source=git_source,
                           idempotency_token=idempotency_token,
                           run_name=run_name,
                           tasks=tasks,
                           timeout_seconds=timeout_seconds,
                           webhook_notifications=webhook_notifications).result(timeout=timeout)

    def update(self,
               job_id: int,
               *,
               fields_to_remove: Optional[List[str]] = None,
               new_settings: Optional[JobSettings] = None,
               **kwargs: dict):
        """Partially updates a job.
        
        Add, update, or remove specific settings of an existing job. Use the ResetJob to overwrite all job
        settings."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateJob(fields_to_remove=fields_to_remove, job_id=job_id, new_settings=new_settings)
        body = request.as_dict()
        self._api.do('POST', '/api/2.1/jobs/update', body=body)

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

from .clusters import BaseClusterInfo
from .libraries import Library
from .permissions import AccessControlRequest

# all definitions in this file are in alphabetical order


@dataclass
class BaseJob:
    created_time: int = None
    creator_user_name: str = None
    job_id: int = None
    settings: 'JobSettings' = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_time: body['created_time'] = self.created_time
        if self.creator_user_name: body['creator_user_name'] = self.creator_user_name
        if self.job_id: body['job_id'] = self.job_id
        if self.settings: body['settings'] = self.settings.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'BaseJob':
        return cls(created_time=d.get('created_time', None),
                   creator_user_name=d.get('creator_user_name', None),
                   job_id=d.get('job_id', None),
                   settings=_from_dict(d, 'settings', JobSettings))


@dataclass
class BaseRun:
    attempt_number: int = None
    cleanup_duration: int = None
    cluster_instance: 'ClusterInstance' = None
    cluster_spec: 'ClusterSpec' = None
    continuous: 'Continuous' = None
    creator_user_name: str = None
    end_time: int = None
    execution_duration: int = None
    git_source: 'GitSource' = None
    job_clusters: 'List[JobCluster]' = None
    job_id: int = None
    number_in_job: int = None
    original_attempt_run_id: int = None
    overriding_parameters: 'RunParameters' = None
    run_duration: int = None
    run_id: int = None
    run_name: str = None
    run_page_url: str = None
    run_type: 'RunType' = None
    schedule: 'CronSchedule' = None
    setup_duration: int = None
    start_time: int = None
    state: 'RunState' = None
    tasks: 'List[RunTask]' = None
    trigger: 'TriggerType' = None

    def as_dict(self) -> dict:
        body = {}
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
    def from_dict(cls, d: Dict[str, any]) -> 'BaseRun':
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
        body = {}
        if self.job_id: body['job_id'] = self.job_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CancelAllRuns':
        return cls(job_id=d.get('job_id', None))


@dataclass
class CancelRun:
    run_id: int

    def as_dict(self) -> dict:
        body = {}
        if self.run_id: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CancelRun':
        return cls(run_id=d.get('run_id', None))


@dataclass
class ClusterInstance:
    cluster_id: str = None
    spark_context_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.spark_context_id: body['spark_context_id'] = self.spark_context_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterInstance':
        return cls(cluster_id=d.get('cluster_id', None), spark_context_id=d.get('spark_context_id', None))


@dataclass
class ClusterSpec:
    existing_cluster_id: str = None
    libraries: 'List[Library]' = None
    new_cluster: 'BaseClusterInfo' = None

    def as_dict(self) -> dict:
        body = {}
        if self.existing_cluster_id: body['existing_cluster_id'] = self.existing_cluster_id
        if self.libraries: body['libraries'] = [v for v in self.libraries]
        if self.new_cluster: body['new_cluster'] = self.new_cluster
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterSpec':
        return cls(existing_cluster_id=d.get('existing_cluster_id', None),
                   libraries=d.get('libraries', None),
                   new_cluster=_from_dict(d, 'new_cluster', BaseClusterInfo))


@dataclass
class Continuous:
    pause_status: 'ContinuousPauseStatus' = None

    def as_dict(self) -> dict:
        body = {}
        if self.pause_status: body['pause_status'] = self.pause_status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Continuous':
        return cls(pause_status=_enum(d, 'pause_status', ContinuousPauseStatus))


class ContinuousPauseStatus(Enum):
    """Indicate whether the continuous execution of the job is paused or not. Defaults to UNPAUSED."""

    PAUSED = 'PAUSED'
    UNPAUSED = 'UNPAUSED'


@dataclass
class CreateJob:
    access_control_list: 'List[AccessControlRequest]' = None
    continuous: 'Continuous' = None
    email_notifications: 'JobEmailNotifications' = None
    format: 'CreateJobFormat' = None
    git_source: 'GitSource' = None
    job_clusters: 'List[JobCluster]' = None
    max_concurrent_runs: int = None
    name: str = None
    schedule: 'CronSchedule' = None
    tags: 'Dict[str,str]' = None
    tasks: 'List[JobTaskSettings]' = None
    timeout_seconds: int = None
    trigger: 'TriggerSettings' = None
    webhook_notifications: 'JobWebhookNotifications' = None

    def as_dict(self) -> dict:
        body = {}
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
    def from_dict(cls, d: Dict[str, any]) -> 'CreateJob':
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
    job_id: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.job_id: body['job_id'] = self.job_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateResponse':
        return cls(job_id=d.get('job_id', None))


@dataclass
class CronSchedule:
    quartz_cron_expression: str
    timezone_id: str
    pause_status: 'CronSchedulePauseStatus' = None

    def as_dict(self) -> dict:
        body = {}
        if self.pause_status: body['pause_status'] = self.pause_status.value
        if self.quartz_cron_expression: body['quartz_cron_expression'] = self.quartz_cron_expression
        if self.timezone_id: body['timezone_id'] = self.timezone_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CronSchedule':
        return cls(pause_status=_enum(d, 'pause_status', CronSchedulePauseStatus),
                   quartz_cron_expression=d.get('quartz_cron_expression', None),
                   timezone_id=d.get('timezone_id', None))


class CronSchedulePauseStatus(Enum):
    """Indicate whether this schedule is paused or not."""

    PAUSED = 'PAUSED'
    UNPAUSED = 'UNPAUSED'


@dataclass
class DbtOutput:
    artifacts_headers: 'Dict[str,str]' = None
    artifacts_link: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.artifacts_headers: body['artifacts_headers'] = self.artifacts_headers
        if self.artifacts_link: body['artifacts_link'] = self.artifacts_link
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DbtOutput':
        return cls(artifacts_headers=d.get('artifacts_headers', None),
                   artifacts_link=d.get('artifacts_link', None))


@dataclass
class DbtTask:
    commands: 'List[str]'
    catalog: str = None
    profiles_directory: str = None
    project_directory: str = None
    schema: str = None
    warehouse_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.catalog: body['catalog'] = self.catalog
        if self.commands: body['commands'] = [v for v in self.commands]
        if self.profiles_directory: body['profiles_directory'] = self.profiles_directory
        if self.project_directory: body['project_directory'] = self.project_directory
        if self.schema: body['schema'] = self.schema
        if self.warehouse_id: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DbtTask':
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
        body = {}
        if self.job_id: body['job_id'] = self.job_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteJob':
        return cls(job_id=d.get('job_id', None))


@dataclass
class DeleteRun:
    run_id: int

    def as_dict(self) -> dict:
        body = {}
        if self.run_id: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteRun':
        return cls(run_id=d.get('run_id', None))


@dataclass
class ExportRun:
    """Export and retrieve a job run"""

    run_id: int
    views_to_export: 'ViewsToExport' = None


@dataclass
class ExportRunOutput:
    views: 'List[ViewItem]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.views: body['views'] = [v.as_dict() for v in self.views]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ExportRunOutput':
        return cls(views=_repeated(d, 'views', ViewItem))


@dataclass
class FileArrivalTriggerSettings:
    min_time_between_trigger_seconds: int = None
    url: str = None
    wait_after_last_change_seconds: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.min_time_between_trigger_seconds:
            body['min_time_between_trigger_seconds'] = self.min_time_between_trigger_seconds
        if self.url: body['url'] = self.url
        if self.wait_after_last_change_seconds:
            body['wait_after_last_change_seconds'] = self.wait_after_last_change_seconds
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FileArrivalTriggerSettings':
        return cls(min_time_between_trigger_seconds=d.get('min_time_between_trigger_seconds', None),
                   url=d.get('url', None),
                   wait_after_last_change_seconds=d.get('wait_after_last_change_seconds', None))


@dataclass
class Get:
    """Get a single job"""

    job_id: int


@dataclass
class GetRun:
    """Get a single job run"""

    run_id: int
    include_history: bool = None


@dataclass
class GetRunOutput:
    """Get the output for a single run"""

    run_id: int


@dataclass
class GitSnapshot:
    """Read-only state of the remote repository at the time the job was run. This field is only
    included on job runs."""

    used_commit: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.used_commit: body['used_commit'] = self.used_commit
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GitSnapshot':
        return cls(used_commit=d.get('used_commit', None))


@dataclass
class GitSource:
    """An optional specification for a remote repository containing the notebooks used by this job's
    notebook tasks."""

    git_url: str
    git_provider: 'GitSourceGitProvider'
    git_branch: str = None
    git_commit: str = None
    git_snapshot: 'GitSnapshot' = None
    git_tag: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.git_branch: body['git_branch'] = self.git_branch
        if self.git_commit: body['git_commit'] = self.git_commit
        if self.git_provider: body['git_provider'] = self.git_provider.value
        if self.git_snapshot: body['git_snapshot'] = self.git_snapshot.as_dict()
        if self.git_tag: body['git_tag'] = self.git_tag
        if self.git_url: body['git_url'] = self.git_url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GitSource':
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
    created_time: int = None
    creator_user_name: str = None
    job_id: int = None
    run_as_user_name: str = None
    settings: 'JobSettings' = None
    trigger_history: 'TriggerHistory' = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_time: body['created_time'] = self.created_time
        if self.creator_user_name: body['creator_user_name'] = self.creator_user_name
        if self.job_id: body['job_id'] = self.job_id
        if self.run_as_user_name: body['run_as_user_name'] = self.run_as_user_name
        if self.settings: body['settings'] = self.settings.as_dict()
        if self.trigger_history: body['trigger_history'] = self.trigger_history.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Job':
        return cls(created_time=d.get('created_time', None),
                   creator_user_name=d.get('creator_user_name', None),
                   job_id=d.get('job_id', None),
                   run_as_user_name=d.get('run_as_user_name', None),
                   settings=_from_dict(d, 'settings', JobSettings),
                   trigger_history=_from_dict(d, 'trigger_history', TriggerHistory))


@dataclass
class JobCluster:
    job_cluster_key: str
    new_cluster: 'BaseClusterInfo' = None

    def as_dict(self) -> dict:
        body = {}
        if self.job_cluster_key: body['job_cluster_key'] = self.job_cluster_key
        if self.new_cluster: body['new_cluster'] = self.new_cluster
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobCluster':
        return cls(job_cluster_key=d.get('job_cluster_key', None),
                   new_cluster=_from_dict(d, 'new_cluster', BaseClusterInfo))


@dataclass
class JobEmailNotifications:
    no_alert_for_skipped_runs: bool = None
    on_failure: 'List[str]' = None
    on_start: 'List[str]' = None
    on_success: 'List[str]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.no_alert_for_skipped_runs: body['no_alert_for_skipped_runs'] = self.no_alert_for_skipped_runs
        if self.on_failure: body['on_failure'] = [v for v in self.on_failure]
        if self.on_start: body['on_start'] = [v for v in self.on_start]
        if self.on_success: body['on_success'] = [v for v in self.on_success]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobEmailNotifications':
        return cls(no_alert_for_skipped_runs=d.get('no_alert_for_skipped_runs', None),
                   on_failure=d.get('on_failure', None),
                   on_start=d.get('on_start', None),
                   on_success=d.get('on_success', None))


@dataclass
class JobSettings:
    continuous: 'Continuous' = None
    email_notifications: 'JobEmailNotifications' = None
    format: 'JobSettingsFormat' = None
    git_source: 'GitSource' = None
    job_clusters: 'List[JobCluster]' = None
    max_concurrent_runs: int = None
    name: str = None
    schedule: 'CronSchedule' = None
    tags: 'Dict[str,str]' = None
    tasks: 'List[JobTaskSettings]' = None
    timeout_seconds: int = None
    trigger: 'TriggerSettings' = None
    webhook_notifications: 'JobWebhookNotifications' = None

    def as_dict(self) -> dict:
        body = {}
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
    def from_dict(cls, d: Dict[str, any]) -> 'JobSettings':
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
    dbt_task: 'DbtTask' = None
    depends_on: 'List[TaskDependenciesItem]' = None
    description: str = None
    email_notifications: 'JobEmailNotifications' = None
    existing_cluster_id: str = None
    job_cluster_key: str = None
    libraries: 'List[Library]' = None
    max_retries: int = None
    min_retry_interval_millis: int = None
    new_cluster: 'BaseClusterInfo' = None
    notebook_task: 'NotebookTask' = None
    pipeline_task: 'PipelineTask' = None
    python_wheel_task: 'PythonWheelTask' = None
    retry_on_timeout: bool = None
    spark_jar_task: 'SparkJarTask' = None
    spark_python_task: 'SparkPythonTask' = None
    spark_submit_task: 'SparkSubmitTask' = None
    sql_task: 'SqlTask' = None
    timeout_seconds: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.dbt_task: body['dbt_task'] = self.dbt_task.as_dict()
        if self.depends_on: body['depends_on'] = [v.as_dict() for v in self.depends_on]
        if self.description: body['description'] = self.description
        if self.email_notifications: body['email_notifications'] = self.email_notifications.as_dict()
        if self.existing_cluster_id: body['existing_cluster_id'] = self.existing_cluster_id
        if self.job_cluster_key: body['job_cluster_key'] = self.job_cluster_key
        if self.libraries: body['libraries'] = [v for v in self.libraries]
        if self.max_retries: body['max_retries'] = self.max_retries
        if self.min_retry_interval_millis: body['min_retry_interval_millis'] = self.min_retry_interval_millis
        if self.new_cluster: body['new_cluster'] = self.new_cluster
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
    def from_dict(cls, d: Dict[str, any]) -> 'JobTaskSettings':
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
    on_failure: 'List[JobWebhookNotificationsOnFailureItem]' = None
    on_start: 'List[JobWebhookNotificationsOnStartItem]' = None
    on_success: 'List[JobWebhookNotificationsOnSuccessItem]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.on_failure: body['on_failure'] = [v.as_dict() for v in self.on_failure]
        if self.on_start: body['on_start'] = [v.as_dict() for v in self.on_start]
        if self.on_success: body['on_success'] = [v.as_dict() for v in self.on_success]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobWebhookNotifications':
        return cls(on_failure=_repeated(d, 'on_failure', JobWebhookNotificationsOnFailureItem),
                   on_start=_repeated(d, 'on_start', JobWebhookNotificationsOnStartItem),
                   on_success=_repeated(d, 'on_success', JobWebhookNotificationsOnSuccessItem))


@dataclass
class JobWebhookNotificationsOnFailureItem:
    id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.id: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobWebhookNotificationsOnFailureItem':
        return cls(id=d.get('id', None))


@dataclass
class JobWebhookNotificationsOnStartItem:
    id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.id: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobWebhookNotificationsOnStartItem':
        return cls(id=d.get('id', None))


@dataclass
class JobWebhookNotificationsOnSuccessItem:
    id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.id: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobWebhookNotificationsOnSuccessItem':
        return cls(id=d.get('id', None))


@dataclass
class ListRequest:
    """List all jobs"""

    expand_tasks: bool = None
    limit: int = None
    name: str = None
    offset: int = None


@dataclass
class ListJobsResponse:
    has_more: bool = None
    jobs: 'List[BaseJob]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.has_more: body['has_more'] = self.has_more
        if self.jobs: body['jobs'] = [v.as_dict() for v in self.jobs]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListJobsResponse':
        return cls(has_more=d.get('has_more', None), jobs=_repeated(d, 'jobs', BaseJob))


@dataclass
class ListRuns:
    """List runs for a job"""

    active_only: bool = None
    completed_only: bool = None
    expand_tasks: bool = None
    job_id: int = None
    limit: int = None
    offset: int = None
    run_type: 'ListRunsRunType' = None
    start_time_from: int = None
    start_time_to: int = None


@dataclass
class ListRunsResponse:
    has_more: bool = None
    runs: 'List[BaseRun]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.has_more: body['has_more'] = self.has_more
        if self.runs: body['runs'] = [v.as_dict() for v in self.runs]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListRunsResponse':
        return cls(has_more=d.get('has_more', None), runs=_repeated(d, 'runs', BaseRun))


class ListRunsRunType(Enum):
    """This describes an enum"""

    JOB_RUN = 'JOB_RUN'
    SUBMIT_RUN = 'SUBMIT_RUN'
    WORKFLOW_RUN = 'WORKFLOW_RUN'


@dataclass
class NotebookOutput:
    result: str = None
    truncated: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.result: body['result'] = self.result
        if self.truncated: body['truncated'] = self.truncated
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NotebookOutput':
        return cls(result=d.get('result', None), truncated=d.get('truncated', None))


@dataclass
class NotebookTask:
    notebook_path: str
    base_parameters: 'Dict[str,str]' = None
    source: 'NotebookTaskSource' = None

    def as_dict(self) -> dict:
        body = {}
        if self.base_parameters: body['base_parameters'] = self.base_parameters
        if self.notebook_path: body['notebook_path'] = self.notebook_path
        if self.source: body['source'] = self.source.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NotebookTask':
        return cls(base_parameters=d.get('base_parameters', None),
                   notebook_path=d.get('notebook_path', None),
                   source=_enum(d, 'source', NotebookTaskSource))


class NotebookTaskSource(Enum):
    """This describes an enum"""

    GIT = 'GIT'
    WORKSPACE = 'WORKSPACE'


@dataclass
class PipelineParams:
    full_refresh: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.full_refresh: body['full_refresh'] = self.full_refresh
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineParams':
        return cls(full_refresh=d.get('full_refresh', None))


@dataclass
class PipelineTask:
    full_refresh: bool = None
    pipeline_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.full_refresh: body['full_refresh'] = self.full_refresh
        if self.pipeline_id: body['pipeline_id'] = self.pipeline_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineTask':
        return cls(full_refresh=d.get('full_refresh', None), pipeline_id=d.get('pipeline_id', None))


@dataclass
class PythonWheelTask:
    entry_point: str = None
    named_parameters: 'Dict[str,str]' = None
    package_name: str = None
    parameters: 'List[str]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.entry_point: body['entry_point'] = self.entry_point
        if self.named_parameters: body['named_parameters'] = self.named_parameters
        if self.package_name: body['package_name'] = self.package_name
        if self.parameters: body['parameters'] = [v for v in self.parameters]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PythonWheelTask':
        return cls(entry_point=d.get('entry_point', None),
                   named_parameters=d.get('named_parameters', None),
                   package_name=d.get('package_name', None),
                   parameters=d.get('parameters', None))


@dataclass
class RepairHistoryItem:
    end_time: int = None
    id: int = None
    start_time: int = None
    state: 'RunState' = None
    task_run_ids: 'List[int]' = None
    type: 'RepairHistoryItemType' = None

    def as_dict(self) -> dict:
        body = {}
        if self.end_time: body['end_time'] = self.end_time
        if self.id: body['id'] = self.id
        if self.start_time: body['start_time'] = self.start_time
        if self.state: body['state'] = self.state.as_dict()
        if self.task_run_ids: body['task_run_ids'] = [v for v in self.task_run_ids]
        if self.type: body['type'] = self.type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RepairHistoryItem':
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
    dbt_commands: 'List[str]' = None
    jar_params: 'List[str]' = None
    latest_repair_id: int = None
    notebook_params: 'Dict[str,str]' = None
    pipeline_params: 'PipelineParams' = None
    python_named_params: 'Dict[str,str]' = None
    python_params: 'List[str]' = None
    rerun_all_failed_tasks: bool = None
    rerun_tasks: 'List[str]' = None
    spark_submit_params: 'List[str]' = None
    sql_params: 'Dict[str,str]' = None

    def as_dict(self) -> dict:
        body = {}
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
    def from_dict(cls, d: Dict[str, any]) -> 'RepairRun':
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
    repair_id: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.repair_id: body['repair_id'] = self.repair_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RepairRunResponse':
        return cls(repair_id=d.get('repair_id', None))


@dataclass
class ResetJob:
    job_id: int
    new_settings: 'JobSettings'

    def as_dict(self) -> dict:
        body = {}
        if self.job_id: body['job_id'] = self.job_id
        if self.new_settings: body['new_settings'] = self.new_settings.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResetJob':
        return cls(job_id=d.get('job_id', None), new_settings=_from_dict(d, 'new_settings', JobSettings))


@dataclass
class Run:
    attempt_number: int = None
    cleanup_duration: int = None
    cluster_instance: 'ClusterInstance' = None
    cluster_spec: 'ClusterSpec' = None
    continuous: 'Continuous' = None
    creator_user_name: str = None
    end_time: int = None
    execution_duration: int = None
    git_source: 'GitSource' = None
    job_clusters: 'List[JobCluster]' = None
    job_id: int = None
    number_in_job: int = None
    original_attempt_run_id: int = None
    overriding_parameters: 'RunParameters' = None
    repair_history: 'List[RepairHistoryItem]' = None
    run_duration: int = None
    run_id: int = None
    run_name: str = None
    run_page_url: str = None
    run_type: 'RunType' = None
    schedule: 'CronSchedule' = None
    setup_duration: int = None
    start_time: int = None
    state: 'RunState' = None
    tasks: 'List[RunTask]' = None
    trigger: 'TriggerType' = None

    def as_dict(self) -> dict:
        body = {}
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
    def from_dict(cls, d: Dict[str, any]) -> 'Run':
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
    dbt_commands: 'List[str]' = None
    idempotency_token: str = None
    jar_params: 'List[str]' = None
    notebook_params: 'Dict[str,str]' = None
    pipeline_params: 'PipelineParams' = None
    python_named_params: 'Dict[str,str]' = None
    python_params: 'List[str]' = None
    spark_submit_params: 'List[str]' = None
    sql_params: 'Dict[str,str]' = None

    def as_dict(self) -> dict:
        body = {}
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
    def from_dict(cls, d: Dict[str, any]) -> 'RunNow':
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
    number_in_job: int = None
    run_id: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.number_in_job: body['number_in_job'] = self.number_in_job
        if self.run_id: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunNowResponse':
        return cls(number_in_job=d.get('number_in_job', None), run_id=d.get('run_id', None))


@dataclass
class RunOutput:
    dbt_output: 'DbtOutput' = None
    error: str = None
    error_trace: str = None
    logs: str = None
    logs_truncated: bool = None
    metadata: 'Run' = None
    notebook_output: 'NotebookOutput' = None
    sql_output: 'SqlOutput' = None

    def as_dict(self) -> dict:
        body = {}
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
    def from_dict(cls, d: Dict[str, any]) -> 'RunOutput':
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
    dbt_commands: 'List[str]' = None
    jar_params: 'List[str]' = None
    notebook_params: 'Dict[str,str]' = None
    pipeline_params: 'PipelineParams' = None
    python_named_params: 'Dict[str,str]' = None
    python_params: 'List[str]' = None
    spark_submit_params: 'List[str]' = None
    sql_params: 'Dict[str,str]' = None

    def as_dict(self) -> dict:
        body = {}
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
    def from_dict(cls, d: Dict[str, any]) -> 'RunParameters':
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

    life_cycle_state: 'RunLifeCycleState' = None
    result_state: 'RunResultState' = None
    state_message: str = None
    user_cancelled_or_timedout: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.life_cycle_state: body['life_cycle_state'] = self.life_cycle_state.value
        if self.result_state: body['result_state'] = self.result_state.value
        if self.state_message: body['state_message'] = self.state_message
        if self.user_cancelled_or_timedout:
            body['user_cancelled_or_timedout'] = self.user_cancelled_or_timedout
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunState':
        return cls(life_cycle_state=_enum(d, 'life_cycle_state', RunLifeCycleState),
                   result_state=_enum(d, 'result_state', RunResultState),
                   state_message=d.get('state_message', None),
                   user_cancelled_or_timedout=d.get('user_cancelled_or_timedout', None))


@dataclass
class RunSubmitTaskSettings:
    task_key: str
    depends_on: 'List[TaskDependenciesItem]' = None
    existing_cluster_id: str = None
    libraries: 'List[Library]' = None
    new_cluster: 'BaseClusterInfo' = None
    notebook_task: 'NotebookTask' = None
    pipeline_task: 'PipelineTask' = None
    python_wheel_task: 'PythonWheelTask' = None
    spark_jar_task: 'SparkJarTask' = None
    spark_python_task: 'SparkPythonTask' = None
    spark_submit_task: 'SparkSubmitTask' = None
    timeout_seconds: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.depends_on: body['depends_on'] = [v.as_dict() for v in self.depends_on]
        if self.existing_cluster_id: body['existing_cluster_id'] = self.existing_cluster_id
        if self.libraries: body['libraries'] = [v for v in self.libraries]
        if self.new_cluster: body['new_cluster'] = self.new_cluster
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
    def from_dict(cls, d: Dict[str, any]) -> 'RunSubmitTaskSettings':
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
    attempt_number: int = None
    cleanup_duration: int = None
    cluster_instance: 'ClusterInstance' = None
    dbt_task: 'DbtTask' = None
    depends_on: 'List[TaskDependenciesItem]' = None
    description: str = None
    end_time: int = None
    execution_duration: int = None
    existing_cluster_id: str = None
    git_source: 'GitSource' = None
    libraries: 'List[Library]' = None
    new_cluster: 'BaseClusterInfo' = None
    notebook_task: 'NotebookTask' = None
    pipeline_task: 'PipelineTask' = None
    python_wheel_task: 'PythonWheelTask' = None
    run_id: int = None
    setup_duration: int = None
    spark_jar_task: 'SparkJarTask' = None
    spark_python_task: 'SparkPythonTask' = None
    spark_submit_task: 'SparkSubmitTask' = None
    sql_task: 'SqlTask' = None
    start_time: int = None
    state: 'RunState' = None
    task_key: str = None

    def as_dict(self) -> dict:
        body = {}
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
        if self.new_cluster: body['new_cluster'] = self.new_cluster
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
    def from_dict(cls, d: Dict[str, any]) -> 'RunTask':
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
    jar_uri: str = None
    main_class_name: str = None
    parameters: 'List[str]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.jar_uri: body['jar_uri'] = self.jar_uri
        if self.main_class_name: body['main_class_name'] = self.main_class_name
        if self.parameters: body['parameters'] = [v for v in self.parameters]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparkJarTask':
        return cls(jar_uri=d.get('jar_uri', None),
                   main_class_name=d.get('main_class_name', None),
                   parameters=d.get('parameters', None))


@dataclass
class SparkPythonTask:
    python_file: str
    parameters: 'List[str]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.parameters: body['parameters'] = [v for v in self.parameters]
        if self.python_file: body['python_file'] = self.python_file
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparkPythonTask':
        return cls(parameters=d.get('parameters', None), python_file=d.get('python_file', None))


@dataclass
class SparkSubmitTask:
    parameters: 'List[str]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.parameters: body['parameters'] = [v for v in self.parameters]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparkSubmitTask':
        return cls(parameters=d.get('parameters', None))


@dataclass
class SqlAlertOutput:
    alert_state: 'SqlAlertState' = None
    output_link: str = None
    query_text: str = None
    sql_statements: 'List[SqlStatementOutput]' = None
    warehouse_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.alert_state: body['alert_state'] = self.alert_state.value
        if self.output_link: body['output_link'] = self.output_link
        if self.query_text: body['query_text'] = self.query_text
        if self.sql_statements: body['sql_statements'] = [v.as_dict() for v in self.sql_statements]
        if self.warehouse_id: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlAlertOutput':
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
    warehouse_id: str = None
    widgets: 'SqlDashboardWidgetOutput' = None

    def as_dict(self) -> dict:
        body = {}
        if self.warehouse_id: body['warehouse_id'] = self.warehouse_id
        if self.widgets: body['widgets'] = self.widgets.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlDashboardOutput':
        return cls(warehouse_id=d.get('warehouse_id', None),
                   widgets=_from_dict(d, 'widgets', SqlDashboardWidgetOutput))


@dataclass
class SqlDashboardWidgetOutput:
    end_time: int = None
    error: 'SqlOutputError' = None
    output_link: str = None
    start_time: int = None
    status: 'SqlDashboardWidgetOutputStatus' = None
    widget_id: str = None
    widget_title: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.end_time: body['end_time'] = self.end_time
        if self.error: body['error'] = self.error.as_dict()
        if self.output_link: body['output_link'] = self.output_link
        if self.start_time: body['start_time'] = self.start_time
        if self.status: body['status'] = self.status.value
        if self.widget_id: body['widget_id'] = self.widget_id
        if self.widget_title: body['widget_title'] = self.widget_title
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlDashboardWidgetOutput':
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
    alert_output: 'SqlAlertOutput' = None
    dashboard_output: 'SqlDashboardOutput' = None
    query_output: 'SqlQueryOutput' = None

    def as_dict(self) -> dict:
        body = {}
        if self.alert_output: body['alert_output'] = self.alert_output.as_dict()
        if self.dashboard_output: body['dashboard_output'] = self.dashboard_output.as_dict()
        if self.query_output: body['query_output'] = self.query_output.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlOutput':
        return cls(alert_output=_from_dict(d, 'alert_output', SqlAlertOutput),
                   dashboard_output=_from_dict(d, 'dashboard_output', SqlDashboardOutput),
                   query_output=_from_dict(d, 'query_output', SqlQueryOutput))


@dataclass
class SqlOutputError:
    message: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.message: body['message'] = self.message
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlOutputError':
        return cls(message=d.get('message', None))


@dataclass
class SqlQueryOutput:
    output_link: str = None
    query_text: str = None
    sql_statements: 'List[SqlStatementOutput]' = None
    warehouse_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.output_link: body['output_link'] = self.output_link
        if self.query_text: body['query_text'] = self.query_text
        if self.sql_statements: body['sql_statements'] = [v.as_dict() for v in self.sql_statements]
        if self.warehouse_id: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlQueryOutput':
        return cls(output_link=d.get('output_link', None),
                   query_text=d.get('query_text', None),
                   sql_statements=_repeated(d, 'sql_statements', SqlStatementOutput),
                   warehouse_id=d.get('warehouse_id', None))


@dataclass
class SqlStatementOutput:
    lookup_key: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.lookup_key: body['lookup_key'] = self.lookup_key
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlStatementOutput':
        return cls(lookup_key=d.get('lookup_key', None))


@dataclass
class SqlTask:
    warehouse_id: str
    alert: 'SqlTaskAlert' = None
    dashboard: 'SqlTaskDashboard' = None
    parameters: 'Dict[str,str]' = None
    query: 'SqlTaskQuery' = None

    def as_dict(self) -> dict:
        body = {}
        if self.alert: body['alert'] = self.alert.as_dict()
        if self.dashboard: body['dashboard'] = self.dashboard.as_dict()
        if self.parameters: body['parameters'] = self.parameters
        if self.query: body['query'] = self.query.as_dict()
        if self.warehouse_id: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlTask':
        return cls(alert=_from_dict(d, 'alert', SqlTaskAlert),
                   dashboard=_from_dict(d, 'dashboard', SqlTaskDashboard),
                   parameters=d.get('parameters', None),
                   query=_from_dict(d, 'query', SqlTaskQuery),
                   warehouse_id=d.get('warehouse_id', None))


@dataclass
class SqlTaskAlert:
    alert_id: str
    pause_subscriptions: bool = None
    subscriptions: 'List[SqlTaskSubscription]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.alert_id: body['alert_id'] = self.alert_id
        if self.pause_subscriptions: body['pause_subscriptions'] = self.pause_subscriptions
        if self.subscriptions: body['subscriptions'] = [v.as_dict() for v in self.subscriptions]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlTaskAlert':
        return cls(alert_id=d.get('alert_id', None),
                   pause_subscriptions=d.get('pause_subscriptions', None),
                   subscriptions=_repeated(d, 'subscriptions', SqlTaskSubscription))


@dataclass
class SqlTaskDashboard:
    dashboard_id: str
    custom_subject: str = None
    pause_subscriptions: bool = None
    subscriptions: 'List[SqlTaskSubscription]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.custom_subject: body['custom_subject'] = self.custom_subject
        if self.dashboard_id: body['dashboard_id'] = self.dashboard_id
        if self.pause_subscriptions: body['pause_subscriptions'] = self.pause_subscriptions
        if self.subscriptions: body['subscriptions'] = [v.as_dict() for v in self.subscriptions]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlTaskDashboard':
        return cls(custom_subject=d.get('custom_subject', None),
                   dashboard_id=d.get('dashboard_id', None),
                   pause_subscriptions=d.get('pause_subscriptions', None),
                   subscriptions=_repeated(d, 'subscriptions', SqlTaskSubscription))


@dataclass
class SqlTaskQuery:
    query_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.query_id: body['query_id'] = self.query_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlTaskQuery':
        return cls(query_id=d.get('query_id', None))


@dataclass
class SqlTaskSubscription:
    destination_id: str = None
    user_name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.destination_id: body['destination_id'] = self.destination_id
        if self.user_name: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlTaskSubscription':
        return cls(destination_id=d.get('destination_id', None), user_name=d.get('user_name', None))


@dataclass
class SubmitRun:
    access_control_list: 'List[AccessControlRequest]' = None
    git_source: 'GitSource' = None
    idempotency_token: str = None
    run_name: str = None
    tasks: 'List[RunSubmitTaskSettings]' = None
    timeout_seconds: int = None
    webhook_notifications: 'JobWebhookNotifications' = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list: body['access_control_list'] = [v for v in self.access_control_list]
        if self.git_source: body['git_source'] = self.git_source.as_dict()
        if self.idempotency_token: body['idempotency_token'] = self.idempotency_token
        if self.run_name: body['run_name'] = self.run_name
        if self.tasks: body['tasks'] = [v.as_dict() for v in self.tasks]
        if self.timeout_seconds: body['timeout_seconds'] = self.timeout_seconds
        if self.webhook_notifications: body['webhook_notifications'] = self.webhook_notifications.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SubmitRun':
        return cls(access_control_list=d.get('access_control_list', None),
                   git_source=_from_dict(d, 'git_source', GitSource),
                   idempotency_token=d.get('idempotency_token', None),
                   run_name=d.get('run_name', None),
                   tasks=_repeated(d, 'tasks', RunSubmitTaskSettings),
                   timeout_seconds=d.get('timeout_seconds', None),
                   webhook_notifications=_from_dict(d, 'webhook_notifications', JobWebhookNotifications))


@dataclass
class SubmitRunResponse:
    run_id: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.run_id: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SubmitRunResponse':
        return cls(run_id=d.get('run_id', None))


@dataclass
class TaskDependenciesItem:
    task_key: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.task_key: body['task_key'] = self.task_key
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TaskDependenciesItem':
        return cls(task_key=d.get('task_key', None))


@dataclass
class TriggerEvaluation:
    description: str = None
    run_id: int = None
    timestamp: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.description: body['description'] = self.description
        if self.run_id: body['run_id'] = self.run_id
        if self.timestamp: body['timestamp'] = self.timestamp
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TriggerEvaluation':
        return cls(description=d.get('description', None),
                   run_id=d.get('run_id', None),
                   timestamp=d.get('timestamp', None))


@dataclass
class TriggerHistory:
    last_failed: 'TriggerEvaluation' = None
    last_not_triggered: 'TriggerEvaluation' = None
    last_triggered: 'TriggerEvaluation' = None

    def as_dict(self) -> dict:
        body = {}
        if self.last_failed: body['last_failed'] = self.last_failed.as_dict()
        if self.last_not_triggered: body['last_not_triggered'] = self.last_not_triggered.as_dict()
        if self.last_triggered: body['last_triggered'] = self.last_triggered.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TriggerHistory':
        return cls(last_failed=_from_dict(d, 'last_failed', TriggerEvaluation),
                   last_not_triggered=_from_dict(d, 'last_not_triggered', TriggerEvaluation),
                   last_triggered=_from_dict(d, 'last_triggered', TriggerEvaluation))


@dataclass
class TriggerSettings:
    file_arrival: 'FileArrivalTriggerSettings' = None
    pause_status: 'TriggerSettingsPauseStatus' = None

    def as_dict(self) -> dict:
        body = {}
        if self.file_arrival: body['file_arrival'] = self.file_arrival.as_dict()
        if self.pause_status: body['pause_status'] = self.pause_status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TriggerSettings':
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
    fields_to_remove: 'List[str]' = None
    new_settings: 'JobSettings' = None

    def as_dict(self) -> dict:
        body = {}
        if self.fields_to_remove: body['fields_to_remove'] = [v for v in self.fields_to_remove]
        if self.job_id: body['job_id'] = self.job_id
        if self.new_settings: body['new_settings'] = self.new_settings.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateJob':
        return cls(fields_to_remove=d.get('fields_to_remove', None),
                   job_id=d.get('job_id', None),
                   new_settings=_from_dict(d, 'new_settings', JobSettings))


@dataclass
class ViewItem:
    content: str = None
    name: str = None
    type: 'ViewType' = None

    def as_dict(self) -> dict:
        body = {}
        if self.content: body['content'] = self.content
        if self.name: body['name'] = self.name
        if self.type: body['type'] = self.type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ViewItem':
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

    def __init__(self, api_client):
        self._api = api_client

    def wait_get_run_job_terminated_or_skipped(self, run_id: int, timeout=timedelta(minutes=20)) -> Run:
        deadline = time.time() + timeout.total_seconds()
        target_states = (RunLifeCycleState.TERMINATED, RunLifeCycleState.SKIPPED, )
        failure_states = (RunLifeCycleState.INTERNAL_ERROR, )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.get_run(run_id=run_id)
            status = poll.state.life_cycle_state
            status_message = f'current status: {status}'
            if poll.state:
                status_message = poll.state.state_message
            if status in target_states:
                return poll
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

    def cancel_all_runs(self, job_id: int, **kwargs):
        """Cancel all runs of a job.
        
        Cancels all active runs of a job. The runs are canceled asynchronously, so it doesn't prevent new runs
        from being started."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CancelAllRuns(job_id=job_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.1/jobs/runs/cancel-all', body=body)

    def cancel_run(self, run_id: int, **kwargs) -> Wait[Run]:
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
               access_control_list: List[AccessControlRequest] = None,
               continuous: Continuous = None,
               email_notifications: JobEmailNotifications = None,
               format: CreateJobFormat = None,
               git_source: GitSource = None,
               job_clusters: List[JobCluster] = None,
               max_concurrent_runs: int = None,
               name: str = None,
               schedule: CronSchedule = None,
               tags: Dict[str, str] = None,
               tasks: List[JobTaskSettings] = None,
               timeout_seconds: int = None,
               trigger: TriggerSettings = None,
               webhook_notifications: JobWebhookNotifications = None,
               **kwargs) -> CreateResponse:
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

    def delete(self, job_id: int, **kwargs):
        """Delete a job.
        
        Deletes a job."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteJob(job_id=job_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.1/jobs/delete', body=body)

    def delete_run(self, run_id: int, **kwargs):
        """Delete a job run.
        
        Deletes a non-active run. Returns an error if the run is active."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteRun(run_id=run_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.1/jobs/runs/delete', body=body)

    def export_run(self, run_id: int, *, views_to_export: ViewsToExport = None, **kwargs) -> ExportRunOutput:
        """Export and retrieve a job run.
        
        Export and retrieve the job run task."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ExportRun(run_id=run_id, views_to_export=views_to_export)

        query = {}
        if run_id: query['run_id'] = request.run_id
        if views_to_export: query['views_to_export'] = request.views_to_export.value

        json = self._api.do('GET', '/api/2.1/jobs/runs/export', query=query)
        return ExportRunOutput.from_dict(json)

    def get(self, job_id: int, **kwargs) -> Job:
        """Get a single job.
        
        Retrieves the details for a single job."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Get(job_id=job_id)

        query = {}
        if job_id: query['job_id'] = request.job_id

        json = self._api.do('GET', '/api/2.1/jobs/get', query=query)
        return Job.from_dict(json)

    def get_run(self, run_id: int, *, include_history: bool = None, **kwargs) -> Run:
        """Get a single job run.
        
        Retrieve the metadata of a run."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetRun(include_history=include_history, run_id=run_id)

        query = {}
        if include_history: query['include_history'] = request.include_history
        if run_id: query['run_id'] = request.run_id

        json = self._api.do('GET', '/api/2.1/jobs/runs/get', query=query)
        return Run.from_dict(json)

    def get_run_output(self, run_id: int, **kwargs) -> RunOutput:
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
            request = GetRunOutput(run_id=run_id)

        query = {}
        if run_id: query['run_id'] = request.run_id

        json = self._api.do('GET', '/api/2.1/jobs/runs/get-output', query=query)
        return RunOutput.from_dict(json)

    def list(self,
             *,
             expand_tasks: bool = None,
             limit: int = None,
             name: str = None,
             offset: int = None,
             **kwargs) -> Iterator[BaseJob]:
        """List all jobs.
        
        Retrieves a list of jobs."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListRequest(expand_tasks=expand_tasks, limit=limit, name=name, offset=offset)

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
                  active_only: bool = None,
                  completed_only: bool = None,
                  expand_tasks: bool = None,
                  job_id: int = None,
                  limit: int = None,
                  offset: int = None,
                  run_type: ListRunsRunType = None,
                  start_time_from: int = None,
                  start_time_to: int = None,
                  **kwargs) -> Iterator[BaseRun]:
        """List runs for a job.
        
        List runs in descending order by start time."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListRuns(active_only=active_only,
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
                   dbt_commands: List[str] = None,
                   jar_params: List[str] = None,
                   latest_repair_id: int = None,
                   notebook_params: Dict[str, str] = None,
                   pipeline_params: PipelineParams = None,
                   python_named_params: Dict[str, str] = None,
                   python_params: List[str] = None,
                   rerun_all_failed_tasks: bool = None,
                   rerun_tasks: List[str] = None,
                   spark_submit_params: List[str] = None,
                   sql_params: Dict[str, str] = None,
                   **kwargs) -> Wait[Run]:
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
        return Wait(self.wait_get_run_job_terminated_or_skipped, run_id=request.run_id)

    def repair_run_and_wait(self,
                            run_id: int,
                            *,
                            dbt_commands: List[str] = None,
                            jar_params: List[str] = None,
                            latest_repair_id: int = None,
                            notebook_params: Dict[str, str] = None,
                            pipeline_params: PipelineParams = None,
                            python_named_params: Dict[str, str] = None,
                            python_params: List[str] = None,
                            rerun_all_failed_tasks: bool = None,
                            rerun_tasks: List[str] = None,
                            spark_submit_params: List[str] = None,
                            sql_params: Dict[str, str] = None,
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

    def reset(self, job_id: int, new_settings: JobSettings, **kwargs):
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
                dbt_commands: List[str] = None,
                idempotency_token: str = None,
                jar_params: List[str] = None,
                notebook_params: Dict[str, str] = None,
                pipeline_params: PipelineParams = None,
                python_named_params: Dict[str, str] = None,
                python_params: List[str] = None,
                spark_submit_params: List[str] = None,
                sql_params: Dict[str, str] = None,
                **kwargs) -> Wait[Run]:
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
        return Wait(self.wait_get_run_job_terminated_or_skipped, run_id=op_response['run_id'])

    def run_now_and_wait(self,
                         job_id: int,
                         *,
                         dbt_commands: List[str] = None,
                         idempotency_token: str = None,
                         jar_params: List[str] = None,
                         notebook_params: Dict[str, str] = None,
                         pipeline_params: PipelineParams = None,
                         python_named_params: Dict[str, str] = None,
                         python_params: List[str] = None,
                         spark_submit_params: List[str] = None,
                         sql_params: Dict[str, str] = None,
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
               access_control_list: List[AccessControlRequest] = None,
               git_source: GitSource = None,
               idempotency_token: str = None,
               run_name: str = None,
               tasks: List[RunSubmitTaskSettings] = None,
               timeout_seconds: int = None,
               webhook_notifications: JobWebhookNotifications = None,
               **kwargs) -> Wait[Run]:
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
        return Wait(self.wait_get_run_job_terminated_or_skipped, run_id=op_response['run_id'])

    def submit_and_wait(
        self,
        *,
        access_control_list: List[AccessControlRequest] = None,
        git_source: GitSource = None,
        idempotency_token: str = None,
        run_name: str = None,
        tasks: List[RunSubmitTaskSettings] = None,
        timeout_seconds: int = None,
        webhook_notifications: JobWebhookNotifications = None,
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
               fields_to_remove: List[str] = None,
               new_settings: JobSettings = None,
               **kwargs):
        """Partially updates a job.
        
        Add, update, or remove specific settings of an existing job. Use the ResetJob to overwrite all job
        settings."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateJob(fields_to_remove=fields_to_remove, job_id=job_id, new_settings=new_settings)
        body = request.as_dict()
        self._api.do('POST', '/api/2.1/jobs/update', body=body)

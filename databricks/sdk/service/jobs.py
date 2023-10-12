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

from databricks.sdk.service import compute, iam

# all definitions in this file are in alphabetical order


@dataclass
class BaseJob:
    created_time: Optional[int] = None
    creator_user_name: Optional[str] = None
    job_id: Optional[int] = None
    settings: Optional['JobSettings'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_time is not None: body['created_time'] = self.created_time
        if self.creator_user_name is not None: body['creator_user_name'] = self.creator_user_name
        if self.job_id is not None: body['job_id'] = self.job_id
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
    job_parameters: Optional['List[JobParameter]'] = None
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
    trigger_info: Optional['TriggerInfo'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.attempt_number is not None: body['attempt_number'] = self.attempt_number
        if self.cleanup_duration is not None: body['cleanup_duration'] = self.cleanup_duration
        if self.cluster_instance: body['cluster_instance'] = self.cluster_instance.as_dict()
        if self.cluster_spec: body['cluster_spec'] = self.cluster_spec.as_dict()
        if self.continuous: body['continuous'] = self.continuous.as_dict()
        if self.creator_user_name is not None: body['creator_user_name'] = self.creator_user_name
        if self.end_time is not None: body['end_time'] = self.end_time
        if self.execution_duration is not None: body['execution_duration'] = self.execution_duration
        if self.git_source: body['git_source'] = self.git_source.as_dict()
        if self.job_clusters: body['job_clusters'] = [v.as_dict() for v in self.job_clusters]
        if self.job_id is not None: body['job_id'] = self.job_id
        if self.job_parameters: body['job_parameters'] = [v.as_dict() for v in self.job_parameters]
        if self.number_in_job is not None: body['number_in_job'] = self.number_in_job
        if self.original_attempt_run_id is not None:
            body['original_attempt_run_id'] = self.original_attempt_run_id
        if self.overriding_parameters: body['overriding_parameters'] = self.overriding_parameters.as_dict()
        if self.run_duration is not None: body['run_duration'] = self.run_duration
        if self.run_id is not None: body['run_id'] = self.run_id
        if self.run_name is not None: body['run_name'] = self.run_name
        if self.run_page_url is not None: body['run_page_url'] = self.run_page_url
        if self.run_type is not None: body['run_type'] = self.run_type.value
        if self.schedule: body['schedule'] = self.schedule.as_dict()
        if self.setup_duration is not None: body['setup_duration'] = self.setup_duration
        if self.start_time is not None: body['start_time'] = self.start_time
        if self.state: body['state'] = self.state.as_dict()
        if self.tasks: body['tasks'] = [v.as_dict() for v in self.tasks]
        if self.trigger is not None: body['trigger'] = self.trigger.value
        if self.trigger_info: body['trigger_info'] = self.trigger_info.as_dict()
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
                   job_parameters=_repeated(d, 'job_parameters', JobParameter),
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
                   trigger=_enum(d, 'trigger', TriggerType),
                   trigger_info=_from_dict(d, 'trigger_info', TriggerInfo))


@dataclass
class CancelAllRuns:
    all_queued_runs: Optional[bool] = None
    job_id: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.all_queued_runs is not None: body['all_queued_runs'] = self.all_queued_runs
        if self.job_id is not None: body['job_id'] = self.job_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CancelAllRuns':
        return cls(all_queued_runs=d.get('all_queued_runs', None), job_id=d.get('job_id', None))


@dataclass
class CancelRun:
    run_id: int

    def as_dict(self) -> dict:
        body = {}
        if self.run_id is not None: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CancelRun':
        return cls(run_id=d.get('run_id', None))


@dataclass
class ClusterInstance:
    cluster_id: Optional[str] = None
    spark_context_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        if self.spark_context_id is not None: body['spark_context_id'] = self.spark_context_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterInstance':
        return cls(cluster_id=d.get('cluster_id', None), spark_context_id=d.get('spark_context_id', None))


@dataclass
class ClusterSpec:
    existing_cluster_id: Optional[str] = None
    libraries: Optional['List[compute.Library]'] = None
    new_cluster: Optional['compute.ClusterSpec'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.existing_cluster_id is not None: body['existing_cluster_id'] = self.existing_cluster_id
        if self.libraries: body['libraries'] = [v.as_dict() for v in self.libraries]
        if self.new_cluster: body['new_cluster'] = self.new_cluster.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterSpec':
        return cls(existing_cluster_id=d.get('existing_cluster_id', None),
                   libraries=_repeated(d, 'libraries', compute.Library),
                   new_cluster=_from_dict(d, 'new_cluster', compute.ClusterSpec))


@dataclass
class ConditionTask:
    left: Optional[str] = None
    op: Optional['ConditionTaskOp'] = None
    right: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.left is not None: body['left'] = self.left
        if self.op is not None: body['op'] = self.op.value
        if self.right is not None: body['right'] = self.right
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ConditionTask':
        return cls(left=d.get('left', None), op=_enum(d, 'op', ConditionTaskOp), right=d.get('right', None))


class ConditionTaskOp(Enum):
    """* `EQUAL_TO`, `NOT_EQUAL` operators perform string comparison of their operands. This means that
    `“12.0” == “12”` will evaluate to `false`. * `GREATER_THAN`, `GREATER_THAN_OR_EQUAL`,
    `LESS_THAN`, `LESS_THAN_OR_EQUAL` operators perform numeric comparison of their operands.
    `“12.0” >= “12”` will evaluate to `true`, `“10.0” >= “12”` will evaluate to
    `false`.
    
    The boolean comparison to task values can be implemented with operators `EQUAL_TO`, `NOT_EQUAL`.
    If a task value was set to a boolean value, it will be serialized to `“true”` or
    `“false”` for the comparison."""

    EQUAL_TO = 'EQUAL_TO'
    GREATER_THAN = 'GREATER_THAN'
    GREATER_THAN_OR_EQUAL = 'GREATER_THAN_OR_EQUAL'
    LESS_THAN = 'LESS_THAN'
    LESS_THAN_OR_EQUAL = 'LESS_THAN_OR_EQUAL'
    NOT_EQUAL = 'NOT_EQUAL'


@dataclass
class Continuous:
    pause_status: Optional['PauseStatus'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.pause_status is not None: body['pause_status'] = self.pause_status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Continuous':
        return cls(pause_status=_enum(d, 'pause_status', PauseStatus))


@dataclass
class CreateJob:
    access_control_list: Optional['List[iam.AccessControlRequest]'] = None
    compute: Optional['List[JobCompute]'] = None
    continuous: Optional['Continuous'] = None
    deployment: Optional['JobDeployment'] = None
    email_notifications: Optional['JobEmailNotifications'] = None
    format: Optional['Format'] = None
    git_source: Optional['GitSource'] = None
    health: Optional['JobsHealthRules'] = None
    job_clusters: Optional['List[JobCluster]'] = None
    max_concurrent_runs: Optional[int] = None
    name: Optional[str] = None
    notification_settings: Optional['JobNotificationSettings'] = None
    parameters: Optional['List[JobParameterDefinition]'] = None
    queue: Optional['QueueSettings'] = None
    run_as: Optional['JobRunAs'] = None
    schedule: Optional['CronSchedule'] = None
    tags: Optional['Dict[str,str]'] = None
    tasks: Optional['List[Task]'] = None
    timeout_seconds: Optional[int] = None
    trigger: Optional['TriggerSettings'] = None
    ui_state: Optional['CreateJobUiState'] = None
    webhook_notifications: Optional['WebhookNotifications'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.compute: body['compute'] = [v.as_dict() for v in self.compute]
        if self.continuous: body['continuous'] = self.continuous.as_dict()
        if self.deployment: body['deployment'] = self.deployment.as_dict()
        if self.email_notifications: body['email_notifications'] = self.email_notifications.as_dict()
        if self.format is not None: body['format'] = self.format.value
        if self.git_source: body['git_source'] = self.git_source.as_dict()
        if self.health: body['health'] = self.health.as_dict()
        if self.job_clusters: body['job_clusters'] = [v.as_dict() for v in self.job_clusters]
        if self.max_concurrent_runs is not None: body['max_concurrent_runs'] = self.max_concurrent_runs
        if self.name is not None: body['name'] = self.name
        if self.notification_settings: body['notification_settings'] = self.notification_settings.as_dict()
        if self.parameters: body['parameters'] = [v.as_dict() for v in self.parameters]
        if self.queue: body['queue'] = self.queue.as_dict()
        if self.run_as: body['run_as'] = self.run_as.as_dict()
        if self.schedule: body['schedule'] = self.schedule.as_dict()
        if self.tags: body['tags'] = self.tags
        if self.tasks: body['tasks'] = [v.as_dict() for v in self.tasks]
        if self.timeout_seconds is not None: body['timeout_seconds'] = self.timeout_seconds
        if self.trigger: body['trigger'] = self.trigger.as_dict()
        if self.ui_state is not None: body['ui_state'] = self.ui_state.value
        if self.webhook_notifications: body['webhook_notifications'] = self.webhook_notifications.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateJob':
        return cls(access_control_list=_repeated(d, 'access_control_list', iam.AccessControlRequest),
                   compute=_repeated(d, 'compute', JobCompute),
                   continuous=_from_dict(d, 'continuous', Continuous),
                   deployment=_from_dict(d, 'deployment', JobDeployment),
                   email_notifications=_from_dict(d, 'email_notifications', JobEmailNotifications),
                   format=_enum(d, 'format', Format),
                   git_source=_from_dict(d, 'git_source', GitSource),
                   health=_from_dict(d, 'health', JobsHealthRules),
                   job_clusters=_repeated(d, 'job_clusters', JobCluster),
                   max_concurrent_runs=d.get('max_concurrent_runs', None),
                   name=d.get('name', None),
                   notification_settings=_from_dict(d, 'notification_settings', JobNotificationSettings),
                   parameters=_repeated(d, 'parameters', JobParameterDefinition),
                   queue=_from_dict(d, 'queue', QueueSettings),
                   run_as=_from_dict(d, 'run_as', JobRunAs),
                   schedule=_from_dict(d, 'schedule', CronSchedule),
                   tags=d.get('tags', None),
                   tasks=_repeated(d, 'tasks', Task),
                   timeout_seconds=d.get('timeout_seconds', None),
                   trigger=_from_dict(d, 'trigger', TriggerSettings),
                   ui_state=_enum(d, 'ui_state', CreateJobUiState),
                   webhook_notifications=_from_dict(d, 'webhook_notifications', WebhookNotifications))


class CreateJobUiState(Enum):
    """State of the job in UI.
    
    * `LOCKED`: The job is in a locked state and cannot be modified. * `EDITABLE`: The job is in an
    editable state and can be modified."""

    EDITABLE = 'EDITABLE'
    LOCKED = 'LOCKED'


@dataclass
class CreateResponse:
    job_id: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.job_id is not None: body['job_id'] = self.job_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateResponse':
        return cls(job_id=d.get('job_id', None))


@dataclass
class CronSchedule:
    quartz_cron_expression: str
    timezone_id: str
    pause_status: Optional['PauseStatus'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.pause_status is not None: body['pause_status'] = self.pause_status.value
        if self.quartz_cron_expression is not None:
            body['quartz_cron_expression'] = self.quartz_cron_expression
        if self.timezone_id is not None: body['timezone_id'] = self.timezone_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CronSchedule':
        return cls(pause_status=_enum(d, 'pause_status', PauseStatus),
                   quartz_cron_expression=d.get('quartz_cron_expression', None),
                   timezone_id=d.get('timezone_id', None))


@dataclass
class DbtOutput:
    artifacts_headers: Optional['Dict[str,str]'] = None
    artifacts_link: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.artifacts_headers: body['artifacts_headers'] = self.artifacts_headers
        if self.artifacts_link is not None: body['artifacts_link'] = self.artifacts_link
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DbtOutput':
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
        body = {}
        if self.catalog is not None: body['catalog'] = self.catalog
        if self.commands: body['commands'] = [v for v in self.commands]
        if self.profiles_directory is not None: body['profiles_directory'] = self.profiles_directory
        if self.project_directory is not None: body['project_directory'] = self.project_directory
        if self.schema is not None: body['schema'] = self.schema
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
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
        if self.job_id is not None: body['job_id'] = self.job_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteJob':
        return cls(job_id=d.get('job_id', None))


@dataclass
class DeleteRun:
    run_id: int

    def as_dict(self) -> dict:
        body = {}
        if self.run_id is not None: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteRun':
        return cls(run_id=d.get('run_id', None))


@dataclass
class ExportRunOutput:
    views: Optional['List[ViewItem]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.views: body['views'] = [v.as_dict() for v in self.views]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ExportRunOutput':
        return cls(views=_repeated(d, 'views', ViewItem))


@dataclass
class FileArrivalTriggerConfiguration:
    min_time_between_triggers_seconds: Optional[int] = None
    url: Optional[str] = None
    wait_after_last_change_seconds: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.min_time_between_triggers_seconds is not None:
            body['min_time_between_triggers_seconds'] = self.min_time_between_triggers_seconds
        if self.url is not None: body['url'] = self.url
        if self.wait_after_last_change_seconds is not None:
            body['wait_after_last_change_seconds'] = self.wait_after_last_change_seconds
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FileArrivalTriggerConfiguration':
        return cls(min_time_between_triggers_seconds=d.get('min_time_between_triggers_seconds', None),
                   url=d.get('url', None),
                   wait_after_last_change_seconds=d.get('wait_after_last_change_seconds', None))


class Format(Enum):

    MULTI_TASK = 'MULTI_TASK'
    SINGLE_TASK = 'SINGLE_TASK'


@dataclass
class GetJobPermissionLevelsResponse:
    permission_levels: Optional['List[JobPermissionsDescription]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.permission_levels: body['permission_levels'] = [v.as_dict() for v in self.permission_levels]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetJobPermissionLevelsResponse':
        return cls(permission_levels=_repeated(d, 'permission_levels', JobPermissionsDescription))


class GitProvider(Enum):

    AWS_CODE_COMMIT = 'awsCodeCommit'
    AZURE_DEV_OPS_SERVICES = 'azureDevOpsServices'
    BITBUCKET_CLOUD = 'bitbucketCloud'
    BITBUCKET_SERVER = 'bitbucketServer'
    GIT_HUB = 'gitHub'
    GIT_HUB_ENTERPRISE = 'gitHubEnterprise'
    GIT_LAB = 'gitLab'
    GIT_LAB_ENTERPRISE_EDITION = 'gitLabEnterpriseEdition'


@dataclass
class GitSnapshot:
    """Read-only state of the remote repository at the time the job was run. This field is only
    included on job runs."""

    used_commit: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.used_commit is not None: body['used_commit'] = self.used_commit
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GitSnapshot':
        return cls(used_commit=d.get('used_commit', None))


@dataclass
class GitSource:
    """An optional specification for a remote Git repository containing the source code used by tasks.
    Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks.
    
    If `git_source` is set, these tasks retrieve the file from the remote repository by default.
    However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task.
    
    Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks
    are used, `git_source` must be defined on the job."""

    git_url: str
    git_provider: 'GitProvider'
    git_branch: Optional[str] = None
    git_commit: Optional[str] = None
    git_snapshot: Optional['GitSnapshot'] = None
    git_tag: Optional[str] = None
    job_source: Optional['JobSource'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.git_branch is not None: body['git_branch'] = self.git_branch
        if self.git_commit is not None: body['git_commit'] = self.git_commit
        if self.git_provider is not None: body['git_provider'] = self.git_provider.value
        if self.git_snapshot: body['git_snapshot'] = self.git_snapshot.as_dict()
        if self.git_tag is not None: body['git_tag'] = self.git_tag
        if self.git_url is not None: body['git_url'] = self.git_url
        if self.job_source: body['job_source'] = self.job_source.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GitSource':
        return cls(git_branch=d.get('git_branch', None),
                   git_commit=d.get('git_commit', None),
                   git_provider=_enum(d, 'git_provider', GitProvider),
                   git_snapshot=_from_dict(d, 'git_snapshot', GitSnapshot),
                   git_tag=d.get('git_tag', None),
                   git_url=d.get('git_url', None),
                   job_source=_from_dict(d, 'job_source', JobSource))


@dataclass
class Job:
    created_time: Optional[int] = None
    creator_user_name: Optional[str] = None
    job_id: Optional[int] = None
    run_as_user_name: Optional[str] = None
    settings: Optional['JobSettings'] = None
    trigger_history: Optional['TriggerHistory'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_time is not None: body['created_time'] = self.created_time
        if self.creator_user_name is not None: body['creator_user_name'] = self.creator_user_name
        if self.job_id is not None: body['job_id'] = self.job_id
        if self.run_as_user_name is not None: body['run_as_user_name'] = self.run_as_user_name
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
class JobAccessControlRequest:
    group_name: Optional[str] = None
    permission_level: Optional['JobPermissionLevel'] = None
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
    def from_dict(cls, d: Dict[str, any]) -> 'JobAccessControlRequest':
        return cls(group_name=d.get('group_name', None),
                   permission_level=_enum(d, 'permission_level', JobPermissionLevel),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class JobAccessControlResponse:
    all_permissions: Optional['List[JobPermission]'] = None
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
    def from_dict(cls, d: Dict[str, any]) -> 'JobAccessControlResponse':
        return cls(all_permissions=_repeated(d, 'all_permissions', JobPermission),
                   display_name=d.get('display_name', None),
                   group_name=d.get('group_name', None),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class JobCluster:
    job_cluster_key: str
    new_cluster: Optional['compute.ClusterSpec'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.job_cluster_key is not None: body['job_cluster_key'] = self.job_cluster_key
        if self.new_cluster: body['new_cluster'] = self.new_cluster.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobCluster':
        return cls(job_cluster_key=d.get('job_cluster_key', None),
                   new_cluster=_from_dict(d, 'new_cluster', compute.ClusterSpec))


@dataclass
class JobCompute:
    compute_key: str
    spec: 'compute.ComputeSpec'

    def as_dict(self) -> dict:
        body = {}
        if self.compute_key is not None: body['compute_key'] = self.compute_key
        if self.spec: body['spec'] = self.spec.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobCompute':
        return cls(compute_key=d.get('compute_key', None), spec=_from_dict(d, 'spec', compute.ComputeSpec))


@dataclass
class JobDeployment:
    kind: 'JobDeploymentKind'
    metadata_file_path: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.kind is not None: body['kind'] = self.kind.value
        if self.metadata_file_path is not None: body['metadata_file_path'] = self.metadata_file_path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobDeployment':
        return cls(kind=_enum(d, 'kind', JobDeploymentKind),
                   metadata_file_path=d.get('metadata_file_path', None))


class JobDeploymentKind(Enum):
    """The kind of deployment that manages the job.
    
    * `BUNDLE`: The job is managed by Databricks Asset Bundle."""

    BUNDLE = 'BUNDLE'


@dataclass
class JobEmailNotifications:
    no_alert_for_skipped_runs: Optional[bool] = None
    on_duration_warning_threshold_exceeded: Optional['List[str]'] = None
    on_failure: Optional['List[str]'] = None
    on_start: Optional['List[str]'] = None
    on_success: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.no_alert_for_skipped_runs is not None:
            body['no_alert_for_skipped_runs'] = self.no_alert_for_skipped_runs
        if self.on_duration_warning_threshold_exceeded:
            body['on_duration_warning_threshold_exceeded'] = [
                v for v in self.on_duration_warning_threshold_exceeded
            ]
        if self.on_failure: body['on_failure'] = [v for v in self.on_failure]
        if self.on_start: body['on_start'] = [v for v in self.on_start]
        if self.on_success: body['on_success'] = [v for v in self.on_success]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobEmailNotifications':
        return cls(no_alert_for_skipped_runs=d.get('no_alert_for_skipped_runs', None),
                   on_duration_warning_threshold_exceeded=d.get('on_duration_warning_threshold_exceeded',
                                                                None),
                   on_failure=d.get('on_failure', None),
                   on_start=d.get('on_start', None),
                   on_success=d.get('on_success', None))


@dataclass
class JobNotificationSettings:
    no_alert_for_canceled_runs: Optional[bool] = None
    no_alert_for_skipped_runs: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.no_alert_for_canceled_runs is not None:
            body['no_alert_for_canceled_runs'] = self.no_alert_for_canceled_runs
        if self.no_alert_for_skipped_runs is not None:
            body['no_alert_for_skipped_runs'] = self.no_alert_for_skipped_runs
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobNotificationSettings':
        return cls(no_alert_for_canceled_runs=d.get('no_alert_for_canceled_runs', None),
                   no_alert_for_skipped_runs=d.get('no_alert_for_skipped_runs', None))


@dataclass
class JobParameter:
    default: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.default is not None: body['default'] = self.default
        if self.name is not None: body['name'] = self.name
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobParameter':
        return cls(default=d.get('default', None), name=d.get('name', None), value=d.get('value', None))


@dataclass
class JobParameterDefinition:
    name: str
    default: str

    def as_dict(self) -> dict:
        body = {}
        if self.default is not None: body['default'] = self.default
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobParameterDefinition':
        return cls(default=d.get('default', None), name=d.get('name', None))


@dataclass
class JobPermission:
    inherited: Optional[bool] = None
    inherited_from_object: Optional['List[str]'] = None
    permission_level: Optional['JobPermissionLevel'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.inherited is not None: body['inherited'] = self.inherited
        if self.inherited_from_object: body['inherited_from_object'] = [v for v in self.inherited_from_object]
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobPermission':
        return cls(inherited=d.get('inherited', None),
                   inherited_from_object=d.get('inherited_from_object', None),
                   permission_level=_enum(d, 'permission_level', JobPermissionLevel))


class JobPermissionLevel(Enum):
    """Permission level"""

    CAN_MANAGE = 'CAN_MANAGE'
    CAN_MANAGE_RUN = 'CAN_MANAGE_RUN'
    CAN_VIEW = 'CAN_VIEW'
    IS_OWNER = 'IS_OWNER'


@dataclass
class JobPermissions:
    access_control_list: Optional['List[JobAccessControlResponse]'] = None
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
    def from_dict(cls, d: Dict[str, any]) -> 'JobPermissions':
        return cls(access_control_list=_repeated(d, 'access_control_list', JobAccessControlResponse),
                   object_id=d.get('object_id', None),
                   object_type=d.get('object_type', None))


@dataclass
class JobPermissionsDescription:
    description: Optional[str] = None
    permission_level: Optional['JobPermissionLevel'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobPermissionsDescription':
        return cls(description=d.get('description', None),
                   permission_level=_enum(d, 'permission_level', JobPermissionLevel))


@dataclass
class JobPermissionsRequest:
    access_control_list: Optional['List[JobAccessControlRequest]'] = None
    job_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.job_id is not None: body['job_id'] = self.job_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobPermissionsRequest':
        return cls(access_control_list=_repeated(d, 'access_control_list', JobAccessControlRequest),
                   job_id=d.get('job_id', None))


@dataclass
class JobRunAs:
    """Write-only setting, available only in Create/Update/Reset and Submit calls. Specifies the user
    or service principal that the job runs as. If not specified, the job runs as the user who
    created the job.
    
    Only `user_name` or `service_principal_name` can be specified. If both are specified, an error
    is thrown."""

    service_principal_name: Optional[str] = None
    user_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobRunAs':
        return cls(service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class JobSettings:
    compute: Optional['List[JobCompute]'] = None
    continuous: Optional['Continuous'] = None
    deployment: Optional['JobDeployment'] = None
    email_notifications: Optional['JobEmailNotifications'] = None
    format: Optional['Format'] = None
    git_source: Optional['GitSource'] = None
    health: Optional['JobsHealthRules'] = None
    job_clusters: Optional['List[JobCluster]'] = None
    max_concurrent_runs: Optional[int] = None
    name: Optional[str] = None
    notification_settings: Optional['JobNotificationSettings'] = None
    parameters: Optional['List[JobParameterDefinition]'] = None
    queue: Optional['QueueSettings'] = None
    run_as: Optional['JobRunAs'] = None
    schedule: Optional['CronSchedule'] = None
    tags: Optional['Dict[str,str]'] = None
    tasks: Optional['List[Task]'] = None
    timeout_seconds: Optional[int] = None
    trigger: Optional['TriggerSettings'] = None
    ui_state: Optional['JobSettingsUiState'] = None
    webhook_notifications: Optional['WebhookNotifications'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.compute: body['compute'] = [v.as_dict() for v in self.compute]
        if self.continuous: body['continuous'] = self.continuous.as_dict()
        if self.deployment: body['deployment'] = self.deployment.as_dict()
        if self.email_notifications: body['email_notifications'] = self.email_notifications.as_dict()
        if self.format is not None: body['format'] = self.format.value
        if self.git_source: body['git_source'] = self.git_source.as_dict()
        if self.health: body['health'] = self.health.as_dict()
        if self.job_clusters: body['job_clusters'] = [v.as_dict() for v in self.job_clusters]
        if self.max_concurrent_runs is not None: body['max_concurrent_runs'] = self.max_concurrent_runs
        if self.name is not None: body['name'] = self.name
        if self.notification_settings: body['notification_settings'] = self.notification_settings.as_dict()
        if self.parameters: body['parameters'] = [v.as_dict() for v in self.parameters]
        if self.queue: body['queue'] = self.queue.as_dict()
        if self.run_as: body['run_as'] = self.run_as.as_dict()
        if self.schedule: body['schedule'] = self.schedule.as_dict()
        if self.tags: body['tags'] = self.tags
        if self.tasks: body['tasks'] = [v.as_dict() for v in self.tasks]
        if self.timeout_seconds is not None: body['timeout_seconds'] = self.timeout_seconds
        if self.trigger: body['trigger'] = self.trigger.as_dict()
        if self.ui_state is not None: body['ui_state'] = self.ui_state.value
        if self.webhook_notifications: body['webhook_notifications'] = self.webhook_notifications.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobSettings':
        return cls(compute=_repeated(d, 'compute', JobCompute),
                   continuous=_from_dict(d, 'continuous', Continuous),
                   deployment=_from_dict(d, 'deployment', JobDeployment),
                   email_notifications=_from_dict(d, 'email_notifications', JobEmailNotifications),
                   format=_enum(d, 'format', Format),
                   git_source=_from_dict(d, 'git_source', GitSource),
                   health=_from_dict(d, 'health', JobsHealthRules),
                   job_clusters=_repeated(d, 'job_clusters', JobCluster),
                   max_concurrent_runs=d.get('max_concurrent_runs', None),
                   name=d.get('name', None),
                   notification_settings=_from_dict(d, 'notification_settings', JobNotificationSettings),
                   parameters=_repeated(d, 'parameters', JobParameterDefinition),
                   queue=_from_dict(d, 'queue', QueueSettings),
                   run_as=_from_dict(d, 'run_as', JobRunAs),
                   schedule=_from_dict(d, 'schedule', CronSchedule),
                   tags=d.get('tags', None),
                   tasks=_repeated(d, 'tasks', Task),
                   timeout_seconds=d.get('timeout_seconds', None),
                   trigger=_from_dict(d, 'trigger', TriggerSettings),
                   ui_state=_enum(d, 'ui_state', JobSettingsUiState),
                   webhook_notifications=_from_dict(d, 'webhook_notifications', WebhookNotifications))


class JobSettingsUiState(Enum):
    """State of the job in UI.
    
    * `LOCKED`: The job is in a locked state and cannot be modified. * `EDITABLE`: The job is in an
    editable state and can be modified."""

    EDITABLE = 'EDITABLE'
    LOCKED = 'LOCKED'


@dataclass
class JobSource:
    """The source of the job specification in the remote repository when the job is source controlled."""

    job_config_path: str
    import_from_git_branch: str
    dirty_state: Optional['JobSourceDirtyState'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.dirty_state is not None: body['dirty_state'] = self.dirty_state.value
        if self.import_from_git_branch is not None:
            body['import_from_git_branch'] = self.import_from_git_branch
        if self.job_config_path is not None: body['job_config_path'] = self.job_config_path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobSource':
        return cls(dirty_state=_enum(d, 'dirty_state', JobSourceDirtyState),
                   import_from_git_branch=d.get('import_from_git_branch', None),
                   job_config_path=d.get('job_config_path', None))


class JobSourceDirtyState(Enum):
    """Dirty state indicates the job is not fully synced with the job specification in the remote
    repository.
    
    Possible values are: * `NOT_SYNCED`: The job is not yet synced with the remote job
    specification. Import the remote job specification from UI to make the job fully synced. *
    `DISCONNECTED`: The job is temporary disconnected from the remote job specification and is
    allowed for live edit. Import the remote job specification again from UI to make the job fully
    synced."""

    DISCONNECTED = 'DISCONNECTED'
    NOT_SYNCED = 'NOT_SYNCED'


class JobsHealthMetric(Enum):
    """Specifies the health metric that is being evaluated for a particular health rule."""

    RUN_DURATION_SECONDS = 'RUN_DURATION_SECONDS'


class JobsHealthOperator(Enum):
    """Specifies the operator used to compare the health metric value with the specified threshold."""

    GREATER_THAN = 'GREATER_THAN'


@dataclass
class JobsHealthRule:
    metric: Optional['JobsHealthMetric'] = None
    op: Optional['JobsHealthOperator'] = None
    value: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.metric is not None: body['metric'] = self.metric.value
        if self.op is not None: body['op'] = self.op.value
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobsHealthRule':
        return cls(metric=_enum(d, 'metric', JobsHealthMetric),
                   op=_enum(d, 'op', JobsHealthOperator),
                   value=d.get('value', None))


@dataclass
class JobsHealthRules:
    """An optional set of health rules that can be defined for this job."""

    rules: Optional['List[JobsHealthRule]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.rules: body['rules'] = [v.as_dict() for v in self.rules]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobsHealthRules':
        return cls(rules=_repeated(d, 'rules', JobsHealthRule))


@dataclass
class ListJobsResponse:
    has_more: Optional[bool] = None
    jobs: Optional['List[BaseJob]'] = None
    next_page_token: Optional[str] = None
    prev_page_token: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.has_more is not None: body['has_more'] = self.has_more
        if self.jobs: body['jobs'] = [v.as_dict() for v in self.jobs]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.prev_page_token is not None: body['prev_page_token'] = self.prev_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListJobsResponse':
        return cls(has_more=d.get('has_more', None),
                   jobs=_repeated(d, 'jobs', BaseJob),
                   next_page_token=d.get('next_page_token', None),
                   prev_page_token=d.get('prev_page_token', None))


@dataclass
class ListRunsResponse:
    has_more: Optional[bool] = None
    next_page_token: Optional[str] = None
    prev_page_token: Optional[str] = None
    runs: Optional['List[BaseRun]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.has_more is not None: body['has_more'] = self.has_more
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.prev_page_token is not None: body['prev_page_token'] = self.prev_page_token
        if self.runs: body['runs'] = [v.as_dict() for v in self.runs]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListRunsResponse':
        return cls(has_more=d.get('has_more', None),
                   next_page_token=d.get('next_page_token', None),
                   prev_page_token=d.get('prev_page_token', None),
                   runs=_repeated(d, 'runs', BaseRun))


class ListRunsRunType(Enum):
    """* `JOB_RUN`: Normal job run. A run created with :method:jobs/runNow. * `WORKFLOW_RUN`: Workflow
    run. A run created with [dbutils.notebook.run]. * `SUBMIT_RUN`: Submit run. A run created with
    :method:jobs/submit.
    
    [dbutils.notebook.run]: https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-workflow"""

    JOB_RUN = 'JOB_RUN'
    SUBMIT_RUN = 'SUBMIT_RUN'
    WORKFLOW_RUN = 'WORKFLOW_RUN'


@dataclass
class NotebookOutput:
    result: Optional[str] = None
    truncated: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.result is not None: body['result'] = self.result
        if self.truncated is not None: body['truncated'] = self.truncated
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NotebookOutput':
        return cls(result=d.get('result', None), truncated=d.get('truncated', None))


@dataclass
class NotebookTask:
    notebook_path: str
    base_parameters: Optional['Dict[str,str]'] = None
    source: Optional['Source'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.base_parameters: body['base_parameters'] = self.base_parameters
        if self.notebook_path is not None: body['notebook_path'] = self.notebook_path
        if self.source is not None: body['source'] = self.source.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NotebookTask':
        return cls(base_parameters=d.get('base_parameters', None),
                   notebook_path=d.get('notebook_path', None),
                   source=_enum(d, 'source', Source))


ParamPairs = Dict[str, str]


class PauseStatus(Enum):

    PAUSED = 'PAUSED'
    UNPAUSED = 'UNPAUSED'


@dataclass
class PipelineParams:
    full_refresh: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.full_refresh is not None: body['full_refresh'] = self.full_refresh
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineParams':
        return cls(full_refresh=d.get('full_refresh', None))


@dataclass
class PipelineTask:
    full_refresh: Optional[bool] = None
    pipeline_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.full_refresh is not None: body['full_refresh'] = self.full_refresh
        if self.pipeline_id is not None: body['pipeline_id'] = self.pipeline_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineTask':
        return cls(full_refresh=d.get('full_refresh', None), pipeline_id=d.get('pipeline_id', None))


@dataclass
class PythonWheelTask:
    entry_point: Optional[str] = None
    named_parameters: Optional['Dict[str,str]'] = None
    package_name: Optional[str] = None
    parameters: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.entry_point is not None: body['entry_point'] = self.entry_point
        if self.named_parameters: body['named_parameters'] = self.named_parameters
        if self.package_name is not None: body['package_name'] = self.package_name
        if self.parameters: body['parameters'] = [v for v in self.parameters]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PythonWheelTask':
        return cls(entry_point=d.get('entry_point', None),
                   named_parameters=d.get('named_parameters', None),
                   package_name=d.get('package_name', None),
                   parameters=d.get('parameters', None))


@dataclass
class QueueSettings:
    enabled: bool

    def as_dict(self) -> dict:
        body = {}
        if self.enabled is not None: body['enabled'] = self.enabled
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueueSettings':
        return cls(enabled=d.get('enabled', None))


@dataclass
class RepairHistoryItem:
    end_time: Optional[int] = None
    id: Optional[int] = None
    start_time: Optional[int] = None
    state: Optional['RunState'] = None
    task_run_ids: Optional['List[int]'] = None
    type: Optional['RepairHistoryItemType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.end_time is not None: body['end_time'] = self.end_time
        if self.id is not None: body['id'] = self.id
        if self.start_time is not None: body['start_time'] = self.start_time
        if self.state: body['state'] = self.state.as_dict()
        if self.task_run_ids: body['task_run_ids'] = [v for v in self.task_run_ids]
        if self.type is not None: body['type'] = self.type.value
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
    dbt_commands: Optional['List[str]'] = None
    jar_params: Optional['List[str]'] = None
    job_parameters: Optional['Dict[str,str]'] = None
    latest_repair_id: Optional[int] = None
    notebook_params: Optional['Dict[str,str]'] = None
    pipeline_params: Optional['PipelineParams'] = None
    python_named_params: Optional['Dict[str,str]'] = None
    python_params: Optional['List[str]'] = None
    rerun_all_failed_tasks: Optional[bool] = None
    rerun_dependent_tasks: Optional[bool] = None
    rerun_tasks: Optional['List[str]'] = None
    spark_submit_params: Optional['List[str]'] = None
    sql_params: Optional['Dict[str,str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.dbt_commands: body['dbt_commands'] = [v for v in self.dbt_commands]
        if self.jar_params: body['jar_params'] = [v for v in self.jar_params]
        if self.job_parameters: body['job_parameters'] = self.job_parameters
        if self.latest_repair_id is not None: body['latest_repair_id'] = self.latest_repair_id
        if self.notebook_params: body['notebook_params'] = self.notebook_params
        if self.pipeline_params: body['pipeline_params'] = self.pipeline_params.as_dict()
        if self.python_named_params: body['python_named_params'] = self.python_named_params
        if self.python_params: body['python_params'] = [v for v in self.python_params]
        if self.rerun_all_failed_tasks is not None:
            body['rerun_all_failed_tasks'] = self.rerun_all_failed_tasks
        if self.rerun_dependent_tasks is not None: body['rerun_dependent_tasks'] = self.rerun_dependent_tasks
        if self.rerun_tasks: body['rerun_tasks'] = [v for v in self.rerun_tasks]
        if self.run_id is not None: body['run_id'] = self.run_id
        if self.spark_submit_params: body['spark_submit_params'] = [v for v in self.spark_submit_params]
        if self.sql_params: body['sql_params'] = self.sql_params
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RepairRun':
        return cls(dbt_commands=d.get('dbt_commands', None),
                   jar_params=d.get('jar_params', None),
                   job_parameters=d.get('job_parameters', None),
                   latest_repair_id=d.get('latest_repair_id', None),
                   notebook_params=d.get('notebook_params', None),
                   pipeline_params=_from_dict(d, 'pipeline_params', PipelineParams),
                   python_named_params=d.get('python_named_params', None),
                   python_params=d.get('python_params', None),
                   rerun_all_failed_tasks=d.get('rerun_all_failed_tasks', None),
                   rerun_dependent_tasks=d.get('rerun_dependent_tasks', None),
                   rerun_tasks=d.get('rerun_tasks', None),
                   run_id=d.get('run_id', None),
                   spark_submit_params=d.get('spark_submit_params', None),
                   sql_params=d.get('sql_params', None))


@dataclass
class RepairRunResponse:
    repair_id: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.repair_id is not None: body['repair_id'] = self.repair_id
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
        if self.job_id is not None: body['job_id'] = self.job_id
        if self.new_settings: body['new_settings'] = self.new_settings.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResetJob':
        return cls(job_id=d.get('job_id', None), new_settings=_from_dict(d, 'new_settings', JobSettings))


@dataclass
class ResolvedConditionTaskValues:
    left: Optional[str] = None
    right: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.left is not None: body['left'] = self.left
        if self.right is not None: body['right'] = self.right
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResolvedConditionTaskValues':
        return cls(left=d.get('left', None), right=d.get('right', None))


@dataclass
class ResolvedDbtTaskValues:
    commands: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.commands: body['commands'] = [v for v in self.commands]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResolvedDbtTaskValues':
        return cls(commands=d.get('commands', None))


@dataclass
class ResolvedNotebookTaskValues:
    base_parameters: Optional['Dict[str,str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.base_parameters: body['base_parameters'] = self.base_parameters
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResolvedNotebookTaskValues':
        return cls(base_parameters=d.get('base_parameters', None))


@dataclass
class ResolvedParamPairValues:
    parameters: Optional['Dict[str,str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.parameters: body['parameters'] = self.parameters
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResolvedParamPairValues':
        return cls(parameters=d.get('parameters', None))


@dataclass
class ResolvedPythonWheelTaskValues:
    named_parameters: Optional['Dict[str,str]'] = None
    parameters: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.named_parameters: body['named_parameters'] = self.named_parameters
        if self.parameters: body['parameters'] = [v for v in self.parameters]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResolvedPythonWheelTaskValues':
        return cls(named_parameters=d.get('named_parameters', None), parameters=d.get('parameters', None))


@dataclass
class ResolvedRunJobTaskValues:
    named_parameters: Optional['Dict[str,str]'] = None
    parameters: Optional['Dict[str,str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.named_parameters: body['named_parameters'] = self.named_parameters
        if self.parameters: body['parameters'] = self.parameters
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResolvedRunJobTaskValues':
        return cls(named_parameters=d.get('named_parameters', None), parameters=d.get('parameters', None))


@dataclass
class ResolvedStringParamsValues:
    parameters: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.parameters: body['parameters'] = [v for v in self.parameters]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResolvedStringParamsValues':
        return cls(parameters=d.get('parameters', None))


@dataclass
class ResolvedValues:
    condition_task: Optional['ResolvedConditionTaskValues'] = None
    dbt_task: Optional['ResolvedDbtTaskValues'] = None
    notebook_task: Optional['ResolvedNotebookTaskValues'] = None
    python_wheel_task: Optional['ResolvedPythonWheelTaskValues'] = None
    run_job_task: Optional['ResolvedRunJobTaskValues'] = None
    simulation_task: Optional['ResolvedParamPairValues'] = None
    spark_jar_task: Optional['ResolvedStringParamsValues'] = None
    spark_python_task: Optional['ResolvedStringParamsValues'] = None
    spark_submit_task: Optional['ResolvedStringParamsValues'] = None
    sql_task: Optional['ResolvedParamPairValues'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.condition_task: body['condition_task'] = self.condition_task.as_dict()
        if self.dbt_task: body['dbt_task'] = self.dbt_task.as_dict()
        if self.notebook_task: body['notebook_task'] = self.notebook_task.as_dict()
        if self.python_wheel_task: body['python_wheel_task'] = self.python_wheel_task.as_dict()
        if self.run_job_task: body['run_job_task'] = self.run_job_task.as_dict()
        if self.simulation_task: body['simulation_task'] = self.simulation_task.as_dict()
        if self.spark_jar_task: body['spark_jar_task'] = self.spark_jar_task.as_dict()
        if self.spark_python_task: body['spark_python_task'] = self.spark_python_task.as_dict()
        if self.spark_submit_task: body['spark_submit_task'] = self.spark_submit_task.as_dict()
        if self.sql_task: body['sql_task'] = self.sql_task.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResolvedValues':
        return cls(condition_task=_from_dict(d, 'condition_task', ResolvedConditionTaskValues),
                   dbt_task=_from_dict(d, 'dbt_task', ResolvedDbtTaskValues),
                   notebook_task=_from_dict(d, 'notebook_task', ResolvedNotebookTaskValues),
                   python_wheel_task=_from_dict(d, 'python_wheel_task', ResolvedPythonWheelTaskValues),
                   run_job_task=_from_dict(d, 'run_job_task', ResolvedRunJobTaskValues),
                   simulation_task=_from_dict(d, 'simulation_task', ResolvedParamPairValues),
                   spark_jar_task=_from_dict(d, 'spark_jar_task', ResolvedStringParamsValues),
                   spark_python_task=_from_dict(d, 'spark_python_task', ResolvedStringParamsValues),
                   spark_submit_task=_from_dict(d, 'spark_submit_task', ResolvedStringParamsValues),
                   sql_task=_from_dict(d, 'sql_task', ResolvedParamPairValues))


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
    job_parameters: Optional['List[JobParameter]'] = None
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
    trigger_info: Optional['TriggerInfo'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.attempt_number is not None: body['attempt_number'] = self.attempt_number
        if self.cleanup_duration is not None: body['cleanup_duration'] = self.cleanup_duration
        if self.cluster_instance: body['cluster_instance'] = self.cluster_instance.as_dict()
        if self.cluster_spec: body['cluster_spec'] = self.cluster_spec.as_dict()
        if self.continuous: body['continuous'] = self.continuous.as_dict()
        if self.creator_user_name is not None: body['creator_user_name'] = self.creator_user_name
        if self.end_time is not None: body['end_time'] = self.end_time
        if self.execution_duration is not None: body['execution_duration'] = self.execution_duration
        if self.git_source: body['git_source'] = self.git_source.as_dict()
        if self.job_clusters: body['job_clusters'] = [v.as_dict() for v in self.job_clusters]
        if self.job_id is not None: body['job_id'] = self.job_id
        if self.job_parameters: body['job_parameters'] = [v.as_dict() for v in self.job_parameters]
        if self.number_in_job is not None: body['number_in_job'] = self.number_in_job
        if self.original_attempt_run_id is not None:
            body['original_attempt_run_id'] = self.original_attempt_run_id
        if self.overriding_parameters: body['overriding_parameters'] = self.overriding_parameters.as_dict()
        if self.repair_history: body['repair_history'] = [v.as_dict() for v in self.repair_history]
        if self.run_duration is not None: body['run_duration'] = self.run_duration
        if self.run_id is not None: body['run_id'] = self.run_id
        if self.run_name is not None: body['run_name'] = self.run_name
        if self.run_page_url is not None: body['run_page_url'] = self.run_page_url
        if self.run_type is not None: body['run_type'] = self.run_type.value
        if self.schedule: body['schedule'] = self.schedule.as_dict()
        if self.setup_duration is not None: body['setup_duration'] = self.setup_duration
        if self.start_time is not None: body['start_time'] = self.start_time
        if self.state: body['state'] = self.state.as_dict()
        if self.tasks: body['tasks'] = [v.as_dict() for v in self.tasks]
        if self.trigger is not None: body['trigger'] = self.trigger.value
        if self.trigger_info: body['trigger_info'] = self.trigger_info.as_dict()
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
                   job_parameters=_repeated(d, 'job_parameters', JobParameter),
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
                   trigger=_enum(d, 'trigger', TriggerType),
                   trigger_info=_from_dict(d, 'trigger_info', TriggerInfo))


@dataclass
class RunConditionTask:
    left: str
    right: str
    op: 'RunConditionTaskOp'
    outcome: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.left is not None: body['left'] = self.left
        if self.op is not None: body['op'] = self.op.value
        if self.outcome is not None: body['outcome'] = self.outcome
        if self.right is not None: body['right'] = self.right
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunConditionTask':
        return cls(left=d.get('left', None),
                   op=_enum(d, 'op', RunConditionTaskOp),
                   outcome=d.get('outcome', None),
                   right=d.get('right', None))


class RunConditionTaskOp(Enum):
    """The condtion task operator."""

    EQUAL_TO = 'EQUAL_TO'
    GREATER_THAN = 'GREATER_THAN'
    GREATER_THAN_OR_EQUAL = 'GREATER_THAN_OR_EQUAL'
    LESS_THAN = 'LESS_THAN'
    LESS_THAN_OR_EQUAL = 'LESS_THAN_OR_EQUAL'
    NOT_EQUAL = 'NOT_EQUAL'


class RunIf(Enum):
    """An optional value indicating the condition that determines whether the task should be run once
    its dependencies have been completed. When omitted, defaults to `ALL_SUCCESS`.
    
    Possible values are: * `ALL_SUCCESS`: All dependencies have executed and succeeded *
    `AT_LEAST_ONE_SUCCESS`: At least one dependency has succeeded * `NONE_FAILED`: None of the
    dependencies have failed and at least one was executed * `ALL_DONE`: All dependencies have been
    completed * `AT_LEAST_ONE_FAILED`: At least one dependency failed * `ALL_FAILED`: ALl
    dependencies have failed"""

    ALL_DONE = 'ALL_DONE'
    ALL_FAILED = 'ALL_FAILED'
    ALL_SUCCESS = 'ALL_SUCCESS'
    AT_LEAST_ONE_FAILED = 'AT_LEAST_ONE_FAILED'
    AT_LEAST_ONE_SUCCESS = 'AT_LEAST_ONE_SUCCESS'
    NONE_FAILED = 'NONE_FAILED'


@dataclass
class RunJobOutput:
    run_id: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.run_id is not None: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunJobOutput':
        return cls(run_id=d.get('run_id', None))


@dataclass
class RunJobTask:
    job_id: int
    job_parameters: Optional[Any] = None

    def as_dict(self) -> dict:
        body = {}
        if self.job_id is not None: body['job_id'] = self.job_id
        if self.job_parameters: body['job_parameters'] = self.job_parameters
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunJobTask':
        return cls(job_id=d.get('job_id', None), job_parameters=d.get('job_parameters', None))


class RunLifeCycleState(Enum):
    """A value indicating the run's lifecycle state. The possible values are: * `QUEUED`: The run is
    queued. * `PENDING`: The run is waiting to be executed while the cluster and execution context
    are being prepared. * `RUNNING`: The task of this run is being executed. * `TERMINATING`: The
    task of this run has completed, and the cluster and execution context are being cleaned up. *
    `TERMINATED`: The task of this run has completed, and the cluster and execution context have
    been cleaned up. This state is terminal. * `SKIPPED`: This run was aborted because a previous
    run of the same job was already active. This state is terminal. * `INTERNAL_ERROR`: An
    exceptional state that indicates a failure in the Jobs service, such as network failure over a
    long period. If a run on a new cluster ends in the `INTERNAL_ERROR` state, the Jobs service
    terminates the cluster as soon as possible. This state is terminal. * `BLOCKED`: The run is
    blocked on an upstream dependency. * `WAITING_FOR_RETRY`: The run is waiting for a retry."""

    BLOCKED = 'BLOCKED'
    INTERNAL_ERROR = 'INTERNAL_ERROR'
    PENDING = 'PENDING'
    QUEUED = 'QUEUED'
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
    job_parameters: Optional['Dict[str,str]'] = None
    notebook_params: Optional['Dict[str,str]'] = None
    pipeline_params: Optional['PipelineParams'] = None
    python_named_params: Optional['Dict[str,str]'] = None
    python_params: Optional['List[str]'] = None
    queue: Optional['QueueSettings'] = None
    spark_submit_params: Optional['List[str]'] = None
    sql_params: Optional['Dict[str,str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.dbt_commands: body['dbt_commands'] = [v for v in self.dbt_commands]
        if self.idempotency_token is not None: body['idempotency_token'] = self.idempotency_token
        if self.jar_params: body['jar_params'] = [v for v in self.jar_params]
        if self.job_id is not None: body['job_id'] = self.job_id
        if self.job_parameters: body['job_parameters'] = self.job_parameters
        if self.notebook_params: body['notebook_params'] = self.notebook_params
        if self.pipeline_params: body['pipeline_params'] = self.pipeline_params.as_dict()
        if self.python_named_params: body['python_named_params'] = self.python_named_params
        if self.python_params: body['python_params'] = [v for v in self.python_params]
        if self.queue: body['queue'] = self.queue.as_dict()
        if self.spark_submit_params: body['spark_submit_params'] = [v for v in self.spark_submit_params]
        if self.sql_params: body['sql_params'] = self.sql_params
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunNow':
        return cls(dbt_commands=d.get('dbt_commands', None),
                   idempotency_token=d.get('idempotency_token', None),
                   jar_params=d.get('jar_params', None),
                   job_id=d.get('job_id', None),
                   job_parameters=d.get('job_parameters', None),
                   notebook_params=d.get('notebook_params', None),
                   pipeline_params=_from_dict(d, 'pipeline_params', PipelineParams),
                   python_named_params=d.get('python_named_params', None),
                   python_params=d.get('python_params', None),
                   queue=_from_dict(d, 'queue', QueueSettings),
                   spark_submit_params=d.get('spark_submit_params', None),
                   sql_params=d.get('sql_params', None))


@dataclass
class RunNowResponse:
    number_in_job: Optional[int] = None
    run_id: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.number_in_job is not None: body['number_in_job'] = self.number_in_job
        if self.run_id is not None: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunNowResponse':
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
    run_job_output: Optional['RunJobOutput'] = None
    sql_output: Optional['SqlOutput'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.dbt_output: body['dbt_output'] = self.dbt_output.as_dict()
        if self.error is not None: body['error'] = self.error
        if self.error_trace is not None: body['error_trace'] = self.error_trace
        if self.logs is not None: body['logs'] = self.logs
        if self.logs_truncated is not None: body['logs_truncated'] = self.logs_truncated
        if self.metadata: body['metadata'] = self.metadata.as_dict()
        if self.notebook_output: body['notebook_output'] = self.notebook_output.as_dict()
        if self.run_job_output: body['run_job_output'] = self.run_job_output.as_dict()
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
                   run_job_output=_from_dict(d, 'run_job_output', RunJobOutput),
                   sql_output=_from_dict(d, 'sql_output', SqlOutput))


@dataclass
class RunParameters:
    dbt_commands: Optional['List[str]'] = None
    jar_params: Optional['List[str]'] = None
    job_parameters: Optional['Dict[str,str]'] = None
    notebook_params: Optional['Dict[str,str]'] = None
    pipeline_params: Optional['PipelineParams'] = None
    python_named_params: Optional['Dict[str,str]'] = None
    python_params: Optional['List[str]'] = None
    spark_submit_params: Optional['List[str]'] = None
    sql_params: Optional['Dict[str,str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.dbt_commands: body['dbt_commands'] = [v for v in self.dbt_commands]
        if self.jar_params: body['jar_params'] = [v for v in self.jar_params]
        if self.job_parameters: body['job_parameters'] = self.job_parameters
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
                   job_parameters=d.get('job_parameters', None),
                   notebook_params=d.get('notebook_params', None),
                   pipeline_params=_from_dict(d, 'pipeline_params', PipelineParams),
                   python_named_params=d.get('python_named_params', None),
                   python_params=d.get('python_params', None),
                   spark_submit_params=d.get('spark_submit_params', None),
                   sql_params=d.get('sql_params', None))


class RunResultState(Enum):
    """A value indicating the run's result. The possible values are: * `SUCCESS`: The task completed
    successfully. * `FAILED`: The task completed with an error. * `TIMEDOUT`: The run was stopped
    after reaching the timeout. * `CANCELED`: The run was canceled at user request. *
    `MAXIMUM_CONCURRENT_RUNS_REACHED`: The run was skipped because the maximum concurrent runs were
    reached. * `EXCLUDED`: The run was skipped because the necessary conditions were not met. *
    `SUCCESS_WITH_FAILURES`: The job run completed successfully with some failures; leaf tasks were
    successful. * `UPSTREAM_FAILED`: The run was skipped because of an upstream failure. *
    `UPSTREAM_CANCELED`: The run was skipped because an upstream task was canceled."""

    CANCELED = 'CANCELED'
    EXCLUDED = 'EXCLUDED'
    FAILED = 'FAILED'
    MAXIMUM_CONCURRENT_RUNS_REACHED = 'MAXIMUM_CONCURRENT_RUNS_REACHED'
    SUCCESS = 'SUCCESS'
    SUCCESS_WITH_FAILURES = 'SUCCESS_WITH_FAILURES'
    TIMEDOUT = 'TIMEDOUT'
    UPSTREAM_CANCELED = 'UPSTREAM_CANCELED'
    UPSTREAM_FAILED = 'UPSTREAM_FAILED'


@dataclass
class RunState:
    """The current state of the run."""

    life_cycle_state: Optional['RunLifeCycleState'] = None
    queue_reason: Optional[str] = None
    result_state: Optional['RunResultState'] = None
    state_message: Optional[str] = None
    user_cancelled_or_timedout: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.life_cycle_state is not None: body['life_cycle_state'] = self.life_cycle_state.value
        if self.queue_reason is not None: body['queue_reason'] = self.queue_reason
        if self.result_state is not None: body['result_state'] = self.result_state.value
        if self.state_message is not None: body['state_message'] = self.state_message
        if self.user_cancelled_or_timedout is not None:
            body['user_cancelled_or_timedout'] = self.user_cancelled_or_timedout
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunState':
        return cls(life_cycle_state=_enum(d, 'life_cycle_state', RunLifeCycleState),
                   queue_reason=d.get('queue_reason', None),
                   result_state=_enum(d, 'result_state', RunResultState),
                   state_message=d.get('state_message', None),
                   user_cancelled_or_timedout=d.get('user_cancelled_or_timedout', None))


@dataclass
class RunTask:
    attempt_number: Optional[int] = None
    cleanup_duration: Optional[int] = None
    cluster_instance: Optional['ClusterInstance'] = None
    condition_task: Optional['RunConditionTask'] = None
    dbt_task: Optional['DbtTask'] = None
    depends_on: Optional['List[TaskDependency]'] = None
    description: Optional[str] = None
    end_time: Optional[int] = None
    execution_duration: Optional[int] = None
    existing_cluster_id: Optional[str] = None
    git_source: Optional['GitSource'] = None
    libraries: Optional['List[compute.Library]'] = None
    new_cluster: Optional['compute.ClusterSpec'] = None
    notebook_task: Optional['NotebookTask'] = None
    pipeline_task: Optional['PipelineTask'] = None
    python_wheel_task: Optional['PythonWheelTask'] = None
    queue_duration: Optional[int] = None
    resolved_values: Optional['ResolvedValues'] = None
    run_id: Optional[int] = None
    run_if: Optional['RunIf'] = None
    run_job_task: Optional['RunJobTask'] = None
    setup_duration: Optional[int] = None
    spark_jar_task: Optional['SparkJarTask'] = None
    spark_python_task: Optional['SparkPythonTask'] = None
    spark_submit_task: Optional['SparkSubmitTask'] = None
    sql_task: Optional['SqlTask'] = None
    start_time: Optional[int] = None
    state: Optional['RunState'] = None
    task_key: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.attempt_number is not None: body['attempt_number'] = self.attempt_number
        if self.cleanup_duration is not None: body['cleanup_duration'] = self.cleanup_duration
        if self.cluster_instance: body['cluster_instance'] = self.cluster_instance.as_dict()
        if self.condition_task: body['condition_task'] = self.condition_task.as_dict()
        if self.dbt_task: body['dbt_task'] = self.dbt_task.as_dict()
        if self.depends_on: body['depends_on'] = [v.as_dict() for v in self.depends_on]
        if self.description is not None: body['description'] = self.description
        if self.end_time is not None: body['end_time'] = self.end_time
        if self.execution_duration is not None: body['execution_duration'] = self.execution_duration
        if self.existing_cluster_id is not None: body['existing_cluster_id'] = self.existing_cluster_id
        if self.git_source: body['git_source'] = self.git_source.as_dict()
        if self.libraries: body['libraries'] = [v.as_dict() for v in self.libraries]
        if self.new_cluster: body['new_cluster'] = self.new_cluster.as_dict()
        if self.notebook_task: body['notebook_task'] = self.notebook_task.as_dict()
        if self.pipeline_task: body['pipeline_task'] = self.pipeline_task.as_dict()
        if self.python_wheel_task: body['python_wheel_task'] = self.python_wheel_task.as_dict()
        if self.queue_duration is not None: body['queue_duration'] = self.queue_duration
        if self.resolved_values: body['resolved_values'] = self.resolved_values.as_dict()
        if self.run_id is not None: body['run_id'] = self.run_id
        if self.run_if is not None: body['run_if'] = self.run_if.value
        if self.run_job_task: body['run_job_task'] = self.run_job_task.as_dict()
        if self.setup_duration is not None: body['setup_duration'] = self.setup_duration
        if self.spark_jar_task: body['spark_jar_task'] = self.spark_jar_task.as_dict()
        if self.spark_python_task: body['spark_python_task'] = self.spark_python_task.as_dict()
        if self.spark_submit_task: body['spark_submit_task'] = self.spark_submit_task.as_dict()
        if self.sql_task: body['sql_task'] = self.sql_task.as_dict()
        if self.start_time is not None: body['start_time'] = self.start_time
        if self.state: body['state'] = self.state.as_dict()
        if self.task_key is not None: body['task_key'] = self.task_key
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunTask':
        return cls(attempt_number=d.get('attempt_number', None),
                   cleanup_duration=d.get('cleanup_duration', None),
                   cluster_instance=_from_dict(d, 'cluster_instance', ClusterInstance),
                   condition_task=_from_dict(d, 'condition_task', RunConditionTask),
                   dbt_task=_from_dict(d, 'dbt_task', DbtTask),
                   depends_on=_repeated(d, 'depends_on', TaskDependency),
                   description=d.get('description', None),
                   end_time=d.get('end_time', None),
                   execution_duration=d.get('execution_duration', None),
                   existing_cluster_id=d.get('existing_cluster_id', None),
                   git_source=_from_dict(d, 'git_source', GitSource),
                   libraries=_repeated(d, 'libraries', compute.Library),
                   new_cluster=_from_dict(d, 'new_cluster', compute.ClusterSpec),
                   notebook_task=_from_dict(d, 'notebook_task', NotebookTask),
                   pipeline_task=_from_dict(d, 'pipeline_task', PipelineTask),
                   python_wheel_task=_from_dict(d, 'python_wheel_task', PythonWheelTask),
                   queue_duration=d.get('queue_duration', None),
                   resolved_values=_from_dict(d, 'resolved_values', ResolvedValues),
                   run_id=d.get('run_id', None),
                   run_if=_enum(d, 'run_if', RunIf),
                   run_job_task=_from_dict(d, 'run_job_task', RunJobTask),
                   setup_duration=d.get('setup_duration', None),
                   spark_jar_task=_from_dict(d, 'spark_jar_task', SparkJarTask),
                   spark_python_task=_from_dict(d, 'spark_python_task', SparkPythonTask),
                   spark_submit_task=_from_dict(d, 'spark_submit_task', SparkSubmitTask),
                   sql_task=_from_dict(d, 'sql_task', SqlTask),
                   start_time=d.get('start_time', None),
                   state=_from_dict(d, 'state', RunState),
                   task_key=d.get('task_key', None))


class RunType(Enum):
    """* `JOB_RUN`: Normal job run. A run created with :method:jobs/runNow. * `WORKFLOW_RUN`: Workflow
    run. A run created with [dbutils.notebook.run]. * `SUBMIT_RUN`: Submit run. A run created with
    :method:jobs/submit.
    
    [dbutils.notebook.run]: https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-workflow"""

    JOB_RUN = 'JOB_RUN'
    SUBMIT_RUN = 'SUBMIT_RUN'
    WORKFLOW_RUN = 'WORKFLOW_RUN'


class Source(Enum):

    GIT = 'GIT'
    WORKSPACE = 'WORKSPACE'


@dataclass
class SparkJarTask:
    jar_uri: Optional[str] = None
    main_class_name: Optional[str] = None
    parameters: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.jar_uri is not None: body['jar_uri'] = self.jar_uri
        if self.main_class_name is not None: body['main_class_name'] = self.main_class_name
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
    parameters: Optional['List[str]'] = None
    source: Optional['Source'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.parameters: body['parameters'] = [v for v in self.parameters]
        if self.python_file is not None: body['python_file'] = self.python_file
        if self.source is not None: body['source'] = self.source.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparkPythonTask':
        return cls(parameters=d.get('parameters', None),
                   python_file=d.get('python_file', None),
                   source=_enum(d, 'source', Source))


@dataclass
class SparkSubmitTask:
    parameters: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.parameters: body['parameters'] = [v for v in self.parameters]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparkSubmitTask':
        return cls(parameters=d.get('parameters', None))


@dataclass
class SqlAlertOutput:
    alert_state: Optional['SqlAlertState'] = None
    output_link: Optional[str] = None
    query_text: Optional[str] = None
    sql_statements: Optional['List[SqlStatementOutput]'] = None
    warehouse_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.alert_state is not None: body['alert_state'] = self.alert_state.value
        if self.output_link is not None: body['output_link'] = self.output_link
        if self.query_text is not None: body['query_text'] = self.query_text
        if self.sql_statements: body['sql_statements'] = [v.as_dict() for v in self.sql_statements]
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
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
    warehouse_id: Optional[str] = None
    widgets: Optional['List[SqlDashboardWidgetOutput]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        if self.widgets: body['widgets'] = [v.as_dict() for v in self.widgets]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlDashboardOutput':
        return cls(warehouse_id=d.get('warehouse_id', None),
                   widgets=_repeated(d, 'widgets', SqlDashboardWidgetOutput))


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
        body = {}
        if self.end_time is not None: body['end_time'] = self.end_time
        if self.error: body['error'] = self.error.as_dict()
        if self.output_link is not None: body['output_link'] = self.output_link
        if self.start_time is not None: body['start_time'] = self.start_time
        if self.status is not None: body['status'] = self.status.value
        if self.widget_id is not None: body['widget_id'] = self.widget_id
        if self.widget_title is not None: body['widget_title'] = self.widget_title
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
    alert_output: Optional['SqlAlertOutput'] = None
    dashboard_output: Optional['SqlDashboardOutput'] = None
    query_output: Optional['SqlQueryOutput'] = None

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
    message: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.message is not None: body['message'] = self.message
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlOutputError':
        return cls(message=d.get('message', None))


@dataclass
class SqlQueryOutput:
    output_link: Optional[str] = None
    query_text: Optional[str] = None
    sql_statements: Optional['List[SqlStatementOutput]'] = None
    warehouse_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.output_link is not None: body['output_link'] = self.output_link
        if self.query_text is not None: body['query_text'] = self.query_text
        if self.sql_statements: body['sql_statements'] = [v.as_dict() for v in self.sql_statements]
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlQueryOutput':
        return cls(output_link=d.get('output_link', None),
                   query_text=d.get('query_text', None),
                   sql_statements=_repeated(d, 'sql_statements', SqlStatementOutput),
                   warehouse_id=d.get('warehouse_id', None))


@dataclass
class SqlStatementOutput:
    lookup_key: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.lookup_key is not None: body['lookup_key'] = self.lookup_key
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlStatementOutput':
        return cls(lookup_key=d.get('lookup_key', None))


@dataclass
class SqlTask:
    warehouse_id: str
    alert: Optional['SqlTaskAlert'] = None
    dashboard: Optional['SqlTaskDashboard'] = None
    file: Optional['SqlTaskFile'] = None
    parameters: Optional['Dict[str,str]'] = None
    query: Optional['SqlTaskQuery'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.alert: body['alert'] = self.alert.as_dict()
        if self.dashboard: body['dashboard'] = self.dashboard.as_dict()
        if self.file: body['file'] = self.file.as_dict()
        if self.parameters: body['parameters'] = self.parameters
        if self.query: body['query'] = self.query.as_dict()
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlTask':
        return cls(alert=_from_dict(d, 'alert', SqlTaskAlert),
                   dashboard=_from_dict(d, 'dashboard', SqlTaskDashboard),
                   file=_from_dict(d, 'file', SqlTaskFile),
                   parameters=d.get('parameters', None),
                   query=_from_dict(d, 'query', SqlTaskQuery),
                   warehouse_id=d.get('warehouse_id', None))


@dataclass
class SqlTaskAlert:
    alert_id: str
    pause_subscriptions: Optional[bool] = None
    subscriptions: Optional['List[SqlTaskSubscription]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.alert_id is not None: body['alert_id'] = self.alert_id
        if self.pause_subscriptions is not None: body['pause_subscriptions'] = self.pause_subscriptions
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
    custom_subject: Optional[str] = None
    pause_subscriptions: Optional[bool] = None
    subscriptions: Optional['List[SqlTaskSubscription]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.custom_subject is not None: body['custom_subject'] = self.custom_subject
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.pause_subscriptions is not None: body['pause_subscriptions'] = self.pause_subscriptions
        if self.subscriptions: body['subscriptions'] = [v.as_dict() for v in self.subscriptions]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlTaskDashboard':
        return cls(custom_subject=d.get('custom_subject', None),
                   dashboard_id=d.get('dashboard_id', None),
                   pause_subscriptions=d.get('pause_subscriptions', None),
                   subscriptions=_repeated(d, 'subscriptions', SqlTaskSubscription))


@dataclass
class SqlTaskFile:
    path: str

    def as_dict(self) -> dict:
        body = {}
        if self.path is not None: body['path'] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlTaskFile':
        return cls(path=d.get('path', None))


@dataclass
class SqlTaskQuery:
    query_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.query_id is not None: body['query_id'] = self.query_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlTaskQuery':
        return cls(query_id=d.get('query_id', None))


@dataclass
class SqlTaskSubscription:
    destination_id: Optional[str] = None
    user_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.destination_id is not None: body['destination_id'] = self.destination_id
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SqlTaskSubscription':
        return cls(destination_id=d.get('destination_id', None), user_name=d.get('user_name', None))


@dataclass
class SubmitRun:
    access_control_list: Optional['List[iam.AccessControlRequest]'] = None
    email_notifications: Optional['JobEmailNotifications'] = None
    git_source: Optional['GitSource'] = None
    health: Optional['JobsHealthRules'] = None
    idempotency_token: Optional[str] = None
    notification_settings: Optional['JobNotificationSettings'] = None
    queue: Optional['QueueSettings'] = None
    run_name: Optional[str] = None
    tasks: Optional['List[SubmitTask]'] = None
    timeout_seconds: Optional[int] = None
    webhook_notifications: Optional['WebhookNotifications'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.email_notifications: body['email_notifications'] = self.email_notifications.as_dict()
        if self.git_source: body['git_source'] = self.git_source.as_dict()
        if self.health: body['health'] = self.health.as_dict()
        if self.idempotency_token is not None: body['idempotency_token'] = self.idempotency_token
        if self.notification_settings: body['notification_settings'] = self.notification_settings.as_dict()
        if self.queue: body['queue'] = self.queue.as_dict()
        if self.run_name is not None: body['run_name'] = self.run_name
        if self.tasks: body['tasks'] = [v.as_dict() for v in self.tasks]
        if self.timeout_seconds is not None: body['timeout_seconds'] = self.timeout_seconds
        if self.webhook_notifications: body['webhook_notifications'] = self.webhook_notifications.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SubmitRun':
        return cls(access_control_list=_repeated(d, 'access_control_list', iam.AccessControlRequest),
                   email_notifications=_from_dict(d, 'email_notifications', JobEmailNotifications),
                   git_source=_from_dict(d, 'git_source', GitSource),
                   health=_from_dict(d, 'health', JobsHealthRules),
                   idempotency_token=d.get('idempotency_token', None),
                   notification_settings=_from_dict(d, 'notification_settings', JobNotificationSettings),
                   queue=_from_dict(d, 'queue', QueueSettings),
                   run_name=d.get('run_name', None),
                   tasks=_repeated(d, 'tasks', SubmitTask),
                   timeout_seconds=d.get('timeout_seconds', None),
                   webhook_notifications=_from_dict(d, 'webhook_notifications', WebhookNotifications))


@dataclass
class SubmitRunResponse:
    run_id: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.run_id is not None: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SubmitRunResponse':
        return cls(run_id=d.get('run_id', None))


@dataclass
class SubmitTask:
    task_key: str
    condition_task: Optional['ConditionTask'] = None
    depends_on: Optional['List[TaskDependency]'] = None
    email_notifications: Optional['JobEmailNotifications'] = None
    existing_cluster_id: Optional[str] = None
    health: Optional['JobsHealthRules'] = None
    libraries: Optional['List[compute.Library]'] = None
    new_cluster: Optional['compute.ClusterSpec'] = None
    notebook_task: Optional['NotebookTask'] = None
    notification_settings: Optional['TaskNotificationSettings'] = None
    pipeline_task: Optional['PipelineTask'] = None
    python_wheel_task: Optional['PythonWheelTask'] = None
    spark_jar_task: Optional['SparkJarTask'] = None
    spark_python_task: Optional['SparkPythonTask'] = None
    spark_submit_task: Optional['SparkSubmitTask'] = None
    sql_task: Optional['SqlTask'] = None
    timeout_seconds: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.condition_task: body['condition_task'] = self.condition_task.as_dict()
        if self.depends_on: body['depends_on'] = [v.as_dict() for v in self.depends_on]
        if self.email_notifications: body['email_notifications'] = self.email_notifications.as_dict()
        if self.existing_cluster_id is not None: body['existing_cluster_id'] = self.existing_cluster_id
        if self.health: body['health'] = self.health.as_dict()
        if self.libraries: body['libraries'] = [v.as_dict() for v in self.libraries]
        if self.new_cluster: body['new_cluster'] = self.new_cluster.as_dict()
        if self.notebook_task: body['notebook_task'] = self.notebook_task.as_dict()
        if self.notification_settings: body['notification_settings'] = self.notification_settings.as_dict()
        if self.pipeline_task: body['pipeline_task'] = self.pipeline_task.as_dict()
        if self.python_wheel_task: body['python_wheel_task'] = self.python_wheel_task.as_dict()
        if self.spark_jar_task: body['spark_jar_task'] = self.spark_jar_task.as_dict()
        if self.spark_python_task: body['spark_python_task'] = self.spark_python_task.as_dict()
        if self.spark_submit_task: body['spark_submit_task'] = self.spark_submit_task.as_dict()
        if self.sql_task: body['sql_task'] = self.sql_task.as_dict()
        if self.task_key is not None: body['task_key'] = self.task_key
        if self.timeout_seconds is not None: body['timeout_seconds'] = self.timeout_seconds
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SubmitTask':
        return cls(condition_task=_from_dict(d, 'condition_task', ConditionTask),
                   depends_on=_repeated(d, 'depends_on', TaskDependency),
                   email_notifications=_from_dict(d, 'email_notifications', JobEmailNotifications),
                   existing_cluster_id=d.get('existing_cluster_id', None),
                   health=_from_dict(d, 'health', JobsHealthRules),
                   libraries=_repeated(d, 'libraries', compute.Library),
                   new_cluster=_from_dict(d, 'new_cluster', compute.ClusterSpec),
                   notebook_task=_from_dict(d, 'notebook_task', NotebookTask),
                   notification_settings=_from_dict(d, 'notification_settings', TaskNotificationSettings),
                   pipeline_task=_from_dict(d, 'pipeline_task', PipelineTask),
                   python_wheel_task=_from_dict(d, 'python_wheel_task', PythonWheelTask),
                   spark_jar_task=_from_dict(d, 'spark_jar_task', SparkJarTask),
                   spark_python_task=_from_dict(d, 'spark_python_task', SparkPythonTask),
                   spark_submit_task=_from_dict(d, 'spark_submit_task', SparkSubmitTask),
                   sql_task=_from_dict(d, 'sql_task', SqlTask),
                   task_key=d.get('task_key', None),
                   timeout_seconds=d.get('timeout_seconds', None))


@dataclass
class Task:
    task_key: str
    compute_key: Optional[str] = None
    condition_task: Optional['ConditionTask'] = None
    dbt_task: Optional['DbtTask'] = None
    depends_on: Optional['List[TaskDependency]'] = None
    description: Optional[str] = None
    email_notifications: Optional['TaskEmailNotifications'] = None
    existing_cluster_id: Optional[str] = None
    health: Optional['JobsHealthRules'] = None
    job_cluster_key: Optional[str] = None
    libraries: Optional['List[compute.Library]'] = None
    max_retries: Optional[int] = None
    min_retry_interval_millis: Optional[int] = None
    new_cluster: Optional['compute.ClusterSpec'] = None
    notebook_task: Optional['NotebookTask'] = None
    notification_settings: Optional['TaskNotificationSettings'] = None
    pipeline_task: Optional['PipelineTask'] = None
    python_wheel_task: Optional['PythonWheelTask'] = None
    retry_on_timeout: Optional[bool] = None
    run_if: Optional['RunIf'] = None
    run_job_task: Optional['RunJobTask'] = None
    spark_jar_task: Optional['SparkJarTask'] = None
    spark_python_task: Optional['SparkPythonTask'] = None
    spark_submit_task: Optional['SparkSubmitTask'] = None
    sql_task: Optional['SqlTask'] = None
    timeout_seconds: Optional[int] = None
    webhook_notifications: Optional['WebhookNotifications'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.compute_key is not None: body['compute_key'] = self.compute_key
        if self.condition_task: body['condition_task'] = self.condition_task.as_dict()
        if self.dbt_task: body['dbt_task'] = self.dbt_task.as_dict()
        if self.depends_on: body['depends_on'] = [v.as_dict() for v in self.depends_on]
        if self.description is not None: body['description'] = self.description
        if self.email_notifications: body['email_notifications'] = self.email_notifications.as_dict()
        if self.existing_cluster_id is not None: body['existing_cluster_id'] = self.existing_cluster_id
        if self.health: body['health'] = self.health.as_dict()
        if self.job_cluster_key is not None: body['job_cluster_key'] = self.job_cluster_key
        if self.libraries: body['libraries'] = [v.as_dict() for v in self.libraries]
        if self.max_retries is not None: body['max_retries'] = self.max_retries
        if self.min_retry_interval_millis is not None:
            body['min_retry_interval_millis'] = self.min_retry_interval_millis
        if self.new_cluster: body['new_cluster'] = self.new_cluster.as_dict()
        if self.notebook_task: body['notebook_task'] = self.notebook_task.as_dict()
        if self.notification_settings: body['notification_settings'] = self.notification_settings.as_dict()
        if self.pipeline_task: body['pipeline_task'] = self.pipeline_task.as_dict()
        if self.python_wheel_task: body['python_wheel_task'] = self.python_wheel_task.as_dict()
        if self.retry_on_timeout is not None: body['retry_on_timeout'] = self.retry_on_timeout
        if self.run_if is not None: body['run_if'] = self.run_if.value
        if self.run_job_task: body['run_job_task'] = self.run_job_task.as_dict()
        if self.spark_jar_task: body['spark_jar_task'] = self.spark_jar_task.as_dict()
        if self.spark_python_task: body['spark_python_task'] = self.spark_python_task.as_dict()
        if self.spark_submit_task: body['spark_submit_task'] = self.spark_submit_task.as_dict()
        if self.sql_task: body['sql_task'] = self.sql_task.as_dict()
        if self.task_key is not None: body['task_key'] = self.task_key
        if self.timeout_seconds is not None: body['timeout_seconds'] = self.timeout_seconds
        if self.webhook_notifications: body['webhook_notifications'] = self.webhook_notifications.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Task':
        return cls(compute_key=d.get('compute_key', None),
                   condition_task=_from_dict(d, 'condition_task', ConditionTask),
                   dbt_task=_from_dict(d, 'dbt_task', DbtTask),
                   depends_on=_repeated(d, 'depends_on', TaskDependency),
                   description=d.get('description', None),
                   email_notifications=_from_dict(d, 'email_notifications', TaskEmailNotifications),
                   existing_cluster_id=d.get('existing_cluster_id', None),
                   health=_from_dict(d, 'health', JobsHealthRules),
                   job_cluster_key=d.get('job_cluster_key', None),
                   libraries=_repeated(d, 'libraries', compute.Library),
                   max_retries=d.get('max_retries', None),
                   min_retry_interval_millis=d.get('min_retry_interval_millis', None),
                   new_cluster=_from_dict(d, 'new_cluster', compute.ClusterSpec),
                   notebook_task=_from_dict(d, 'notebook_task', NotebookTask),
                   notification_settings=_from_dict(d, 'notification_settings', TaskNotificationSettings),
                   pipeline_task=_from_dict(d, 'pipeline_task', PipelineTask),
                   python_wheel_task=_from_dict(d, 'python_wheel_task', PythonWheelTask),
                   retry_on_timeout=d.get('retry_on_timeout', None),
                   run_if=_enum(d, 'run_if', RunIf),
                   run_job_task=_from_dict(d, 'run_job_task', RunJobTask),
                   spark_jar_task=_from_dict(d, 'spark_jar_task', SparkJarTask),
                   spark_python_task=_from_dict(d, 'spark_python_task', SparkPythonTask),
                   spark_submit_task=_from_dict(d, 'spark_submit_task', SparkSubmitTask),
                   sql_task=_from_dict(d, 'sql_task', SqlTask),
                   task_key=d.get('task_key', None),
                   timeout_seconds=d.get('timeout_seconds', None),
                   webhook_notifications=_from_dict(d, 'webhook_notifications', WebhookNotifications))


@dataclass
class TaskDependency:
    task_key: str
    outcome: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.outcome is not None: body['outcome'] = self.outcome
        if self.task_key is not None: body['task_key'] = self.task_key
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TaskDependency':
        return cls(outcome=d.get('outcome', None), task_key=d.get('task_key', None))


@dataclass
class TaskEmailNotifications:
    on_duration_warning_threshold_exceeded: Optional['List[str]'] = None
    on_failure: Optional['List[str]'] = None
    on_start: Optional['List[str]'] = None
    on_success: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.on_duration_warning_threshold_exceeded:
            body['on_duration_warning_threshold_exceeded'] = [
                v for v in self.on_duration_warning_threshold_exceeded
            ]
        if self.on_failure: body['on_failure'] = [v for v in self.on_failure]
        if self.on_start: body['on_start'] = [v for v in self.on_start]
        if self.on_success: body['on_success'] = [v for v in self.on_success]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TaskEmailNotifications':
        return cls(on_duration_warning_threshold_exceeded=d.get('on_duration_warning_threshold_exceeded',
                                                                None),
                   on_failure=d.get('on_failure', None),
                   on_start=d.get('on_start', None),
                   on_success=d.get('on_success', None))


@dataclass
class TaskNotificationSettings:
    alert_on_last_attempt: Optional[bool] = None
    no_alert_for_canceled_runs: Optional[bool] = None
    no_alert_for_skipped_runs: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.alert_on_last_attempt is not None: body['alert_on_last_attempt'] = self.alert_on_last_attempt
        if self.no_alert_for_canceled_runs is not None:
            body['no_alert_for_canceled_runs'] = self.no_alert_for_canceled_runs
        if self.no_alert_for_skipped_runs is not None:
            body['no_alert_for_skipped_runs'] = self.no_alert_for_skipped_runs
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TaskNotificationSettings':
        return cls(alert_on_last_attempt=d.get('alert_on_last_attempt', None),
                   no_alert_for_canceled_runs=d.get('no_alert_for_canceled_runs', None),
                   no_alert_for_skipped_runs=d.get('no_alert_for_skipped_runs', None))


@dataclass
class TriggerEvaluation:
    description: Optional[str] = None
    run_id: Optional[int] = None
    timestamp: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.run_id is not None: body['run_id'] = self.run_id
        if self.timestamp is not None: body['timestamp'] = self.timestamp
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TriggerEvaluation':
        return cls(description=d.get('description', None),
                   run_id=d.get('run_id', None),
                   timestamp=d.get('timestamp', None))


@dataclass
class TriggerHistory:
    last_failed: Optional['TriggerEvaluation'] = None
    last_not_triggered: Optional['TriggerEvaluation'] = None
    last_triggered: Optional['TriggerEvaluation'] = None

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
class TriggerInfo:
    run_id: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.run_id is not None: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TriggerInfo':
        return cls(run_id=d.get('run_id', None))


@dataclass
class TriggerSettings:
    file_arrival: Optional['FileArrivalTriggerConfiguration'] = None
    pause_status: Optional['PauseStatus'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.file_arrival: body['file_arrival'] = self.file_arrival.as_dict()
        if self.pause_status is not None: body['pause_status'] = self.pause_status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TriggerSettings':
        return cls(file_arrival=_from_dict(d, 'file_arrival', FileArrivalTriggerConfiguration),
                   pause_status=_enum(d, 'pause_status', PauseStatus))


class TriggerType(Enum):
    """The type of trigger that fired this run.
    
    * `PERIODIC`: Schedules that periodically trigger runs, such as a cron scheduler. * `ONE_TIME`:
    One time triggers that fire a single run. This occurs you triggered a single run on demand
    through the UI or the API. * `RETRY`: Indicates a run that is triggered as a retry of a
    previously failed run. This occurs when you request to re-run the job in case of failures. *
    `RUN_JOB_TASK`: Indicates a run that is triggered using a Run Job task.
    
    * `FILE_ARRIVAL`: Indicates a run that is triggered by a file arrival."""

    FILE_ARRIVAL = 'FILE_ARRIVAL'
    ONE_TIME = 'ONE_TIME'
    PERIODIC = 'PERIODIC'
    RETRY = 'RETRY'
    RUN_JOB_TASK = 'RUN_JOB_TASK'


@dataclass
class UpdateJob:
    job_id: int
    fields_to_remove: Optional['List[str]'] = None
    new_settings: Optional['JobSettings'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.fields_to_remove: body['fields_to_remove'] = [v for v in self.fields_to_remove]
        if self.job_id is not None: body['job_id'] = self.job_id
        if self.new_settings: body['new_settings'] = self.new_settings.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateJob':
        return cls(fields_to_remove=d.get('fields_to_remove', None),
                   job_id=d.get('job_id', None),
                   new_settings=_from_dict(d, 'new_settings', JobSettings))


@dataclass
class ViewItem:
    content: Optional[str] = None
    name: Optional[str] = None
    type: Optional['ViewType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.content is not None: body['content'] = self.content
        if self.name is not None: body['name'] = self.name
        if self.type is not None: body['type'] = self.type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ViewItem':
        return cls(content=d.get('content', None), name=d.get('name', None), type=_enum(d, 'type', ViewType))


class ViewType(Enum):
    """* `NOTEBOOK`: Notebook view item. * `DASHBOARD`: Dashboard view item."""

    DASHBOARD = 'DASHBOARD'
    NOTEBOOK = 'NOTEBOOK'


class ViewsToExport(Enum):
    """* `CODE`: Code view of the notebook. * `DASHBOARDS`: All dashboard views of the notebook. *
    `ALL`: All views of the notebook."""

    ALL = 'ALL'
    CODE = 'CODE'
    DASHBOARDS = 'DASHBOARDS'


@dataclass
class Webhook:
    id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.id is not None: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Webhook':
        return cls(id=d.get('id', None))


@dataclass
class WebhookNotifications:
    on_duration_warning_threshold_exceeded: Optional[
        'List[WebhookNotificationsOnDurationWarningThresholdExceededItem]'] = None
    on_failure: Optional['List[Webhook]'] = None
    on_start: Optional['List[Webhook]'] = None
    on_success: Optional['List[Webhook]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.on_duration_warning_threshold_exceeded:
            body['on_duration_warning_threshold_exceeded'] = [
                v.as_dict() for v in self.on_duration_warning_threshold_exceeded
            ]
        if self.on_failure: body['on_failure'] = [v.as_dict() for v in self.on_failure]
        if self.on_start: body['on_start'] = [v.as_dict() for v in self.on_start]
        if self.on_success: body['on_success'] = [v.as_dict() for v in self.on_success]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WebhookNotifications':
        return cls(on_duration_warning_threshold_exceeded=_repeated(
            d, 'on_duration_warning_threshold_exceeded',
            WebhookNotificationsOnDurationWarningThresholdExceededItem),
                   on_failure=_repeated(d, 'on_failure', Webhook),
                   on_start=_repeated(d, 'on_start', Webhook),
                   on_success=_repeated(d, 'on_success', Webhook))


@dataclass
class WebhookNotificationsOnDurationWarningThresholdExceededItem:
    id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.id is not None: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WebhookNotificationsOnDurationWarningThresholdExceededItem':
        return cls(id=d.get('id', None))


class JobsAPI:
    """The Jobs API allows you to create, edit, and delete jobs.
    
    You can use a Databricks job to run a data processing or data analysis task in a Databricks cluster with
    scalable resources. Your job can consist of a single task or can be a large, multi-task workflow with
    complex dependencies. Databricks manages the task orchestration, cluster management, monitoring, and error
    reporting for all of your jobs. You can run your jobs immediately or periodically through an easy-to-use
    scheduling system. You can implement job tasks using notebooks, JARS, Delta Live Tables pipelines, or
    Python, Scala, Spark submit, and Java applications.
    
    You should never hard code secrets or store them in plain text. Use the [Secrets CLI] to manage secrets in
    the [Databricks CLI]. Use the [Secrets utility] to reference secrets in notebooks and jobs.
    
    [Databricks CLI]: https://docs.databricks.com/dev-tools/cli/index.html
    [Secrets CLI]: https://docs.databricks.com/dev-tools/cli/secrets-cli.html
    [Secrets utility]: https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-secrets"""

    def __init__(self, api_client):
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
            if poll.state:
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

    def cancel_all_runs(self, *, all_queued_runs: Optional[bool] = None, job_id: Optional[int] = None):
        """Cancel all runs of a job.
        
        Cancels all active runs of a job. The runs are canceled asynchronously, so it doesn't prevent new runs
        from being started.
        
        :param all_queued_runs: bool (optional)
          Optional boolean parameter to cancel all queued runs. If no job_id is provided, all queued runs in
          the workspace are canceled.
        :param job_id: int (optional)
          The canonical identifier of the job to cancel all runs of.
        
        
        """
        body = {}
        if all_queued_runs is not None: body['all_queued_runs'] = all_queued_runs
        if job_id is not None: body['job_id'] = job_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.1/jobs/runs/cancel-all', body=body, headers=headers)

    def cancel_run(self, run_id: int) -> Wait[Run]:
        """Cancel a run.
        
        Cancels a job run or a task run. The run is canceled asynchronously, so it may still be running when
        this request completes.
        
        :param run_id: int
          This field is required.
        
        :returns:
          Long-running operation waiter for :class:`Run`.
          See :method:wait_get_run_job_terminated_or_skipped for more details.
        """
        body = {}
        if run_id is not None: body['run_id'] = run_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.1/jobs/runs/cancel', body=body, headers=headers)
        return Wait(self.wait_get_run_job_terminated_or_skipped, run_id=run_id)

    def cancel_run_and_wait(self, run_id: int, timeout=timedelta(minutes=20)) -> Run:
        return self.cancel_run(run_id=run_id).result(timeout=timeout)

    def create(self,
               *,
               access_control_list: Optional[List[iam.AccessControlRequest]] = None,
               compute: Optional[List[JobCompute]] = None,
               continuous: Optional[Continuous] = None,
               deployment: Optional[JobDeployment] = None,
               email_notifications: Optional[JobEmailNotifications] = None,
               format: Optional[Format] = None,
               git_source: Optional[GitSource] = None,
               health: Optional[JobsHealthRules] = None,
               job_clusters: Optional[List[JobCluster]] = None,
               max_concurrent_runs: Optional[int] = None,
               name: Optional[str] = None,
               notification_settings: Optional[JobNotificationSettings] = None,
               parameters: Optional[List[JobParameterDefinition]] = None,
               queue: Optional[QueueSettings] = None,
               run_as: Optional[JobRunAs] = None,
               schedule: Optional[CronSchedule] = None,
               tags: Optional[Dict[str, str]] = None,
               tasks: Optional[List[Task]] = None,
               timeout_seconds: Optional[int] = None,
               trigger: Optional[TriggerSettings] = None,
               ui_state: Optional[CreateJobUiState] = None,
               webhook_notifications: Optional[WebhookNotifications] = None) -> CreateResponse:
        """Create a new job.
        
        Create a new job.
        
        :param access_control_list: List[:class:`AccessControlRequest`] (optional)
          List of permissions to set on the job.
        :param compute: List[:class:`JobCompute`] (optional)
          A list of compute requirements that can be referenced by tasks of this job.
        :param continuous: :class:`Continuous` (optional)
          An optional continuous property for this job. The continuous property will ensure that there is
          always one run executing. Only one of `schedule` and `continuous` can be used.
        :param deployment: :class:`JobDeployment` (optional)
          Deployment information for jobs managed by external sources.
        :param email_notifications: :class:`JobEmailNotifications` (optional)
          An optional set of email addresses that is notified when runs of this job begin or complete as well
          as when this job is deleted.
        :param format: :class:`Format` (optional)
          Used to tell what is the format of the job. This field is ignored in Create/Update/Reset calls. When
          using the Jobs API 2.1 this value is always set to `"MULTI_TASK"`.
        :param git_source: :class:`GitSource` (optional)
          An optional specification for a remote Git repository containing the source code used by tasks.
          Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks.
          
          If `git_source` is set, these tasks retrieve the file from the remote repository by default.
          However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task.
          
          Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are
          used, `git_source` must be defined on the job.
        :param health: :class:`JobsHealthRules` (optional)
          An optional set of health rules that can be defined for this job.
        :param job_clusters: List[:class:`JobCluster`] (optional)
          A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries
          cannot be declared in a shared job cluster. You must declare dependent libraries in task settings.
        :param max_concurrent_runs: int (optional)
          An optional maximum allowed number of concurrent runs of the job.
          
          Set this value if you want to be able to execute multiple runs of the same job concurrently. This is
          useful for example if you trigger your job on a frequent schedule and want to allow consecutive runs
          to overlap with each other, or if you want to trigger multiple runs which differ by their input
          parameters.
          
          This setting affects only new runs. For example, suppose the job’s concurrency is 4 and there are
          4 concurrent active runs. Then setting the concurrency to 3 won’t kill any of the active runs.
          However, from then on, new runs are skipped unless there are fewer than 3 active runs.
          
          This value cannot exceed 1000\. Setting this value to `0` causes all new runs to be skipped.
        :param name: str (optional)
          An optional name for the job. The maximum length is 4096 bytes in UTF-8 encoding.
        :param notification_settings: :class:`JobNotificationSettings` (optional)
          Optional notification settings that are used when sending notifications to each of the
          `email_notifications` and `webhook_notifications` for this job.
        :param parameters: List[:class:`JobParameterDefinition`] (optional)
          Job-level parameter definitions
        :param queue: :class:`QueueSettings` (optional)
          The queue settings of the job.
        :param run_as: :class:`JobRunAs` (optional)
          Write-only setting, available only in Create/Update/Reset and Submit calls. Specifies the user or
          service principal that the job runs as. If not specified, the job runs as the user who created the
          job.
          
          Only `user_name` or `service_principal_name` can be specified. If both are specified, an error is
          thrown.
        :param schedule: :class:`CronSchedule` (optional)
          An optional periodic schedule for this job. The default behavior is that the job only runs when
          triggered by clicking “Run Now” in the Jobs UI or sending an API request to `runNow`.
        :param tags: Dict[str,str] (optional)
          A map of tags associated with the job. These are forwarded to the cluster as cluster tags for jobs
          clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags can be added
          to the job.
        :param tasks: List[:class:`Task`] (optional)
          A list of task specifications to be executed by this job.
        :param timeout_seconds: int (optional)
          An optional timeout applied to each run of this job. A value of `0` means no timeout.
        :param trigger: :class:`TriggerSettings` (optional)
          Trigger settings for the job. Can be used to trigger a run when new files arrive in an external
          location. The default behavior is that the job runs only when triggered by clicking “Run Now” in
          the Jobs UI or sending an API request to `runNow`.
        :param ui_state: :class:`CreateJobUiState` (optional)
          State of the job in UI.
          
          * `LOCKED`: The job is in a locked state and cannot be modified. * `EDITABLE`: The job is in an
          editable state and can be modified.
        :param webhook_notifications: :class:`WebhookNotifications` (optional)
          A collection of system notification IDs to notify when runs of this job begin or complete.
        
        :returns: :class:`CreateResponse`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        if compute is not None: body['compute'] = [v.as_dict() for v in compute]
        if continuous is not None: body['continuous'] = continuous.as_dict()
        if deployment is not None: body['deployment'] = deployment.as_dict()
        if email_notifications is not None: body['email_notifications'] = email_notifications.as_dict()
        if format is not None: body['format'] = format.value
        if git_source is not None: body['git_source'] = git_source.as_dict()
        if health is not None: body['health'] = health.as_dict()
        if job_clusters is not None: body['job_clusters'] = [v.as_dict() for v in job_clusters]
        if max_concurrent_runs is not None: body['max_concurrent_runs'] = max_concurrent_runs
        if name is not None: body['name'] = name
        if notification_settings is not None: body['notification_settings'] = notification_settings.as_dict()
        if parameters is not None: body['parameters'] = [v.as_dict() for v in parameters]
        if queue is not None: body['queue'] = queue.as_dict()
        if run_as is not None: body['run_as'] = run_as.as_dict()
        if schedule is not None: body['schedule'] = schedule.as_dict()
        if tags is not None: body['tags'] = tags
        if tasks is not None: body['tasks'] = [v.as_dict() for v in tasks]
        if timeout_seconds is not None: body['timeout_seconds'] = timeout_seconds
        if trigger is not None: body['trigger'] = trigger.as_dict()
        if ui_state is not None: body['ui_state'] = ui_state.value
        if webhook_notifications is not None: body['webhook_notifications'] = webhook_notifications.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.1/jobs/create', body=body, headers=headers)
        return CreateResponse.from_dict(res)

    def delete(self, job_id: int):
        """Delete a job.
        
        Deletes a job.
        
        :param job_id: int
          The canonical identifier of the job to delete. This field is required.
        
        
        """
        body = {}
        if job_id is not None: body['job_id'] = job_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.1/jobs/delete', body=body, headers=headers)

    def delete_run(self, run_id: int):
        """Delete a job run.
        
        Deletes a non-active run. Returns an error if the run is active.
        
        :param run_id: int
          The canonical identifier of the run for which to retrieve the metadata.
        
        
        """
        body = {}
        if run_id is not None: body['run_id'] = run_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.1/jobs/runs/delete', body=body, headers=headers)

    def export_run(self, run_id: int, *, views_to_export: Optional[ViewsToExport] = None) -> ExportRunOutput:
        """Export and retrieve a job run.
        
        Export and retrieve the job run task.
        
        :param run_id: int
          The canonical identifier for the run. This field is required.
        :param views_to_export: :class:`ViewsToExport` (optional)
          Which views to export (CODE, DASHBOARDS, or ALL). Defaults to CODE.
        
        :returns: :class:`ExportRunOutput`
        """

        query = {}
        if run_id is not None: query['run_id'] = run_id
        if views_to_export is not None: query['views_to_export'] = views_to_export.value
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.1/jobs/runs/export', query=query, headers=headers)
        return ExportRunOutput.from_dict(res)

    def get(self, job_id: int) -> Job:
        """Get a single job.
        
        Retrieves the details for a single job.
        
        :param job_id: int
          The canonical identifier of the job to retrieve information about. This field is required.
        
        :returns: :class:`Job`
        """

        query = {}
        if job_id is not None: query['job_id'] = job_id
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.1/jobs/get', query=query, headers=headers)
        return Job.from_dict(res)

    def get_permission_levels(self, job_id: str) -> GetJobPermissionLevelsResponse:
        """Get job permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param job_id: str
          The job for which to get or manage permissions.
        
        :returns: :class:`GetJobPermissionLevelsResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/permissions/jobs/{job_id}/permissionLevels', headers=headers)
        return GetJobPermissionLevelsResponse.from_dict(res)

    def get_permissions(self, job_id: str) -> JobPermissions:
        """Get job permissions.
        
        Gets the permissions of a job. Jobs can inherit permissions from their root object.
        
        :param job_id: str
          The job for which to get or manage permissions.
        
        :returns: :class:`JobPermissions`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/permissions/jobs/{job_id}', headers=headers)
        return JobPermissions.from_dict(res)

    def get_run(self, run_id: int, *, include_history: Optional[bool] = None) -> Run:
        """Get a single job run.
        
        Retrieve the metadata of a run.
        
        :param run_id: int
          The canonical identifier of the run for which to retrieve the metadata. This field is required.
        :param include_history: bool (optional)
          Whether to include the repair history in the response.
        
        :returns: :class:`Run`
        """

        query = {}
        if include_history is not None: query['include_history'] = include_history
        if run_id is not None: query['run_id'] = run_id
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.1/jobs/runs/get', query=query, headers=headers)
        return Run.from_dict(res)

    def get_run_output(self, run_id: int) -> RunOutput:
        """Get the output for a single run.
        
        Retrieve the output and metadata of a single task run. When a notebook task returns a value through
        the `dbutils.notebook.exit()` call, you can use this endpoint to retrieve that value. Databricks
        restricts this API to returning the first 5 MB of the output. To return a larger result, you can store
        job results in a cloud storage service.
        
        This endpoint validates that the __run_id__ parameter is valid and returns an HTTP status code 400 if
        the __run_id__ parameter is invalid. Runs are automatically removed after 60 days. If you to want to
        reference them beyond 60 days, you must save old run results before they expire.
        
        :param run_id: int
          The canonical identifier for the run. This field is required.
        
        :returns: :class:`RunOutput`
        """

        query = {}
        if run_id is not None: query['run_id'] = run_id
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.1/jobs/runs/get-output', query=query, headers=headers)
        return RunOutput.from_dict(res)

    def list(self,
             *,
             expand_tasks: Optional[bool] = None,
             limit: Optional[int] = None,
             name: Optional[str] = None,
             offset: Optional[int] = None,
             page_token: Optional[str] = None) -> Iterator['BaseJob']:
        """List jobs.
        
        Retrieves a list of jobs.
        
        :param expand_tasks: bool (optional)
          Whether to include task and cluster details in the response.
        :param limit: int (optional)
          The number of jobs to return. This value must be greater than 0 and less or equal to 100. The
          default value is 20.
        :param name: str (optional)
          A filter on the list based on the exact (case insensitive) job name.
        :param offset: int (optional)
          The offset of the first job to return, relative to the most recently created job.
          
          Deprecated since June 2023. Use `page_token` to iterate through the pages instead.
        :param page_token: str (optional)
          Use `next_page_token` or `prev_page_token` returned from the previous request to list the next or
          previous page of jobs respectively.
        
        :returns: Iterator over :class:`BaseJob`
        """

        query = {}
        if expand_tasks is not None: query['expand_tasks'] = expand_tasks
        if limit is not None: query['limit'] = limit
        if name is not None: query['name'] = name
        if offset is not None: query['offset'] = offset
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET', '/api/2.1/jobs/list', query=query, headers=headers)
            if 'jobs' not in json or not json['jobs']:
                return
            for v in json['jobs']:
                yield BaseJob.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def list_runs(self,
                  *,
                  active_only: Optional[bool] = None,
                  completed_only: Optional[bool] = None,
                  expand_tasks: Optional[bool] = None,
                  job_id: Optional[int] = None,
                  limit: Optional[int] = None,
                  offset: Optional[int] = None,
                  page_token: Optional[str] = None,
                  run_type: Optional[ListRunsRunType] = None,
                  start_time_from: Optional[int] = None,
                  start_time_to: Optional[int] = None) -> Iterator['BaseRun']:
        """List job runs.
        
        List runs in descending order by start time.
        
        :param active_only: bool (optional)
          If active_only is `true`, only active runs are included in the results; otherwise, lists both active
          and completed runs. An active run is a run in the `QUEUED`, `PENDING`, `RUNNING`, or `TERMINATING`.
          This field cannot be `true` when completed_only is `true`.
        :param completed_only: bool (optional)
          If completed_only is `true`, only completed runs are included in the results; otherwise, lists both
          active and completed runs. This field cannot be `true` when active_only is `true`.
        :param expand_tasks: bool (optional)
          Whether to include task and cluster details in the response.
        :param job_id: int (optional)
          The job for which to list runs. If omitted, the Jobs service lists runs from all jobs.
        :param limit: int (optional)
          The number of runs to return. This value must be greater than 0 and less than 25. The default value
          is 25. If a request specifies a limit of 0, the service instead uses the maximum limit.
        :param offset: int (optional)
          The offset of the first run to return, relative to the most recent run.
          
          Deprecated since June 2023. Use `page_token` to iterate through the pages instead.
        :param page_token: str (optional)
          Use `next_page_token` or `prev_page_token` returned from the previous request to list the next or
          previous page of runs respectively.
        :param run_type: :class:`ListRunsRunType` (optional)
          The type of runs to return. For a description of run types, see :method:jobs/getRun.
        :param start_time_from: int (optional)
          Show runs that started _at or after_ this value. The value must be a UTC timestamp in milliseconds.
          Can be combined with _start_time_to_ to filter by a time range.
        :param start_time_to: int (optional)
          Show runs that started _at or before_ this value. The value must be a UTC timestamp in milliseconds.
          Can be combined with _start_time_from_ to filter by a time range.
        
        :returns: Iterator over :class:`BaseRun`
        """

        query = {}
        if active_only is not None: query['active_only'] = active_only
        if completed_only is not None: query['completed_only'] = completed_only
        if expand_tasks is not None: query['expand_tasks'] = expand_tasks
        if job_id is not None: query['job_id'] = job_id
        if limit is not None: query['limit'] = limit
        if offset is not None: query['offset'] = offset
        if page_token is not None: query['page_token'] = page_token
        if run_type is not None: query['run_type'] = run_type.value
        if start_time_from is not None: query['start_time_from'] = start_time_from
        if start_time_to is not None: query['start_time_to'] = start_time_to
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET', '/api/2.1/jobs/runs/list', query=query, headers=headers)
            if 'runs' not in json or not json['runs']:
                return
            for v in json['runs']:
                yield BaseRun.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def repair_run(self,
                   run_id: int,
                   *,
                   dbt_commands: Optional[List[str]] = None,
                   jar_params: Optional[List[str]] = None,
                   job_parameters: Optional[Dict[str, str]] = None,
                   latest_repair_id: Optional[int] = None,
                   notebook_params: Optional[Dict[str, str]] = None,
                   pipeline_params: Optional[PipelineParams] = None,
                   python_named_params: Optional[Dict[str, str]] = None,
                   python_params: Optional[List[str]] = None,
                   rerun_all_failed_tasks: Optional[bool] = None,
                   rerun_dependent_tasks: Optional[bool] = None,
                   rerun_tasks: Optional[List[str]] = None,
                   spark_submit_params: Optional[List[str]] = None,
                   sql_params: Optional[Dict[str, str]] = None) -> Wait[Run]:
        """Repair a job run.
        
        Re-run one or more tasks. Tasks are re-run as part of the original job run. They use the current job
        and task settings, and can be viewed in the history for the original job run.
        
        :param run_id: int
          The job run ID of the run to repair. The run must not be in progress.
        :param dbt_commands: List[str] (optional)
          An array of commands to execute for jobs with the dbt task, for example `"dbt_commands": ["dbt
          deps", "dbt seed", "dbt run"]`
        :param jar_params: List[str] (optional)
          A list of parameters for jobs with Spark JAR tasks, for example `"jar_params": ["john doe", "35"]`.
          The parameters are used to invoke the main function of the main class specified in the Spark JAR
          task. If not specified upon `run-now`, it defaults to an empty list. jar_params cannot be specified
          in conjunction with notebook_params. The JSON representation of this field (for example
          `{"jar_params":["john doe","35"]}`) cannot exceed 10,000 bytes.
          
          Use [Task parameter variables](/jobs.html"#parameter-variables") to set parameters containing
          information about job runs.
        :param job_parameters: Dict[str,str] (optional)
          Job-level parameters used in the run. for example `"param": "overriding_val"`
        :param latest_repair_id: int (optional)
          The ID of the latest repair. This parameter is not required when repairing a run for the first time,
          but must be provided on subsequent requests to repair the same run.
        :param notebook_params: Dict[str,str] (optional)
          A map from keys to values for jobs with notebook task, for example `"notebook_params": {"name":
          "john doe", "age": "35"}`. The map is passed to the notebook and is accessible through the
          [dbutils.widgets.get] function.
          
          If not specified upon `run-now`, the triggered run uses the job’s base parameters.
          
          notebook_params cannot be specified in conjunction with jar_params.
          
          Use [Task parameter variables] to set parameters containing information about job runs.
          
          The JSON representation of this field (for example `{"notebook_params":{"name":"john
          doe","age":"35"}}`) cannot exceed 10,000 bytes.
          
          [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
          [dbutils.widgets.get]: https://docs.databricks.com/dev-tools/databricks-utils.html
        :param pipeline_params: :class:`PipelineParams` (optional)
        :param python_named_params: Dict[str,str] (optional)
          A map from keys to values for jobs with Python wheel task, for example `"python_named_params":
          {"name": "task", "data": "dbfs:/path/to/data.json"}`.
        :param python_params: List[str] (optional)
          A list of parameters for jobs with Python tasks, for example `"python_params": ["john doe", "35"]`.
          The parameters are passed to Python file as command-line parameters. If specified upon `run-now`, it
          would overwrite the parameters specified in job setting. The JSON representation of this field (for
          example `{"python_params":["john doe","35"]}`) cannot exceed 10,000 bytes.
          
          Use [Task parameter variables] to set parameters containing information about job runs.
          
          Important
          
          These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters
          returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and
          emojis.
          
          [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
        :param rerun_all_failed_tasks: bool (optional)
          If true, repair all failed tasks. Only one of `rerun_tasks` or `rerun_all_failed_tasks` can be used.
        :param rerun_dependent_tasks: bool (optional)
          If true, repair all tasks that depend on the tasks in `rerun_tasks`, even if they were previously
          successful. Can be also used in combination with `rerun_all_failed_tasks`.
        :param rerun_tasks: List[str] (optional)
          The task keys of the task runs to repair.
        :param spark_submit_params: List[str] (optional)
          A list of parameters for jobs with spark submit task, for example `"spark_submit_params":
          ["--class", "org.apache.spark.examples.SparkPi"]`. The parameters are passed to spark-submit script
          as command-line parameters. If specified upon `run-now`, it would overwrite the parameters specified
          in job setting. The JSON representation of this field (for example `{"python_params":["john
          doe","35"]}`) cannot exceed 10,000 bytes.
          
          Use [Task parameter variables] to set parameters containing information about job runs
          
          Important
          
          These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters
          returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and
          emojis.
          
          [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
        :param sql_params: Dict[str,str] (optional)
          A map from keys to values for jobs with SQL task, for example `"sql_params": {"name": "john doe",
          "age": "35"}`. The SQL alert task does not support custom parameters.
        
        :returns:
          Long-running operation waiter for :class:`Run`.
          See :method:wait_get_run_job_terminated_or_skipped for more details.
        """
        body = {}
        if dbt_commands is not None: body['dbt_commands'] = [v for v in dbt_commands]
        if jar_params is not None: body['jar_params'] = [v for v in jar_params]
        if job_parameters is not None: body['job_parameters'] = job_parameters
        if latest_repair_id is not None: body['latest_repair_id'] = latest_repair_id
        if notebook_params is not None: body['notebook_params'] = notebook_params
        if pipeline_params is not None: body['pipeline_params'] = pipeline_params.as_dict()
        if python_named_params is not None: body['python_named_params'] = python_named_params
        if python_params is not None: body['python_params'] = [v for v in python_params]
        if rerun_all_failed_tasks is not None: body['rerun_all_failed_tasks'] = rerun_all_failed_tasks
        if rerun_dependent_tasks is not None: body['rerun_dependent_tasks'] = rerun_dependent_tasks
        if rerun_tasks is not None: body['rerun_tasks'] = [v for v in rerun_tasks]
        if run_id is not None: body['run_id'] = run_id
        if spark_submit_params is not None: body['spark_submit_params'] = [v for v in spark_submit_params]
        if sql_params is not None: body['sql_params'] = sql_params
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        op_response = self._api.do('POST', '/api/2.1/jobs/runs/repair', body=body, headers=headers)
        return Wait(self.wait_get_run_job_terminated_or_skipped,
                    response=RepairRunResponse.from_dict(op_response),
                    run_id=run_id)

    def repair_run_and_wait(
        self,
        run_id: int,
        *,
        dbt_commands: Optional[List[str]] = None,
        jar_params: Optional[List[str]] = None,
        job_parameters: Optional[Dict[str, str]] = None,
        latest_repair_id: Optional[int] = None,
        notebook_params: Optional[Dict[str, str]] = None,
        pipeline_params: Optional[PipelineParams] = None,
        python_named_params: Optional[Dict[str, str]] = None,
        python_params: Optional[List[str]] = None,
        rerun_all_failed_tasks: Optional[bool] = None,
        rerun_dependent_tasks: Optional[bool] = None,
        rerun_tasks: Optional[List[str]] = None,
        spark_submit_params: Optional[List[str]] = None,
        sql_params: Optional[Dict[str, str]] = None,
        timeout=timedelta(minutes=20)) -> Run:
        return self.repair_run(dbt_commands=dbt_commands,
                               jar_params=jar_params,
                               job_parameters=job_parameters,
                               latest_repair_id=latest_repair_id,
                               notebook_params=notebook_params,
                               pipeline_params=pipeline_params,
                               python_named_params=python_named_params,
                               python_params=python_params,
                               rerun_all_failed_tasks=rerun_all_failed_tasks,
                               rerun_dependent_tasks=rerun_dependent_tasks,
                               rerun_tasks=rerun_tasks,
                               run_id=run_id,
                               spark_submit_params=spark_submit_params,
                               sql_params=sql_params).result(timeout=timeout)

    def reset(self, job_id: int, new_settings: JobSettings):
        """Overwrite all settings for a job.
        
        Overwrite all settings for the given job. Use the Update endpoint to update job settings partially.
        
        :param job_id: int
          The canonical identifier of the job to reset. This field is required.
        :param new_settings: :class:`JobSettings`
          The new settings of the job. These settings completely replace the old settings.
          
          Changes to the field `JobBaseSettings.timeout_seconds` are applied to active runs. Changes to other
          fields are applied to future runs only.
        
        
        """
        body = {}
        if job_id is not None: body['job_id'] = job_id
        if new_settings is not None: body['new_settings'] = new_settings.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.1/jobs/reset', body=body, headers=headers)

    def run_now(self,
                job_id: int,
                *,
                dbt_commands: Optional[List[str]] = None,
                idempotency_token: Optional[str] = None,
                jar_params: Optional[List[str]] = None,
                job_parameters: Optional[Dict[str, str]] = None,
                notebook_params: Optional[Dict[str, str]] = None,
                pipeline_params: Optional[PipelineParams] = None,
                python_named_params: Optional[Dict[str, str]] = None,
                python_params: Optional[List[str]] = None,
                queue: Optional[QueueSettings] = None,
                spark_submit_params: Optional[List[str]] = None,
                sql_params: Optional[Dict[str, str]] = None) -> Wait[Run]:
        """Trigger a new job run.
        
        Run a job and return the `run_id` of the triggered run.
        
        :param job_id: int
          The ID of the job to be executed
        :param dbt_commands: List[str] (optional)
          An array of commands to execute for jobs with the dbt task, for example `"dbt_commands": ["dbt
          deps", "dbt seed", "dbt run"]`
        :param idempotency_token: str (optional)
          An optional token to guarantee the idempotency of job run requests. If a run with the provided token
          already exists, the request does not create a new run but returns the ID of the existing run
          instead. If a run with the provided token is deleted, an error is returned.
          
          If you specify the idempotency token, upon failure you can retry until the request succeeds.
          Databricks guarantees that exactly one run is launched with that idempotency token.
          
          This token must have at most 64 characters.
          
          For more information, see [How to ensure idempotency for jobs].
          
          [How to ensure idempotency for jobs]: https://kb.databricks.com/jobs/jobs-idempotency.html
        :param jar_params: List[str] (optional)
          A list of parameters for jobs with Spark JAR tasks, for example `"jar_params": ["john doe", "35"]`.
          The parameters are used to invoke the main function of the main class specified in the Spark JAR
          task. If not specified upon `run-now`, it defaults to an empty list. jar_params cannot be specified
          in conjunction with notebook_params. The JSON representation of this field (for example
          `{"jar_params":["john doe","35"]}`) cannot exceed 10,000 bytes.
          
          Use [Task parameter variables](/jobs.html"#parameter-variables") to set parameters containing
          information about job runs.
        :param job_parameters: Dict[str,str] (optional)
          Job-level parameters used in the run. for example `"param": "overriding_val"`
        :param notebook_params: Dict[str,str] (optional)
          A map from keys to values for jobs with notebook task, for example `"notebook_params": {"name":
          "john doe", "age": "35"}`. The map is passed to the notebook and is accessible through the
          [dbutils.widgets.get] function.
          
          If not specified upon `run-now`, the triggered run uses the job’s base parameters.
          
          notebook_params cannot be specified in conjunction with jar_params.
          
          Use [Task parameter variables] to set parameters containing information about job runs.
          
          The JSON representation of this field (for example `{"notebook_params":{"name":"john
          doe","age":"35"}}`) cannot exceed 10,000 bytes.
          
          [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
          [dbutils.widgets.get]: https://docs.databricks.com/dev-tools/databricks-utils.html
        :param pipeline_params: :class:`PipelineParams` (optional)
        :param python_named_params: Dict[str,str] (optional)
          A map from keys to values for jobs with Python wheel task, for example `"python_named_params":
          {"name": "task", "data": "dbfs:/path/to/data.json"}`.
        :param python_params: List[str] (optional)
          A list of parameters for jobs with Python tasks, for example `"python_params": ["john doe", "35"]`.
          The parameters are passed to Python file as command-line parameters. If specified upon `run-now`, it
          would overwrite the parameters specified in job setting. The JSON representation of this field (for
          example `{"python_params":["john doe","35"]}`) cannot exceed 10,000 bytes.
          
          Use [Task parameter variables] to set parameters containing information about job runs.
          
          Important
          
          These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters
          returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and
          emojis.
          
          [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
        :param queue: :class:`QueueSettings` (optional)
          The queue settings of the run.
        :param spark_submit_params: List[str] (optional)
          A list of parameters for jobs with spark submit task, for example `"spark_submit_params":
          ["--class", "org.apache.spark.examples.SparkPi"]`. The parameters are passed to spark-submit script
          as command-line parameters. If specified upon `run-now`, it would overwrite the parameters specified
          in job setting. The JSON representation of this field (for example `{"python_params":["john
          doe","35"]}`) cannot exceed 10,000 bytes.
          
          Use [Task parameter variables] to set parameters containing information about job runs
          
          Important
          
          These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters
          returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and
          emojis.
          
          [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
        :param sql_params: Dict[str,str] (optional)
          A map from keys to values for jobs with SQL task, for example `"sql_params": {"name": "john doe",
          "age": "35"}`. The SQL alert task does not support custom parameters.
        
        :returns:
          Long-running operation waiter for :class:`Run`.
          See :method:wait_get_run_job_terminated_or_skipped for more details.
        """
        body = {}
        if dbt_commands is not None: body['dbt_commands'] = [v for v in dbt_commands]
        if idempotency_token is not None: body['idempotency_token'] = idempotency_token
        if jar_params is not None: body['jar_params'] = [v for v in jar_params]
        if job_id is not None: body['job_id'] = job_id
        if job_parameters is not None: body['job_parameters'] = job_parameters
        if notebook_params is not None: body['notebook_params'] = notebook_params
        if pipeline_params is not None: body['pipeline_params'] = pipeline_params.as_dict()
        if python_named_params is not None: body['python_named_params'] = python_named_params
        if python_params is not None: body['python_params'] = [v for v in python_params]
        if queue is not None: body['queue'] = queue.as_dict()
        if spark_submit_params is not None: body['spark_submit_params'] = [v for v in spark_submit_params]
        if sql_params is not None: body['sql_params'] = sql_params
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        op_response = self._api.do('POST', '/api/2.1/jobs/run-now', body=body, headers=headers)
        return Wait(self.wait_get_run_job_terminated_or_skipped,
                    response=RunNowResponse.from_dict(op_response),
                    run_id=op_response['run_id'])

    def run_now_and_wait(self,
                         job_id: int,
                         *,
                         dbt_commands: Optional[List[str]] = None,
                         idempotency_token: Optional[str] = None,
                         jar_params: Optional[List[str]] = None,
                         job_parameters: Optional[Dict[str, str]] = None,
                         notebook_params: Optional[Dict[str, str]] = None,
                         pipeline_params: Optional[PipelineParams] = None,
                         python_named_params: Optional[Dict[str, str]] = None,
                         python_params: Optional[List[str]] = None,
                         queue: Optional[QueueSettings] = None,
                         spark_submit_params: Optional[List[str]] = None,
                         sql_params: Optional[Dict[str, str]] = None,
                         timeout=timedelta(minutes=20)) -> Run:
        return self.run_now(dbt_commands=dbt_commands,
                            idempotency_token=idempotency_token,
                            jar_params=jar_params,
                            job_id=job_id,
                            job_parameters=job_parameters,
                            notebook_params=notebook_params,
                            pipeline_params=pipeline_params,
                            python_named_params=python_named_params,
                            python_params=python_params,
                            queue=queue,
                            spark_submit_params=spark_submit_params,
                            sql_params=sql_params).result(timeout=timeout)

    def set_permissions(
            self,
            job_id: str,
            *,
            access_control_list: Optional[List[JobAccessControlRequest]] = None) -> JobPermissions:
        """Set job permissions.
        
        Sets permissions on a job. Jobs can inherit permissions from their root object.
        
        :param job_id: str
          The job for which to get or manage permissions.
        :param access_control_list: List[:class:`JobAccessControlRequest`] (optional)
        
        :returns: :class:`JobPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PUT', f'/api/2.0/permissions/jobs/{job_id}', body=body, headers=headers)
        return JobPermissions.from_dict(res)

    def submit(self,
               *,
               access_control_list: Optional[List[iam.AccessControlRequest]] = None,
               email_notifications: Optional[JobEmailNotifications] = None,
               git_source: Optional[GitSource] = None,
               health: Optional[JobsHealthRules] = None,
               idempotency_token: Optional[str] = None,
               notification_settings: Optional[JobNotificationSettings] = None,
               queue: Optional[QueueSettings] = None,
               run_name: Optional[str] = None,
               tasks: Optional[List[SubmitTask]] = None,
               timeout_seconds: Optional[int] = None,
               webhook_notifications: Optional[WebhookNotifications] = None) -> Wait[Run]:
        """Create and trigger a one-time run.
        
        Submit a one-time run. This endpoint allows you to submit a workload directly without creating a job.
        Runs submitted using this endpoint don’t display in the UI. Use the `jobs/runs/get` API to check the
        run state after the job is submitted.
        
        :param access_control_list: List[:class:`AccessControlRequest`] (optional)
          List of permissions to set on the job.
        :param email_notifications: :class:`JobEmailNotifications` (optional)
          An optional set of email addresses notified when the run begins or completes.
        :param git_source: :class:`GitSource` (optional)
          An optional specification for a remote Git repository containing the source code used by tasks.
          Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks.
          
          If `git_source` is set, these tasks retrieve the file from the remote repository by default.
          However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task.
          
          Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are
          used, `git_source` must be defined on the job.
        :param health: :class:`JobsHealthRules` (optional)
          An optional set of health rules that can be defined for this job.
        :param idempotency_token: str (optional)
          An optional token that can be used to guarantee the idempotency of job run requests. If a run with
          the provided token already exists, the request does not create a new run but returns the ID of the
          existing run instead. If a run with the provided token is deleted, an error is returned.
          
          If you specify the idempotency token, upon failure you can retry until the request succeeds.
          Databricks guarantees that exactly one run is launched with that idempotency token.
          
          This token must have at most 64 characters.
          
          For more information, see [How to ensure idempotency for jobs].
          
          [How to ensure idempotency for jobs]: https://kb.databricks.com/jobs/jobs-idempotency.html
        :param notification_settings: :class:`JobNotificationSettings` (optional)
          Optional notification settings that are used when sending notifications to each of the
          `email_notifications` and `webhook_notifications` for this run.
        :param queue: :class:`QueueSettings` (optional)
          The queue settings of the one-time run.
        :param run_name: str (optional)
          An optional name for the run. The default value is `Untitled`.
        :param tasks: List[:class:`SubmitTask`] (optional)
        :param timeout_seconds: int (optional)
          An optional timeout applied to each run of this job. A value of `0` means no timeout.
        :param webhook_notifications: :class:`WebhookNotifications` (optional)
          A collection of system notification IDs to notify when the run begins or completes.
        
        :returns:
          Long-running operation waiter for :class:`Run`.
          See :method:wait_get_run_job_terminated_or_skipped for more details.
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        if email_notifications is not None: body['email_notifications'] = email_notifications.as_dict()
        if git_source is not None: body['git_source'] = git_source.as_dict()
        if health is not None: body['health'] = health.as_dict()
        if idempotency_token is not None: body['idempotency_token'] = idempotency_token
        if notification_settings is not None: body['notification_settings'] = notification_settings.as_dict()
        if queue is not None: body['queue'] = queue.as_dict()
        if run_name is not None: body['run_name'] = run_name
        if tasks is not None: body['tasks'] = [v.as_dict() for v in tasks]
        if timeout_seconds is not None: body['timeout_seconds'] = timeout_seconds
        if webhook_notifications is not None: body['webhook_notifications'] = webhook_notifications.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        op_response = self._api.do('POST', '/api/2.1/jobs/runs/submit', body=body, headers=headers)
        return Wait(self.wait_get_run_job_terminated_or_skipped,
                    response=SubmitRunResponse.from_dict(op_response),
                    run_id=op_response['run_id'])

    def submit_and_wait(
        self,
        *,
        access_control_list: Optional[List[iam.AccessControlRequest]] = None,
        email_notifications: Optional[JobEmailNotifications] = None,
        git_source: Optional[GitSource] = None,
        health: Optional[JobsHealthRules] = None,
        idempotency_token: Optional[str] = None,
        notification_settings: Optional[JobNotificationSettings] = None,
        queue: Optional[QueueSettings] = None,
        run_name: Optional[str] = None,
        tasks: Optional[List[SubmitTask]] = None,
        timeout_seconds: Optional[int] = None,
        webhook_notifications: Optional[WebhookNotifications] = None,
        timeout=timedelta(minutes=20)) -> Run:
        return self.submit(access_control_list=access_control_list,
                           email_notifications=email_notifications,
                           git_source=git_source,
                           health=health,
                           idempotency_token=idempotency_token,
                           notification_settings=notification_settings,
                           queue=queue,
                           run_name=run_name,
                           tasks=tasks,
                           timeout_seconds=timeout_seconds,
                           webhook_notifications=webhook_notifications).result(timeout=timeout)

    def update(self,
               job_id: int,
               *,
               fields_to_remove: Optional[List[str]] = None,
               new_settings: Optional[JobSettings] = None):
        """Partially update a job.
        
        Add, update, or remove specific settings of an existing job. Use the ResetJob to overwrite all job
        settings.
        
        :param job_id: int
          The canonical identifier of the job to update. This field is required.
        :param fields_to_remove: List[str] (optional)
          Remove top-level fields in the job settings. Removing nested fields is not supported, except for
          tasks and job clusters (`tasks/task_1`). This field is optional.
        :param new_settings: :class:`JobSettings` (optional)
          The new settings for the job.
          
          Top-level fields specified in `new_settings` are completely replaced, except for arrays which are
          merged. That is, new and existing entries are completely replaced based on the respective key
          fields, i.e. `task_key` or `job_cluster_key`, while previous entries are kept.
          
          Partially updating nested fields is not supported.
          
          Changes to the field `JobSettings.timeout_seconds` are applied to active runs. Changes to other
          fields are applied to future runs only.
        
        
        """
        body = {}
        if fields_to_remove is not None: body['fields_to_remove'] = [v for v in fields_to_remove]
        if job_id is not None: body['job_id'] = job_id
        if new_settings is not None: body['new_settings'] = new_settings.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.1/jobs/update', body=body, headers=headers)

    def update_permissions(
            self,
            job_id: str,
            *,
            access_control_list: Optional[List[JobAccessControlRequest]] = None) -> JobPermissions:
        """Update job permissions.
        
        Updates the permissions on a job. Jobs can inherit permissions from their root object.
        
        :param job_id: str
          The job for which to get or manage permissions.
        :param access_control_list: List[:class:`JobAccessControlRequest`] (optional)
        
        :returns: :class:`JobPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PATCH', f'/api/2.0/permissions/jobs/{job_id}', body=body, headers=headers)
        return JobPermissions.from_dict(res)

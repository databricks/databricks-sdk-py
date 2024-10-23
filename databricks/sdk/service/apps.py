# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
import random
import time
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Callable, Dict, Iterator, List, Optional

from ..errors import OperationFailed
from ._internal import Wait, _enum, _from_dict, _repeated_dict

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class App:
    name: str
    """The name of the app. The name must contain only lowercase alphanumeric characters and hyphens.
    It must be unique within the workspace."""

    active_deployment: Optional[AppDeployment] = None
    """The active deployment of the app. A deployment is considered active when it has been deployed to
    the app compute."""

    app_status: Optional[ApplicationStatus] = None

    compute_status: Optional[ComputeStatus] = None

    create_time: Optional[str] = None
    """The creation time of the app. Formatted timestamp in ISO 6801."""

    creator: Optional[str] = None
    """The email of the user that created the app."""

    default_source_code_path: Optional[str] = None
    """The default workspace file system path of the source code from which app deployment are created.
    This field tracks the workspace source code path of the last active deployment."""

    description: Optional[str] = None
    """The description of the app."""

    pending_deployment: Optional[AppDeployment] = None
    """The pending deployment of the app. A deployment is considered pending when it is being prepared
    for deployment to the app compute."""

    resources: Optional[List[AppResource]] = None
    """Resources for the app."""

    service_principal_id: Optional[int] = None

    service_principal_name: Optional[str] = None

    update_time: Optional[str] = None
    """The update time of the app. Formatted timestamp in ISO 6801."""

    updater: Optional[str] = None
    """The email of the user that last updated the app."""

    url: Optional[str] = None
    """The URL of the app once it is deployed."""

    def as_dict(self) -> dict:
        """Serializes the App into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.active_deployment: body['active_deployment'] = self.active_deployment.as_dict()
        if self.app_status: body['app_status'] = self.app_status.as_dict()
        if self.compute_status: body['compute_status'] = self.compute_status.as_dict()
        if self.create_time is not None: body['create_time'] = self.create_time
        if self.creator is not None: body['creator'] = self.creator
        if self.default_source_code_path is not None:
            body['default_source_code_path'] = self.default_source_code_path
        if self.description is not None: body['description'] = self.description
        if self.name is not None: body['name'] = self.name
        if self.pending_deployment: body['pending_deployment'] = self.pending_deployment.as_dict()
        if self.resources: body['resources'] = [v.as_dict() for v in self.resources]
        if self.service_principal_id is not None: body['service_principal_id'] = self.service_principal_id
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.update_time is not None: body['update_time'] = self.update_time
        if self.updater is not None: body['updater'] = self.updater
        if self.url is not None: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> App:
        """Deserializes the App from a dictionary."""
        return cls(active_deployment=_from_dict(d, 'active_deployment', AppDeployment),
                   app_status=_from_dict(d, 'app_status', ApplicationStatus),
                   compute_status=_from_dict(d, 'compute_status', ComputeStatus),
                   create_time=d.get('create_time', None),
                   creator=d.get('creator', None),
                   default_source_code_path=d.get('default_source_code_path', None),
                   description=d.get('description', None),
                   name=d.get('name', None),
                   pending_deployment=_from_dict(d, 'pending_deployment', AppDeployment),
                   resources=_repeated_dict(d, 'resources', AppResource),
                   service_principal_id=d.get('service_principal_id', None),
                   service_principal_name=d.get('service_principal_name', None),
                   update_time=d.get('update_time', None),
                   updater=d.get('updater', None),
                   url=d.get('url', None))


@dataclass
class AppAccessControlRequest:
    group_name: Optional[str] = None
    """name of the group"""

    permission_level: Optional[AppPermissionLevel] = None
    """Permission level"""

    service_principal_name: Optional[str] = None
    """application ID of a service principal"""

    user_name: Optional[str] = None
    """name of the user"""

    def as_dict(self) -> dict:
        """Serializes the AppAccessControlRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AppAccessControlRequest:
        """Deserializes the AppAccessControlRequest from a dictionary."""
        return cls(group_name=d.get('group_name', None),
                   permission_level=_enum(d, 'permission_level', AppPermissionLevel),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class AppAccessControlResponse:
    all_permissions: Optional[List[AppPermission]] = None
    """All permissions."""

    display_name: Optional[str] = None
    """Display name of the user or service principal."""

    group_name: Optional[str] = None
    """name of the group"""

    service_principal_name: Optional[str] = None
    """Name of the service principal."""

    user_name: Optional[str] = None
    """name of the user"""

    def as_dict(self) -> dict:
        """Serializes the AppAccessControlResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.all_permissions: body['all_permissions'] = [v.as_dict() for v in self.all_permissions]
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AppAccessControlResponse:
        """Deserializes the AppAccessControlResponse from a dictionary."""
        return cls(all_permissions=_repeated_dict(d, 'all_permissions', AppPermission),
                   display_name=d.get('display_name', None),
                   group_name=d.get('group_name', None),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class AppDeployment:
    create_time: Optional[str] = None
    """The creation time of the deployment. Formatted timestamp in ISO 6801."""

    creator: Optional[str] = None
    """The email of the user creates the deployment."""

    deployment_artifacts: Optional[AppDeploymentArtifacts] = None
    """The deployment artifacts for an app."""

    deployment_id: Optional[str] = None
    """The unique id of the deployment."""

    mode: Optional[AppDeploymentMode] = None
    """The mode of which the deployment will manage the source code."""

    source_code_path: Optional[str] = None
    """The workspace file system path of the source code used to create the app deployment. This is
    different from `deployment_artifacts.source_code_path`, which is the path used by the deployed
    app. The former refers to the original source code location of the app in the workspace during
    deployment creation, whereas the latter provides a system generated stable snapshotted source
    code path used by the deployment."""

    status: Optional[AppDeploymentStatus] = None
    """Status and status message of the deployment"""

    update_time: Optional[str] = None
    """The update time of the deployment. Formatted timestamp in ISO 6801."""

    def as_dict(self) -> dict:
        """Serializes the AppDeployment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None: body['create_time'] = self.create_time
        if self.creator is not None: body['creator'] = self.creator
        if self.deployment_artifacts: body['deployment_artifacts'] = self.deployment_artifacts.as_dict()
        if self.deployment_id is not None: body['deployment_id'] = self.deployment_id
        if self.mode is not None: body['mode'] = self.mode.value
        if self.source_code_path is not None: body['source_code_path'] = self.source_code_path
        if self.status: body['status'] = self.status.as_dict()
        if self.update_time is not None: body['update_time'] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AppDeployment:
        """Deserializes the AppDeployment from a dictionary."""
        return cls(create_time=d.get('create_time', None),
                   creator=d.get('creator', None),
                   deployment_artifacts=_from_dict(d, 'deployment_artifacts', AppDeploymentArtifacts),
                   deployment_id=d.get('deployment_id', None),
                   mode=_enum(d, 'mode', AppDeploymentMode),
                   source_code_path=d.get('source_code_path', None),
                   status=_from_dict(d, 'status', AppDeploymentStatus),
                   update_time=d.get('update_time', None))


@dataclass
class AppDeploymentArtifacts:
    source_code_path: Optional[str] = None
    """The snapshotted workspace file system path of the source code loaded by the deployed app."""

    def as_dict(self) -> dict:
        """Serializes the AppDeploymentArtifacts into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.source_code_path is not None: body['source_code_path'] = self.source_code_path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AppDeploymentArtifacts:
        """Deserializes the AppDeploymentArtifacts from a dictionary."""
        return cls(source_code_path=d.get('source_code_path', None))


class AppDeploymentMode(Enum):

    AUTO_SYNC = 'AUTO_SYNC'
    SNAPSHOT = 'SNAPSHOT'


class AppDeploymentState(Enum):

    CANCELLED = 'CANCELLED'
    FAILED = 'FAILED'
    IN_PROGRESS = 'IN_PROGRESS'
    SUCCEEDED = 'SUCCEEDED'


@dataclass
class AppDeploymentStatus:
    message: Optional[str] = None
    """Message corresponding with the deployment state."""

    state: Optional[AppDeploymentState] = None
    """State of the deployment."""

    def as_dict(self) -> dict:
        """Serializes the AppDeploymentStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.message is not None: body['message'] = self.message
        if self.state is not None: body['state'] = self.state.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AppDeploymentStatus:
        """Deserializes the AppDeploymentStatus from a dictionary."""
        return cls(message=d.get('message', None), state=_enum(d, 'state', AppDeploymentState))


@dataclass
class AppPermission:
    inherited: Optional[bool] = None

    inherited_from_object: Optional[List[str]] = None

    permission_level: Optional[AppPermissionLevel] = None
    """Permission level"""

    def as_dict(self) -> dict:
        """Serializes the AppPermission into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.inherited is not None: body['inherited'] = self.inherited
        if self.inherited_from_object: body['inherited_from_object'] = [v for v in self.inherited_from_object]
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AppPermission:
        """Deserializes the AppPermission from a dictionary."""
        return cls(inherited=d.get('inherited', None),
                   inherited_from_object=d.get('inherited_from_object', None),
                   permission_level=_enum(d, 'permission_level', AppPermissionLevel))


class AppPermissionLevel(Enum):
    """Permission level"""

    CAN_MANAGE = 'CAN_MANAGE'
    CAN_USE = 'CAN_USE'


@dataclass
class AppPermissions:
    access_control_list: Optional[List[AppAccessControlResponse]] = None

    object_id: Optional[str] = None

    object_type: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the AppPermissions into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.object_id is not None: body['object_id'] = self.object_id
        if self.object_type is not None: body['object_type'] = self.object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AppPermissions:
        """Deserializes the AppPermissions from a dictionary."""
        return cls(access_control_list=_repeated_dict(d, 'access_control_list', AppAccessControlResponse),
                   object_id=d.get('object_id', None),
                   object_type=d.get('object_type', None))


@dataclass
class AppPermissionsDescription:
    description: Optional[str] = None

    permission_level: Optional[AppPermissionLevel] = None
    """Permission level"""

    def as_dict(self) -> dict:
        """Serializes the AppPermissionsDescription into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AppPermissionsDescription:
        """Deserializes the AppPermissionsDescription from a dictionary."""
        return cls(description=d.get('description', None),
                   permission_level=_enum(d, 'permission_level', AppPermissionLevel))


@dataclass
class AppPermissionsRequest:
    access_control_list: Optional[List[AppAccessControlRequest]] = None

    app_name: Optional[str] = None
    """The app for which to get or manage permissions."""

    def as_dict(self) -> dict:
        """Serializes the AppPermissionsRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.app_name is not None: body['app_name'] = self.app_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AppPermissionsRequest:
        """Deserializes the AppPermissionsRequest from a dictionary."""
        return cls(access_control_list=_repeated_dict(d, 'access_control_list', AppAccessControlRequest),
                   app_name=d.get('app_name', None))


@dataclass
class AppResource:
    name: str
    """Name of the App Resource."""

    description: Optional[str] = None
    """Description of the App Resource."""

    job: Optional[AppResourceJob] = None

    secret: Optional[AppResourceSecret] = None

    serving_endpoint: Optional[AppResourceServingEndpoint] = None

    sql_warehouse: Optional[AppResourceSqlWarehouse] = None

    def as_dict(self) -> dict:
        """Serializes the AppResource into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.job: body['job'] = self.job.as_dict()
        if self.name is not None: body['name'] = self.name
        if self.secret: body['secret'] = self.secret.as_dict()
        if self.serving_endpoint: body['serving_endpoint'] = self.serving_endpoint.as_dict()
        if self.sql_warehouse: body['sql_warehouse'] = self.sql_warehouse.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AppResource:
        """Deserializes the AppResource from a dictionary."""
        return cls(description=d.get('description', None),
                   job=_from_dict(d, 'job', AppResourceJob),
                   name=d.get('name', None),
                   secret=_from_dict(d, 'secret', AppResourceSecret),
                   serving_endpoint=_from_dict(d, 'serving_endpoint', AppResourceServingEndpoint),
                   sql_warehouse=_from_dict(d, 'sql_warehouse', AppResourceSqlWarehouse))


@dataclass
class AppResourceJob:
    id: str
    """Id of the job to grant permission on."""

    permission: AppResourceJobJobPermission
    """Permissions to grant on the Job. Supported permissions are: "CAN_MANAGE", "IS_OWNER",
    "CAN_MANAGE_RUN", "CAN_VIEW"."""

    def as_dict(self) -> dict:
        """Serializes the AppResourceJob into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.id is not None: body['id'] = self.id
        if self.permission is not None: body['permission'] = self.permission.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AppResourceJob:
        """Deserializes the AppResourceJob from a dictionary."""
        return cls(id=d.get('id', None), permission=_enum(d, 'permission', AppResourceJobJobPermission))


class AppResourceJobJobPermission(Enum):

    CAN_MANAGE = 'CAN_MANAGE'
    CAN_MANAGE_RUN = 'CAN_MANAGE_RUN'
    CAN_VIEW = 'CAN_VIEW'
    IS_OWNER = 'IS_OWNER'


@dataclass
class AppResourceSecret:
    scope: str
    """Scope of the secret to grant permission on."""

    key: str
    """Key of the secret to grant permission on."""

    permission: AppResourceSecretSecretPermission
    """Permission to grant on the secret scope. For secrets, only one permission is allowed. Permission
    must be one of: "READ", "WRITE", "MANAGE"."""

    def as_dict(self) -> dict:
        """Serializes the AppResourceSecret into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.permission is not None: body['permission'] = self.permission.value
        if self.scope is not None: body['scope'] = self.scope
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AppResourceSecret:
        """Deserializes the AppResourceSecret from a dictionary."""
        return cls(key=d.get('key', None),
                   permission=_enum(d, 'permission', AppResourceSecretSecretPermission),
                   scope=d.get('scope', None))


class AppResourceSecretSecretPermission(Enum):
    """Permission to grant on the secret scope. Supported permissions are: "READ", "WRITE", "MANAGE"."""

    MANAGE = 'MANAGE'
    READ = 'READ'
    WRITE = 'WRITE'


@dataclass
class AppResourceServingEndpoint:
    name: str
    """Name of the serving endpoint to grant permission on."""

    permission: AppResourceServingEndpointServingEndpointPermission
    """Permission to grant on the serving endpoint. Supported permissions are: "CAN_MANAGE",
    "CAN_QUERY", "CAN_VIEW"."""

    def as_dict(self) -> dict:
        """Serializes the AppResourceServingEndpoint into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.permission is not None: body['permission'] = self.permission.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AppResourceServingEndpoint:
        """Deserializes the AppResourceServingEndpoint from a dictionary."""
        return cls(name=d.get('name', None),
                   permission=_enum(d, 'permission', AppResourceServingEndpointServingEndpointPermission))


class AppResourceServingEndpointServingEndpointPermission(Enum):

    CAN_MANAGE = 'CAN_MANAGE'
    CAN_QUERY = 'CAN_QUERY'
    CAN_VIEW = 'CAN_VIEW'


@dataclass
class AppResourceSqlWarehouse:
    id: str
    """Id of the SQL warehouse to grant permission on."""

    permission: AppResourceSqlWarehouseSqlWarehousePermission
    """Permission to grant on the SQL warehouse. Supported permissions are: "CAN_MANAGE", "CAN_USE",
    "IS_OWNER"."""

    def as_dict(self) -> dict:
        """Serializes the AppResourceSqlWarehouse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.id is not None: body['id'] = self.id
        if self.permission is not None: body['permission'] = self.permission.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AppResourceSqlWarehouse:
        """Deserializes the AppResourceSqlWarehouse from a dictionary."""
        return cls(id=d.get('id', None),
                   permission=_enum(d, 'permission', AppResourceSqlWarehouseSqlWarehousePermission))


class AppResourceSqlWarehouseSqlWarehousePermission(Enum):

    CAN_MANAGE = 'CAN_MANAGE'
    CAN_USE = 'CAN_USE'
    IS_OWNER = 'IS_OWNER'


class ApplicationState(Enum):

    CRASHED = 'CRASHED'
    DEPLOYING = 'DEPLOYING'
    RUNNING = 'RUNNING'
    UNAVAILABLE = 'UNAVAILABLE'


@dataclass
class ApplicationStatus:
    message: Optional[str] = None
    """Application status message"""

    state: Optional[ApplicationState] = None
    """State of the application."""

    def as_dict(self) -> dict:
        """Serializes the ApplicationStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.message is not None: body['message'] = self.message
        if self.state is not None: body['state'] = self.state.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ApplicationStatus:
        """Deserializes the ApplicationStatus from a dictionary."""
        return cls(message=d.get('message', None), state=_enum(d, 'state', ApplicationState))


class ComputeState(Enum):

    ACTIVE = 'ACTIVE'
    DELETING = 'DELETING'
    ERROR = 'ERROR'
    STARTING = 'STARTING'
    STOPPED = 'STOPPED'
    STOPPING = 'STOPPING'
    UPDATING = 'UPDATING'


@dataclass
class ComputeStatus:
    message: Optional[str] = None
    """Compute status message"""

    state: Optional[ComputeState] = None
    """State of the app compute."""

    def as_dict(self) -> dict:
        """Serializes the ComputeStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.message is not None: body['message'] = self.message
        if self.state is not None: body['state'] = self.state.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ComputeStatus:
        """Deserializes the ComputeStatus from a dictionary."""
        return cls(message=d.get('message', None), state=_enum(d, 'state', ComputeState))


@dataclass
class CreateAppDeploymentRequest:
    app_name: Optional[str] = None
    """The name of the app."""

    deployment_id: Optional[str] = None
    """The unique id of the deployment."""

    mode: Optional[AppDeploymentMode] = None
    """The mode of which the deployment will manage the source code."""

    source_code_path: Optional[str] = None
    """The workspace file system path of the source code used to create the app deployment. This is
    different from `deployment_artifacts.source_code_path`, which is the path used by the deployed
    app. The former refers to the original source code location of the app in the workspace during
    deployment creation, whereas the latter provides a system generated stable snapshotted source
    code path used by the deployment."""

    def as_dict(self) -> dict:
        """Serializes the CreateAppDeploymentRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.app_name is not None: body['app_name'] = self.app_name
        if self.deployment_id is not None: body['deployment_id'] = self.deployment_id
        if self.mode is not None: body['mode'] = self.mode.value
        if self.source_code_path is not None: body['source_code_path'] = self.source_code_path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateAppDeploymentRequest:
        """Deserializes the CreateAppDeploymentRequest from a dictionary."""
        return cls(app_name=d.get('app_name', None),
                   deployment_id=d.get('deployment_id', None),
                   mode=_enum(d, 'mode', AppDeploymentMode),
                   source_code_path=d.get('source_code_path', None))


@dataclass
class CreateAppRequest:
    name: str
    """The name of the app. The name must contain only lowercase alphanumeric characters and hyphens.
    It must be unique within the workspace."""

    description: Optional[str] = None
    """The description of the app."""

    resources: Optional[List[AppResource]] = None
    """Resources for the app."""

    def as_dict(self) -> dict:
        """Serializes the CreateAppRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.name is not None: body['name'] = self.name
        if self.resources: body['resources'] = [v.as_dict() for v in self.resources]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateAppRequest:
        """Deserializes the CreateAppRequest from a dictionary."""
        return cls(description=d.get('description', None),
                   name=d.get('name', None),
                   resources=_repeated_dict(d, 'resources', AppResource))


@dataclass
class GetAppPermissionLevelsResponse:
    permission_levels: Optional[List[AppPermissionsDescription]] = None
    """Specific permission levels"""

    def as_dict(self) -> dict:
        """Serializes the GetAppPermissionLevelsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permission_levels: body['permission_levels'] = [v.as_dict() for v in self.permission_levels]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetAppPermissionLevelsResponse:
        """Deserializes the GetAppPermissionLevelsResponse from a dictionary."""
        return cls(permission_levels=_repeated_dict(d, 'permission_levels', AppPermissionsDescription))


@dataclass
class ListAppDeploymentsResponse:
    app_deployments: Optional[List[AppDeployment]] = None
    """Deployment history of the app."""

    next_page_token: Optional[str] = None
    """Pagination token to request the next page of apps."""

    def as_dict(self) -> dict:
        """Serializes the ListAppDeploymentsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.app_deployments: body['app_deployments'] = [v.as_dict() for v in self.app_deployments]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListAppDeploymentsResponse:
        """Deserializes the ListAppDeploymentsResponse from a dictionary."""
        return cls(app_deployments=_repeated_dict(d, 'app_deployments', AppDeployment),
                   next_page_token=d.get('next_page_token', None))


@dataclass
class ListAppsResponse:
    apps: Optional[List[App]] = None

    next_page_token: Optional[str] = None
    """Pagination token to request the next page of apps."""

    def as_dict(self) -> dict:
        """Serializes the ListAppsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.apps: body['apps'] = [v.as_dict() for v in self.apps]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListAppsResponse:
        """Deserializes the ListAppsResponse from a dictionary."""
        return cls(apps=_repeated_dict(d, 'apps', App), next_page_token=d.get('next_page_token', None))


@dataclass
class StartAppRequest:
    name: Optional[str] = None
    """The name of the app."""


@dataclass
class StopAppRequest:
    name: Optional[str] = None
    """The name of the app."""


@dataclass
class UpdateAppRequest:
    name: str
    """The name of the app. The name must contain only lowercase alphanumeric characters and hyphens.
    It must be unique within the workspace."""

    description: Optional[str] = None
    """The description of the app."""

    resources: Optional[List[AppResource]] = None
    """Resources for the app."""

    def as_dict(self) -> dict:
        """Serializes the UpdateAppRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.name is not None: body['name'] = self.name
        if self.resources: body['resources'] = [v.as_dict() for v in self.resources]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateAppRequest:
        """Deserializes the UpdateAppRequest from a dictionary."""
        return cls(description=d.get('description', None),
                   name=d.get('name', None),
                   resources=_repeated_dict(d, 'resources', AppResource))


class AppsAPI:
    """Apps run directly on a customer’s Databricks instance, integrate with their data, use and extend
    Databricks services, and enable users to interact through single sign-on."""

    def __init__(self, api_client):
        self._api = api_client

    def wait_get_app_active(self,
                            name: str,
                            timeout=timedelta(minutes=20),
                            callback: Optional[Callable[[App], None]] = None) -> App:
        deadline = time.time() + timeout.total_seconds()
        target_states = (ComputeState.ACTIVE, )
        failure_states = (ComputeState.ERROR, ComputeState.STOPPED, )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.get(name=name)
            status = poll.compute_status.state
            status_message = f'current status: {status}'
            if poll.compute_status:
                status_message = poll.compute_status.message
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f'failed to reach ACTIVE, got {status}: {status_message}'
                raise OperationFailed(msg)
            prefix = f"name={name}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f'timed out after {timeout}: {status_message}')

    def wait_get_app_stopped(self,
                             name: str,
                             timeout=timedelta(minutes=20),
                             callback: Optional[Callable[[App], None]] = None) -> App:
        deadline = time.time() + timeout.total_seconds()
        target_states = (ComputeState.STOPPED, )
        failure_states = (ComputeState.ERROR, )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.get(name=name)
            status = poll.compute_status.state
            status_message = f'current status: {status}'
            if poll.compute_status:
                status_message = poll.compute_status.message
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f'failed to reach STOPPED, got {status}: {status_message}'
                raise OperationFailed(msg)
            prefix = f"name={name}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f'timed out after {timeout}: {status_message}')

    def wait_get_deployment_app_succeeded(
            self,
            app_name: str,
            deployment_id: str,
            timeout=timedelta(minutes=20),
            callback: Optional[Callable[[AppDeployment], None]] = None) -> AppDeployment:
        deadline = time.time() + timeout.total_seconds()
        target_states = (AppDeploymentState.SUCCEEDED, )
        failure_states = (AppDeploymentState.FAILED, )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.get_deployment(app_name=app_name, deployment_id=deployment_id)
            status = poll.status.state
            status_message = f'current status: {status}'
            if poll.status:
                status_message = poll.status.message
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f'failed to reach SUCCEEDED, got {status}: {status_message}'
                raise OperationFailed(msg)
            prefix = f"app_name={app_name}, deployment_id={deployment_id}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f'timed out after {timeout}: {status_message}')

    def create(self,
               name: str,
               *,
               description: Optional[str] = None,
               resources: Optional[List[AppResource]] = None) -> Wait[App]:
        """Create an app.
        
        Creates a new app.
        
        :param name: str
          The name of the app. The name must contain only lowercase alphanumeric characters and hyphens. It
          must be unique within the workspace.
        :param description: str (optional)
          The description of the app.
        :param resources: List[:class:`AppResource`] (optional)
          Resources for the app.
        
        :returns:
          Long-running operation waiter for :class:`App`.
          See :method:wait_get_app_active for more details.
        """
        body = {}
        if description is not None: body['description'] = description
        if name is not None: body['name'] = name
        if resources is not None: body['resources'] = [v.as_dict() for v in resources]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        op_response = self._api.do('POST', '/api/2.0/apps', body=body, headers=headers)
        return Wait(self.wait_get_app_active, response=App.from_dict(op_response), name=op_response['name'])

    def create_and_wait(self,
                        name: str,
                        *,
                        description: Optional[str] = None,
                        resources: Optional[List[AppResource]] = None,
                        timeout=timedelta(minutes=20)) -> App:
        return self.create(description=description, name=name, resources=resources).result(timeout=timeout)

    def delete(self, name: str) -> App:
        """Delete an app.
        
        Deletes an app.
        
        :param name: str
          The name of the app.
        
        :returns: :class:`App`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('DELETE', f'/api/2.0/apps/{name}', headers=headers)
        return App.from_dict(res)

    def deploy(self,
               app_name: str,
               *,
               deployment_id: Optional[str] = None,
               mode: Optional[AppDeploymentMode] = None,
               source_code_path: Optional[str] = None) -> Wait[AppDeployment]:
        """Create an app deployment.
        
        Creates an app deployment for the app with the supplied name.
        
        :param app_name: str
          The name of the app.
        :param deployment_id: str (optional)
          The unique id of the deployment.
        :param mode: :class:`AppDeploymentMode` (optional)
          The mode of which the deployment will manage the source code.
        :param source_code_path: str (optional)
          The workspace file system path of the source code used to create the app deployment. This is
          different from `deployment_artifacts.source_code_path`, which is the path used by the deployed app.
          The former refers to the original source code location of the app in the workspace during deployment
          creation, whereas the latter provides a system generated stable snapshotted source code path used by
          the deployment.
        
        :returns:
          Long-running operation waiter for :class:`AppDeployment`.
          See :method:wait_get_deployment_app_succeeded for more details.
        """
        body = {}
        if deployment_id is not None: body['deployment_id'] = deployment_id
        if mode is not None: body['mode'] = mode.value
        if source_code_path is not None: body['source_code_path'] = source_code_path
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        op_response = self._api.do('POST',
                                   f'/api/2.0/apps/{app_name}/deployments',
                                   body=body,
                                   headers=headers)
        return Wait(self.wait_get_deployment_app_succeeded,
                    response=AppDeployment.from_dict(op_response),
                    app_name=app_name,
                    deployment_id=op_response['deployment_id'])

    def deploy_and_wait(
        self,
        app_name: str,
        *,
        deployment_id: Optional[str] = None,
        mode: Optional[AppDeploymentMode] = None,
        source_code_path: Optional[str] = None,
        timeout=timedelta(minutes=20)) -> AppDeployment:
        return self.deploy(app_name=app_name,
                           deployment_id=deployment_id,
                           mode=mode,
                           source_code_path=source_code_path).result(timeout=timeout)

    def get(self, name: str) -> App:
        """Get an app.
        
        Retrieves information for the app with the supplied name.
        
        :param name: str
          The name of the app.
        
        :returns: :class:`App`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/apps/{name}', headers=headers)
        return App.from_dict(res)

    def get_deployment(self, app_name: str, deployment_id: str) -> AppDeployment:
        """Get an app deployment.
        
        Retrieves information for the app deployment with the supplied name and deployment id.
        
        :param app_name: str
          The name of the app.
        :param deployment_id: str
          The unique id of the deployment.
        
        :returns: :class:`AppDeployment`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/apps/{app_name}/deployments/{deployment_id}', headers=headers)
        return AppDeployment.from_dict(res)

    def get_permission_levels(self, app_name: str) -> GetAppPermissionLevelsResponse:
        """Get app permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param app_name: str
          The app for which to get or manage permissions.
        
        :returns: :class:`GetAppPermissionLevelsResponse`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/permissions/apps/{app_name}/permissionLevels', headers=headers)
        return GetAppPermissionLevelsResponse.from_dict(res)

    def get_permissions(self, app_name: str) -> AppPermissions:
        """Get app permissions.
        
        Gets the permissions of an app. Apps can inherit permissions from their root object.
        
        :param app_name: str
          The app for which to get or manage permissions.
        
        :returns: :class:`AppPermissions`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/permissions/apps/{app_name}', headers=headers)
        return AppPermissions.from_dict(res)

    def list(self, *, page_size: Optional[int] = None, page_token: Optional[str] = None) -> Iterator[App]:
        """List apps.
        
        Lists all apps in the workspace.
        
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of apps. Requests first page if absent.
        
        :returns: Iterator over :class:`App`
        """

        query = {}
        if page_size is not None: query['page_size'] = page_size
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET', '/api/2.0/apps', query=query, headers=headers)
            if 'apps' in json:
                for v in json['apps']:
                    yield App.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def list_deployments(self,
                         app_name: str,
                         *,
                         page_size: Optional[int] = None,
                         page_token: Optional[str] = None) -> Iterator[AppDeployment]:
        """List app deployments.
        
        Lists all app deployments for the app with the supplied name.
        
        :param app_name: str
          The name of the app.
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of apps. Requests first page if absent.
        
        :returns: Iterator over :class:`AppDeployment`
        """

        query = {}
        if page_size is not None: query['page_size'] = page_size
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET', f'/api/2.0/apps/{app_name}/deployments', query=query, headers=headers)
            if 'app_deployments' in json:
                for v in json['app_deployments']:
                    yield AppDeployment.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def set_permissions(
            self,
            app_name: str,
            *,
            access_control_list: Optional[List[AppAccessControlRequest]] = None) -> AppPermissions:
        """Set app permissions.
        
        Sets permissions on an app. Apps can inherit permissions from their root object.
        
        :param app_name: str
          The app for which to get or manage permissions.
        :param access_control_list: List[:class:`AppAccessControlRequest`] (optional)
        
        :returns: :class:`AppPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PUT', f'/api/2.0/permissions/apps/{app_name}', body=body, headers=headers)
        return AppPermissions.from_dict(res)

    def start(self, name: str) -> Wait[App]:
        """Start an app.
        
        Start the last active deployment of the app in the workspace.
        
        :param name: str
          The name of the app.
        
        :returns:
          Long-running operation waiter for :class:`App`.
          See :method:wait_get_app_active for more details.
        """

        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        op_response = self._api.do('POST', f'/api/2.0/apps/{name}/start', headers=headers)
        return Wait(self.wait_get_app_active, response=App.from_dict(op_response), name=op_response['name'])

    def start_and_wait(self, name: str, timeout=timedelta(minutes=20)) -> App:
        return self.start(name=name).result(timeout=timeout)

    def stop(self, name: str) -> Wait[App]:
        """Stop an app.
        
        Stops the active deployment of the app in the workspace.
        
        :param name: str
          The name of the app.
        
        :returns:
          Long-running operation waiter for :class:`App`.
          See :method:wait_get_app_stopped for more details.
        """

        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        op_response = self._api.do('POST', f'/api/2.0/apps/{name}/stop', headers=headers)
        return Wait(self.wait_get_app_stopped, response=App.from_dict(op_response), name=op_response['name'])

    def stop_and_wait(self, name: str, timeout=timedelta(minutes=20)) -> App:
        return self.stop(name=name).result(timeout=timeout)

    def update(self,
               name: str,
               *,
               description: Optional[str] = None,
               resources: Optional[List[AppResource]] = None) -> App:
        """Update an app.
        
        Updates the app with the supplied name.
        
        :param name: str
          The name of the app. The name must contain only lowercase alphanumeric characters and hyphens. It
          must be unique within the workspace.
        :param description: str (optional)
          The description of the app.
        :param resources: List[:class:`AppResource`] (optional)
          Resources for the app.
        
        :returns: :class:`App`
        """
        body = {}
        if description is not None: body['description'] = description
        if resources is not None: body['resources'] = [v.as_dict() for v in resources]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH', f'/api/2.0/apps/{name}', body=body, headers=headers)
        return App.from_dict(res)

    def update_permissions(
            self,
            app_name: str,
            *,
            access_control_list: Optional[List[AppAccessControlRequest]] = None) -> AppPermissions:
        """Update app permissions.
        
        Updates the permissions on an app. Apps can inherit permissions from their root object.
        
        :param app_name: str
          The app for which to get or manage permissions.
        :param access_control_list: List[:class:`AppAccessControlRequest`] (optional)
        
        :returns: :class:`AppPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH', f'/api/2.0/permissions/apps/{app_name}', body=body, headers=headers)
        return AppPermissions.from_dict(res)

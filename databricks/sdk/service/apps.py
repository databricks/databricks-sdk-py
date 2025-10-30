# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
import random
import time
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Any, Callable, Dict, Iterator, List, Optional

from databricks.sdk.service._internal import (Wait, _enum, _from_dict,
                                              _repeated_dict)

from ..errors import OperationFailed

_LOG = logging.getLogger("databricks.sdk")


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

    budget_policy_id: Optional[str] = None

    compute_size: Optional[ComputeSize] = None

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

    effective_budget_policy_id: Optional[str] = None

    effective_user_api_scopes: Optional[List[str]] = None
    """The effective api scopes granted to the user access token."""

    id: Optional[str] = None
    """The unique identifier of the app."""

    oauth2_app_client_id: Optional[str] = None

    oauth2_app_integration_id: Optional[str] = None

    pending_deployment: Optional[AppDeployment] = None
    """The pending deployment of the app. A deployment is considered pending when it is being prepared
    for deployment to the app compute."""

    resources: Optional[List[AppResource]] = None
    """Resources for the app."""

    service_principal_client_id: Optional[str] = None

    service_principal_id: Optional[int] = None

    service_principal_name: Optional[str] = None

    update_time: Optional[str] = None
    """The update time of the app. Formatted timestamp in ISO 6801."""

    updater: Optional[str] = None
    """The email of the user that last updated the app."""

    url: Optional[str] = None
    """The URL of the app once it is deployed."""

    user_api_scopes: Optional[List[str]] = None

    def as_dict(self) -> dict:
        """Serializes the App into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.active_deployment:
            body["active_deployment"] = self.active_deployment.as_dict()
        if self.app_status:
            body["app_status"] = self.app_status.as_dict()
        if self.budget_policy_id is not None:
            body["budget_policy_id"] = self.budget_policy_id
        if self.compute_size is not None:
            body["compute_size"] = self.compute_size.value
        if self.compute_status:
            body["compute_status"] = self.compute_status.as_dict()
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.creator is not None:
            body["creator"] = self.creator
        if self.default_source_code_path is not None:
            body["default_source_code_path"] = self.default_source_code_path
        if self.description is not None:
            body["description"] = self.description
        if self.effective_budget_policy_id is not None:
            body["effective_budget_policy_id"] = self.effective_budget_policy_id
        if self.effective_user_api_scopes:
            body["effective_user_api_scopes"] = [v for v in self.effective_user_api_scopes]
        if self.id is not None:
            body["id"] = self.id
        if self.name is not None:
            body["name"] = self.name
        if self.oauth2_app_client_id is not None:
            body["oauth2_app_client_id"] = self.oauth2_app_client_id
        if self.oauth2_app_integration_id is not None:
            body["oauth2_app_integration_id"] = self.oauth2_app_integration_id
        if self.pending_deployment:
            body["pending_deployment"] = self.pending_deployment.as_dict()
        if self.resources:
            body["resources"] = [v.as_dict() for v in self.resources]
        if self.service_principal_client_id is not None:
            body["service_principal_client_id"] = self.service_principal_client_id
        if self.service_principal_id is not None:
            body["service_principal_id"] = self.service_principal_id
        if self.service_principal_name is not None:
            body["service_principal_name"] = self.service_principal_name
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.updater is not None:
            body["updater"] = self.updater
        if self.url is not None:
            body["url"] = self.url
        if self.user_api_scopes:
            body["user_api_scopes"] = [v for v in self.user_api_scopes]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the App into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.active_deployment:
            body["active_deployment"] = self.active_deployment
        if self.app_status:
            body["app_status"] = self.app_status
        if self.budget_policy_id is not None:
            body["budget_policy_id"] = self.budget_policy_id
        if self.compute_size is not None:
            body["compute_size"] = self.compute_size
        if self.compute_status:
            body["compute_status"] = self.compute_status
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.creator is not None:
            body["creator"] = self.creator
        if self.default_source_code_path is not None:
            body["default_source_code_path"] = self.default_source_code_path
        if self.description is not None:
            body["description"] = self.description
        if self.effective_budget_policy_id is not None:
            body["effective_budget_policy_id"] = self.effective_budget_policy_id
        if self.effective_user_api_scopes:
            body["effective_user_api_scopes"] = self.effective_user_api_scopes
        if self.id is not None:
            body["id"] = self.id
        if self.name is not None:
            body["name"] = self.name
        if self.oauth2_app_client_id is not None:
            body["oauth2_app_client_id"] = self.oauth2_app_client_id
        if self.oauth2_app_integration_id is not None:
            body["oauth2_app_integration_id"] = self.oauth2_app_integration_id
        if self.pending_deployment:
            body["pending_deployment"] = self.pending_deployment
        if self.resources:
            body["resources"] = self.resources
        if self.service_principal_client_id is not None:
            body["service_principal_client_id"] = self.service_principal_client_id
        if self.service_principal_id is not None:
            body["service_principal_id"] = self.service_principal_id
        if self.service_principal_name is not None:
            body["service_principal_name"] = self.service_principal_name
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.updater is not None:
            body["updater"] = self.updater
        if self.url is not None:
            body["url"] = self.url
        if self.user_api_scopes:
            body["user_api_scopes"] = self.user_api_scopes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> App:
        """Deserializes the App from a dictionary."""
        return cls(
            active_deployment=_from_dict(d, "active_deployment", AppDeployment),
            app_status=_from_dict(d, "app_status", ApplicationStatus),
            budget_policy_id=d.get("budget_policy_id", None),
            compute_size=_enum(d, "compute_size", ComputeSize),
            compute_status=_from_dict(d, "compute_status", ComputeStatus),
            create_time=d.get("create_time", None),
            creator=d.get("creator", None),
            default_source_code_path=d.get("default_source_code_path", None),
            description=d.get("description", None),
            effective_budget_policy_id=d.get("effective_budget_policy_id", None),
            effective_user_api_scopes=d.get("effective_user_api_scopes", None),
            id=d.get("id", None),
            name=d.get("name", None),
            oauth2_app_client_id=d.get("oauth2_app_client_id", None),
            oauth2_app_integration_id=d.get("oauth2_app_integration_id", None),
            pending_deployment=_from_dict(d, "pending_deployment", AppDeployment),
            resources=_repeated_dict(d, "resources", AppResource),
            service_principal_client_id=d.get("service_principal_client_id", None),
            service_principal_id=d.get("service_principal_id", None),
            service_principal_name=d.get("service_principal_name", None),
            update_time=d.get("update_time", None),
            updater=d.get("updater", None),
            url=d.get("url", None),
            user_api_scopes=d.get("user_api_scopes", None),
        )


@dataclass
class AppAccessControlRequest:
    group_name: Optional[str] = None
    """name of the group"""

    permission_level: Optional[AppPermissionLevel] = None

    service_principal_name: Optional[str] = None
    """application ID of a service principal"""

    user_name: Optional[str] = None
    """name of the user"""

    def as_dict(self) -> dict:
        """Serializes the AppAccessControlRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.group_name is not None:
            body["group_name"] = self.group_name
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level.value
        if self.service_principal_name is not None:
            body["service_principal_name"] = self.service_principal_name
        if self.user_name is not None:
            body["user_name"] = self.user_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppAccessControlRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.group_name is not None:
            body["group_name"] = self.group_name
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level
        if self.service_principal_name is not None:
            body["service_principal_name"] = self.service_principal_name
        if self.user_name is not None:
            body["user_name"] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppAccessControlRequest:
        """Deserializes the AppAccessControlRequest from a dictionary."""
        return cls(
            group_name=d.get("group_name", None),
            permission_level=_enum(d, "permission_level", AppPermissionLevel),
            service_principal_name=d.get("service_principal_name", None),
            user_name=d.get("user_name", None),
        )


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
        if self.all_permissions:
            body["all_permissions"] = [v.as_dict() for v in self.all_permissions]
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.group_name is not None:
            body["group_name"] = self.group_name
        if self.service_principal_name is not None:
            body["service_principal_name"] = self.service_principal_name
        if self.user_name is not None:
            body["user_name"] = self.user_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppAccessControlResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.all_permissions:
            body["all_permissions"] = self.all_permissions
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.group_name is not None:
            body["group_name"] = self.group_name
        if self.service_principal_name is not None:
            body["service_principal_name"] = self.service_principal_name
        if self.user_name is not None:
            body["user_name"] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppAccessControlResponse:
        """Deserializes the AppAccessControlResponse from a dictionary."""
        return cls(
            all_permissions=_repeated_dict(d, "all_permissions", AppPermission),
            display_name=d.get("display_name", None),
            group_name=d.get("group_name", None),
            service_principal_name=d.get("service_principal_name", None),
            user_name=d.get("user_name", None),
        )


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
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.creator is not None:
            body["creator"] = self.creator
        if self.deployment_artifacts:
            body["deployment_artifacts"] = self.deployment_artifacts.as_dict()
        if self.deployment_id is not None:
            body["deployment_id"] = self.deployment_id
        if self.mode is not None:
            body["mode"] = self.mode.value
        if self.source_code_path is not None:
            body["source_code_path"] = self.source_code_path
        if self.status:
            body["status"] = self.status.as_dict()
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppDeployment into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.creator is not None:
            body["creator"] = self.creator
        if self.deployment_artifacts:
            body["deployment_artifacts"] = self.deployment_artifacts
        if self.deployment_id is not None:
            body["deployment_id"] = self.deployment_id
        if self.mode is not None:
            body["mode"] = self.mode
        if self.source_code_path is not None:
            body["source_code_path"] = self.source_code_path
        if self.status:
            body["status"] = self.status
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppDeployment:
        """Deserializes the AppDeployment from a dictionary."""
        return cls(
            create_time=d.get("create_time", None),
            creator=d.get("creator", None),
            deployment_artifacts=_from_dict(d, "deployment_artifacts", AppDeploymentArtifacts),
            deployment_id=d.get("deployment_id", None),
            mode=_enum(d, "mode", AppDeploymentMode),
            source_code_path=d.get("source_code_path", None),
            status=_from_dict(d, "status", AppDeploymentStatus),
            update_time=d.get("update_time", None),
        )


@dataclass
class AppDeploymentArtifacts:
    source_code_path: Optional[str] = None
    """The snapshotted workspace file system path of the source code loaded by the deployed app."""

    def as_dict(self) -> dict:
        """Serializes the AppDeploymentArtifacts into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.source_code_path is not None:
            body["source_code_path"] = self.source_code_path
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppDeploymentArtifacts into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.source_code_path is not None:
            body["source_code_path"] = self.source_code_path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppDeploymentArtifacts:
        """Deserializes the AppDeploymentArtifacts from a dictionary."""
        return cls(source_code_path=d.get("source_code_path", None))


class AppDeploymentMode(Enum):

    AUTO_SYNC = "AUTO_SYNC"
    SNAPSHOT = "SNAPSHOT"


class AppDeploymentState(Enum):

    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"


@dataclass
class AppDeploymentStatus:
    message: Optional[str] = None
    """Message corresponding with the deployment state."""

    state: Optional[AppDeploymentState] = None
    """State of the deployment."""

    def as_dict(self) -> dict:
        """Serializes the AppDeploymentStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.message is not None:
            body["message"] = self.message
        if self.state is not None:
            body["state"] = self.state.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppDeploymentStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.message is not None:
            body["message"] = self.message
        if self.state is not None:
            body["state"] = self.state
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppDeploymentStatus:
        """Deserializes the AppDeploymentStatus from a dictionary."""
        return cls(message=d.get("message", None), state=_enum(d, "state", AppDeploymentState))


@dataclass
class AppManifest:
    """App manifest definition"""

    version: int
    """The manifest schema version, for now only 1 is allowed"""

    name: str
    """Name of the app defined by manifest author / publisher"""

    description: Optional[str] = None
    """Description of the app defined by manifest author / publisher"""

    resource_specs: Optional[List[AppManifestAppResourceSpec]] = None

    def as_dict(self) -> dict:
        """Serializes the AppManifest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.name is not None:
            body["name"] = self.name
        if self.resource_specs:
            body["resource_specs"] = [v.as_dict() for v in self.resource_specs]
        if self.version is not None:
            body["version"] = self.version
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppManifest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.name is not None:
            body["name"] = self.name
        if self.resource_specs:
            body["resource_specs"] = self.resource_specs
        if self.version is not None:
            body["version"] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppManifest:
        """Deserializes the AppManifest from a dictionary."""
        return cls(
            description=d.get("description", None),
            name=d.get("name", None),
            resource_specs=_repeated_dict(d, "resource_specs", AppManifestAppResourceSpec),
            version=d.get("version", None),
        )


@dataclass
class AppManifestAppResourceJobSpec:
    permission: AppManifestAppResourceJobSpecJobPermission
    """Permissions to grant on the Job. Supported permissions are: "CAN_MANAGE", "IS_OWNER",
    "CAN_MANAGE_RUN", "CAN_VIEW"."""

    def as_dict(self) -> dict:
        """Serializes the AppManifestAppResourceJobSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permission is not None:
            body["permission"] = self.permission.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppManifestAppResourceJobSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.permission is not None:
            body["permission"] = self.permission
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppManifestAppResourceJobSpec:
        """Deserializes the AppManifestAppResourceJobSpec from a dictionary."""
        return cls(permission=_enum(d, "permission", AppManifestAppResourceJobSpecJobPermission))


class AppManifestAppResourceJobSpecJobPermission(Enum):

    CAN_MANAGE = "CAN_MANAGE"
    CAN_MANAGE_RUN = "CAN_MANAGE_RUN"
    CAN_VIEW = "CAN_VIEW"
    IS_OWNER = "IS_OWNER"


@dataclass
class AppManifestAppResourceSecretSpec:
    permission: AppManifestAppResourceSecretSpecSecretPermission
    """Permission to grant on the secret scope. For secrets, only one permission is allowed. Permission
    must be one of: "READ", "WRITE", "MANAGE"."""

    def as_dict(self) -> dict:
        """Serializes the AppManifestAppResourceSecretSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permission is not None:
            body["permission"] = self.permission.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppManifestAppResourceSecretSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.permission is not None:
            body["permission"] = self.permission
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppManifestAppResourceSecretSpec:
        """Deserializes the AppManifestAppResourceSecretSpec from a dictionary."""
        return cls(permission=_enum(d, "permission", AppManifestAppResourceSecretSpecSecretPermission))


class AppManifestAppResourceSecretSpecSecretPermission(Enum):
    """Permission to grant on the secret scope. Supported permissions are: "READ", "WRITE", "MANAGE"."""

    MANAGE = "MANAGE"
    READ = "READ"
    WRITE = "WRITE"


@dataclass
class AppManifestAppResourceServingEndpointSpec:
    permission: AppManifestAppResourceServingEndpointSpecServingEndpointPermission
    """Permission to grant on the serving endpoint. Supported permissions are: "CAN_MANAGE",
    "CAN_QUERY", "CAN_VIEW"."""

    def as_dict(self) -> dict:
        """Serializes the AppManifestAppResourceServingEndpointSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permission is not None:
            body["permission"] = self.permission.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppManifestAppResourceServingEndpointSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.permission is not None:
            body["permission"] = self.permission
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppManifestAppResourceServingEndpointSpec:
        """Deserializes the AppManifestAppResourceServingEndpointSpec from a dictionary."""
        return cls(
            permission=_enum(d, "permission", AppManifestAppResourceServingEndpointSpecServingEndpointPermission)
        )


class AppManifestAppResourceServingEndpointSpecServingEndpointPermission(Enum):

    CAN_MANAGE = "CAN_MANAGE"
    CAN_QUERY = "CAN_QUERY"
    CAN_VIEW = "CAN_VIEW"


@dataclass
class AppManifestAppResourceSpec:
    """AppResource related fields are copied from app.proto but excludes resource identifiers (e.g.
    name, id, key, scope, etc.)"""

    name: str
    """Name of the App Resource."""

    description: Optional[str] = None
    """Description of the App Resource."""

    job_spec: Optional[AppManifestAppResourceJobSpec] = None

    secret_spec: Optional[AppManifestAppResourceSecretSpec] = None

    serving_endpoint_spec: Optional[AppManifestAppResourceServingEndpointSpec] = None

    sql_warehouse_spec: Optional[AppManifestAppResourceSqlWarehouseSpec] = None

    uc_securable_spec: Optional[AppManifestAppResourceUcSecurableSpec] = None

    def as_dict(self) -> dict:
        """Serializes the AppManifestAppResourceSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.job_spec:
            body["job_spec"] = self.job_spec.as_dict()
        if self.name is not None:
            body["name"] = self.name
        if self.secret_spec:
            body["secret_spec"] = self.secret_spec.as_dict()
        if self.serving_endpoint_spec:
            body["serving_endpoint_spec"] = self.serving_endpoint_spec.as_dict()
        if self.sql_warehouse_spec:
            body["sql_warehouse_spec"] = self.sql_warehouse_spec.as_dict()
        if self.uc_securable_spec:
            body["uc_securable_spec"] = self.uc_securable_spec.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppManifestAppResourceSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.job_spec:
            body["job_spec"] = self.job_spec
        if self.name is not None:
            body["name"] = self.name
        if self.secret_spec:
            body["secret_spec"] = self.secret_spec
        if self.serving_endpoint_spec:
            body["serving_endpoint_spec"] = self.serving_endpoint_spec
        if self.sql_warehouse_spec:
            body["sql_warehouse_spec"] = self.sql_warehouse_spec
        if self.uc_securable_spec:
            body["uc_securable_spec"] = self.uc_securable_spec
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppManifestAppResourceSpec:
        """Deserializes the AppManifestAppResourceSpec from a dictionary."""
        return cls(
            description=d.get("description", None),
            job_spec=_from_dict(d, "job_spec", AppManifestAppResourceJobSpec),
            name=d.get("name", None),
            secret_spec=_from_dict(d, "secret_spec", AppManifestAppResourceSecretSpec),
            serving_endpoint_spec=_from_dict(d, "serving_endpoint_spec", AppManifestAppResourceServingEndpointSpec),
            sql_warehouse_spec=_from_dict(d, "sql_warehouse_spec", AppManifestAppResourceSqlWarehouseSpec),
            uc_securable_spec=_from_dict(d, "uc_securable_spec", AppManifestAppResourceUcSecurableSpec),
        )


@dataclass
class AppManifestAppResourceSqlWarehouseSpec:
    permission: AppManifestAppResourceSqlWarehouseSpecSqlWarehousePermission
    """Permission to grant on the SQL warehouse. Supported permissions are: "CAN_MANAGE", "CAN_USE",
    "IS_OWNER"."""

    def as_dict(self) -> dict:
        """Serializes the AppManifestAppResourceSqlWarehouseSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permission is not None:
            body["permission"] = self.permission.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppManifestAppResourceSqlWarehouseSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.permission is not None:
            body["permission"] = self.permission
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppManifestAppResourceSqlWarehouseSpec:
        """Deserializes the AppManifestAppResourceSqlWarehouseSpec from a dictionary."""
        return cls(permission=_enum(d, "permission", AppManifestAppResourceSqlWarehouseSpecSqlWarehousePermission))


class AppManifestAppResourceSqlWarehouseSpecSqlWarehousePermission(Enum):

    CAN_MANAGE = "CAN_MANAGE"
    CAN_USE = "CAN_USE"
    IS_OWNER = "IS_OWNER"


@dataclass
class AppManifestAppResourceUcSecurableSpec:
    securable_type: AppManifestAppResourceUcSecurableSpecUcSecurableType

    permission: AppManifestAppResourceUcSecurableSpecUcSecurablePermission

    def as_dict(self) -> dict:
        """Serializes the AppManifestAppResourceUcSecurableSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permission is not None:
            body["permission"] = self.permission.value
        if self.securable_type is not None:
            body["securable_type"] = self.securable_type.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppManifestAppResourceUcSecurableSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.permission is not None:
            body["permission"] = self.permission
        if self.securable_type is not None:
            body["securable_type"] = self.securable_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppManifestAppResourceUcSecurableSpec:
        """Deserializes the AppManifestAppResourceUcSecurableSpec from a dictionary."""
        return cls(
            permission=_enum(d, "permission", AppManifestAppResourceUcSecurableSpecUcSecurablePermission),
            securable_type=_enum(d, "securable_type", AppManifestAppResourceUcSecurableSpecUcSecurableType),
        )


class AppManifestAppResourceUcSecurableSpecUcSecurablePermission(Enum):

    MANAGE = "MANAGE"
    READ_VOLUME = "READ_VOLUME"
    SELECT = "SELECT"
    WRITE_VOLUME = "WRITE_VOLUME"


class AppManifestAppResourceUcSecurableSpecUcSecurableType(Enum):

    TABLE = "TABLE"
    VOLUME = "VOLUME"


@dataclass
class AppPermission:
    inherited: Optional[bool] = None

    inherited_from_object: Optional[List[str]] = None

    permission_level: Optional[AppPermissionLevel] = None

    def as_dict(self) -> dict:
        """Serializes the AppPermission into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.inherited is not None:
            body["inherited"] = self.inherited
        if self.inherited_from_object:
            body["inherited_from_object"] = [v for v in self.inherited_from_object]
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppPermission into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.inherited is not None:
            body["inherited"] = self.inherited
        if self.inherited_from_object:
            body["inherited_from_object"] = self.inherited_from_object
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppPermission:
        """Deserializes the AppPermission from a dictionary."""
        return cls(
            inherited=d.get("inherited", None),
            inherited_from_object=d.get("inherited_from_object", None),
            permission_level=_enum(d, "permission_level", AppPermissionLevel),
        )


class AppPermissionLevel(Enum):
    """Permission level"""

    CAN_MANAGE = "CAN_MANAGE"
    CAN_USE = "CAN_USE"


@dataclass
class AppPermissions:
    access_control_list: Optional[List[AppAccessControlResponse]] = None

    object_id: Optional[str] = None

    object_type: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the AppPermissions into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_control_list:
            body["access_control_list"] = [v.as_dict() for v in self.access_control_list]
        if self.object_id is not None:
            body["object_id"] = self.object_id
        if self.object_type is not None:
            body["object_type"] = self.object_type
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppPermissions into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.access_control_list:
            body["access_control_list"] = self.access_control_list
        if self.object_id is not None:
            body["object_id"] = self.object_id
        if self.object_type is not None:
            body["object_type"] = self.object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppPermissions:
        """Deserializes the AppPermissions from a dictionary."""
        return cls(
            access_control_list=_repeated_dict(d, "access_control_list", AppAccessControlResponse),
            object_id=d.get("object_id", None),
            object_type=d.get("object_type", None),
        )


@dataclass
class AppPermissionsDescription:
    description: Optional[str] = None

    permission_level: Optional[AppPermissionLevel] = None

    def as_dict(self) -> dict:
        """Serializes the AppPermissionsDescription into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppPermissionsDescription into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppPermissionsDescription:
        """Deserializes the AppPermissionsDescription from a dictionary."""
        return cls(
            description=d.get("description", None), permission_level=_enum(d, "permission_level", AppPermissionLevel)
        )


@dataclass
class AppResource:
    name: str
    """Name of the App Resource."""

    database: Optional[AppResourceDatabase] = None

    description: Optional[str] = None
    """Description of the App Resource."""

    genie_space: Optional[AppResourceGenieSpace] = None

    job: Optional[AppResourceJob] = None

    secret: Optional[AppResourceSecret] = None

    serving_endpoint: Optional[AppResourceServingEndpoint] = None

    sql_warehouse: Optional[AppResourceSqlWarehouse] = None

    uc_securable: Optional[AppResourceUcSecurable] = None

    def as_dict(self) -> dict:
        """Serializes the AppResource into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.database:
            body["database"] = self.database.as_dict()
        if self.description is not None:
            body["description"] = self.description
        if self.genie_space:
            body["genie_space"] = self.genie_space.as_dict()
        if self.job:
            body["job"] = self.job.as_dict()
        if self.name is not None:
            body["name"] = self.name
        if self.secret:
            body["secret"] = self.secret.as_dict()
        if self.serving_endpoint:
            body["serving_endpoint"] = self.serving_endpoint.as_dict()
        if self.sql_warehouse:
            body["sql_warehouse"] = self.sql_warehouse.as_dict()
        if self.uc_securable:
            body["uc_securable"] = self.uc_securable.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppResource into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.database:
            body["database"] = self.database
        if self.description is not None:
            body["description"] = self.description
        if self.genie_space:
            body["genie_space"] = self.genie_space
        if self.job:
            body["job"] = self.job
        if self.name is not None:
            body["name"] = self.name
        if self.secret:
            body["secret"] = self.secret
        if self.serving_endpoint:
            body["serving_endpoint"] = self.serving_endpoint
        if self.sql_warehouse:
            body["sql_warehouse"] = self.sql_warehouse
        if self.uc_securable:
            body["uc_securable"] = self.uc_securable
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppResource:
        """Deserializes the AppResource from a dictionary."""
        return cls(
            database=_from_dict(d, "database", AppResourceDatabase),
            description=d.get("description", None),
            genie_space=_from_dict(d, "genie_space", AppResourceGenieSpace),
            job=_from_dict(d, "job", AppResourceJob),
            name=d.get("name", None),
            secret=_from_dict(d, "secret", AppResourceSecret),
            serving_endpoint=_from_dict(d, "serving_endpoint", AppResourceServingEndpoint),
            sql_warehouse=_from_dict(d, "sql_warehouse", AppResourceSqlWarehouse),
            uc_securable=_from_dict(d, "uc_securable", AppResourceUcSecurable),
        )


@dataclass
class AppResourceDatabase:
    instance_name: str

    database_name: str

    permission: AppResourceDatabaseDatabasePermission

    def as_dict(self) -> dict:
        """Serializes the AppResourceDatabase into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.database_name is not None:
            body["database_name"] = self.database_name
        if self.instance_name is not None:
            body["instance_name"] = self.instance_name
        if self.permission is not None:
            body["permission"] = self.permission.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppResourceDatabase into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.database_name is not None:
            body["database_name"] = self.database_name
        if self.instance_name is not None:
            body["instance_name"] = self.instance_name
        if self.permission is not None:
            body["permission"] = self.permission
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppResourceDatabase:
        """Deserializes the AppResourceDatabase from a dictionary."""
        return cls(
            database_name=d.get("database_name", None),
            instance_name=d.get("instance_name", None),
            permission=_enum(d, "permission", AppResourceDatabaseDatabasePermission),
        )


class AppResourceDatabaseDatabasePermission(Enum):

    CAN_CONNECT_AND_CREATE = "CAN_CONNECT_AND_CREATE"


@dataclass
class AppResourceGenieSpace:
    name: str

    space_id: str

    permission: AppResourceGenieSpaceGenieSpacePermission

    def as_dict(self) -> dict:
        """Serializes the AppResourceGenieSpace into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.permission is not None:
            body["permission"] = self.permission.value
        if self.space_id is not None:
            body["space_id"] = self.space_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppResourceGenieSpace into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.permission is not None:
            body["permission"] = self.permission
        if self.space_id is not None:
            body["space_id"] = self.space_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppResourceGenieSpace:
        """Deserializes the AppResourceGenieSpace from a dictionary."""
        return cls(
            name=d.get("name", None),
            permission=_enum(d, "permission", AppResourceGenieSpaceGenieSpacePermission),
            space_id=d.get("space_id", None),
        )


class AppResourceGenieSpaceGenieSpacePermission(Enum):

    CAN_EDIT = "CAN_EDIT"
    CAN_MANAGE = "CAN_MANAGE"
    CAN_RUN = "CAN_RUN"
    CAN_VIEW = "CAN_VIEW"


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
        if self.id is not None:
            body["id"] = self.id
        if self.permission is not None:
            body["permission"] = self.permission.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppResourceJob into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.id is not None:
            body["id"] = self.id
        if self.permission is not None:
            body["permission"] = self.permission
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppResourceJob:
        """Deserializes the AppResourceJob from a dictionary."""
        return cls(id=d.get("id", None), permission=_enum(d, "permission", AppResourceJobJobPermission))


class AppResourceJobJobPermission(Enum):

    CAN_MANAGE = "CAN_MANAGE"
    CAN_MANAGE_RUN = "CAN_MANAGE_RUN"
    CAN_VIEW = "CAN_VIEW"
    IS_OWNER = "IS_OWNER"


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
        if self.key is not None:
            body["key"] = self.key
        if self.permission is not None:
            body["permission"] = self.permission.value
        if self.scope is not None:
            body["scope"] = self.scope
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppResourceSecret into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.key is not None:
            body["key"] = self.key
        if self.permission is not None:
            body["permission"] = self.permission
        if self.scope is not None:
            body["scope"] = self.scope
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppResourceSecret:
        """Deserializes the AppResourceSecret from a dictionary."""
        return cls(
            key=d.get("key", None),
            permission=_enum(d, "permission", AppResourceSecretSecretPermission),
            scope=d.get("scope", None),
        )


class AppResourceSecretSecretPermission(Enum):
    """Permission to grant on the secret scope. Supported permissions are: "READ", "WRITE", "MANAGE"."""

    MANAGE = "MANAGE"
    READ = "READ"
    WRITE = "WRITE"


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
        if self.name is not None:
            body["name"] = self.name
        if self.permission is not None:
            body["permission"] = self.permission.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppResourceServingEndpoint into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.permission is not None:
            body["permission"] = self.permission
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppResourceServingEndpoint:
        """Deserializes the AppResourceServingEndpoint from a dictionary."""
        return cls(
            name=d.get("name", None),
            permission=_enum(d, "permission", AppResourceServingEndpointServingEndpointPermission),
        )


class AppResourceServingEndpointServingEndpointPermission(Enum):

    CAN_MANAGE = "CAN_MANAGE"
    CAN_QUERY = "CAN_QUERY"
    CAN_VIEW = "CAN_VIEW"


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
        if self.id is not None:
            body["id"] = self.id
        if self.permission is not None:
            body["permission"] = self.permission.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppResourceSqlWarehouse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.id is not None:
            body["id"] = self.id
        if self.permission is not None:
            body["permission"] = self.permission
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppResourceSqlWarehouse:
        """Deserializes the AppResourceSqlWarehouse from a dictionary."""
        return cls(
            id=d.get("id", None), permission=_enum(d, "permission", AppResourceSqlWarehouseSqlWarehousePermission)
        )


class AppResourceSqlWarehouseSqlWarehousePermission(Enum):

    CAN_MANAGE = "CAN_MANAGE"
    CAN_USE = "CAN_USE"
    IS_OWNER = "IS_OWNER"


@dataclass
class AppResourceUcSecurable:
    securable_full_name: str

    securable_type: AppResourceUcSecurableUcSecurableType

    permission: AppResourceUcSecurableUcSecurablePermission

    def as_dict(self) -> dict:
        """Serializes the AppResourceUcSecurable into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permission is not None:
            body["permission"] = self.permission.value
        if self.securable_full_name is not None:
            body["securable_full_name"] = self.securable_full_name
        if self.securable_type is not None:
            body["securable_type"] = self.securable_type.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppResourceUcSecurable into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.permission is not None:
            body["permission"] = self.permission
        if self.securable_full_name is not None:
            body["securable_full_name"] = self.securable_full_name
        if self.securable_type is not None:
            body["securable_type"] = self.securable_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppResourceUcSecurable:
        """Deserializes the AppResourceUcSecurable from a dictionary."""
        return cls(
            permission=_enum(d, "permission", AppResourceUcSecurableUcSecurablePermission),
            securable_full_name=d.get("securable_full_name", None),
            securable_type=_enum(d, "securable_type", AppResourceUcSecurableUcSecurableType),
        )


class AppResourceUcSecurableUcSecurablePermission(Enum):

    READ_VOLUME = "READ_VOLUME"
    WRITE_VOLUME = "WRITE_VOLUME"


class AppResourceUcSecurableUcSecurableType(Enum):

    VOLUME = "VOLUME"


@dataclass
class AppUpdate:
    budget_policy_id: Optional[str] = None

    compute_size: Optional[ComputeSize] = None

    description: Optional[str] = None

    resources: Optional[List[AppResource]] = None

    status: Optional[AppUpdateUpdateStatus] = None

    usage_policy_id: Optional[str] = None

    user_api_scopes: Optional[List[str]] = None

    def as_dict(self) -> dict:
        """Serializes the AppUpdate into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.budget_policy_id is not None:
            body["budget_policy_id"] = self.budget_policy_id
        if self.compute_size is not None:
            body["compute_size"] = self.compute_size.value
        if self.description is not None:
            body["description"] = self.description
        if self.resources:
            body["resources"] = [v.as_dict() for v in self.resources]
        if self.status:
            body["status"] = self.status.as_dict()
        if self.usage_policy_id is not None:
            body["usage_policy_id"] = self.usage_policy_id
        if self.user_api_scopes:
            body["user_api_scopes"] = [v for v in self.user_api_scopes]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppUpdate into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.budget_policy_id is not None:
            body["budget_policy_id"] = self.budget_policy_id
        if self.compute_size is not None:
            body["compute_size"] = self.compute_size
        if self.description is not None:
            body["description"] = self.description
        if self.resources:
            body["resources"] = self.resources
        if self.status:
            body["status"] = self.status
        if self.usage_policy_id is not None:
            body["usage_policy_id"] = self.usage_policy_id
        if self.user_api_scopes:
            body["user_api_scopes"] = self.user_api_scopes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppUpdate:
        """Deserializes the AppUpdate from a dictionary."""
        return cls(
            budget_policy_id=d.get("budget_policy_id", None),
            compute_size=_enum(d, "compute_size", ComputeSize),
            description=d.get("description", None),
            resources=_repeated_dict(d, "resources", AppResource),
            status=_from_dict(d, "status", AppUpdateUpdateStatus),
            usage_policy_id=d.get("usage_policy_id", None),
            user_api_scopes=d.get("user_api_scopes", None),
        )


@dataclass
class AppUpdateUpdateStatus:
    message: Optional[str] = None

    state: Optional[AppUpdateUpdateStatusUpdateState] = None

    def as_dict(self) -> dict:
        """Serializes the AppUpdateUpdateStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.message is not None:
            body["message"] = self.message
        if self.state is not None:
            body["state"] = self.state.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppUpdateUpdateStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.message is not None:
            body["message"] = self.message
        if self.state is not None:
            body["state"] = self.state
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppUpdateUpdateStatus:
        """Deserializes the AppUpdateUpdateStatus from a dictionary."""
        return cls(message=d.get("message", None), state=_enum(d, "state", AppUpdateUpdateStatusUpdateState))


class AppUpdateUpdateStatusUpdateState(Enum):

    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    NOT_UPDATED = "NOT_UPDATED"
    SUCCEEDED = "SUCCEEDED"


class ApplicationState(Enum):

    CRASHED = "CRASHED"
    DEPLOYING = "DEPLOYING"
    RUNNING = "RUNNING"
    UNAVAILABLE = "UNAVAILABLE"


@dataclass
class ApplicationStatus:
    message: Optional[str] = None
    """Application status message"""

    state: Optional[ApplicationState] = None
    """State of the application."""

    def as_dict(self) -> dict:
        """Serializes the ApplicationStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.message is not None:
            body["message"] = self.message
        if self.state is not None:
            body["state"] = self.state.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ApplicationStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.message is not None:
            body["message"] = self.message
        if self.state is not None:
            body["state"] = self.state
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ApplicationStatus:
        """Deserializes the ApplicationStatus from a dictionary."""
        return cls(message=d.get("message", None), state=_enum(d, "state", ApplicationState))


class ComputeSize(Enum):

    LARGE = "LARGE"
    LIQUID = "LIQUID"
    MEDIUM = "MEDIUM"


class ComputeState(Enum):

    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    ERROR = "ERROR"
    STARTING = "STARTING"
    STOPPED = "STOPPED"
    STOPPING = "STOPPING"
    UPDATING = "UPDATING"


@dataclass
class ComputeStatus:
    message: Optional[str] = None
    """Compute status message"""

    state: Optional[ComputeState] = None
    """State of the app compute."""

    def as_dict(self) -> dict:
        """Serializes the ComputeStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.message is not None:
            body["message"] = self.message
        if self.state is not None:
            body["state"] = self.state.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ComputeStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.message is not None:
            body["message"] = self.message
        if self.state is not None:
            body["state"] = self.state
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ComputeStatus:
        """Deserializes the ComputeStatus from a dictionary."""
        return cls(message=d.get("message", None), state=_enum(d, "state", ComputeState))


@dataclass
class CustomTemplate:
    name: str
    """The name of the template. It must contain only alphanumeric characters, hyphens, underscores,
    and whitespaces. It must be unique within the workspace."""

    git_repo: str
    """The Git repository URL that the template resides in."""

    path: str
    """The path to the template within the Git repository."""

    manifest: AppManifest
    """The manifest of the template. It defines fields and default values when installing the template."""

    git_provider: str
    """The Git provider of the template."""

    creator: Optional[str] = None

    description: Optional[str] = None
    """The description of the template."""

    def as_dict(self) -> dict:
        """Serializes the CustomTemplate into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.creator is not None:
            body["creator"] = self.creator
        if self.description is not None:
            body["description"] = self.description
        if self.git_provider is not None:
            body["git_provider"] = self.git_provider
        if self.git_repo is not None:
            body["git_repo"] = self.git_repo
        if self.manifest:
            body["manifest"] = self.manifest.as_dict()
        if self.name is not None:
            body["name"] = self.name
        if self.path is not None:
            body["path"] = self.path
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CustomTemplate into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.creator is not None:
            body["creator"] = self.creator
        if self.description is not None:
            body["description"] = self.description
        if self.git_provider is not None:
            body["git_provider"] = self.git_provider
        if self.git_repo is not None:
            body["git_repo"] = self.git_repo
        if self.manifest:
            body["manifest"] = self.manifest
        if self.name is not None:
            body["name"] = self.name
        if self.path is not None:
            body["path"] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CustomTemplate:
        """Deserializes the CustomTemplate from a dictionary."""
        return cls(
            creator=d.get("creator", None),
            description=d.get("description", None),
            git_provider=d.get("git_provider", None),
            git_repo=d.get("git_repo", None),
            manifest=_from_dict(d, "manifest", AppManifest),
            name=d.get("name", None),
            path=d.get("path", None),
        )


@dataclass
class GetAppPermissionLevelsResponse:
    permission_levels: Optional[List[AppPermissionsDescription]] = None
    """Specific permission levels"""

    def as_dict(self) -> dict:
        """Serializes the GetAppPermissionLevelsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permission_levels:
            body["permission_levels"] = [v.as_dict() for v in self.permission_levels]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GetAppPermissionLevelsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.permission_levels:
            body["permission_levels"] = self.permission_levels
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GetAppPermissionLevelsResponse:
        """Deserializes the GetAppPermissionLevelsResponse from a dictionary."""
        return cls(permission_levels=_repeated_dict(d, "permission_levels", AppPermissionsDescription))


@dataclass
class ListAppDeploymentsResponse:
    app_deployments: Optional[List[AppDeployment]] = None
    """Deployment history of the app."""

    next_page_token: Optional[str] = None
    """Pagination token to request the next page of apps."""

    def as_dict(self) -> dict:
        """Serializes the ListAppDeploymentsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.app_deployments:
            body["app_deployments"] = [v.as_dict() for v in self.app_deployments]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListAppDeploymentsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.app_deployments:
            body["app_deployments"] = self.app_deployments
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListAppDeploymentsResponse:
        """Deserializes the ListAppDeploymentsResponse from a dictionary."""
        return cls(
            app_deployments=_repeated_dict(d, "app_deployments", AppDeployment),
            next_page_token=d.get("next_page_token", None),
        )


@dataclass
class ListAppsResponse:
    apps: Optional[List[App]] = None

    next_page_token: Optional[str] = None
    """Pagination token to request the next page of apps."""

    def as_dict(self) -> dict:
        """Serializes the ListAppsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.apps:
            body["apps"] = [v.as_dict() for v in self.apps]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListAppsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.apps:
            body["apps"] = self.apps
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListAppsResponse:
        """Deserializes the ListAppsResponse from a dictionary."""
        return cls(apps=_repeated_dict(d, "apps", App), next_page_token=d.get("next_page_token", None))


@dataclass
class ListCustomTemplatesResponse:
    next_page_token: Optional[str] = None
    """Pagination token to request the next page of custom templates."""

    templates: Optional[List[CustomTemplate]] = None

    def as_dict(self) -> dict:
        """Serializes the ListCustomTemplatesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.templates:
            body["templates"] = [v.as_dict() for v in self.templates]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListCustomTemplatesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.templates:
            body["templates"] = self.templates
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListCustomTemplatesResponse:
        """Deserializes the ListCustomTemplatesResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None), templates=_repeated_dict(d, "templates", CustomTemplate)
        )


class AppsAPI:
    """Apps run directly on a customer’s Databricks instance, integrate with their data, use and extend
    Databricks services, and enable users to interact through single sign-on."""

    def __init__(self, api_client):
        self._api = api_client

    def wait_get_app_active(
        self, name: str, timeout=timedelta(minutes=20), callback: Optional[Callable[[App], None]] = None
    ) -> App:
        deadline = time.time() + timeout.total_seconds()
        target_states = (ComputeState.ACTIVE,)
        failure_states = (
            ComputeState.ERROR,
            ComputeState.STOPPED,
        )
        status_message = "polling..."
        attempt = 1
        while time.time() < deadline:
            poll = self.get(name=name)
            status = poll.compute_status.state
            status_message = f"current status: {status}"
            if poll.compute_status:
                status_message = poll.compute_status.message
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f"failed to reach ACTIVE, got {status}: {status_message}"
                raise OperationFailed(msg)
            prefix = f"name={name}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f"{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)")
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f"timed out after {timeout}: {status_message}")

    def wait_get_update_app_succeeded(
        self, app_name: str, timeout=timedelta(minutes=20), callback: Optional[Callable[[AppUpdate], None]] = None
    ) -> AppUpdate:
        deadline = time.time() + timeout.total_seconds()
        target_states = (AppUpdateUpdateStatusUpdateState.SUCCEEDED,)
        failure_states = (AppUpdateUpdateStatusUpdateState.FAILED,)
        status_message = "polling..."
        attempt = 1
        while time.time() < deadline:
            poll = self.get_update(app_name=app_name)
            status = poll.status.state
            status_message = f"current status: {status}"
            if poll.status:
                status_message = poll.status.message
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f"failed to reach SUCCEEDED, got {status}: {status_message}"
                raise OperationFailed(msg)
            prefix = f"app_name={app_name}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f"{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)")
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f"timed out after {timeout}: {status_message}")

    def wait_get_deployment_app_succeeded(
        self,
        app_name: str,
        deployment_id: str,
        timeout=timedelta(minutes=20),
        callback: Optional[Callable[[AppDeployment], None]] = None,
    ) -> AppDeployment:
        deadline = time.time() + timeout.total_seconds()
        target_states = (AppDeploymentState.SUCCEEDED,)
        failure_states = (AppDeploymentState.FAILED,)
        status_message = "polling..."
        attempt = 1
        while time.time() < deadline:
            poll = self.get_deployment(app_name=app_name, deployment_id=deployment_id)
            status = poll.status.state
            status_message = f"current status: {status}"
            if poll.status:
                status_message = poll.status.message
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f"failed to reach SUCCEEDED, got {status}: {status_message}"
                raise OperationFailed(msg)
            prefix = f"app_name={app_name}, deployment_id={deployment_id}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f"{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)")
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f"timed out after {timeout}: {status_message}")

    def wait_get_app_stopped(
        self, name: str, timeout=timedelta(minutes=20), callback: Optional[Callable[[App], None]] = None
    ) -> App:
        deadline = time.time() + timeout.total_seconds()
        target_states = (ComputeState.STOPPED,)
        failure_states = (ComputeState.ERROR,)
        status_message = "polling..."
        attempt = 1
        while time.time() < deadline:
            poll = self.get(name=name)
            status = poll.compute_status.state
            status_message = f"current status: {status}"
            if poll.compute_status:
                status_message = poll.compute_status.message
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f"failed to reach STOPPED, got {status}: {status_message}"
                raise OperationFailed(msg)
            prefix = f"name={name}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f"{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)")
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f"timed out after {timeout}: {status_message}")

    def create(self, app: App, *, no_compute: Optional[bool] = None) -> Wait[App]:
        """Creates a new app.

        :param app: :class:`App`
        :param no_compute: bool (optional)
          If true, the app will not be started after creation.

        :returns:
          Long-running operation waiter for :class:`App`.
          See :method:wait_get_app_active for more details.
        """

        body = app.as_dict()
        query = {}
        if no_compute is not None:
            query["no_compute"] = no_compute
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        op_response = self._api.do("POST", "/api/2.0/apps", query=query, body=body, headers=headers)
        return Wait(self.wait_get_app_active, response=App.from_dict(op_response), name=op_response["name"])

    def create_and_wait(self, app: App, *, no_compute: Optional[bool] = None, timeout=timedelta(minutes=20)) -> App:
        return self.create(app=app, no_compute=no_compute).result(timeout=timeout)

    def create_update(self, app_name: str, update_mask: str, *, app: Optional[App] = None) -> Wait[AppUpdate]:
        """Creates an app update and starts the update process. The update process is asynchronous and the status
        of the update can be checked with the GetAppUpdate method.

        :param app_name: str
        :param update_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.
        :param app: :class:`App` (optional)

        :returns:
          Long-running operation waiter for :class:`AppUpdate`.
          See :method:wait_get_update_app_succeeded for more details.
        """

        body = {}
        if app is not None:
            body["app"] = app.as_dict()
        if update_mask is not None:
            body["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        op_response = self._api.do("POST", f"/api/2.0/apps/{app_name}/update", body=body, headers=headers)
        return Wait(self.wait_get_update_app_succeeded, response=AppUpdate.from_dict(op_response), app_name=app_name)

    def create_update_and_wait(
        self, app_name: str, update_mask: str, *, app: Optional[App] = None, timeout=timedelta(minutes=20)
    ) -> AppUpdate:
        return self.create_update(app=app, app_name=app_name, update_mask=update_mask).result(timeout=timeout)

    def delete(self, name: str) -> App:
        """Deletes an app.

        :param name: str
          The name of the app.

        :returns: :class:`App`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("DELETE", f"/api/2.0/apps/{name}", headers=headers)
        return App.from_dict(res)

    def deploy(self, app_name: str, app_deployment: AppDeployment) -> Wait[AppDeployment]:
        """Creates an app deployment for the app with the supplied name.

        :param app_name: str
          The name of the app.
        :param app_deployment: :class:`AppDeployment`
          The app deployment configuration.

        :returns:
          Long-running operation waiter for :class:`AppDeployment`.
          See :method:wait_get_deployment_app_succeeded for more details.
        """

        body = app_deployment.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        op_response = self._api.do("POST", f"/api/2.0/apps/{app_name}/deployments", body=body, headers=headers)
        return Wait(
            self.wait_get_deployment_app_succeeded,
            response=AppDeployment.from_dict(op_response),
            app_name=app_name,
            deployment_id=op_response["deployment_id"],
        )

    def deploy_and_wait(
        self, app_name: str, app_deployment: AppDeployment, timeout=timedelta(minutes=20)
    ) -> AppDeployment:
        return self.deploy(app_deployment=app_deployment, app_name=app_name).result(timeout=timeout)

    def get(self, name: str) -> App:
        """Retrieves information for the app with the supplied name.

        :param name: str
          The name of the app.

        :returns: :class:`App`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/apps/{name}", headers=headers)
        return App.from_dict(res)

    def get_deployment(self, app_name: str, deployment_id: str) -> AppDeployment:
        """Retrieves information for the app deployment with the supplied name and deployment id.

        :param app_name: str
          The name of the app.
        :param deployment_id: str
          The unique id of the deployment.

        :returns: :class:`AppDeployment`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/apps/{app_name}/deployments/{deployment_id}", headers=headers)
        return AppDeployment.from_dict(res)

    def get_permission_levels(self, app_name: str) -> GetAppPermissionLevelsResponse:
        """Gets the permission levels that a user can have on an object.

        :param app_name: str
          The app for which to get or manage permissions.

        :returns: :class:`GetAppPermissionLevelsResponse`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/permissions/apps/{app_name}/permissionLevels", headers=headers)
        return GetAppPermissionLevelsResponse.from_dict(res)

    def get_permissions(self, app_name: str) -> AppPermissions:
        """Gets the permissions of an app. Apps can inherit permissions from their root object.

        :param app_name: str
          The app for which to get or manage permissions.

        :returns: :class:`AppPermissions`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/permissions/apps/{app_name}", headers=headers)
        return AppPermissions.from_dict(res)

    def get_update(self, app_name: str) -> AppUpdate:
        """Gets the status of an app update.

        :param app_name: str
          The name of the app.

        :returns: :class:`AppUpdate`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/apps/{app_name}/update", headers=headers)
        return AppUpdate.from_dict(res)

    def list(self, *, page_size: Optional[int] = None, page_token: Optional[str] = None) -> Iterator[App]:
        """Lists all apps in the workspace.

        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of apps. Requests first page if absent.

        :returns: Iterator over :class:`App`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        while True:
            json = self._api.do("GET", "/api/2.0/apps", query=query, headers=headers)
            if "apps" in json:
                for v in json["apps"]:
                    yield App.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_deployments(
        self, app_name: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[AppDeployment]:
        """Lists all app deployments for the app with the supplied name.

        :param app_name: str
          The name of the app.
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of apps. Requests first page if absent.

        :returns: Iterator over :class:`AppDeployment`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        while True:
            json = self._api.do("GET", f"/api/2.0/apps/{app_name}/deployments", query=query, headers=headers)
            if "app_deployments" in json:
                for v in json["app_deployments"]:
                    yield AppDeployment.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def set_permissions(
        self, app_name: str, *, access_control_list: Optional[List[AppAccessControlRequest]] = None
    ) -> AppPermissions:
        """Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct
        permissions if none are specified. Objects can inherit permissions from their root object.

        :param app_name: str
          The app for which to get or manage permissions.
        :param access_control_list: List[:class:`AppAccessControlRequest`] (optional)

        :returns: :class:`AppPermissions`
        """

        body = {}
        if access_control_list is not None:
            body["access_control_list"] = [v.as_dict() for v in access_control_list]
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PUT", f"/api/2.0/permissions/apps/{app_name}", body=body, headers=headers)
        return AppPermissions.from_dict(res)

    def start(self, name: str) -> Wait[App]:
        """Start the last active deployment of the app in the workspace.

        :param name: str
          The name of the app.

        :returns:
          Long-running operation waiter for :class:`App`.
          See :method:wait_get_app_active for more details.
        """

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        op_response = self._api.do("POST", f"/api/2.0/apps/{name}/start", headers=headers)
        return Wait(self.wait_get_app_active, response=App.from_dict(op_response), name=op_response["name"])

    def start_and_wait(self, name: str, timeout=timedelta(minutes=20)) -> App:
        return self.start(name=name).result(timeout=timeout)

    def stop(self, name: str) -> Wait[App]:
        """Stops the active deployment of the app in the workspace.

        :param name: str
          The name of the app.

        :returns:
          Long-running operation waiter for :class:`App`.
          See :method:wait_get_app_stopped for more details.
        """

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        op_response = self._api.do("POST", f"/api/2.0/apps/{name}/stop", headers=headers)
        return Wait(self.wait_get_app_stopped, response=App.from_dict(op_response), name=op_response["name"])

    def stop_and_wait(self, name: str, timeout=timedelta(minutes=20)) -> App:
        return self.stop(name=name).result(timeout=timeout)

    def update(self, name: str, app: App) -> App:
        """Updates the app with the supplied name.

        :param name: str
          The name of the app. The name must contain only lowercase alphanumeric characters and hyphens. It
          must be unique within the workspace.
        :param app: :class:`App`

        :returns: :class:`App`
        """

        body = app.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.0/apps/{name}", body=body, headers=headers)
        return App.from_dict(res)

    def update_permissions(
        self, app_name: str, *, access_control_list: Optional[List[AppAccessControlRequest]] = None
    ) -> AppPermissions:
        """Updates the permissions on an app. Apps can inherit permissions from their root object.

        :param app_name: str
          The app for which to get or manage permissions.
        :param access_control_list: List[:class:`AppAccessControlRequest`] (optional)

        :returns: :class:`AppPermissions`
        """

        body = {}
        if access_control_list is not None:
            body["access_control_list"] = [v.as_dict() for v in access_control_list]
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.0/permissions/apps/{app_name}", body=body, headers=headers)
        return AppPermissions.from_dict(res)


class AppsSettingsAPI:
    """Apps Settings manage the settings for the Apps service on a customer's Databricks instance."""

    def __init__(self, api_client):
        self._api = api_client

    def create_custom_template(self, template: CustomTemplate) -> CustomTemplate:
        """Creates a custom template.

        :param template: :class:`CustomTemplate`

        :returns: :class:`CustomTemplate`
        """

        body = template.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/apps-settings/templates", body=body, headers=headers)
        return CustomTemplate.from_dict(res)

    def delete_custom_template(self, name: str) -> CustomTemplate:
        """Deletes the custom template with the specified name.

        :param name: str
          The name of the custom template.

        :returns: :class:`CustomTemplate`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("DELETE", f"/api/2.0/apps-settings/templates/{name}", headers=headers)
        return CustomTemplate.from_dict(res)

    def get_custom_template(self, name: str) -> CustomTemplate:
        """Gets the custom template with the specified name.

        :param name: str
          The name of the custom template.

        :returns: :class:`CustomTemplate`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/apps-settings/templates/{name}", headers=headers)
        return CustomTemplate.from_dict(res)

    def list_custom_templates(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[CustomTemplate]:
        """Lists all custom templates in the workspace.

        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of custom templates. Requests first page if absent.

        :returns: Iterator over :class:`CustomTemplate`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        while True:
            json = self._api.do("GET", "/api/2.0/apps-settings/templates", query=query, headers=headers)
            if "templates" in json:
                for v in json["templates"]:
                    yield CustomTemplate.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def update_custom_template(self, name: str, template: CustomTemplate) -> CustomTemplate:
        """Updates the custom template with the specified name. Note that the template name cannot be updated.

        :param name: str
          The name of the template. It must contain only alphanumeric characters, hyphens, underscores, and
          whitespaces. It must be unique within the workspace.
        :param template: :class:`CustomTemplate`

        :returns: :class:`CustomTemplate`
        """

        body = template.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PUT", f"/api/2.0/apps-settings/templates/{name}", body=body, headers=headers)
        return CustomTemplate.from_dict(res)

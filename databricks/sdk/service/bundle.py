# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.
# ruff: noqa: F811, F841
# F401 is intentionally NOT covered: `make fmt` uses `ruff check --fix-only`
# to strip the fat-import header below; ignoring F401 would defeat that.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List, Optional

from google.protobuf.timestamp_pb2 import Timestamp

from databricks.sdk.service._internal import (
    _enum,
    _repeated_dict,
    _timestamp,
)

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class Deployment:
    """A bundle deployment registered with the control plane."""

    create_time: Optional[Timestamp] = None
    """When the deployment was created."""

    created_by: Optional[str] = None
    """The user who created the deployment (email or principal name)."""

    destroy_time: Optional[Timestamp] = None
    """When the deployment was destroyed (i.e. `bundle destroy` completed). Unset if the deployment has
    not been destroyed. Named destroy_time (not delete_time) because this tracks the `databricks
    bundle destroy` command, not the API-level deletion."""

    destroyed_by: Optional[str] = None
    """The user who destroyed the deployment (email or principal name). Unset if the deployment has not
    been destroyed."""

    display_name: Optional[str] = None
    """Human-readable name for the deployment."""

    last_version_id: Optional[str] = None
    """The version_id of the most recent deployment version."""

    name: Optional[str] = None
    """Resource name of the deployment. Format: deployments/{deployment_id}"""

    status: Optional[DeploymentStatus] = None
    """Current status of the deployment."""

    target_name: Optional[str] = None
    """The bundle target name associated with this deployment."""

    update_time: Optional[Timestamp] = None
    """When the deployment was last updated."""

    def as_dict(self) -> dict:
        """Serializes the Deployment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.created_by is not None:
            body["created_by"] = self.created_by
        if self.destroy_time is not None:
            body["destroy_time"] = self.destroy_time.ToJsonString()
        if self.destroyed_by is not None:
            body["destroyed_by"] = self.destroyed_by
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.last_version_id is not None:
            body["last_version_id"] = self.last_version_id
        if self.name is not None:
            body["name"] = self.name
        if self.status is not None:
            body["status"] = self.status.value
        if self.target_name is not None:
            body["target_name"] = self.target_name
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Deployment into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.created_by is not None:
            body["created_by"] = self.created_by
        if self.destroy_time is not None:
            body["destroy_time"] = self.destroy_time
        if self.destroyed_by is not None:
            body["destroyed_by"] = self.destroyed_by
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.last_version_id is not None:
            body["last_version_id"] = self.last_version_id
        if self.name is not None:
            body["name"] = self.name
        if self.status is not None:
            body["status"] = self.status
        if self.target_name is not None:
            body["target_name"] = self.target_name
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Deployment:
        """Deserializes the Deployment from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            created_by=d.get("created_by", None),
            destroy_time=_timestamp(d, "destroy_time"),
            destroyed_by=d.get("destroyed_by", None),
            display_name=d.get("display_name", None),
            last_version_id=d.get("last_version_id", None),
            name=d.get("name", None),
            status=_enum(d, "status", DeploymentStatus),
            target_name=d.get("target_name", None),
            update_time=_timestamp(d, "update_time"),
        )


class DeploymentResourceType(Enum):
    """Type of a deployment resource."""

    DEPLOYMENT_RESOURCE_TYPE_ALERT = "DEPLOYMENT_RESOURCE_TYPE_ALERT"
    DEPLOYMENT_RESOURCE_TYPE_APP = "DEPLOYMENT_RESOURCE_TYPE_APP"
    DEPLOYMENT_RESOURCE_TYPE_CATALOG = "DEPLOYMENT_RESOURCE_TYPE_CATALOG"
    DEPLOYMENT_RESOURCE_TYPE_CLUSTER = "DEPLOYMENT_RESOURCE_TYPE_CLUSTER"
    DEPLOYMENT_RESOURCE_TYPE_DASHBOARD = "DEPLOYMENT_RESOURCE_TYPE_DASHBOARD"
    DEPLOYMENT_RESOURCE_TYPE_DATABASE_CATALOG = "DEPLOYMENT_RESOURCE_TYPE_DATABASE_CATALOG"
    DEPLOYMENT_RESOURCE_TYPE_DATABASE_INSTANCE = "DEPLOYMENT_RESOURCE_TYPE_DATABASE_INSTANCE"
    DEPLOYMENT_RESOURCE_TYPE_EXPERIMENT = "DEPLOYMENT_RESOURCE_TYPE_EXPERIMENT"
    DEPLOYMENT_RESOURCE_TYPE_EXTERNAL_LOCATION = "DEPLOYMENT_RESOURCE_TYPE_EXTERNAL_LOCATION"
    DEPLOYMENT_RESOURCE_TYPE_JOB = "DEPLOYMENT_RESOURCE_TYPE_JOB"
    DEPLOYMENT_RESOURCE_TYPE_MODEL = "DEPLOYMENT_RESOURCE_TYPE_MODEL"
    DEPLOYMENT_RESOURCE_TYPE_MODEL_SERVING_ENDPOINT = "DEPLOYMENT_RESOURCE_TYPE_MODEL_SERVING_ENDPOINT"
    DEPLOYMENT_RESOURCE_TYPE_PIPELINE = "DEPLOYMENT_RESOURCE_TYPE_PIPELINE"
    DEPLOYMENT_RESOURCE_TYPE_POSTGRES_BRANCH = "DEPLOYMENT_RESOURCE_TYPE_POSTGRES_BRANCH"
    DEPLOYMENT_RESOURCE_TYPE_POSTGRES_ENDPOINT = "DEPLOYMENT_RESOURCE_TYPE_POSTGRES_ENDPOINT"
    DEPLOYMENT_RESOURCE_TYPE_POSTGRES_PROJECT = "DEPLOYMENT_RESOURCE_TYPE_POSTGRES_PROJECT"
    DEPLOYMENT_RESOURCE_TYPE_QUALITY_MONITOR = "DEPLOYMENT_RESOURCE_TYPE_QUALITY_MONITOR"
    DEPLOYMENT_RESOURCE_TYPE_REGISTERED_MODEL = "DEPLOYMENT_RESOURCE_TYPE_REGISTERED_MODEL"
    DEPLOYMENT_RESOURCE_TYPE_SCHEMA = "DEPLOYMENT_RESOURCE_TYPE_SCHEMA"
    DEPLOYMENT_RESOURCE_TYPE_SECRET_SCOPE = "DEPLOYMENT_RESOURCE_TYPE_SECRET_SCOPE"
    DEPLOYMENT_RESOURCE_TYPE_SQL_WAREHOUSE = "DEPLOYMENT_RESOURCE_TYPE_SQL_WAREHOUSE"
    DEPLOYMENT_RESOURCE_TYPE_SYNCED_DATABASE_TABLE = "DEPLOYMENT_RESOURCE_TYPE_SYNCED_DATABASE_TABLE"
    DEPLOYMENT_RESOURCE_TYPE_VOLUME = "DEPLOYMENT_RESOURCE_TYPE_VOLUME"


class DeploymentStatus(Enum):
    """Status of a deployment."""

    DEPLOYMENT_STATUS_ACTIVE = "DEPLOYMENT_STATUS_ACTIVE"
    DEPLOYMENT_STATUS_DELETED = "DEPLOYMENT_STATUS_DELETED"
    DEPLOYMENT_STATUS_FAILED = "DEPLOYMENT_STATUS_FAILED"
    DEPLOYMENT_STATUS_IN_PROGRESS = "DEPLOYMENT_STATUS_IN_PROGRESS"


@dataclass
class HeartbeatResponse:
    """Response for Heartbeat."""

    expire_time: Optional[Timestamp] = None
    """The new lock expiry time after renewal."""

    def as_dict(self) -> dict:
        """Serializes the HeartbeatResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.expire_time is not None:
            body["expire_time"] = self.expire_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the HeartbeatResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.expire_time is not None:
            body["expire_time"] = self.expire_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> HeartbeatResponse:
        """Deserializes the HeartbeatResponse from a dictionary."""
        return cls(expire_time=_timestamp(d, "expire_time"))


@dataclass
class ListDeploymentsResponse:
    """Response for ListDeployments."""

    deployments: Optional[List[Deployment]] = None
    """The deployments from the queried workspace."""

    next_page_token: Optional[str] = None
    """A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted,
    there are no subsequent pages."""

    def as_dict(self) -> dict:
        """Serializes the ListDeploymentsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.deployments:
            body["deployments"] = [v.as_dict() for v in self.deployments]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListDeploymentsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.deployments:
            body["deployments"] = self.deployments
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListDeploymentsResponse:
        """Deserializes the ListDeploymentsResponse from a dictionary."""
        return cls(
            deployments=_repeated_dict(d, "deployments", Deployment), next_page_token=d.get("next_page_token", None)
        )


@dataclass
class ListOperationsResponse:
    """Response for ListOperations."""

    next_page_token: Optional[str] = None
    """A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted,
    there are no subsequent pages."""

    operations: Optional[List[Operation]] = None
    """The resource operations under the specified version."""

    def as_dict(self) -> dict:
        """Serializes the ListOperationsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.operations:
            body["operations"] = [v.as_dict() for v in self.operations]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListOperationsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.operations:
            body["operations"] = self.operations
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListOperationsResponse:
        """Deserializes the ListOperationsResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None), operations=_repeated_dict(d, "operations", Operation)
        )


@dataclass
class ListResourcesResponse:
    """Response for ListResources."""

    next_page_token: Optional[str] = None
    """A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted,
    there are no subsequent pages."""

    resources: Optional[List[Resource]] = None
    """The resources under the specified deployment."""

    def as_dict(self) -> dict:
        """Serializes the ListResourcesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.resources:
            body["resources"] = [v.as_dict() for v in self.resources]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListResourcesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.resources:
            body["resources"] = self.resources
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListResourcesResponse:
        """Deserializes the ListResourcesResponse from a dictionary."""
        return cls(next_page_token=d.get("next_page_token", None), resources=_repeated_dict(d, "resources", Resource))


@dataclass
class ListVersionsResponse:
    """Response for ListVersions."""

    next_page_token: Optional[str] = None
    """A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted,
    there are no subsequent pages."""

    versions: Optional[List[Version]] = None
    """The versions under the specified deployment."""

    def as_dict(self) -> dict:
        """Serializes the ListVersionsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.versions:
            body["versions"] = [v.as_dict() for v in self.versions]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListVersionsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.versions:
            body["versions"] = self.versions
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListVersionsResponse:
        """Deserializes the ListVersionsResponse from a dictionary."""
        return cls(next_page_token=d.get("next_page_token", None), versions=_repeated_dict(d, "versions", Version))


@dataclass
class Operation:
    """An operation on a single resource performed during a version. Operations are append-only and
    record the result of applying a resource change to the workspace."""

    action_type: OperationActionType
    """The type of operation performed on this resource."""

    resource_id: str
    """ID reference for the actual resource in the workspace (e.g. the job ID, pipeline ID)."""

    status: OperationStatus
    """Whether the operation succeeded or failed."""

    create_time: Optional[Timestamp] = None
    """When the operation was recorded."""

    error_message: Optional[str] = None
    """Error message if the operation failed. Set when status is OPERATION_STATUS_FAILED. Captures the
    error encountered while applying the resource to the workspace."""

    name: Optional[str] = None
    """Resource name of the operation. Format:
    deployments/{deployment_id}/versions/{version_id}/operations/{resource_key}"""

    resource_key: Optional[str] = None
    """Resource identifier within the bundle (e.g. "jobs.foo", "pipelines.bar", "jobs.foo.permissions",
    "files.<rel-path>"). Can be an arbitrary UTF-8 encoded string key. This key links the operation
    to the corresponding deployment-level Resource."""

    resource_type: Optional[DeploymentResourceType] = None
    """The type of the deployment resource this operation applies to. Derived from the `resource_key`
    prefix (e.g. "jobs" → JOB); the caller does not set this field."""

    state: Optional[any] = None
    """Serialized local config state after the operation. Should be unset for delete operations."""

    def as_dict(self) -> dict:
        """Serializes the Operation into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.action_type is not None:
            body["action_type"] = self.action_type.value
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.error_message is not None:
            body["error_message"] = self.error_message
        if self.name is not None:
            body["name"] = self.name
        if self.resource_id is not None:
            body["resource_id"] = self.resource_id
        if self.resource_key is not None:
            body["resource_key"] = self.resource_key
        if self.resource_type is not None:
            body["resource_type"] = self.resource_type.value
        if self.state:
            body["state"] = self.state
        if self.status is not None:
            body["status"] = self.status.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Operation into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.action_type is not None:
            body["action_type"] = self.action_type
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.error_message is not None:
            body["error_message"] = self.error_message
        if self.name is not None:
            body["name"] = self.name
        if self.resource_id is not None:
            body["resource_id"] = self.resource_id
        if self.resource_key is not None:
            body["resource_key"] = self.resource_key
        if self.resource_type is not None:
            body["resource_type"] = self.resource_type
        if self.state:
            body["state"] = self.state
        if self.status is not None:
            body["status"] = self.status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Operation:
        """Deserializes the Operation from a dictionary."""
        return cls(
            action_type=_enum(d, "action_type", OperationActionType),
            create_time=_timestamp(d, "create_time"),
            error_message=d.get("error_message", None),
            name=d.get("name", None),
            resource_id=d.get("resource_id", None),
            resource_key=d.get("resource_key", None),
            resource_type=_enum(d, "resource_type", DeploymentResourceType),
            state=d.get("state", None),
            status=_enum(d, "status", OperationStatus),
        )


class OperationActionType(Enum):
    """Type of action performed on a resource during a deployment."""

    OPERATION_ACTION_TYPE_BIND = "OPERATION_ACTION_TYPE_BIND"
    OPERATION_ACTION_TYPE_BIND_AND_UPDATE = "OPERATION_ACTION_TYPE_BIND_AND_UPDATE"
    OPERATION_ACTION_TYPE_CREATE = "OPERATION_ACTION_TYPE_CREATE"
    OPERATION_ACTION_TYPE_DELETE = "OPERATION_ACTION_TYPE_DELETE"
    OPERATION_ACTION_TYPE_INITIAL_REGISTER = "OPERATION_ACTION_TYPE_INITIAL_REGISTER"
    OPERATION_ACTION_TYPE_RECREATE = "OPERATION_ACTION_TYPE_RECREATE"
    OPERATION_ACTION_TYPE_RESIZE = "OPERATION_ACTION_TYPE_RESIZE"
    OPERATION_ACTION_TYPE_UPDATE = "OPERATION_ACTION_TYPE_UPDATE"
    OPERATION_ACTION_TYPE_UPDATE_WITH_ID = "OPERATION_ACTION_TYPE_UPDATE_WITH_ID"


class OperationStatus(Enum):
    """Status of a resource operation."""

    OPERATION_STATUS_FAILED = "OPERATION_STATUS_FAILED"
    OPERATION_STATUS_SUCCEEDED = "OPERATION_STATUS_SUCCEEDED"


@dataclass
class Resource:
    """A resource managed by a deployment. Resources are implicitly created, updated, or deleted when
    operations are recorded on a version."""

    resource_type: DeploymentResourceType
    """The type of the deployment resource."""

    last_action_type: Optional[OperationActionType] = None
    """The action performed on this resource during the last version."""

    last_version_id: Optional[str] = None
    """The version_id of the last version where this resource was updated."""

    name: Optional[str] = None
    """Resource name. Format: deployments/{deployment_id}/resources/{resource_key}"""

    resource_id: Optional[str] = None
    """ID that references the actual resource in the workspace (e.g. the job ID, pipeline ID)."""

    resource_key: Optional[str] = None
    """Resource identifier within the bundle (e.g. "jobs.foo", "pipelines.bar",
    "jobs.foo.permissions")."""

    state: Optional[any] = None
    """Serialized local config state (what the CLI deployed)."""

    def as_dict(self) -> dict:
        """Serializes the Resource into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.last_action_type is not None:
            body["last_action_type"] = self.last_action_type.value
        if self.last_version_id is not None:
            body["last_version_id"] = self.last_version_id
        if self.name is not None:
            body["name"] = self.name
        if self.resource_id is not None:
            body["resource_id"] = self.resource_id
        if self.resource_key is not None:
            body["resource_key"] = self.resource_key
        if self.resource_type is not None:
            body["resource_type"] = self.resource_type.value
        if self.state:
            body["state"] = self.state
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Resource into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.last_action_type is not None:
            body["last_action_type"] = self.last_action_type
        if self.last_version_id is not None:
            body["last_version_id"] = self.last_version_id
        if self.name is not None:
            body["name"] = self.name
        if self.resource_id is not None:
            body["resource_id"] = self.resource_id
        if self.resource_key is not None:
            body["resource_key"] = self.resource_key
        if self.resource_type is not None:
            body["resource_type"] = self.resource_type
        if self.state:
            body["state"] = self.state
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Resource:
        """Deserializes the Resource from a dictionary."""
        return cls(
            last_action_type=_enum(d, "last_action_type", OperationActionType),
            last_version_id=d.get("last_version_id", None),
            name=d.get("name", None),
            resource_id=d.get("resource_id", None),
            resource_key=d.get("resource_key", None),
            resource_type=_enum(d, "resource_type", DeploymentResourceType),
            state=d.get("state", None),
        )


@dataclass
class Version:
    """A single invocation of a deploy or destroy command against a deployment. Creating a version
    acquires an exclusive lock on the parent deployment."""

    cli_version: str
    """CLI version used to initiate the version."""

    version_type: VersionType
    """Type of version (deploy or destroy)."""

    complete_time: Optional[Timestamp] = None
    """When the version completed. Unset while the version is in progress."""

    completed_by: Optional[str] = None
    """The user who completed the version (email or principal name). May differ from `created_by` when
    another user force-completes the version."""

    completion_reason: Optional[VersionComplete] = None
    """Why the version was completed. Unset while in progress. Set when status transitions to
    COMPLETED."""

    create_time: Optional[Timestamp] = None
    """When the version was created."""

    created_by: Optional[str] = None
    """The user who created the version (email or principal name)."""

    display_name: Optional[str] = None
    """Display name for the deployment, captured at the time of this version."""

    name: Optional[str] = None
    """Resource name of the version. Format: deployments/{deployment_id}/versions/{version_id}"""

    status: Optional[VersionStatus] = None
    """Status of the version: IN_PROGRESS or COMPLETED."""

    target_name: Optional[str] = None
    """Target name of the deployment, captured at the time of this version."""

    version_id: Optional[str] = None
    """Monotonically increasing version identifier within the parent deployment. Assigned by the client
    on creation."""

    def as_dict(self) -> dict:
        """Serializes the Version into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.cli_version is not None:
            body["cli_version"] = self.cli_version
        if self.complete_time is not None:
            body["complete_time"] = self.complete_time.ToJsonString()
        if self.completed_by is not None:
            body["completed_by"] = self.completed_by
        if self.completion_reason is not None:
            body["completion_reason"] = self.completion_reason.value
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.created_by is not None:
            body["created_by"] = self.created_by
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.name is not None:
            body["name"] = self.name
        if self.status is not None:
            body["status"] = self.status.value
        if self.target_name is not None:
            body["target_name"] = self.target_name
        if self.version_id is not None:
            body["version_id"] = self.version_id
        if self.version_type is not None:
            body["version_type"] = self.version_type.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Version into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.cli_version is not None:
            body["cli_version"] = self.cli_version
        if self.complete_time is not None:
            body["complete_time"] = self.complete_time
        if self.completed_by is not None:
            body["completed_by"] = self.completed_by
        if self.completion_reason is not None:
            body["completion_reason"] = self.completion_reason
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.created_by is not None:
            body["created_by"] = self.created_by
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.name is not None:
            body["name"] = self.name
        if self.status is not None:
            body["status"] = self.status
        if self.target_name is not None:
            body["target_name"] = self.target_name
        if self.version_id is not None:
            body["version_id"] = self.version_id
        if self.version_type is not None:
            body["version_type"] = self.version_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Version:
        """Deserializes the Version from a dictionary."""
        return cls(
            cli_version=d.get("cli_version", None),
            complete_time=_timestamp(d, "complete_time"),
            completed_by=d.get("completed_by", None),
            completion_reason=_enum(d, "completion_reason", VersionComplete),
            create_time=_timestamp(d, "create_time"),
            created_by=d.get("created_by", None),
            display_name=d.get("display_name", None),
            name=d.get("name", None),
            status=_enum(d, "status", VersionStatus),
            target_name=d.get("target_name", None),
            version_id=d.get("version_id", None),
            version_type=_enum(d, "version_type", VersionType),
        )


class VersionComplete(Enum):
    """Reason why a version was completed."""

    VERSION_COMPLETE_FAILURE = "VERSION_COMPLETE_FAILURE"
    VERSION_COMPLETE_FORCE_ABORT = "VERSION_COMPLETE_FORCE_ABORT"
    VERSION_COMPLETE_LEASE_EXPIRED = "VERSION_COMPLETE_LEASE_EXPIRED"
    VERSION_COMPLETE_SUCCESS = "VERSION_COMPLETE_SUCCESS"


class VersionStatus(Enum):
    """Status of a version."""

    VERSION_STATUS_COMPLETED = "VERSION_STATUS_COMPLETED"
    VERSION_STATUS_IN_PROGRESS = "VERSION_STATUS_IN_PROGRESS"


class VersionType(Enum):
    """Type of version."""

    VERSION_TYPE_DEPLOY = "VERSION_TYPE_DEPLOY"
    VERSION_TYPE_DESTROY = "VERSION_TYPE_DESTROY"


class BundleAPI:
    """Service for managing bundle deployment metadata."""

    def __init__(self, api_client):
        self._api = api_client

    def complete_version(
        self, name: str, completion_reason: VersionComplete, *, force: Optional[bool] = None
    ) -> Version:
        """Marks a version as complete and releases the deployment lock.

        The server atomically: 1. Sets the version status to the provided terminal status. 2. Sets
        `complete_time` to the current server timestamp. 3. Releases the lock on the parent deployment. 4.
        Updates the parent deployment's `status` and `last_version_id`.

        :param name: str
          The name of the version to complete. Format: deployments/{deployment_id}/versions/{version_id}
        :param completion_reason: :class:`VersionComplete`
          The reason for completing the version. Must be a terminal reason: VERSION_COMPLETE_SUCCESS,
          VERSION_COMPLETE_FAILURE, or VERSION_COMPLETE_FORCE_ABORT.
        :param force: bool (optional)
          If true, force-completes the version even if the caller is not the original creator. The
          completion_reason must be VERSION_COMPLETE_FORCE_ABORT when force is true.

        :returns: :class:`Version`
        """

        body = {}
        if completion_reason is not None:
            body["completion_reason"] = completion_reason.value
        if force is not None:
            body["force"] = force
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/bundle/{name}/complete", body=body, headers=headers)
        return Version.from_dict(res)

    def create_deployment(self, deployment: Deployment, deployment_id: str) -> Deployment:
        """Creates a new deployment in the workspace.

        The caller must provide a `deployment_id` which becomes the final component of the deployment's
        resource name. If a deployment with the same ID already exists, the server returns `ALREADY_EXISTS`.

        :param deployment: :class:`Deployment`
          The deployment to create.
        :param deployment_id: str
          The ID to use for the deployment, which will become the final component of the deployment's resource
          name (i.e. `deployments/{deployment_id}`).

        :returns: :class:`Deployment`
        """

        body = deployment.as_dict()
        query = {}
        if deployment_id is not None:
            query["deployment_id"] = deployment_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/bundle/deployments", query=query, body=body, headers=headers)
        return Deployment.from_dict(res)

    def create_operation(self, parent: str, operation: Operation, resource_key: str) -> Operation:
        """Creates a resource operation under a version.

        The caller must provide a `resource_key` which becomes the final component of the operation's name. If
        an operation with the same key already exists under the version, the server returns `ALREADY_EXISTS`.

        On success the server also updates the corresponding deployment-level Resource (creating it if this is
        the first operation for that resource_key, or removing it if action_type is DELETE).

        :param parent: str
          The parent version where this operation will be recorded. Format:
          deployments/{deployment_id}/versions/{version_id}
        :param operation: :class:`Operation`
          The resource operation to create.
        :param resource_key: str
          The key identifying the resource this operation applies to. Becomes the final component of the
          operation's name.

        :returns: :class:`Operation`
        """

        body = operation.as_dict()
        query = {}
        if resource_key is not None:
            query["resource_key"] = resource_key
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/bundle/{parent}/operations", query=query, body=body, headers=headers)
        return Operation.from_dict(res)

    def create_version(self, parent: str, version: Version, version_id: str) -> Version:
        """Creates a new version under a deployment.

        Creating a version acquires an exclusive lock on the deployment, preventing concurrent deploys. The
        caller provides a `version_id` which the server validates equals `last_version_id + 1` on the
        deployment.

        :param parent: str
          The parent deployment where this version will be created. Format: deployments/{deployment_id}
        :param version: :class:`Version`
          The version to create.
        :param version_id: str
          The version ID the caller expects to create. The server validates this equals `last_version_id + 1`
          on the deployment. If it doesn't match, the server returns `ABORTED`.

        :returns: :class:`Version`
        """

        body = version.as_dict()
        query = {}
        if version_id is not None:
            query["version_id"] = version_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/bundle/{parent}/versions", query=query, body=body, headers=headers)
        return Version.from_dict(res)

    def delete_deployment(self, name: str):
        """Deletes a deployment.

        The deployment is marked as deleted. It and all its children (versions and their operations) will be
        permanently deleted after the retention policy expires. If the deployment has an in-progress version,
        the server returns `RESOURCE_CONFLICT`.

        :param name: str
          Resource name of the deployment to delete. Format: deployments/{deployment_id}


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/bundle/{name}", headers=headers)

    def get_deployment(self, name: str) -> Deployment:
        """Retrieves a deployment by its resource name.

        :param name: str
          Resource name of the deployment to retrieve. Format: deployments/{deployment_id}

        :returns: :class:`Deployment`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/bundle/{name}", headers=headers)
        return Deployment.from_dict(res)

    def get_operation(self, name: str) -> Operation:
        """Retrieves a resource operation by its resource name.

        :param name: str
          The name of the resource operation to retrieve. Format:
          deployments/{deployment_id}/versions/{version_id}/operations/{resource_key}

        :returns: :class:`Operation`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/bundle/{name}", headers=headers)
        return Operation.from_dict(res)

    def get_resource(self, name: str) -> Resource:
        """Retrieves a deployment resource by its resource name.

        :param name: str
          The name of the resource to retrieve. Format: deployments/{deployment_id}/resources/{resource_key}

        :returns: :class:`Resource`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/bundle/{name}", headers=headers)
        return Resource.from_dict(res)

    def get_version(self, name: str) -> Version:
        """Retrieves a version by its resource name.

        :param name: str
          The name of the version to retrieve. Format: deployments/{deployment_id}/versions/{version_id}

        :returns: :class:`Version`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/bundle/{name}", headers=headers)
        return Version.from_dict(res)

    def heartbeat(self, name: str) -> HeartbeatResponse:
        """Sends a heartbeat to renew the lock held by a version.

        The server validates that the version is the active (non-terminal) version on the parent deployment
        and resets the lock expiry. If the lock has already expired or the version is no longer active, the
        server returns `ABORTED`.

        :param name: str
          The version whose lock to renew. Format: deployments/{deployment_id}/versions/{version_id}

        :returns: :class:`HeartbeatResponse`
        """

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/bundle/{name}/heartbeat", headers=headers)
        return HeartbeatResponse.from_dict(res)

    def list_deployments(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Deployment]:
        """Lists deployments in the workspace.

        :param page_size: int (optional)
          The maximum number of deployments to return. The service may return fewer than this value. If
          unspecified, at most 50 deployments will be returned. The maximum value is 1000; values above 1000
          will be coerced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous `ListDeployments` call. Provide this to retrieve the
          subsequent page.

        :returns: Iterator over :class:`Deployment`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", "/api/2.0/bundle/deployments", query=query, headers=headers)
            if "deployments" in json:
                for v in json["deployments"]:
                    yield Deployment.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_operations(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Operation]:
        """Lists resource operations under a version.

        :param parent: str
          The parent version. Format: deployments/{deployment_id}/versions/{version_id}
        :param page_size: int (optional)
          The maximum number of operations to return. The service may return fewer than this value. If
          unspecified, at most 50 operations will be returned. The maximum value is 1000; values above 1000
          will be coerced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous `ListOperations` call. Provide this to retrieve the
          subsequent page.

        :returns: Iterator over :class:`Operation`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", f"/api/2.0/bundle/{parent}/operations", query=query, headers=headers)
            if "operations" in json:
                for v in json["operations"]:
                    yield Operation.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_resources(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Resource]:
        """Lists resources under a deployment.

        :param parent: str
          The parent deployment. Format: deployments/{deployment_id}
        :param page_size: int (optional)
          The maximum number of resources to return. The service may return fewer than this value. If
          unspecified, at most 50 resources will be returned. The maximum value is 1000; values above 1000
          will be coerced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous `ListResources` call. Provide this to retrieve the subsequent
          page.

        :returns: Iterator over :class:`Resource`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", f"/api/2.0/bundle/{parent}/resources", query=query, headers=headers)
            if "resources" in json:
                for v in json["resources"]:
                    yield Resource.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_versions(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Version]:
        """Lists versions under a deployment, ordered by version_id descending (most recent first).

        :param parent: str
          The parent deployment. Format: deployments/{deployment_id}
        :param page_size: int (optional)
          The maximum number of versions to return. The service may return fewer than this value. If
          unspecified, at most 50 versions will be returned. The maximum value is 1000; values above 1000 will
          be coerced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous `ListVersions` call. Provide this to retrieve the subsequent
          page.

        :returns: Iterator over :class:`Version`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", f"/api/2.0/bundle/{parent}/versions", query=query, headers=headers)
            if "versions" in json:
                for v in json["versions"]:
                    yield Version.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

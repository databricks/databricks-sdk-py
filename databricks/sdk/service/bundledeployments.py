# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.
# ruff: noqa: F811, F841
# F401 is intentionally NOT covered: `make fmt` uses `ruff check --fix-only`
# to strip the fat-import header below; ignoring F401 would defeat that.

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any, Iterator, Optional

from google.protobuf.timestamp_pb2 import Timestamp

import logging

from databricks.sdk.service._internal import (
    _enum,
    _from_dict,
    _int64,
    _repeated_dict,
    _timestamp,
)
from databricks.sdk.common.types.fieldmask import FieldMask


_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class DashboardMetadata:
    """Dashboard-specific per-resource metadata. Set only for dashboard resources."""

    definition_path: Optional[str] = None
    """Path of the file that declares this dashboard, relative to the bundle's workspace.file_path
    (Version.workspace_info.file_path) — join the two to get the file's absolute workspace path.
    
    For now this lives only on the dashboard metadata, and is a single string because it was a
    single string (``relative_path``) in the legacy bundle metadata.json. We may generalize it in
    the future: lifting it to a top-level field on Resource/Operation (every resource type has a
    definition location) and converting it to a repeated field, since a resource can be declared
    across multiple files/locations."""

    source_path: Optional[str] = None
    """Path of the dashboard's source artifact (its ``.lvdash.json``), relative to the deployment root."""

    def as_dict(self) -> dict:
        """Serializes the DashboardMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.definition_path is not None:
            body["definition_path"] = self.definition_path
        if self.source_path is not None:
            body["source_path"] = self.source_path
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DashboardMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.definition_path is not None:
            body["definition_path"] = self.definition_path
        if self.source_path is not None:
            body["source_path"] = self.source_path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DashboardMetadata:
        """Deserializes the DashboardMetadata from a dictionary."""
        return cls(definition_path=d.get("definition_path", None), source_path=d.get("source_path", None))


@dataclass
class Deployment:
    """A bundle deployment registered with the control plane."""

    create_time: Optional[Timestamp] = None
    """When the deployment was created."""

    created_by: Optional[str] = None
    """The user who created the deployment (email or principal name). Empty if authoritative deployment
    metadata does not identify a creator or the principal cannot be resolved."""

    deployment_mode: Optional[DeploymentMode] = None
    """Bundle target deployment mode (development or production), derived from the most recent
    version's mode."""

    destroy_time: Optional[Timestamp] = None
    """When deletion was recorded. Unset if deletion has not been recorded. This response metadata does
    not determine the deployment's lifecycle status."""

    destroyed_by: Optional[str] = None
    """The user who destroyed the deployment (email or principal name). Unset if the deployment has not
    been destroyed."""

    display_name: Optional[str] = None
    """Human-readable name for the deployment, up to 256 characters. Output only: clients update it by
    setting ``display_name`` when creating a version."""

    git_info: Optional[GitInfo] = None
    """Git provenance of the deployment's source, derived from the latest version."""

    initial_parent_path: Optional[str] = None
    """The workspace path of the existing folder where the deployment is initially created. Must be
    absolute and canonical, with single separators, no ``.`` or ``..`` segments, and no trailing
    slash unless the path is ``/``. It may contain at most 24 path segments, excluding an optional
    leading ``/Workspace`` segment. The complete path may contain up to 1,024 characters, and each
    segment may contain up to 511 characters. This field is input only and is not returned in
    create, get, or list responses."""

    last_successful_version_id: Optional[str] = None
    """The version_id of the most recent version that completed successfully. Unset until a version has
    completed successfully. Unlike last_version_id, it is not advanced when a version fails, so it
    always points at the last known-good deployment state (or is unset if there has never been one)."""

    last_version_id: Optional[str] = None
    """The version_id of the most recent deployment version."""

    name: Optional[str] = None
    """Resource name of the deployment. Format: deployments/{deployment_id}"""

    status: Optional[DeploymentStatus] = None
    """Current status of the deployment."""

    target_name: Optional[str] = None
    """The bundle target name associated with this deployment. Output only: it is denormalized from the
    latest version, not set directly on the deployment."""

    update_time: Optional[Timestamp] = None
    """When the deployment was last updated."""

    updated_by: Optional[str] = None
    """The user who most recently updated the deployment (email or principal name). Empty if
    authoritative deployment metadata does not identify a modifier or the principal cannot be
    resolved."""

    workspace_info: Optional[WorkspaceInfo] = None
    """Workspace location of the deployment, derived from the latest version."""

    def as_dict(self) -> dict:
        """Serializes the Deployment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.created_by is not None:
            body["created_by"] = self.created_by
        if self.deployment_mode is not None:
            body["deployment_mode"] = self.deployment_mode.value
        if self.destroy_time is not None:
            body["destroy_time"] = self.destroy_time.ToJsonString()
        if self.destroyed_by is not None:
            body["destroyed_by"] = self.destroyed_by
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.git_info:
            body["git_info"] = self.git_info.as_dict()
        if self.initial_parent_path is not None:
            body["initial_parent_path"] = self.initial_parent_path
        if self.last_successful_version_id is not None:
            body["last_successful_version_id"] = self.last_successful_version_id
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
        if self.updated_by is not None:
            body["updated_by"] = self.updated_by
        if self.workspace_info:
            body["workspace_info"] = self.workspace_info.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Deployment into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.created_by is not None:
            body["created_by"] = self.created_by
        if self.deployment_mode is not None:
            body["deployment_mode"] = self.deployment_mode
        if self.destroy_time is not None:
            body["destroy_time"] = self.destroy_time
        if self.destroyed_by is not None:
            body["destroyed_by"] = self.destroyed_by
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.git_info:
            body["git_info"] = self.git_info
        if self.initial_parent_path is not None:
            body["initial_parent_path"] = self.initial_parent_path
        if self.last_successful_version_id is not None:
            body["last_successful_version_id"] = self.last_successful_version_id
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
        if self.updated_by is not None:
            body["updated_by"] = self.updated_by
        if self.workspace_info:
            body["workspace_info"] = self.workspace_info
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Deployment:
        """Deserializes the Deployment from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            created_by=d.get("created_by", None),
            deployment_mode=_enum(d, "deployment_mode", DeploymentMode),
            destroy_time=_timestamp(d, "destroy_time"),
            destroyed_by=d.get("destroyed_by", None),
            display_name=d.get("display_name", None),
            git_info=_from_dict(d, "git_info", GitInfo),
            initial_parent_path=d.get("initial_parent_path", None),
            last_successful_version_id=d.get("last_successful_version_id", None),
            last_version_id=d.get("last_version_id", None),
            name=d.get("name", None),
            status=_enum(d, "status", DeploymentStatus),
            target_name=d.get("target_name", None),
            update_time=_timestamp(d, "update_time"),
            updated_by=d.get("updated_by", None),
            workspace_info=_from_dict(d, "workspace_info", WorkspaceInfo),
        )


class DeploymentMode(Enum):
    """Bundle target deployment mode. Mirrors the ``mode`` field on a bundle target in
    ``databricks.yml`` (see https://docs.databricks.com/dev-tools/bundles/deployment-modes)."""

    DEPLOYMENT_MODE_DEVELOPMENT = "DEPLOYMENT_MODE_DEVELOPMENT"
    DEPLOYMENT_MODE_PRODUCTION = "DEPLOYMENT_MODE_PRODUCTION"


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
    DEPLOYMENT_RESOURCE_TYPE_GENIE_SPACE = "DEPLOYMENT_RESOURCE_TYPE_GENIE_SPACE"
    DEPLOYMENT_RESOURCE_TYPE_INSTANCE_POOL = "DEPLOYMENT_RESOURCE_TYPE_INSTANCE_POOL"
    DEPLOYMENT_RESOURCE_TYPE_JOB = "DEPLOYMENT_RESOURCE_TYPE_JOB"
    DEPLOYMENT_RESOURCE_TYPE_JOB_RUN = "DEPLOYMENT_RESOURCE_TYPE_JOB_RUN"
    DEPLOYMENT_RESOURCE_TYPE_MODEL = "DEPLOYMENT_RESOURCE_TYPE_MODEL"
    DEPLOYMENT_RESOURCE_TYPE_MODEL_SERVING_ENDPOINT = "DEPLOYMENT_RESOURCE_TYPE_MODEL_SERVING_ENDPOINT"
    DEPLOYMENT_RESOURCE_TYPE_PIPELINE = "DEPLOYMENT_RESOURCE_TYPE_PIPELINE"
    DEPLOYMENT_RESOURCE_TYPE_POSTGRES_BRANCH = "DEPLOYMENT_RESOURCE_TYPE_POSTGRES_BRANCH"
    DEPLOYMENT_RESOURCE_TYPE_POSTGRES_CATALOG = "DEPLOYMENT_RESOURCE_TYPE_POSTGRES_CATALOG"
    DEPLOYMENT_RESOURCE_TYPE_POSTGRES_DATABASE = "DEPLOYMENT_RESOURCE_TYPE_POSTGRES_DATABASE"
    DEPLOYMENT_RESOURCE_TYPE_POSTGRES_ENDPOINT = "DEPLOYMENT_RESOURCE_TYPE_POSTGRES_ENDPOINT"
    DEPLOYMENT_RESOURCE_TYPE_POSTGRES_PROJECT = "DEPLOYMENT_RESOURCE_TYPE_POSTGRES_PROJECT"
    DEPLOYMENT_RESOURCE_TYPE_POSTGRES_ROLE = "DEPLOYMENT_RESOURCE_TYPE_POSTGRES_ROLE"
    DEPLOYMENT_RESOURCE_TYPE_POSTGRES_SYNCED_TABLE = "DEPLOYMENT_RESOURCE_TYPE_POSTGRES_SYNCED_TABLE"
    DEPLOYMENT_RESOURCE_TYPE_QUALITY_MONITOR = "DEPLOYMENT_RESOURCE_TYPE_QUALITY_MONITOR"
    DEPLOYMENT_RESOURCE_TYPE_REGISTERED_MODEL = "DEPLOYMENT_RESOURCE_TYPE_REGISTERED_MODEL"
    DEPLOYMENT_RESOURCE_TYPE_SCHEMA = "DEPLOYMENT_RESOURCE_TYPE_SCHEMA"
    DEPLOYMENT_RESOURCE_TYPE_SECRET_SCOPE = "DEPLOYMENT_RESOURCE_TYPE_SECRET_SCOPE"
    DEPLOYMENT_RESOURCE_TYPE_SQL_WAREHOUSE = "DEPLOYMENT_RESOURCE_TYPE_SQL_WAREHOUSE"
    DEPLOYMENT_RESOURCE_TYPE_SYNCED_DATABASE_TABLE = "DEPLOYMENT_RESOURCE_TYPE_SYNCED_DATABASE_TABLE"
    DEPLOYMENT_RESOURCE_TYPE_VECTOR_SEARCH_ENDPOINT = "DEPLOYMENT_RESOURCE_TYPE_VECTOR_SEARCH_ENDPOINT"
    DEPLOYMENT_RESOURCE_TYPE_VECTOR_SEARCH_INDEX = "DEPLOYMENT_RESOURCE_TYPE_VECTOR_SEARCH_INDEX"
    DEPLOYMENT_RESOURCE_TYPE_VOLUME = "DEPLOYMENT_RESOURCE_TYPE_VOLUME"


class DeploymentStatus(Enum):
    """Status of a deployment."""

    DEPLOYMENT_STATUS_ACTIVE = "DEPLOYMENT_STATUS_ACTIVE"
    DEPLOYMENT_STATUS_DELETED = "DEPLOYMENT_STATUS_DELETED"
    DEPLOYMENT_STATUS_FAILED = "DEPLOYMENT_STATUS_FAILED"
    DEPLOYMENT_STATUS_IN_PROGRESS = "DEPLOYMENT_STATUS_IN_PROGRESS"


@dataclass
class GitInfo:
    """Git provenance of a bundle's source, captured at deploy time. Lets consumers link a deployed
    resource back to its source in version control."""

    branch: Optional[str] = None
    """Branch the source was deployed from."""

    commit: Optional[str] = None
    """Commit SHA of the deployed source."""

    origin_url: Optional[str] = None
    """URL of the git remote the source was deployed from."""

    def as_dict(self) -> dict:
        """Serializes the GitInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.branch is not None:
            body["branch"] = self.branch
        if self.commit is not None:
            body["commit"] = self.commit
        if self.origin_url is not None:
            body["origin_url"] = self.origin_url
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GitInfo into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.branch is not None:
            body["branch"] = self.branch
        if self.commit is not None:
            body["commit"] = self.commit
        if self.origin_url is not None:
            body["origin_url"] = self.origin_url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GitInfo:
        """Deserializes the GitInfo from a dictionary."""
        return cls(branch=d.get("branch", None), commit=d.get("commit", None), origin_url=d.get("origin_url", None))


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
    """A token, which can be sent as ``page_token`` to retrieve the next page. If this field is
    omitted, there are no subsequent pages."""

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
    """A token, which can be sent as ``page_token`` to retrieve the next page. If this field is
    omitted, there are no subsequent pages."""

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
    """A token, which can be sent as ``page_token`` to retrieve the next page. If this field is
    omitted, there are no subsequent pages."""

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
    """A token, which can be sent as ``page_token`` to retrieve the next page. If this field is
    omitted, there are no subsequent pages."""

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
    """An operation on a single resource performed during a version. The full set of operations for a
    version is recorded when the version is created: each carries its ``resource_key`` and
    ``action_type`` and starts in ``OPERATION_STATUS_PENDING``. As each resource is applied, its
    operation is updated (via UpdateOperation) to record the result of applying the change to the
    workspace. ``state``, ``error_message``, ``resource_id``, ``status``, and ``dashboard_metadata``
    may be updated afterwards, guarded by ``sequence_id`` for optimistic concurrency control; all
    other fields are immutable once recorded."""

    action_type: Optional[OperationActionType] = None
    """The type of operation performed on this resource. Set when the version is created and immutable
    thereafter."""

    create_time: Optional[Timestamp] = None
    """When the operation was recorded."""

    dashboard_metadata: Optional[DashboardMetadata] = None
    """Dashboard-specific metadata; set only for dashboard resources. Mutable: may be set or updated
    via UpdateOperation as the resource is applied, and is mirrored onto the corresponding
    deployment-level resource."""

    error_message: Optional[str] = None
    """Error message if the operation failed. Set when status is OPERATION_STATUS_FAILED. Captures the
    error encountered while applying the resource to the workspace. Mutable: may be updated after
    creation via UpdateOperation; setting it to an empty string clears it. After an update is
    applied, an operation whose status is OPERATION_STATUS_SUCCEEDED cannot carry an error_message."""

    name: Optional[str] = None
    """Resource name of the operation. Format:
    deployments/{deployment_id}/versions/{version_id}/operations/{resource_key}"""

    resource_id: Optional[str] = None
    """ID of the actual resource in the workspace (e.g. the job ID, pipeline ID). Required whenever
    ``state`` is set, because state records a resource that exists. A CREATE or RECREATE that has
    not produced its resource yet records neither. Mutable: may be filled in (or corrected) later
    via UpdateOperation once the ID is known."""

    resource_key: Optional[str] = None
    """Resource identifier within the bundle (e.g. "jobs.foo", "pipelines.bar", "jobs.foo.permissions",
    "files.<rel-path>"). Can be an arbitrary UTF-8 encoded string key. This key links the operation
    to the corresponding deployment-level Resource. Set when the version is created and immutable
    thereafter."""

    resource_type: Optional[DeploymentResourceType] = None
    """The type of the deployment resource this operation applies to. Derived from the ``resource_key``
    prefix (e.g. "jobs" → JOB); the caller does not set this field."""

    sequence_id: Optional[int] = None
    """Monotonically increasing revision used for optimistic concurrency control (the AIP-154
    concurrency token for this resource, realized as a sequence number rather than an opaque etag).
    The server assigns 0 when the operation is created and increments it on every successful
    UpdateOperation, so a never-updated operation is at 0 and the first successful update makes it
    1. It is OPTIONAL rather than OUTPUT_ONLY because it is dual-purpose: GetOperation returns the
    current value, and UpdateOperation reads the caller-supplied value as a precondition. The caller
    must echo the value it last observed; if it no longer matches the server's value, the update is
    rejected with ABORTED so the caller can re-read and retry."""

    state: Optional[str] = None
    """Serialized local config state after the operation. Its presence records whether the resource
    still exists, so an operation that records no state removes its resource from the deployment. It
    may be unset only for an operation that left no resource behind: a ``DELETE`` that succeeded, or
    a ``CREATE`` or ``RECREATE`` that failed. It is required otherwise, including for a failed
    ``DELETE``, whose resource survives.
    
    Mutable: may be updated after creation via UpdateOperation. When updating, the caller must echo
    the last-observed ``sequence_id`` as a concurrency precondition.
    
    Opaque to this service: the string is stored and returned unchanged. This is deliberately not
    google.protobuf.Value, whose only numeric case is ``double number_value``, so parsing the
    client's JSON into it rewrites every integer as a double - ``1`` reads back as ``1.0``, which no
    longer deserializes into an integer field - and silently loses precision above 2^53, which is
    within range for IDs the client records.
    
    A string rather than bytes: the payload is always UTF-8 JSON, and proto3 JSON maps bytes to
    base64, which inflates every request and response by a third and makes state unreadable in logs
    and API responses. Both generate the same OpenAPI schema ("type": "string"), so the SDKs are
    identical either way."""

    status: Optional[OperationStatus] = None
    """Status of the operation. Starts as OPERATION_STATUS_PENDING when the version is created and
    moves to a terminal status once the resource is applied. Mutable: updated via UpdateOperation,
    e.g. when an operation recorded as failed is retried and eventually succeeds. A succeeded
    operation cannot carry an ``error_message``."""

    update_time: Optional[Timestamp] = None
    """When the operation was last updated. Set to ``create_time`` when the operation is created and to
    the server timestamp on each successful UpdateOperation."""

    def as_dict(self) -> dict:
        """Serializes the Operation into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.action_type is not None:
            body["action_type"] = self.action_type.value
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.dashboard_metadata:
            body["dashboard_metadata"] = self.dashboard_metadata.as_dict()
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
        if self.sequence_id is not None:
            body["sequence_id"] = self.sequence_id
        if self.state is not None:
            body["state"] = self.state
        if self.status is not None:
            body["status"] = self.status.value
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Operation into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.action_type is not None:
            body["action_type"] = self.action_type
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.dashboard_metadata:
            body["dashboard_metadata"] = self.dashboard_metadata
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
        if self.sequence_id is not None:
            body["sequence_id"] = self.sequence_id
        if self.state is not None:
            body["state"] = self.state
        if self.status is not None:
            body["status"] = self.status
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Operation:
        """Deserializes the Operation from a dictionary."""
        return cls(
            action_type=_enum(d, "action_type", OperationActionType),
            create_time=_timestamp(d, "create_time"),
            dashboard_metadata=_from_dict(d, "dashboard_metadata", DashboardMetadata),
            error_message=d.get("error_message", None),
            name=d.get("name", None),
            resource_id=d.get("resource_id", None),
            resource_key=d.get("resource_key", None),
            resource_type=_enum(d, "resource_type", DeploymentResourceType),
            sequence_id=_int64(d, "sequence_id"),
            state=d.get("state", None),
            status=_enum(d, "status", OperationStatus),
            update_time=_timestamp(d, "update_time"),
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
    OPERATION_STATUS_PENDING = "OPERATION_STATUS_PENDING"
    OPERATION_STATUS_SUCCEEDED = "OPERATION_STATUS_SUCCEEDED"


@dataclass
class Resource:
    """A resource managed by a deployment. Resources are implicitly created, updated, or deleted when
    operations are recorded on a version."""

    resource_type: DeploymentResourceType
    """The type of the deployment resource."""

    dashboard_metadata: Optional[DashboardMetadata] = None
    """Dashboard-specific metadata; set only for dashboard resources."""

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

    state: Optional[str] = None
    """Serialized local config state (what the CLI deployed). Opaque to this service; see
    Operation.state for why this is a string and not google.protobuf.Value."""

    update_time: Optional[Timestamp] = None
    """When the last operation that updated this resource's recorded state was applied. Pairs with
    last_action_type and last_version_id (all three advance together on that write)."""

    def as_dict(self) -> dict:
        """Serializes the Resource into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.dashboard_metadata:
            body["dashboard_metadata"] = self.dashboard_metadata.as_dict()
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
        if self.state is not None:
            body["state"] = self.state
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Resource into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.dashboard_metadata:
            body["dashboard_metadata"] = self.dashboard_metadata
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
        if self.state is not None:
            body["state"] = self.state
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Resource:
        """Deserializes the Resource from a dictionary."""
        return cls(
            dashboard_metadata=_from_dict(d, "dashboard_metadata", DashboardMetadata),
            last_action_type=_enum(d, "last_action_type", OperationActionType),
            last_version_id=d.get("last_version_id", None),
            name=d.get("name", None),
            resource_id=d.get("resource_id", None),
            resource_key=d.get("resource_key", None),
            resource_type=_enum(d, "resource_type", DeploymentResourceType),
            state=d.get("state", None),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class StagedOperation:
    """A resource operation to record when a version is created. Each staged operation identifies the
    resource it applies to and the action planned for it; the server records the operation in
    ``OPERATION_STATUS_PENDING``, and its outcome is filled in later via UpdateOperation."""

    resource_key: str
    """The key identifying the resource this operation applies to (e.g. "jobs.foo", "pipelines.bar").
    Becomes the final component of the operation's name and must be unique among the operations in
    the request."""

    action_type: OperationActionType
    """The type of operation planned for this resource."""

    def as_dict(self) -> dict:
        """Serializes the StagedOperation into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.action_type is not None:
            body["action_type"] = self.action_type.value
        if self.resource_key is not None:
            body["resource_key"] = self.resource_key
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the StagedOperation into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.action_type is not None:
            body["action_type"] = self.action_type
        if self.resource_key is not None:
            body["resource_key"] = self.resource_key
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> StagedOperation:
        """Deserializes the StagedOperation from a dictionary."""
        return cls(action_type=_enum(d, "action_type", OperationActionType), resource_key=d.get("resource_key", None))


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
    """The user who completed the version (email or principal name). May differ from ``created_by``
    when another user force-completes the version."""

    completion_reason: Optional[VersionComplete] = None
    """Why the version was completed. Unset while in progress. Set when status transitions to
    COMPLETED."""

    create_time: Optional[Timestamp] = None
    """When the version was created."""

    created_by: Optional[str] = None
    """The user who created the version (email or principal name)."""

    deployment_mode: Optional[DeploymentMode] = None
    """Bundle target deployment mode (development or production), captured at the time of this version."""

    display_name: Optional[str] = None
    """Display name for the deployment, captured at the time of this version. Up to 256 characters.
    When present, creating the version updates the deployment display name. An empty value clears
    it; an absent value leaves the current deployment display name unchanged."""

    git_info: Optional[GitInfo] = None
    """Git provenance of the source, captured at the time of this version."""

    name: Optional[str] = None
    """Resource name of the version. Format: deployments/{deployment_id}/versions/{version_id}"""

    previous_version_id: Optional[str] = None
    """The version_id this version was created on top of — the deployment's most recent version at
    creation time. Leave unset when creating the first version (the deployment has no prior
    versions). Set by the client on creation and immutable thereafter.
    
    Acts as an optimistic-concurrency precondition: the server requires it to equal the deployment's
    current most-recent version (and to be unset when the deployment has no versions) and returns
    ``INVALID_PARAMETER_VALUE`` on mismatch, so a deploy racing against a concurrent deploy is
    rejected rather than silently overwriting it."""

    status: Optional[VersionStatus] = None
    """Status of the version: IN_PROGRESS or COMPLETED."""

    target_name: Optional[str] = None
    """Target name of the deployment, captured at the time of this version."""

    version_id: Optional[str] = None
    """Version identifier within the parent deployment, assigned by the client on creation. A numeric
    string (base-10, fits in a signed 64-bit integer) that is greater than or equal to 1. Version
    IDs are strictly increasing within a deployment but are not required to start at 1 or to be
    contiguous."""

    workspace_info: Optional[WorkspaceInfo] = None
    """Workspace location of the deployment, captured at the time of this version."""

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
        if self.deployment_mode is not None:
            body["deployment_mode"] = self.deployment_mode.value
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.git_info:
            body["git_info"] = self.git_info.as_dict()
        if self.name is not None:
            body["name"] = self.name
        if self.previous_version_id is not None:
            body["previous_version_id"] = self.previous_version_id
        if self.status is not None:
            body["status"] = self.status.value
        if self.target_name is not None:
            body["target_name"] = self.target_name
        if self.version_id is not None:
            body["version_id"] = self.version_id
        if self.version_type is not None:
            body["version_type"] = self.version_type.value
        if self.workspace_info:
            body["workspace_info"] = self.workspace_info.as_dict()
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
        if self.deployment_mode is not None:
            body["deployment_mode"] = self.deployment_mode
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.git_info:
            body["git_info"] = self.git_info
        if self.name is not None:
            body["name"] = self.name
        if self.previous_version_id is not None:
            body["previous_version_id"] = self.previous_version_id
        if self.status is not None:
            body["status"] = self.status
        if self.target_name is not None:
            body["target_name"] = self.target_name
        if self.version_id is not None:
            body["version_id"] = self.version_id
        if self.version_type is not None:
            body["version_type"] = self.version_type
        if self.workspace_info:
            body["workspace_info"] = self.workspace_info
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
            deployment_mode=_enum(d, "deployment_mode", DeploymentMode),
            display_name=d.get("display_name", None),
            git_info=_from_dict(d, "git_info", GitInfo),
            name=d.get("name", None),
            previous_version_id=d.get("previous_version_id", None),
            status=_enum(d, "status", VersionStatus),
            target_name=d.get("target_name", None),
            version_id=d.get("version_id", None),
            version_type=_enum(d, "version_type", VersionType),
            workspace_info=_from_dict(d, "workspace_info", WorkspaceInfo),
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


@dataclass
class WorkspaceInfo:
    """Workspace location of a bundle deployment, captured at deploy time."""

    bundle_root_path: Optional[str] = None
    """Path of the bundle root (the directory containing databricks.yml) relative to git_folder_path.
    Empty when the deployment is not from a Databricks Git folder."""

    file_path: Optional[str] = None
    """Absolute workspace path where the deployed bundle files live. Mirrors the workspace.file_path
    field in DABs bundle config."""

    git_folder_path: Optional[str] = None
    """When deployed from a Databricks Git folder, the absolute workspace path of that folder; empty
    for local deploys."""

    root_path: Optional[str] = None
    """Absolute workspace path of the deployment root — the base path the deployed files live under.
    Mirrors workspace.root_path in the DABs bundle config; file_path is its files subdirectory."""

    source_linked: Optional[bool] = None
    """Whether files are served directly from the source sync root instead of being copied into
    file_path."""

    def as_dict(self) -> dict:
        """Serializes the WorkspaceInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.bundle_root_path is not None:
            body["bundle_root_path"] = self.bundle_root_path
        if self.file_path is not None:
            body["file_path"] = self.file_path
        if self.git_folder_path is not None:
            body["git_folder_path"] = self.git_folder_path
        if self.root_path is not None:
            body["root_path"] = self.root_path
        if self.source_linked is not None:
            body["source_linked"] = self.source_linked
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the WorkspaceInfo into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.bundle_root_path is not None:
            body["bundle_root_path"] = self.bundle_root_path
        if self.file_path is not None:
            body["file_path"] = self.file_path
        if self.git_folder_path is not None:
            body["git_folder_path"] = self.git_folder_path
        if self.root_path is not None:
            body["root_path"] = self.root_path
        if self.source_linked is not None:
            body["source_linked"] = self.source_linked
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> WorkspaceInfo:
        """Deserializes the WorkspaceInfo from a dictionary."""
        return cls(
            bundle_root_path=d.get("bundle_root_path", None),
            file_path=d.get("file_path", None),
            git_folder_path=d.get("git_folder_path", None),
            root_path=d.get("root_path", None),
            source_linked=d.get("source_linked", None),
        )


class BundleDeploymentsAPI:
    """Service for managing bundle deployment metadata."""

    def __init__(self, api_client):
        self._api = api_client

    def complete_version(
        self, name: str, completion_reason: VersionComplete, *, force: Optional[bool] = None
    ) -> Version:
        """Marks a version as complete and releases the deployment lock.

        The server atomically:

        1. Sets the version status to the provided terminal status.
        2. Sets ``complete_time`` to the current server timestamp.
        3. Releases the lock on the parent deployment.
        4. Updates the parent deployment's ``status`` and ``last_version_id``.

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

    def create_deployment(self, deployment: Deployment) -> Deployment:
        """Creates a new deployment in the workspace.

        :param deployment: :class:`Deployment`
          The deployment to create. The caller must set ``initial_parent_path``. Other fields are ignored on
          input and populated by the service.

        :returns: :class:`Deployment`
        """

        body = deployment.as_dict()
        query = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/bundle/deployments", body=body, headers=headers)
        return Deployment.from_dict(res)

    def create_version(
        self, parent: str, version: Version, version_id: str, *, operations: Optional[List[StagedOperation]] = None
    ) -> Version:
        """Creates a new version under a deployment.

        Creating a version acquires an exclusive lock on the deployment, preventing concurrent deploys. The
        caller provides a ``version_id``, a numeric string that must be numerically greater than the
        deployment's most recent version, and sets the version's ``previous_version_id`` to the deployment's
        most recent version (leaving it unset for the first version), which the server validates to detect
        concurrent deploys.

        The caller also provides the full set of ``operations`` planned for this version, each identified by a
        ``resource_key`` and an ``action_type``. The server records one operation per resource in
        ``OPERATION_STATUS_PENDING`` in the same transaction as the version, so the plan is captured
        atomically. The outcome of each operation is recorded later via UpdateOperation as the resource is
        applied; the set of operations cannot be changed after the version is created.

        :param parent: str
          The parent deployment where this version will be created. Format: deployments/{deployment_id}
        :param version: :class:`Version`
          The version to create.
        :param version_id: str
          The ID to use for the version, which becomes the final component of the version's resource name. A
          numeric string (base-10, fits in a signed 64-bit integer) chosen by the caller; must be greater than
          or equal to 1. Must be numerically greater than the deployment's most recent version (see
          ``version.previous_version_id``); it does not need to start at 1 or increase by exactly 1. If the
          value is not numerically greater, the server returns ``INVALID_PARAMETER_VALUE``.
        :param operations: List[:class:`StagedOperation`] (optional)
          The full set of resource operations to record for this version. The server creates one operation per
          entry in ``OPERATION_STATUS_PENDING``, in the same transaction as the version; each outcome is
          recorded later via UpdateOperation. May be empty for a version that changes no resources. Each
          ``resource_key`` must be unique within the request.

        :returns: :class:`Version`
        """

        body = version.as_dict()
        query = {}
        if operations is not None:
            query["operations"] = [v.as_dict() for v in operations]
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
        server returns ``ABORTED``.

        :param name: str
          The version whose lock to renew. Format: deployments/{deployment_id}/versions/{version_id}

        :returns: :class:`HeartbeatResponse`
        """

        body = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/bundle/{name}/heartbeat", body=body, headers=headers)
        return HeartbeatResponse.from_dict(res)

    def list_deployments(
        self, *, filter: Optional[str] = None, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Deployment]:
        """Lists deployments in the workspace.

        :param filter: str (optional)
          A filter expression restricting which deployments are returned, in the style of AIP-160
          (https://google.aip.dev/160). The expression is a conjunction of one or more ``field operator
          value`` terms joined by ``AND`` (case-insensitive); a deployment is returned only when it matches
          every term. Whitespace around terms is ignored, and a value containing spaces must be wrapped in
          double quotes. An unset or empty filter returns all deployments. Filtering applies only to live
          deployments; deleted deployments are never returned regardless of the filter.

          Supported terms:

          - ``status = <STATUS>``: exact match on the deployment status. The value is a ``DeploymentStatus``
            enum value, with or without the ``DEPLOYMENT_STATUS_`` prefix and case-insensitive (e.g. ``status
            = ACTIVE``).
          - ``deployment_mode = <MODE>``: exact match on the deployment mode. The value is a
            ``DeploymentMode`` enum value, with or without the ``DEPLOYMENT_MODE_`` prefix and
            case-insensitive (e.g. ``deployment_mode = DEVELOPMENT``).
          - ``created_by = "<email>"``: exact match on the creator's email or principal name. To list only the
            deployments you created, pass your own identity (e.g. ``created_by = "me@example.com"``). This
            term matches the same value the deployment reports in ``created_by``, so a deployment whose
            creator cannot currently be resolved reports an empty ``created_by`` and does not match this term.
          - ``display_name = "<name>"``: exact match on the display name.
          - ``display_name : "<substring>"``: case-insensitive substring match on the display name.

          For example: ``status = ACTIVE AND display_name : "etl"``.
        :param page_size: int (optional)
          The maximum number of deployments to return. The service may return fewer than this value. If
          unspecified, at most 20 deployments will be returned. The maximum value is 1000; values above 1000
          will be coerced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous ``ListDeployments`` call. Provide this to retrieve the
          subsequent page.

        :returns: Iterator over :class:`Deployment`
        """

        query = {}
        if filter is not None:
            query["filter"] = filter
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
          A page token, received from a previous ``ListOperations`` call. Provide this to retrieve the
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
          A page token, received from a previous ``ListResources`` call. Provide this to retrieve the
          subsequent page.

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
        """Lists versions under a deployment, ordered numerically by version_id descending (most recent first).

        :param parent: str
          The parent deployment. Format: deployments/{deployment_id}
        :param page_size: int (optional)
          The maximum number of versions to return. The service may return fewer than this value. If
          unspecified, at most 20 versions will be returned. The maximum value is 100; values above 100 will
          be coerced to 100.
        :param page_token: str (optional)
          A page token, received from a previous ``ListVersions`` call. Provide this to retrieve the
          subsequent page.

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

    def update_operation(self, name: str, operation: Operation, update_mask: FieldMask) -> Operation:
        """Updates a resource operation's mutable fields.

        ``state``, ``error_message``, ``resource_id``, ``status``, and ``dashboard_metadata`` may be updated,
        independently; ``update_mask`` must contain only those paths. All other fields are immutable. The
        update is guarded by an optimistic-concurrency check: the caller sets ``operation.sequence_id`` to the
        value it last observed, and the server rejects the update with ``ABORTED`` if the operation has been
        modified since. On success the server increments ``sequence_id``; updates to ``state``,
        ``resource_id``, and ``dashboard_metadata`` are mirrored onto the corresponding deployment-level
        resource. Listing ``state`` in ``update_mask`` with no value clears it, which removes the resource, so
        a delete that is retried until it succeeds must clear ``state``. The parent version must be in
        progress, and after the update is applied a succeeded operation cannot carry an ``error_message``. See
        the ``state`` and ``resource_id`` fields for the rest.

        :param name: str
          Resource name of the operation. Format:
          deployments/{deployment_id}/versions/{version_id}/operations/{resource_key}
        :param operation: :class:`Operation`
          The operation to update. Its ``name`` selects the operation; the fields named in ``update_mask``
          carry the new values; and ``sequence_id`` carries the optimistic-concurrency precondition (see the
          field docs on Operation). All other fields are ignored.
        :param update_mask: FieldMask
          The set of fields to update. Required; supported paths are ``state``, ``error_message``,
          ``resource_id``, ``status``, and ``dashboard_metadata``. An empty mask or any other path is rejected
          with INVALID_PARAMETER_VALUE.

        :returns: :class:`Operation`
        """

        body = operation.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/bundle/{name}", query=query, body=body, headers=headers)
        return Operation.from_dict(res)

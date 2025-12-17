# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List, Optional

from google.protobuf.duration_pb2 import Duration
from google.protobuf.timestamp_pb2 import Timestamp

from databricks.sdk.common import lro
from databricks.sdk.common.types.fieldmask import FieldMask
from databricks.sdk.retries import RetryError, poll
from databricks.sdk.service._internal import (_duration, _enum, _from_dict,
                                              _repeated_dict, _timestamp)

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class Branch:
    create_time: Optional[Timestamp] = None
    """A timestamp indicating when the branch was created."""

    current_state: Optional[BranchState] = None
    """The branch's state, indicating if it is initializing, ready for use, or archived."""

    default: Optional[bool] = None
    """Whether the branch is the project's default branch. This field is only returned on create/update
    responses. See effective_default for the value that is actually applied to the branch."""

    effective_default: Optional[bool] = None
    """Whether the branch is the project's default branch."""

    effective_is_protected: Optional[bool] = None
    """Whether the branch is protected."""

    effective_source_branch: Optional[str] = None
    """The name of the source branch from which this branch was created. Format:
    projects/{project_id}/branches/{branch_id}"""

    effective_source_branch_lsn: Optional[str] = None
    """The Log Sequence Number (LSN) on the source branch from which this branch was created."""

    effective_source_branch_time: Optional[Timestamp] = None
    """The point in time on the source branch from which this branch was created."""

    is_protected: Optional[bool] = None
    """Whether the branch is protected."""

    logical_size_bytes: Optional[int] = None
    """The logical size of the branch."""

    name: Optional[str] = None
    """The resource name of the branch. Format: projects/{project_id}/branches/{branch_id}"""

    parent: Optional[str] = None
    """The project containing this branch. Format: projects/{project_id}"""

    pending_state: Optional[BranchState] = None
    """The pending state of the branch, if a state transition is in progress."""

    source_branch: Optional[str] = None
    """The name of the source branch from which this branch was created. Format:
    projects/{project_id}/branches/{branch_id}"""

    source_branch_lsn: Optional[str] = None
    """The Log Sequence Number (LSN) on the source branch from which this branch was created."""

    source_branch_time: Optional[Timestamp] = None
    """The point in time on the source branch from which this branch was created."""

    state_change_time: Optional[Timestamp] = None
    """A timestamp indicating when the `current_state` began."""

    uid: Optional[str] = None
    """System generated unique ID for the branch."""

    update_time: Optional[Timestamp] = None
    """A timestamp indicating when the branch was last updated."""

    def as_dict(self) -> dict:
        """Serializes the Branch into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.current_state is not None:
            body["current_state"] = self.current_state.value
        if self.default is not None:
            body["default"] = self.default
        if self.effective_default is not None:
            body["effective_default"] = self.effective_default
        if self.effective_is_protected is not None:
            body["effective_is_protected"] = self.effective_is_protected
        if self.effective_source_branch is not None:
            body["effective_source_branch"] = self.effective_source_branch
        if self.effective_source_branch_lsn is not None:
            body["effective_source_branch_lsn"] = self.effective_source_branch_lsn
        if self.effective_source_branch_time is not None:
            body["effective_source_branch_time"] = self.effective_source_branch_time.ToJsonString()
        if self.is_protected is not None:
            body["is_protected"] = self.is_protected
        if self.logical_size_bytes is not None:
            body["logical_size_bytes"] = self.logical_size_bytes
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.pending_state is not None:
            body["pending_state"] = self.pending_state.value
        if self.source_branch is not None:
            body["source_branch"] = self.source_branch
        if self.source_branch_lsn is not None:
            body["source_branch_lsn"] = self.source_branch_lsn
        if self.source_branch_time is not None:
            body["source_branch_time"] = self.source_branch_time.ToJsonString()
        if self.state_change_time is not None:
            body["state_change_time"] = self.state_change_time.ToJsonString()
        if self.uid is not None:
            body["uid"] = self.uid
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Branch into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.current_state is not None:
            body["current_state"] = self.current_state
        if self.default is not None:
            body["default"] = self.default
        if self.effective_default is not None:
            body["effective_default"] = self.effective_default
        if self.effective_is_protected is not None:
            body["effective_is_protected"] = self.effective_is_protected
        if self.effective_source_branch is not None:
            body["effective_source_branch"] = self.effective_source_branch
        if self.effective_source_branch_lsn is not None:
            body["effective_source_branch_lsn"] = self.effective_source_branch_lsn
        if self.effective_source_branch_time is not None:
            body["effective_source_branch_time"] = self.effective_source_branch_time
        if self.is_protected is not None:
            body["is_protected"] = self.is_protected
        if self.logical_size_bytes is not None:
            body["logical_size_bytes"] = self.logical_size_bytes
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.pending_state is not None:
            body["pending_state"] = self.pending_state
        if self.source_branch is not None:
            body["source_branch"] = self.source_branch
        if self.source_branch_lsn is not None:
            body["source_branch_lsn"] = self.source_branch_lsn
        if self.source_branch_time is not None:
            body["source_branch_time"] = self.source_branch_time
        if self.state_change_time is not None:
            body["state_change_time"] = self.state_change_time
        if self.uid is not None:
            body["uid"] = self.uid
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Branch:
        """Deserializes the Branch from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            current_state=_enum(d, "current_state", BranchState),
            default=d.get("default", None),
            effective_default=d.get("effective_default", None),
            effective_is_protected=d.get("effective_is_protected", None),
            effective_source_branch=d.get("effective_source_branch", None),
            effective_source_branch_lsn=d.get("effective_source_branch_lsn", None),
            effective_source_branch_time=_timestamp(d, "effective_source_branch_time"),
            is_protected=d.get("is_protected", None),
            logical_size_bytes=d.get("logical_size_bytes", None),
            name=d.get("name", None),
            parent=d.get("parent", None),
            pending_state=_enum(d, "pending_state", BranchState),
            source_branch=d.get("source_branch", None),
            source_branch_lsn=d.get("source_branch_lsn", None),
            source_branch_time=_timestamp(d, "source_branch_time"),
            state_change_time=_timestamp(d, "state_change_time"),
            uid=d.get("uid", None),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class BranchOperationMetadata:
    def as_dict(self) -> dict:
        """Serializes the BranchOperationMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the BranchOperationMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> BranchOperationMetadata:
        """Deserializes the BranchOperationMetadata from a dictionary."""
        return cls()


class BranchState(Enum):
    """The state of the database branch."""

    ARCHIVED = "ARCHIVED"
    IMPORTING = "IMPORTING"
    INIT = "INIT"
    READY = "READY"
    RESETTING = "RESETTING"


@dataclass
class DatabricksServiceExceptionWithDetailsProto:
    """Databricks Error that is returned by all Databricks APIs."""

    details: Optional[List[dict]] = None
    """@pbjson-skip"""

    error_code: Optional[ErrorCode] = None

    message: Optional[str] = None

    stack_trace: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the DatabricksServiceExceptionWithDetailsProto into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.details:
            body["details"] = [v for v in self.details]
        if self.error_code is not None:
            body["error_code"] = self.error_code.value
        if self.message is not None:
            body["message"] = self.message
        if self.stack_trace is not None:
            body["stack_trace"] = self.stack_trace
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabricksServiceExceptionWithDetailsProto into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.details:
            body["details"] = self.details
        if self.error_code is not None:
            body["error_code"] = self.error_code
        if self.message is not None:
            body["message"] = self.message
        if self.stack_trace is not None:
            body["stack_trace"] = self.stack_trace
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabricksServiceExceptionWithDetailsProto:
        """Deserializes the DatabricksServiceExceptionWithDetailsProto from a dictionary."""
        return cls(
            details=d.get("details", None),
            error_code=_enum(d, "error_code", ErrorCode),
            message=d.get("message", None),
            stack_trace=d.get("stack_trace", None),
        )


@dataclass
class Endpoint:
    endpoint_type: EndpointType
    """The endpoint type. There could be only one READ_WRITE endpoint per branch."""

    autoscaling_limit_max_cu: Optional[float] = None
    """The maximum number of Compute Units."""

    autoscaling_limit_min_cu: Optional[float] = None
    """The minimum number of Compute Units."""

    create_time: Optional[Timestamp] = None
    """A timestamp indicating when the compute endpoint was created."""

    current_state: Optional[EndpointState] = None

    disabled: Optional[bool] = None
    """Whether to restrict connections to the compute endpoint. Enabling this option schedules a
    suspend compute operation. A disabled compute endpoint cannot be enabled by a connection or
    console action."""

    effective_autoscaling_limit_max_cu: Optional[float] = None
    """The maximum number of Compute Units."""

    effective_autoscaling_limit_min_cu: Optional[float] = None
    """The minimum number of Compute Units."""

    effective_disabled: Optional[bool] = None
    """Whether to restrict connections to the compute endpoint. Enabling this option schedules a
    suspend compute operation. A disabled compute endpoint cannot be enabled by a connection or
    console action."""

    effective_pooler_mode: Optional[EndpointPoolerMode] = None

    effective_settings: Optional[EndpointSettings] = None

    effective_suspend_timeout_duration: Optional[Duration] = None
    """Duration of inactivity after which the compute endpoint is automatically suspended."""

    host: Optional[str] = None
    """The hostname of the compute endpoint. This is the hostname specified when connecting to a
    database."""

    last_active_time: Optional[Timestamp] = None
    """A timestamp indicating when the compute endpoint was last active."""

    name: Optional[str] = None
    """The resource name of the endpoint. Format:
    projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}"""

    parent: Optional[str] = None
    """The branch containing this endpoint. Format: projects/{project_id}/branches/{branch_id}"""

    pending_state: Optional[EndpointState] = None

    pooler_mode: Optional[EndpointPoolerMode] = None

    settings: Optional[EndpointSettings] = None

    start_time: Optional[Timestamp] = None
    """A timestamp indicating when the compute endpoint was last started."""

    suspend_time: Optional[Timestamp] = None
    """A timestamp indicating when the compute endpoint was last suspended."""

    suspend_timeout_duration: Optional[Duration] = None
    """Duration of inactivity after which the compute endpoint is automatically suspended."""

    uid: Optional[str] = None
    """System generated unique ID for the endpoint."""

    update_time: Optional[Timestamp] = None
    """A timestamp indicating when the compute endpoint was last updated."""

    def as_dict(self) -> dict:
        """Serializes the Endpoint into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.autoscaling_limit_max_cu is not None:
            body["autoscaling_limit_max_cu"] = self.autoscaling_limit_max_cu
        if self.autoscaling_limit_min_cu is not None:
            body["autoscaling_limit_min_cu"] = self.autoscaling_limit_min_cu
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.current_state is not None:
            body["current_state"] = self.current_state.value
        if self.disabled is not None:
            body["disabled"] = self.disabled
        if self.effective_autoscaling_limit_max_cu is not None:
            body["effective_autoscaling_limit_max_cu"] = self.effective_autoscaling_limit_max_cu
        if self.effective_autoscaling_limit_min_cu is not None:
            body["effective_autoscaling_limit_min_cu"] = self.effective_autoscaling_limit_min_cu
        if self.effective_disabled is not None:
            body["effective_disabled"] = self.effective_disabled
        if self.effective_pooler_mode is not None:
            body["effective_pooler_mode"] = self.effective_pooler_mode.value
        if self.effective_settings:
            body["effective_settings"] = self.effective_settings.as_dict()
        if self.effective_suspend_timeout_duration is not None:
            body["effective_suspend_timeout_duration"] = self.effective_suspend_timeout_duration.ToJsonString()
        if self.endpoint_type is not None:
            body["endpoint_type"] = self.endpoint_type.value
        if self.host is not None:
            body["host"] = self.host
        if self.last_active_time is not None:
            body["last_active_time"] = self.last_active_time.ToJsonString()
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.pending_state is not None:
            body["pending_state"] = self.pending_state.value
        if self.pooler_mode is not None:
            body["pooler_mode"] = self.pooler_mode.value
        if self.settings:
            body["settings"] = self.settings.as_dict()
        if self.start_time is not None:
            body["start_time"] = self.start_time.ToJsonString()
        if self.suspend_time is not None:
            body["suspend_time"] = self.suspend_time.ToJsonString()
        if self.suspend_timeout_duration is not None:
            body["suspend_timeout_duration"] = self.suspend_timeout_duration.ToJsonString()
        if self.uid is not None:
            body["uid"] = self.uid
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Endpoint into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.autoscaling_limit_max_cu is not None:
            body["autoscaling_limit_max_cu"] = self.autoscaling_limit_max_cu
        if self.autoscaling_limit_min_cu is not None:
            body["autoscaling_limit_min_cu"] = self.autoscaling_limit_min_cu
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.current_state is not None:
            body["current_state"] = self.current_state
        if self.disabled is not None:
            body["disabled"] = self.disabled
        if self.effective_autoscaling_limit_max_cu is not None:
            body["effective_autoscaling_limit_max_cu"] = self.effective_autoscaling_limit_max_cu
        if self.effective_autoscaling_limit_min_cu is not None:
            body["effective_autoscaling_limit_min_cu"] = self.effective_autoscaling_limit_min_cu
        if self.effective_disabled is not None:
            body["effective_disabled"] = self.effective_disabled
        if self.effective_pooler_mode is not None:
            body["effective_pooler_mode"] = self.effective_pooler_mode
        if self.effective_settings:
            body["effective_settings"] = self.effective_settings
        if self.effective_suspend_timeout_duration is not None:
            body["effective_suspend_timeout_duration"] = self.effective_suspend_timeout_duration
        if self.endpoint_type is not None:
            body["endpoint_type"] = self.endpoint_type
        if self.host is not None:
            body["host"] = self.host
        if self.last_active_time is not None:
            body["last_active_time"] = self.last_active_time
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.pending_state is not None:
            body["pending_state"] = self.pending_state
        if self.pooler_mode is not None:
            body["pooler_mode"] = self.pooler_mode
        if self.settings:
            body["settings"] = self.settings
        if self.start_time is not None:
            body["start_time"] = self.start_time
        if self.suspend_time is not None:
            body["suspend_time"] = self.suspend_time
        if self.suspend_timeout_duration is not None:
            body["suspend_timeout_duration"] = self.suspend_timeout_duration
        if self.uid is not None:
            body["uid"] = self.uid
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Endpoint:
        """Deserializes the Endpoint from a dictionary."""
        return cls(
            autoscaling_limit_max_cu=d.get("autoscaling_limit_max_cu", None),
            autoscaling_limit_min_cu=d.get("autoscaling_limit_min_cu", None),
            create_time=_timestamp(d, "create_time"),
            current_state=_enum(d, "current_state", EndpointState),
            disabled=d.get("disabled", None),
            effective_autoscaling_limit_max_cu=d.get("effective_autoscaling_limit_max_cu", None),
            effective_autoscaling_limit_min_cu=d.get("effective_autoscaling_limit_min_cu", None),
            effective_disabled=d.get("effective_disabled", None),
            effective_pooler_mode=_enum(d, "effective_pooler_mode", EndpointPoolerMode),
            effective_settings=_from_dict(d, "effective_settings", EndpointSettings),
            effective_suspend_timeout_duration=_duration(d, "effective_suspend_timeout_duration"),
            endpoint_type=_enum(d, "endpoint_type", EndpointType),
            host=d.get("host", None),
            last_active_time=_timestamp(d, "last_active_time"),
            name=d.get("name", None),
            parent=d.get("parent", None),
            pending_state=_enum(d, "pending_state", EndpointState),
            pooler_mode=_enum(d, "pooler_mode", EndpointPoolerMode),
            settings=_from_dict(d, "settings", EndpointSettings),
            start_time=_timestamp(d, "start_time"),
            suspend_time=_timestamp(d, "suspend_time"),
            suspend_timeout_duration=_duration(d, "suspend_timeout_duration"),
            uid=d.get("uid", None),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class EndpointOperationMetadata:
    def as_dict(self) -> dict:
        """Serializes the EndpointOperationMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointOperationMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> EndpointOperationMetadata:
        """Deserializes the EndpointOperationMetadata from a dictionary."""
        return cls()


class EndpointPoolerMode(Enum):
    """The connection pooler mode. Lakebase supports PgBouncer in `transaction` mode only."""

    TRANSACTION = "TRANSACTION"


@dataclass
class EndpointSettings:
    """A collection of settings for a compute endpoint."""

    pg_settings: Optional[Dict[str, str]] = None
    """A raw representation of Postgres settings."""

    pgbouncer_settings: Optional[Dict[str, str]] = None
    """A raw representation of PgBouncer settings."""

    def as_dict(self) -> dict:
        """Serializes the EndpointSettings into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.pg_settings:
            body["pg_settings"] = self.pg_settings
        if self.pgbouncer_settings:
            body["pgbouncer_settings"] = self.pgbouncer_settings
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointSettings into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.pg_settings:
            body["pg_settings"] = self.pg_settings
        if self.pgbouncer_settings:
            body["pgbouncer_settings"] = self.pgbouncer_settings
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> EndpointSettings:
        """Deserializes the EndpointSettings from a dictionary."""
        return cls(pg_settings=d.get("pg_settings", None), pgbouncer_settings=d.get("pgbouncer_settings", None))


class EndpointState(Enum):
    """The state of the compute endpoint."""

    ACTIVE = "ACTIVE"
    IDLE = "IDLE"
    INIT = "INIT"


class EndpointType(Enum):
    """The compute endpoint type. Either `read_write` or `read_only`."""

    READ_ONLY = "READ_ONLY"
    READ_WRITE = "READ_WRITE"


class ErrorCode(Enum):
    """Legacy definition of the ErrorCode enum. Please keep in sync with
    api-base/proto/error_code.proto (except status code mapping annotations as this file doesn't
    have them). Will be removed eventually, pending the ScalaPB 0.4 cleanup."""

    ABORTED = "ABORTED"
    ALREADY_EXISTS = "ALREADY_EXISTS"
    BAD_REQUEST = "BAD_REQUEST"
    CANCELLED = "CANCELLED"
    CATALOG_ALREADY_EXISTS = "CATALOG_ALREADY_EXISTS"
    CATALOG_DOES_NOT_EXIST = "CATALOG_DOES_NOT_EXIST"
    CATALOG_NOT_EMPTY = "CATALOG_NOT_EMPTY"
    COULD_NOT_ACQUIRE_LOCK = "COULD_NOT_ACQUIRE_LOCK"
    CUSTOMER_UNAUTHORIZED = "CUSTOMER_UNAUTHORIZED"
    DAC_ALREADY_EXISTS = "DAC_ALREADY_EXISTS"
    DAC_DOES_NOT_EXIST = "DAC_DOES_NOT_EXIST"
    DATA_LOSS = "DATA_LOSS"
    DEADLINE_EXCEEDED = "DEADLINE_EXCEEDED"
    DEPLOYMENT_TIMEOUT = "DEPLOYMENT_TIMEOUT"
    DIRECTORY_NOT_EMPTY = "DIRECTORY_NOT_EMPTY"
    DIRECTORY_PROTECTED = "DIRECTORY_PROTECTED"
    DRY_RUN_FAILED = "DRY_RUN_FAILED"
    ENDPOINT_NOT_FOUND = "ENDPOINT_NOT_FOUND"
    EXTERNAL_LOCATION_ALREADY_EXISTS = "EXTERNAL_LOCATION_ALREADY_EXISTS"
    EXTERNAL_LOCATION_DOES_NOT_EXIST = "EXTERNAL_LOCATION_DOES_NOT_EXIST"
    FEATURE_DISABLED = "FEATURE_DISABLED"
    GIT_CONFLICT = "GIT_CONFLICT"
    GIT_REMOTE_ERROR = "GIT_REMOTE_ERROR"
    GIT_SENSITIVE_TOKEN_DETECTED = "GIT_SENSITIVE_TOKEN_DETECTED"
    GIT_UNKNOWN_REF = "GIT_UNKNOWN_REF"
    GIT_URL_NOT_ON_ALLOW_LIST = "GIT_URL_NOT_ON_ALLOW_LIST"
    INSECURE_PARTNER_RESPONSE = "INSECURE_PARTNER_RESPONSE"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    INVALID_PARAMETER_VALUE = "INVALID_PARAMETER_VALUE"
    INVALID_STATE = "INVALID_STATE"
    INVALID_STATE_TRANSITION = "INVALID_STATE_TRANSITION"
    IO_ERROR = "IO_ERROR"
    IPYNB_FILE_IN_REPO = "IPYNB_FILE_IN_REPO"
    MALFORMED_PARTNER_RESPONSE = "MALFORMED_PARTNER_RESPONSE"
    MALFORMED_REQUEST = "MALFORMED_REQUEST"
    MANAGED_RESOURCE_GROUP_DOES_NOT_EXIST = "MANAGED_RESOURCE_GROUP_DOES_NOT_EXIST"
    MAX_BLOCK_SIZE_EXCEEDED = "MAX_BLOCK_SIZE_EXCEEDED"
    MAX_CHILD_NODE_SIZE_EXCEEDED = "MAX_CHILD_NODE_SIZE_EXCEEDED"
    MAX_LIST_SIZE_EXCEEDED = "MAX_LIST_SIZE_EXCEEDED"
    MAX_NOTEBOOK_SIZE_EXCEEDED = "MAX_NOTEBOOK_SIZE_EXCEEDED"
    MAX_READ_SIZE_EXCEEDED = "MAX_READ_SIZE_EXCEEDED"
    METASTORE_ALREADY_EXISTS = "METASTORE_ALREADY_EXISTS"
    METASTORE_DOES_NOT_EXIST = "METASTORE_DOES_NOT_EXIST"
    METASTORE_NOT_EMPTY = "METASTORE_NOT_EMPTY"
    NOT_FOUND = "NOT_FOUND"
    NOT_IMPLEMENTED = "NOT_IMPLEMENTED"
    PARTIAL_DELETE = "PARTIAL_DELETE"
    PERMISSION_DENIED = "PERMISSION_DENIED"
    PERMISSION_NOT_PROPAGATED = "PERMISSION_NOT_PROPAGATED"
    PRINCIPAL_DOES_NOT_EXIST = "PRINCIPAL_DOES_NOT_EXIST"
    PROJECTS_OPERATION_TIMEOUT = "PROJECTS_OPERATION_TIMEOUT"
    PROVIDER_ALREADY_EXISTS = "PROVIDER_ALREADY_EXISTS"
    PROVIDER_DOES_NOT_EXIST = "PROVIDER_DOES_NOT_EXIST"
    PROVIDER_SHARE_NOT_ACCESSIBLE = "PROVIDER_SHARE_NOT_ACCESSIBLE"
    QUOTA_EXCEEDED = "QUOTA_EXCEEDED"
    RECIPIENT_ALREADY_EXISTS = "RECIPIENT_ALREADY_EXISTS"
    RECIPIENT_DOES_NOT_EXIST = "RECIPIENT_DOES_NOT_EXIST"
    REQUEST_LIMIT_EXCEEDED = "REQUEST_LIMIT_EXCEEDED"
    RESOURCE_ALREADY_EXISTS = "RESOURCE_ALREADY_EXISTS"
    RESOURCE_CONFLICT = "RESOURCE_CONFLICT"
    RESOURCE_DOES_NOT_EXIST = "RESOURCE_DOES_NOT_EXIST"
    RESOURCE_EXHAUSTED = "RESOURCE_EXHAUSTED"
    RESOURCE_LIMIT_EXCEEDED = "RESOURCE_LIMIT_EXCEEDED"
    SCHEMA_ALREADY_EXISTS = "SCHEMA_ALREADY_EXISTS"
    SCHEMA_DOES_NOT_EXIST = "SCHEMA_DOES_NOT_EXIST"
    SCHEMA_NOT_EMPTY = "SCHEMA_NOT_EMPTY"
    SEARCH_QUERY_TOO_LONG = "SEARCH_QUERY_TOO_LONG"
    SEARCH_QUERY_TOO_SHORT = "SEARCH_QUERY_TOO_SHORT"
    SERVICE_UNDER_MAINTENANCE = "SERVICE_UNDER_MAINTENANCE"
    SHARE_ALREADY_EXISTS = "SHARE_ALREADY_EXISTS"
    SHARE_DOES_NOT_EXIST = "SHARE_DOES_NOT_EXIST"
    STORAGE_CREDENTIAL_ALREADY_EXISTS = "STORAGE_CREDENTIAL_ALREADY_EXISTS"
    STORAGE_CREDENTIAL_DOES_NOT_EXIST = "STORAGE_CREDENTIAL_DOES_NOT_EXIST"
    TABLE_ALREADY_EXISTS = "TABLE_ALREADY_EXISTS"
    TABLE_DOES_NOT_EXIST = "TABLE_DOES_NOT_EXIST"
    TEMPORARILY_UNAVAILABLE = "TEMPORARILY_UNAVAILABLE"
    UNAUTHENTICATED = "UNAUTHENTICATED"
    UNAVAILABLE = "UNAVAILABLE"
    UNKNOWN = "UNKNOWN"
    UNPARSEABLE_HTTP_ERROR = "UNPARSEABLE_HTTP_ERROR"
    WORKSPACE_TEMPORARILY_UNAVAILABLE = "WORKSPACE_TEMPORARILY_UNAVAILABLE"


@dataclass
class ListBranchesResponse:
    branches: Optional[List[Branch]] = None
    """List of branches."""

    next_page_token: Optional[str] = None
    """Pagination token to request the next page of branches."""

    def as_dict(self) -> dict:
        """Serializes the ListBranchesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.branches:
            body["branches"] = [v.as_dict() for v in self.branches]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListBranchesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.branches:
            body["branches"] = self.branches
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListBranchesResponse:
        """Deserializes the ListBranchesResponse from a dictionary."""
        return cls(branches=_repeated_dict(d, "branches", Branch), next_page_token=d.get("next_page_token", None))


@dataclass
class ListEndpointsResponse:
    endpoints: Optional[List[Endpoint]] = None
    """List of endpoints."""

    next_page_token: Optional[str] = None
    """Pagination token to request the next page of endpoints."""

    def as_dict(self) -> dict:
        """Serializes the ListEndpointsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.endpoints:
            body["endpoints"] = [v.as_dict() for v in self.endpoints]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListEndpointsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.endpoints:
            body["endpoints"] = self.endpoints
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListEndpointsResponse:
        """Deserializes the ListEndpointsResponse from a dictionary."""
        return cls(endpoints=_repeated_dict(d, "endpoints", Endpoint), next_page_token=d.get("next_page_token", None))


@dataclass
class ListProjectsResponse:
    next_page_token: Optional[str] = None
    """Pagination token to request the next page of projects."""

    projects: Optional[List[Project]] = None
    """List of projects."""

    def as_dict(self) -> dict:
        """Serializes the ListProjectsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.projects:
            body["projects"] = [v.as_dict() for v in self.projects]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListProjectsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.projects:
            body["projects"] = self.projects
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListProjectsResponse:
        """Deserializes the ListProjectsResponse from a dictionary."""
        return cls(next_page_token=d.get("next_page_token", None), projects=_repeated_dict(d, "projects", Project))


@dataclass
class Operation:
    """This resource represents a long-running operation that is the result of a network API call."""

    done: Optional[bool] = None
    """If the value is `false`, it means the operation is still in progress. If `true`, the operation
    is completed, and either `error` or `response` is available."""

    error: Optional[DatabricksServiceExceptionWithDetailsProto] = None
    """The error result of the operation in case of failure or cancellation."""

    metadata: Optional[dict] = None
    """Service-specific metadata associated with the operation. It typically contains progress
    information and common metadata such as create time. Some services might not provide such
    metadata."""

    name: Optional[str] = None
    """The server-assigned name, which is only unique within the same service that originally returns
    it. If you use the default HTTP mapping, the `name` should be a resource name ending with
    `operations/{unique_id}`."""

    response: Optional[dict] = None
    """The normal, successful response of the operation."""

    def as_dict(self) -> dict:
        """Serializes the Operation into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.done is not None:
            body["done"] = self.done
        if self.error:
            body["error"] = self.error.as_dict()
        if self.metadata:
            body["metadata"] = self.metadata
        if self.name is not None:
            body["name"] = self.name
        if self.response:
            body["response"] = self.response
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Operation into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.done is not None:
            body["done"] = self.done
        if self.error:
            body["error"] = self.error
        if self.metadata:
            body["metadata"] = self.metadata
        if self.name is not None:
            body["name"] = self.name
        if self.response:
            body["response"] = self.response
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Operation:
        """Deserializes the Operation from a dictionary."""
        return cls(
            done=d.get("done", None),
            error=_from_dict(d, "error", DatabricksServiceExceptionWithDetailsProto),
            metadata=d.get("metadata", None),
            name=d.get("name", None),
            response=d.get("response", None),
        )


@dataclass
class Project:
    branch_logical_size_limit_bytes: Optional[int] = None
    """The logical size limit for a branch."""

    compute_last_active_time: Optional[Timestamp] = None
    """The most recent time when any endpoint of this project was active."""

    create_time: Optional[Timestamp] = None
    """A timestamp indicating when the project was created."""

    default_endpoint_settings: Optional[ProjectDefaultEndpointSettings] = None

    display_name: Optional[str] = None
    """Human-readable project name."""

    effective_default_endpoint_settings: Optional[ProjectDefaultEndpointSettings] = None

    effective_display_name: Optional[str] = None

    effective_history_retention_duration: Optional[Duration] = None

    effective_pg_version: Optional[int] = None

    effective_settings: Optional[ProjectSettings] = None

    history_retention_duration: Optional[Duration] = None
    """The number of seconds to retain the shared history for point in time recovery for all branches
    in this project."""

    name: Optional[str] = None
    """The resource name of the project. Format: projects/{project_id}"""

    pg_version: Optional[int] = None
    """The major Postgres version number."""

    settings: Optional[ProjectSettings] = None

    synthetic_storage_size_bytes: Optional[int] = None
    """The current space occupied by the project in storage. Synthetic storage size combines the
    logical data size and Write-Ahead Log (WAL) size for all branches in a project."""

    uid: Optional[str] = None
    """System generated unique ID for the project."""

    update_time: Optional[Timestamp] = None
    """A timestamp indicating when the project was last updated."""

    def as_dict(self) -> dict:
        """Serializes the Project into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.branch_logical_size_limit_bytes is not None:
            body["branch_logical_size_limit_bytes"] = self.branch_logical_size_limit_bytes
        if self.compute_last_active_time is not None:
            body["compute_last_active_time"] = self.compute_last_active_time.ToJsonString()
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.default_endpoint_settings:
            body["default_endpoint_settings"] = self.default_endpoint_settings.as_dict()
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.effective_default_endpoint_settings:
            body["effective_default_endpoint_settings"] = self.effective_default_endpoint_settings.as_dict()
        if self.effective_display_name is not None:
            body["effective_display_name"] = self.effective_display_name
        if self.effective_history_retention_duration is not None:
            body["effective_history_retention_duration"] = self.effective_history_retention_duration.ToJsonString()
        if self.effective_pg_version is not None:
            body["effective_pg_version"] = self.effective_pg_version
        if self.effective_settings:
            body["effective_settings"] = self.effective_settings.as_dict()
        if self.history_retention_duration is not None:
            body["history_retention_duration"] = self.history_retention_duration.ToJsonString()
        if self.name is not None:
            body["name"] = self.name
        if self.pg_version is not None:
            body["pg_version"] = self.pg_version
        if self.settings:
            body["settings"] = self.settings.as_dict()
        if self.synthetic_storage_size_bytes is not None:
            body["synthetic_storage_size_bytes"] = self.synthetic_storage_size_bytes
        if self.uid is not None:
            body["uid"] = self.uid
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Project into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.branch_logical_size_limit_bytes is not None:
            body["branch_logical_size_limit_bytes"] = self.branch_logical_size_limit_bytes
        if self.compute_last_active_time is not None:
            body["compute_last_active_time"] = self.compute_last_active_time
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.default_endpoint_settings:
            body["default_endpoint_settings"] = self.default_endpoint_settings
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.effective_default_endpoint_settings:
            body["effective_default_endpoint_settings"] = self.effective_default_endpoint_settings
        if self.effective_display_name is not None:
            body["effective_display_name"] = self.effective_display_name
        if self.effective_history_retention_duration is not None:
            body["effective_history_retention_duration"] = self.effective_history_retention_duration
        if self.effective_pg_version is not None:
            body["effective_pg_version"] = self.effective_pg_version
        if self.effective_settings:
            body["effective_settings"] = self.effective_settings
        if self.history_retention_duration is not None:
            body["history_retention_duration"] = self.history_retention_duration
        if self.name is not None:
            body["name"] = self.name
        if self.pg_version is not None:
            body["pg_version"] = self.pg_version
        if self.settings:
            body["settings"] = self.settings
        if self.synthetic_storage_size_bytes is not None:
            body["synthetic_storage_size_bytes"] = self.synthetic_storage_size_bytes
        if self.uid is not None:
            body["uid"] = self.uid
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Project:
        """Deserializes the Project from a dictionary."""
        return cls(
            branch_logical_size_limit_bytes=d.get("branch_logical_size_limit_bytes", None),
            compute_last_active_time=_timestamp(d, "compute_last_active_time"),
            create_time=_timestamp(d, "create_time"),
            default_endpoint_settings=_from_dict(d, "default_endpoint_settings", ProjectDefaultEndpointSettings),
            display_name=d.get("display_name", None),
            effective_default_endpoint_settings=_from_dict(
                d, "effective_default_endpoint_settings", ProjectDefaultEndpointSettings
            ),
            effective_display_name=d.get("effective_display_name", None),
            effective_history_retention_duration=_duration(d, "effective_history_retention_duration"),
            effective_pg_version=d.get("effective_pg_version", None),
            effective_settings=_from_dict(d, "effective_settings", ProjectSettings),
            history_retention_duration=_duration(d, "history_retention_duration"),
            name=d.get("name", None),
            pg_version=d.get("pg_version", None),
            settings=_from_dict(d, "settings", ProjectSettings),
            synthetic_storage_size_bytes=d.get("synthetic_storage_size_bytes", None),
            uid=d.get("uid", None),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class ProjectDefaultEndpointSettings:
    """A collection of settings for a compute endpoint."""

    autoscaling_limit_max_cu: Optional[float] = None
    """The maximum number of Compute Units."""

    autoscaling_limit_min_cu: Optional[float] = None
    """The minimum number of Compute Units."""

    pg_settings: Optional[Dict[str, str]] = None
    """A raw representation of Postgres settings."""

    pgbouncer_settings: Optional[Dict[str, str]] = None
    """A raw representation of PgBouncer settings."""

    suspend_timeout_duration: Optional[Duration] = None
    """Duration of inactivity after which the compute endpoint is automatically suspended."""

    def as_dict(self) -> dict:
        """Serializes the ProjectDefaultEndpointSettings into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.autoscaling_limit_max_cu is not None:
            body["autoscaling_limit_max_cu"] = self.autoscaling_limit_max_cu
        if self.autoscaling_limit_min_cu is not None:
            body["autoscaling_limit_min_cu"] = self.autoscaling_limit_min_cu
        if self.pg_settings:
            body["pg_settings"] = self.pg_settings
        if self.pgbouncer_settings:
            body["pgbouncer_settings"] = self.pgbouncer_settings
        if self.suspend_timeout_duration is not None:
            body["suspend_timeout_duration"] = self.suspend_timeout_duration.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ProjectDefaultEndpointSettings into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.autoscaling_limit_max_cu is not None:
            body["autoscaling_limit_max_cu"] = self.autoscaling_limit_max_cu
        if self.autoscaling_limit_min_cu is not None:
            body["autoscaling_limit_min_cu"] = self.autoscaling_limit_min_cu
        if self.pg_settings:
            body["pg_settings"] = self.pg_settings
        if self.pgbouncer_settings:
            body["pgbouncer_settings"] = self.pgbouncer_settings
        if self.suspend_timeout_duration is not None:
            body["suspend_timeout_duration"] = self.suspend_timeout_duration
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ProjectDefaultEndpointSettings:
        """Deserializes the ProjectDefaultEndpointSettings from a dictionary."""
        return cls(
            autoscaling_limit_max_cu=d.get("autoscaling_limit_max_cu", None),
            autoscaling_limit_min_cu=d.get("autoscaling_limit_min_cu", None),
            pg_settings=d.get("pg_settings", None),
            pgbouncer_settings=d.get("pgbouncer_settings", None),
            suspend_timeout_duration=_duration(d, "suspend_timeout_duration"),
        )


@dataclass
class ProjectOperationMetadata:
    def as_dict(self) -> dict:
        """Serializes the ProjectOperationMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ProjectOperationMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ProjectOperationMetadata:
        """Deserializes the ProjectOperationMetadata from a dictionary."""
        return cls()


@dataclass
class ProjectSettings:
    enable_logical_replication: Optional[bool] = None
    """Sets wal_level=logical for all compute endpoints in this project. All active endpoints will be
    suspended. Once enabled, logical replication cannot be disabled."""

    def as_dict(self) -> dict:
        """Serializes the ProjectSettings into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.enable_logical_replication is not None:
            body["enable_logical_replication"] = self.enable_logical_replication
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ProjectSettings into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.enable_logical_replication is not None:
            body["enable_logical_replication"] = self.enable_logical_replication
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ProjectSettings:
        """Deserializes the ProjectSettings from a dictionary."""
        return cls(enable_logical_replication=d.get("enable_logical_replication", None))


class PostgresAPI:
    """The Postgres API provides access to a Postgres database via REST API or direct SQL."""

    def __init__(self, api_client):
        self._api = api_client

    def create_branch(self, parent: str, branch: Branch, *, branch_id: Optional[str] = None) -> CreateBranchOperation:
        """Create a Branch.

        :param parent: str
          The Project where this Branch will be created. Format: projects/{project_id}
        :param branch: :class:`Branch`
          The Branch to create.
        :param branch_id: str (optional)
          The ID to use for the Branch, which will become the final component of the branch's resource name.

          This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

        :returns: :class:`Operation`
        """

        body = branch.as_dict()
        query = {}
        if branch_id is not None:
            query["branch_id"] = branch_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", f"/api/2.0/postgres/{parent}/branches", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return CreateBranchOperation(self, operation)

    def create_endpoint(
        self, parent: str, endpoint: Endpoint, *, endpoint_id: Optional[str] = None
    ) -> CreateEndpointOperation:
        """Create an Endpoint.

        :param parent: str
          The Branch where this Endpoint will be created. Format: projects/{project_id}/branches/{branch_id}
        :param endpoint: :class:`Endpoint`
          The Endpoint to create.
        :param endpoint_id: str (optional)
          The ID to use for the Endpoint, which will become the final component of the endpoint's resource
          name.

          This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

        :returns: :class:`Operation`
        """

        body = endpoint.as_dict()
        query = {}
        if endpoint_id is not None:
            query["endpoint_id"] = endpoint_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", f"/api/2.0/postgres/{parent}/endpoints", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return CreateEndpointOperation(self, operation)

    def create_project(self, project: Project, *, project_id: Optional[str] = None) -> CreateProjectOperation:
        """Create a Project.

        :param project: :class:`Project`
          The Project to create.
        :param project_id: str (optional)
          The ID to use for the Project, which will become the final component of the project's resource name.

          This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

        :returns: :class:`Operation`
        """

        body = project.as_dict()
        query = {}
        if project_id is not None:
            query["project_id"] = project_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/postgres/projects", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return CreateProjectOperation(self, operation)

    def delete_branch(self, name: str):
        """Delete a Branch.

        :param name: str
          The name of the Branch to delete. Format: projects/{project_id}/branches/{branch_id}


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/postgres/{name}", headers=headers)

    def delete_endpoint(self, name: str):
        """Delete an Endpoint.

        :param name: str
          The name of the Endpoint to delete. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/postgres/{name}", headers=headers)

    def delete_project(self, name: str):
        """Delete a Project.

        :param name: str
          The name of the Project to delete. Format: projects/{project_id}


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/postgres/{name}", headers=headers)

    def get_branch(self, name: str) -> Branch:
        """Get a Branch.

        :param name: str
          The name of the Branch to retrieve. Format: projects/{project_id}/branches/{branch_id}

        :returns: :class:`Branch`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return Branch.from_dict(res)

    def get_endpoint(self, name: str) -> Endpoint:
        """Get an Endpoint.

        :param name: str
          The name of the Endpoint to retrieve. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}

        :returns: :class:`Endpoint`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return Endpoint.from_dict(res)

    def get_operation(self, name: str) -> Operation:
        """Get an Operation.

        :param name: str
          The name of the operation resource.

        :returns: :class:`Operation`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return Operation.from_dict(res)

    def get_project(self, name: str) -> Project:
        """Get a Project.

        :param name: str
          The name of the Project to retrieve. Format: projects/{project_id}

        :returns: :class:`Project`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return Project.from_dict(res)

    def list_branches(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Branch]:
        """List Branches.

        :param parent: str
          The Project that owns this collection of branches. Format: projects/{project_id}
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Branches. Requests first page if absent.

        :returns: Iterator over :class:`Branch`
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
            json = self._api.do("GET", f"/api/2.0/postgres/{parent}/branches", query=query, headers=headers)
            if "branches" in json:
                for v in json["branches"]:
                    yield Branch.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_endpoints(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Endpoint]:
        """List Endpoints.

        :param parent: str
          The Branch that owns this collection of endpoints. Format:
          projects/{project_id}/branches/{branch_id}
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Endpoints. Requests first page if absent.

        :returns: Iterator over :class:`Endpoint`
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
            json = self._api.do("GET", f"/api/2.0/postgres/{parent}/endpoints", query=query, headers=headers)
            if "endpoints" in json:
                for v in json["endpoints"]:
                    yield Endpoint.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_projects(self, *, page_size: Optional[int] = None, page_token: Optional[str] = None) -> Iterator[Project]:
        """List Projects.

        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Projects. Requests first page if absent.

        :returns: Iterator over :class:`Project`
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
            json = self._api.do("GET", "/api/2.0/postgres/projects", query=query, headers=headers)
            if "projects" in json:
                for v in json["projects"]:
                    yield Project.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def update_branch(self, name: str, branch: Branch, update_mask: FieldMask) -> UpdateBranchOperation:
        """Update a Branch.

        :param name: str
          The resource name of the branch. Format: projects/{project_id}/branches/{branch_id}
        :param branch: :class:`Branch`
          The Branch to update.

          The branch's `name` field is used to identify the branch to update. Format:
          projects/{project_id}/branches/{branch_id}
        :param update_mask: FieldMask
          The list of fields to update. If unspecified, all fields will be updated when possible.

        :returns: :class:`Operation`
        """

        body = branch.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.0/postgres/{name}", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return UpdateBranchOperation(self, operation)

    def update_endpoint(self, name: str, endpoint: Endpoint, update_mask: FieldMask) -> UpdateEndpointOperation:
        """Update an Endpoint.

        :param name: str
          The resource name of the endpoint. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}
        :param endpoint: :class:`Endpoint`
          The Endpoint to update.

          The endpoint's `name` field is used to identify the endpoint to update. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}
        :param update_mask: FieldMask
          The list of fields to update. If unspecified, all fields will be updated when possible.

        :returns: :class:`Operation`
        """

        body = endpoint.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.0/postgres/{name}", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return UpdateEndpointOperation(self, operation)

    def update_project(self, name: str, project: Project, update_mask: FieldMask) -> UpdateProjectOperation:
        """Update a Project.

        :param name: str
          The resource name of the project. Format: projects/{project_id}
        :param project: :class:`Project`
          The Project to update.

          The project's `name` field is used to identify the project to update. Format: projects/{project_id}
        :param update_mask: FieldMask
          The list of fields to update. If unspecified, all fields will be updated when possible.

        :returns: :class:`Operation`
        """

        body = project.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.0/postgres/{name}", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return UpdateProjectOperation(self, operation)


class CreateBranchOperation:
    """Long-running operation for create_branch"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> Branch:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Branch`
        """

        def poll_operation():
            operation = self._impl.get_operation(name=self._operation.name)

            # Update local operation state
            self._operation = operation

            if not operation.done:
                return None, RetryError.continues("operation still in progress")

            if operation.error:
                error_msg = operation.error.message if operation.error.message else "unknown error"
                if operation.error.error_code:
                    error_msg = f"[{operation.error.error_code}] {error_msg}"
                return None, RetryError.halt(Exception(f"operation failed: {error_msg}"))

            # Operation completed successfully, unmarshal response.
            if operation.response is None:
                return None, RetryError.halt(Exception("operation completed but no response available"))

            branch = Branch.from_dict(operation.response)

            return branch, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> BranchOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`BranchOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return BranchOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class CreateEndpointOperation:
    """Long-running operation for create_endpoint"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> Endpoint:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Endpoint`
        """

        def poll_operation():
            operation = self._impl.get_operation(name=self._operation.name)

            # Update local operation state
            self._operation = operation

            if not operation.done:
                return None, RetryError.continues("operation still in progress")

            if operation.error:
                error_msg = operation.error.message if operation.error.message else "unknown error"
                if operation.error.error_code:
                    error_msg = f"[{operation.error.error_code}] {error_msg}"
                return None, RetryError.halt(Exception(f"operation failed: {error_msg}"))

            # Operation completed successfully, unmarshal response.
            if operation.response is None:
                return None, RetryError.halt(Exception("operation completed but no response available"))

            endpoint = Endpoint.from_dict(operation.response)

            return endpoint, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> EndpointOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`EndpointOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return EndpointOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class CreateProjectOperation:
    """Long-running operation for create_project"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> Project:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Project`
        """

        def poll_operation():
            operation = self._impl.get_operation(name=self._operation.name)

            # Update local operation state
            self._operation = operation

            if not operation.done:
                return None, RetryError.continues("operation still in progress")

            if operation.error:
                error_msg = operation.error.message if operation.error.message else "unknown error"
                if operation.error.error_code:
                    error_msg = f"[{operation.error.error_code}] {error_msg}"
                return None, RetryError.halt(Exception(f"operation failed: {error_msg}"))

            # Operation completed successfully, unmarshal response.
            if operation.response is None:
                return None, RetryError.halt(Exception("operation completed but no response available"))

            project = Project.from_dict(operation.response)

            return project, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> ProjectOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`ProjectOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return ProjectOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class UpdateBranchOperation:
    """Long-running operation for update_branch"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> Branch:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Branch`
        """

        def poll_operation():
            operation = self._impl.get_operation(name=self._operation.name)

            # Update local operation state
            self._operation = operation

            if not operation.done:
                return None, RetryError.continues("operation still in progress")

            if operation.error:
                error_msg = operation.error.message if operation.error.message else "unknown error"
                if operation.error.error_code:
                    error_msg = f"[{operation.error.error_code}] {error_msg}"
                return None, RetryError.halt(Exception(f"operation failed: {error_msg}"))

            # Operation completed successfully, unmarshal response.
            if operation.response is None:
                return None, RetryError.halt(Exception("operation completed but no response available"))

            branch = Branch.from_dict(operation.response)

            return branch, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> BranchOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`BranchOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return BranchOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class UpdateEndpointOperation:
    """Long-running operation for update_endpoint"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> Endpoint:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Endpoint`
        """

        def poll_operation():
            operation = self._impl.get_operation(name=self._operation.name)

            # Update local operation state
            self._operation = operation

            if not operation.done:
                return None, RetryError.continues("operation still in progress")

            if operation.error:
                error_msg = operation.error.message if operation.error.message else "unknown error"
                if operation.error.error_code:
                    error_msg = f"[{operation.error.error_code}] {error_msg}"
                return None, RetryError.halt(Exception(f"operation failed: {error_msg}"))

            # Operation completed successfully, unmarshal response.
            if operation.response is None:
                return None, RetryError.halt(Exception("operation completed but no response available"))

            endpoint = Endpoint.from_dict(operation.response)

            return endpoint, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> EndpointOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`EndpointOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return EndpointOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class UpdateProjectOperation:
    """Long-running operation for update_project"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> Project:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Project`
        """

        def poll_operation():
            operation = self._impl.get_operation(name=self._operation.name)

            # Update local operation state
            self._operation = operation

            if not operation.done:
                return None, RetryError.continues("operation still in progress")

            if operation.error:
                error_msg = operation.error.message if operation.error.message else "unknown error"
                if operation.error.error_code:
                    error_msg = f"[{operation.error.error_code}] {error_msg}"
                return None, RetryError.halt(Exception(f"operation failed: {error_msg}"))

            # Operation completed successfully, unmarshal response.
            if operation.response is None:
                return None, RetryError.halt(Exception("operation completed but no response available"))

            project = Project.from_dict(operation.response)

            return project, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> ProjectOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`ProjectOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return ProjectOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done

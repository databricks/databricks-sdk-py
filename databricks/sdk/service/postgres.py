# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List, Optional

from databricks.sdk.common import lro
from databricks.sdk.retries import RetryError, poll
from databricks.sdk.service._internal import _enum, _from_dict, _repeated_dict

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class DatabaseBranch:
    create_time: Optional[str] = None
    """A timestamp indicating when the branch was created."""

    current_state: Optional[str] = None
    """The branch’s state, indicating if it is initializing, ready for use, or archived."""

    default: Optional[bool] = None
    """Whether the branch is the project's default branch. This field is only returned on create/update
    responses. See effective_default for the value that is actually applied to the database branch."""

    effective_default: Optional[bool] = None
    """Whether the branch is the project's default branch."""

    is_protected: Optional[bool] = None
    """Whether the branch is protected."""

    logical_size_bytes: Optional[int] = None
    """The logical size of the branch."""

    name: Optional[str] = None
    """The resource name of the branch. Format: projects/{project_id}/branches/{branch_id}"""

    parent: Optional[str] = None
    """The parent to list branches from. Format: projects/{project_id}"""

    parent_branch: Optional[str] = None
    """The parent branch Format: projects/{project_id}/branches/{branch_id}"""

    parent_branch_lsn: Optional[str] = None
    """The Log Sequence Number (LSN) on the parent branch from which this branch was created. When
    restoring a branch using the Restore Database Branch endpoint, this value isn’t finalized
    until all operations related to the restore have completed successfully."""

    parent_branch_time: Optional[str] = None
    """The point in time on the parent branch from which this branch was created."""

    pending_state: Optional[str] = None

    state_change_time: Optional[str] = None
    """A timestamp indicating when the `current_state` began."""

    update_time: Optional[str] = None
    """A timestamp indicating when the branch was last updated."""

    def as_dict(self) -> dict:
        """Serializes the DatabaseBranch into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.current_state is not None:
            body["current_state"] = self.current_state
        if self.default is not None:
            body["default"] = self.default
        if self.effective_default is not None:
            body["effective_default"] = self.effective_default
        if self.is_protected is not None:
            body["is_protected"] = self.is_protected
        if self.logical_size_bytes is not None:
            body["logical_size_bytes"] = self.logical_size_bytes
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.parent_branch is not None:
            body["parent_branch"] = self.parent_branch
        if self.parent_branch_lsn is not None:
            body["parent_branch_lsn"] = self.parent_branch_lsn
        if self.parent_branch_time is not None:
            body["parent_branch_time"] = self.parent_branch_time
        if self.pending_state is not None:
            body["pending_state"] = self.pending_state
        if self.state_change_time is not None:
            body["state_change_time"] = self.state_change_time
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabaseBranch into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.current_state is not None:
            body["current_state"] = self.current_state
        if self.default is not None:
            body["default"] = self.default
        if self.effective_default is not None:
            body["effective_default"] = self.effective_default
        if self.is_protected is not None:
            body["is_protected"] = self.is_protected
        if self.logical_size_bytes is not None:
            body["logical_size_bytes"] = self.logical_size_bytes
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.parent_branch is not None:
            body["parent_branch"] = self.parent_branch
        if self.parent_branch_lsn is not None:
            body["parent_branch_lsn"] = self.parent_branch_lsn
        if self.parent_branch_time is not None:
            body["parent_branch_time"] = self.parent_branch_time
        if self.pending_state is not None:
            body["pending_state"] = self.pending_state
        if self.state_change_time is not None:
            body["state_change_time"] = self.state_change_time
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabaseBranch:
        """Deserializes the DatabaseBranch from a dictionary."""
        return cls(
            create_time=d.get("create_time", None),
            current_state=d.get("current_state", None),
            default=d.get("default", None),
            effective_default=d.get("effective_default", None),
            is_protected=d.get("is_protected", None),
            logical_size_bytes=d.get("logical_size_bytes", None),
            name=d.get("name", None),
            parent=d.get("parent", None),
            parent_branch=d.get("parent_branch", None),
            parent_branch_lsn=d.get("parent_branch_lsn", None),
            parent_branch_time=d.get("parent_branch_time", None),
            pending_state=d.get("pending_state", None),
            state_change_time=d.get("state_change_time", None),
            update_time=d.get("update_time", None),
        )


@dataclass
class DatabaseBranchOperationMetadata:
    def as_dict(self) -> dict:
        """Serializes the DatabaseBranchOperationMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabaseBranchOperationMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabaseBranchOperationMetadata:
        """Deserializes the DatabaseBranchOperationMetadata from a dictionary."""
        return cls()


@dataclass
class DatabaseCatalog:
    name: str
    """The name of the catalog in UC."""

    database_name: str
    """The name of the database (in a instance) associated with the catalog."""

    create_database_if_not_exists: Optional[bool] = None

    database_branch_id: Optional[str] = None
    """The branch_id of the database branch associated with the catalog."""

    database_project_id: Optional[str] = None
    """The project_id of the database project associated with the catalog."""

    uid: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the DatabaseCatalog into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_database_if_not_exists is not None:
            body["create_database_if_not_exists"] = self.create_database_if_not_exists
        if self.database_branch_id is not None:
            body["database_branch_id"] = self.database_branch_id
        if self.database_name is not None:
            body["database_name"] = self.database_name
        if self.database_project_id is not None:
            body["database_project_id"] = self.database_project_id
        if self.name is not None:
            body["name"] = self.name
        if self.uid is not None:
            body["uid"] = self.uid
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabaseCatalog into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_database_if_not_exists is not None:
            body["create_database_if_not_exists"] = self.create_database_if_not_exists
        if self.database_branch_id is not None:
            body["database_branch_id"] = self.database_branch_id
        if self.database_name is not None:
            body["database_name"] = self.database_name
        if self.database_project_id is not None:
            body["database_project_id"] = self.database_project_id
        if self.name is not None:
            body["name"] = self.name
        if self.uid is not None:
            body["uid"] = self.uid
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabaseCatalog:
        """Deserializes the DatabaseCatalog from a dictionary."""
        return cls(
            create_database_if_not_exists=d.get("create_database_if_not_exists", None),
            database_branch_id=d.get("database_branch_id", None),
            database_name=d.get("database_name", None),
            database_project_id=d.get("database_project_id", None),
            name=d.get("name", None),
            uid=d.get("uid", None),
        )


@dataclass
class DatabaseEndpoint:
    autoscaling_limit_max_cu: Optional[float] = None
    """The maximum number of Compute Units."""

    autoscaling_limit_min_cu: Optional[float] = None
    """The minimum number of Compute Units."""

    create_time: Optional[str] = None
    """A timestamp indicating when the compute endpoint was created."""

    current_state: Optional[DatabaseEndpointState] = None

    disabled: Optional[bool] = None
    """Whether to restrict connections to the compute endpoint. Enabling this option schedules a
    suspend compute operation. A disabled compute endpoint cannot be enabled by a connection or
    console action."""

    host: Optional[str] = None
    """The hostname of the compute endpoint. This is the hostname specified when connecting to a
    database."""

    last_active_time: Optional[str] = None
    """A timestamp indicating when the compute endpoint was last active."""

    name: Optional[str] = None
    """The resource name of the endpoint. Format:
    projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}"""

    parent: Optional[str] = None
    """The parent to list endpoints from. Format: projects/{project_id}/branches/{branch_id}"""

    pending_state: Optional[DatabaseEndpointState] = None

    pooler_mode: Optional[DatabaseEndpointPoolerMode] = None

    settings: Optional[DatabaseEndpointSettings] = None

    start_time: Optional[str] = None
    """A timestamp indicating when the compute endpoint was last started."""

    suspend_time: Optional[str] = None
    """A timestamp indicating when the compute endpoint was last suspended."""

    suspend_timeout_duration: Optional[str] = None
    """Duration of inactivity after which the compute endpoint is automatically suspended."""

    type: Optional[DatabaseEndpointType] = None
    """NOTE: if want type to default to some value set the server then an effective_type field OR make
    this field REQUIRED"""

    update_time: Optional[str] = None
    """A timestamp indicating when the compute endpoint was last updated."""

    def as_dict(self) -> dict:
        """Serializes the DatabaseEndpoint into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.autoscaling_limit_max_cu is not None:
            body["autoscaling_limit_max_cu"] = self.autoscaling_limit_max_cu
        if self.autoscaling_limit_min_cu is not None:
            body["autoscaling_limit_min_cu"] = self.autoscaling_limit_min_cu
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.current_state is not None:
            body["current_state"] = self.current_state.value
        if self.disabled is not None:
            body["disabled"] = self.disabled
        if self.host is not None:
            body["host"] = self.host
        if self.last_active_time is not None:
            body["last_active_time"] = self.last_active_time
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
            body["start_time"] = self.start_time
        if self.suspend_time is not None:
            body["suspend_time"] = self.suspend_time
        if self.suspend_timeout_duration is not None:
            body["suspend_timeout_duration"] = self.suspend_timeout_duration
        if self.type is not None:
            body["type"] = self.type.value
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabaseEndpoint into a shallow dictionary of its immediate attributes."""
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
        if self.type is not None:
            body["type"] = self.type
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabaseEndpoint:
        """Deserializes the DatabaseEndpoint from a dictionary."""
        return cls(
            autoscaling_limit_max_cu=d.get("autoscaling_limit_max_cu", None),
            autoscaling_limit_min_cu=d.get("autoscaling_limit_min_cu", None),
            create_time=d.get("create_time", None),
            current_state=_enum(d, "current_state", DatabaseEndpointState),
            disabled=d.get("disabled", None),
            host=d.get("host", None),
            last_active_time=d.get("last_active_time", None),
            name=d.get("name", None),
            parent=d.get("parent", None),
            pending_state=_enum(d, "pending_state", DatabaseEndpointState),
            pooler_mode=_enum(d, "pooler_mode", DatabaseEndpointPoolerMode),
            settings=_from_dict(d, "settings", DatabaseEndpointSettings),
            start_time=d.get("start_time", None),
            suspend_time=d.get("suspend_time", None),
            suspend_timeout_duration=d.get("suspend_timeout_duration", None),
            type=_enum(d, "type", DatabaseEndpointType),
            update_time=d.get("update_time", None),
        )


@dataclass
class DatabaseEndpointOperationMetadata:
    def as_dict(self) -> dict:
        """Serializes the DatabaseEndpointOperationMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabaseEndpointOperationMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabaseEndpointOperationMetadata:
        """Deserializes the DatabaseEndpointOperationMetadata from a dictionary."""
        return cls()


class DatabaseEndpointPoolerMode(Enum):
    """The connection pooler mode. Lakebase supports PgBouncer in `transaction` mode only."""

    TRANSACTION = "TRANSACTION"


@dataclass
class DatabaseEndpointSettings:
    """A collection of settings for a compute endpoint"""

    pg_settings: Optional[Dict[str, str]] = None
    """A raw representation of Postgres settings."""

    pgbouncer_settings: Optional[Dict[str, str]] = None
    """A raw representation of PgBouncer settings."""

    def as_dict(self) -> dict:
        """Serializes the DatabaseEndpointSettings into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.pg_settings:
            body["pg_settings"] = self.pg_settings
        if self.pgbouncer_settings:
            body["pgbouncer_settings"] = self.pgbouncer_settings
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabaseEndpointSettings into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.pg_settings:
            body["pg_settings"] = self.pg_settings
        if self.pgbouncer_settings:
            body["pgbouncer_settings"] = self.pgbouncer_settings
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabaseEndpointSettings:
        """Deserializes the DatabaseEndpointSettings from a dictionary."""
        return cls(pg_settings=d.get("pg_settings", None), pgbouncer_settings=d.get("pgbouncer_settings", None))


class DatabaseEndpointState(Enum):
    """The state of the compute endpoint"""

    ACTIVE = "ACTIVE"
    IDLE = "IDLE"
    INIT = "INIT"


class DatabaseEndpointType(Enum):
    """The compute endpoint type. Either `read_write` or `read_only`."""

    READ_ONLY = "READ_ONLY"
    READ_WRITE = "READ_WRITE"


@dataclass
class DatabaseProject:
    branch_logical_size_limit_bytes: Optional[int] = None
    """The logical size limit for a branch."""

    budget_policy_id: Optional[str] = None
    """The desired budget policy to associate with the instance. This field is only returned on
    create/update responses, and represents the customer provided budget policy. See
    effective_budget_policy_id for the policy that is actually applied to the instance."""

    compute_last_active_time: Optional[str] = None
    """The most recent time when any endpoint of this project was active."""

    create_time: Optional[str] = None
    """A timestamp indicating when the project was created."""

    custom_tags: Optional[List[DatabaseProjectCustomTag]] = None
    """Custom tags associated with the instance."""

    default_endpoint_settings: Optional[DatabaseProjectDefaultEndpointSettings] = None

    display_name: Optional[str] = None
    """Human-readable project name."""

    effective_budget_policy_id: Optional[str] = None
    """The policy that is applied to the instance."""

    effective_default_endpoint_settings: Optional[DatabaseProjectDefaultEndpointSettings] = None

    effective_display_name: Optional[str] = None

    effective_history_retention_duration: Optional[str] = None

    effective_pg_version: Optional[int] = None

    effective_settings: Optional[DatabaseProjectSettings] = None

    history_retention_duration: Optional[str] = None
    """The number of seconds to retain the shared history for point in time recovery for all branches
    in this project."""

    name: Optional[str] = None
    """The resource name of the project. Format: projects/{project_id}"""

    pg_version: Optional[int] = None
    """The major Postgres version number."""

    settings: Optional[DatabaseProjectSettings] = None

    synthetic_storage_size_bytes: Optional[int] = None
    """The current space occupied by the project in storage. Synthetic storage size combines the
    logical data size and Write-Ahead Log (WAL) size for all branches in a project."""

    update_time: Optional[str] = None
    """A timestamp indicating when the project was last updated."""

    def as_dict(self) -> dict:
        """Serializes the DatabaseProject into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.branch_logical_size_limit_bytes is not None:
            body["branch_logical_size_limit_bytes"] = self.branch_logical_size_limit_bytes
        if self.budget_policy_id is not None:
            body["budget_policy_id"] = self.budget_policy_id
        if self.compute_last_active_time is not None:
            body["compute_last_active_time"] = self.compute_last_active_time
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.custom_tags:
            body["custom_tags"] = [v.as_dict() for v in self.custom_tags]
        if self.default_endpoint_settings:
            body["default_endpoint_settings"] = self.default_endpoint_settings.as_dict()
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.effective_budget_policy_id is not None:
            body["effective_budget_policy_id"] = self.effective_budget_policy_id
        if self.effective_default_endpoint_settings:
            body["effective_default_endpoint_settings"] = self.effective_default_endpoint_settings.as_dict()
        if self.effective_display_name is not None:
            body["effective_display_name"] = self.effective_display_name
        if self.effective_history_retention_duration is not None:
            body["effective_history_retention_duration"] = self.effective_history_retention_duration
        if self.effective_pg_version is not None:
            body["effective_pg_version"] = self.effective_pg_version
        if self.effective_settings:
            body["effective_settings"] = self.effective_settings.as_dict()
        if self.history_retention_duration is not None:
            body["history_retention_duration"] = self.history_retention_duration
        if self.name is not None:
            body["name"] = self.name
        if self.pg_version is not None:
            body["pg_version"] = self.pg_version
        if self.settings:
            body["settings"] = self.settings.as_dict()
        if self.synthetic_storage_size_bytes is not None:
            body["synthetic_storage_size_bytes"] = self.synthetic_storage_size_bytes
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabaseProject into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.branch_logical_size_limit_bytes is not None:
            body["branch_logical_size_limit_bytes"] = self.branch_logical_size_limit_bytes
        if self.budget_policy_id is not None:
            body["budget_policy_id"] = self.budget_policy_id
        if self.compute_last_active_time is not None:
            body["compute_last_active_time"] = self.compute_last_active_time
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.custom_tags:
            body["custom_tags"] = self.custom_tags
        if self.default_endpoint_settings:
            body["default_endpoint_settings"] = self.default_endpoint_settings
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.effective_budget_policy_id is not None:
            body["effective_budget_policy_id"] = self.effective_budget_policy_id
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
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabaseProject:
        """Deserializes the DatabaseProject from a dictionary."""
        return cls(
            branch_logical_size_limit_bytes=d.get("branch_logical_size_limit_bytes", None),
            budget_policy_id=d.get("budget_policy_id", None),
            compute_last_active_time=d.get("compute_last_active_time", None),
            create_time=d.get("create_time", None),
            custom_tags=_repeated_dict(d, "custom_tags", DatabaseProjectCustomTag),
            default_endpoint_settings=_from_dict(
                d, "default_endpoint_settings", DatabaseProjectDefaultEndpointSettings
            ),
            display_name=d.get("display_name", None),
            effective_budget_policy_id=d.get("effective_budget_policy_id", None),
            effective_default_endpoint_settings=_from_dict(
                d, "effective_default_endpoint_settings", DatabaseProjectDefaultEndpointSettings
            ),
            effective_display_name=d.get("effective_display_name", None),
            effective_history_retention_duration=d.get("effective_history_retention_duration", None),
            effective_pg_version=d.get("effective_pg_version", None),
            effective_settings=_from_dict(d, "effective_settings", DatabaseProjectSettings),
            history_retention_duration=d.get("history_retention_duration", None),
            name=d.get("name", None),
            pg_version=d.get("pg_version", None),
            settings=_from_dict(d, "settings", DatabaseProjectSettings),
            synthetic_storage_size_bytes=d.get("synthetic_storage_size_bytes", None),
            update_time=d.get("update_time", None),
        )


@dataclass
class DatabaseProjectCustomTag:
    key: Optional[str] = None
    """The key of the custom tag."""

    value: Optional[str] = None
    """The value of the custom tag."""

    def as_dict(self) -> dict:
        """Serializes the DatabaseProjectCustomTag into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.key is not None:
            body["key"] = self.key
        if self.value is not None:
            body["value"] = self.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabaseProjectCustomTag into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.key is not None:
            body["key"] = self.key
        if self.value is not None:
            body["value"] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabaseProjectCustomTag:
        """Deserializes the DatabaseProjectCustomTag from a dictionary."""
        return cls(key=d.get("key", None), value=d.get("value", None))


@dataclass
class DatabaseProjectDefaultEndpointSettings:
    """A collection of settings for a database endpoint."""

    autoscaling_limit_max_cu: Optional[float] = None
    """The maximum number of Compute Units."""

    autoscaling_limit_min_cu: Optional[float] = None
    """The minimum number of Compute Units."""

    pg_settings: Optional[Dict[str, str]] = None
    """A raw representation of Postgres settings."""

    pgbouncer_settings: Optional[Dict[str, str]] = None
    """A raw representation of PgBouncer settings."""

    suspend_timeout_duration: Optional[str] = None
    """Duration of inactivity after which the compute endpoint is automatically suspended."""

    def as_dict(self) -> dict:
        """Serializes the DatabaseProjectDefaultEndpointSettings into a dictionary suitable for use as a JSON request body."""
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

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabaseProjectDefaultEndpointSettings into a shallow dictionary of its immediate attributes."""
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
    def from_dict(cls, d: Dict[str, Any]) -> DatabaseProjectDefaultEndpointSettings:
        """Deserializes the DatabaseProjectDefaultEndpointSettings from a dictionary."""
        return cls(
            autoscaling_limit_max_cu=d.get("autoscaling_limit_max_cu", None),
            autoscaling_limit_min_cu=d.get("autoscaling_limit_min_cu", None),
            pg_settings=d.get("pg_settings", None),
            pgbouncer_settings=d.get("pgbouncer_settings", None),
            suspend_timeout_duration=d.get("suspend_timeout_duration", None),
        )


@dataclass
class DatabaseProjectOperationMetadata:
    def as_dict(self) -> dict:
        """Serializes the DatabaseProjectOperationMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabaseProjectOperationMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabaseProjectOperationMetadata:
        """Deserializes the DatabaseProjectOperationMetadata from a dictionary."""
        return cls()


@dataclass
class DatabaseProjectSettings:
    enable_logical_replication: Optional[bool] = None
    """Sets wal_level=logical for all compute endpoints in this project. All active endpoints will be
    suspended. Once enabled, logical replication cannot be disabled."""

    def as_dict(self) -> dict:
        """Serializes the DatabaseProjectSettings into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.enable_logical_replication is not None:
            body["enable_logical_replication"] = self.enable_logical_replication
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabaseProjectSettings into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.enable_logical_replication is not None:
            body["enable_logical_replication"] = self.enable_logical_replication
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabaseProjectSettings:
        """Deserializes the DatabaseProjectSettings from a dictionary."""
        return cls(enable_logical_replication=d.get("enable_logical_replication", None))


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
class ListDatabaseBranchesResponse:
    database_branches: Optional[List[DatabaseBranch]] = None
    """List of branches."""

    next_page_token: Optional[str] = None
    """Pagination token to request the next page of instances."""

    def as_dict(self) -> dict:
        """Serializes the ListDatabaseBranchesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.database_branches:
            body["database_branches"] = [v.as_dict() for v in self.database_branches]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListDatabaseBranchesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.database_branches:
            body["database_branches"] = self.database_branches
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListDatabaseBranchesResponse:
        """Deserializes the ListDatabaseBranchesResponse from a dictionary."""
        return cls(
            database_branches=_repeated_dict(d, "database_branches", DatabaseBranch),
            next_page_token=d.get("next_page_token", None),
        )


@dataclass
class ListDatabaseEndpointsResponse:
    database_endpoints: Optional[List[DatabaseEndpoint]] = None
    """List of endpoints."""

    next_page_token: Optional[str] = None
    """Pagination token to request the next page of instances."""

    def as_dict(self) -> dict:
        """Serializes the ListDatabaseEndpointsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.database_endpoints:
            body["database_endpoints"] = [v.as_dict() for v in self.database_endpoints]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListDatabaseEndpointsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.database_endpoints:
            body["database_endpoints"] = self.database_endpoints
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListDatabaseEndpointsResponse:
        """Deserializes the ListDatabaseEndpointsResponse from a dictionary."""
        return cls(
            database_endpoints=_repeated_dict(d, "database_endpoints", DatabaseEndpoint),
            next_page_token=d.get("next_page_token", None),
        )


@dataclass
class ListDatabaseProjectsResponse:
    database_projects: Optional[List[DatabaseProject]] = None
    """List of projects."""

    next_page_token: Optional[str] = None
    """Pagination token to request the next page of instances."""

    def as_dict(self) -> dict:
        """Serializes the ListDatabaseProjectsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.database_projects:
            body["database_projects"] = [v.as_dict() for v in self.database_projects]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListDatabaseProjectsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.database_projects:
            body["database_projects"] = self.database_projects
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListDatabaseProjectsResponse:
        """Deserializes the ListDatabaseProjectsResponse from a dictionary."""
        return cls(
            database_projects=_repeated_dict(d, "database_projects", DatabaseProject),
            next_page_token=d.get("next_page_token", None),
        )


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


class PostgresAPI:
    """The Postgres API provides access to a Postgres database via REST API or direct SQL."""

    def __init__(self, api_client):
        self._api = api_client

    def create_database_branch(
        self, parent: str, database_branch: DatabaseBranch, *, database_branch_id: Optional[str] = None
    ) -> CreateDatabaseBranchOperation:
        """Create a Database Branch.

        :param parent: str
          The Database Project where this Database Branch will be created. Format: projects/{project_id}
        :param database_branch: :class:`DatabaseBranch`
          The Database Branch to create.
        :param database_branch_id: str (optional)
          The ID to use for the Database Branch, which will become the final component of the branch's
          resource name.

          This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

        :returns: :class:`Operation`
        """

        body = database_branch.as_dict()
        query = {}
        if database_branch_id is not None:
            query["database_branch_id"] = database_branch_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", f"/api/2.0/postgres/{parent}/branches", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return CreateDatabaseBranchOperation(self, operation)

    def create_database_catalog(self, catalog: DatabaseCatalog) -> DatabaseCatalog:
        """Create a Database Catalog.

        :param catalog: :class:`DatabaseCatalog`

        :returns: :class:`DatabaseCatalog`
        """

        body = catalog.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/postgres/catalogs", body=body, headers=headers)
        return DatabaseCatalog.from_dict(res)

    def create_database_endpoint(
        self, parent: str, database_endpoint: DatabaseEndpoint, *, database_endpoint_id: Optional[str] = None
    ) -> CreateDatabaseEndpointOperation:
        """Create a Database Endpoint.

        :param parent: str
          The Database Branch where this Database Endpoint will be created. Format:
          projects/{project_id}/branches/{branch_id}
        :param database_endpoint: :class:`DatabaseEndpoint`
          The Database Endpoint to create.
        :param database_endpoint_id: str (optional)
          The ID to use for the Database Endpoint, which will become the final component of the endpoint's
          resource name.

          This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

        :returns: :class:`Operation`
        """

        body = database_endpoint.as_dict()
        query = {}
        if database_endpoint_id is not None:
            query["database_endpoint_id"] = database_endpoint_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", f"/api/2.0/postgres/{parent}/endpoints", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return CreateDatabaseEndpointOperation(self, operation)

    def create_database_project(
        self, database_project: DatabaseProject, *, database_project_id: Optional[str] = None
    ) -> CreateDatabaseProjectOperation:
        """Create a Database Project.

        :param database_project: :class:`DatabaseProject`
          The Database Project to create
        :param database_project_id: str (optional)
          The ID to use for the Database Project, which will become the final component of the project's
          resource name.

          This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

        :returns: :class:`Operation`
        """

        body = database_project.as_dict()
        query = {}
        if database_project_id is not None:
            query["database_project_id"] = database_project_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/postgres/projects", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return CreateDatabaseProjectOperation(self, operation)

    def delete_database_branch(self, name: str):
        """Delete a Database Branch.

        :param name: str
          The name of the Database Branch to delete. Format: projects/{project_id}/branches/{branch_id}


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/postgres/{name}", headers=headers)

    def delete_database_endpoint(self, name: str):
        """Delete a Database Endpoint.

        :param name: str
          The name of the Database Endpoint to delete. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/postgres/{name}", headers=headers)

    def delete_database_project(self, name: str):
        """Delete a Database Project.

        :param name: str
          The name of the Database Project to delete. Format: projects/{project_id}


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/postgres/{name}", headers=headers)

    def get_database_branch(self, name: str) -> DatabaseBranch:
        """Get a Database Branch.

        :param name: str
          The name of the Database Branch to retrieve. Format: projects/{project_id}/branches/{branch_id}

        :returns: :class:`DatabaseBranch`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return DatabaseBranch.from_dict(res)

    def get_database_endpoint(self, name: str) -> DatabaseEndpoint:
        """Get a Database Endpoint.

        :param name: str
          The name of the Database Endpoint to retrieve. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}

        :returns: :class:`DatabaseEndpoint`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return DatabaseEndpoint.from_dict(res)

    def get_database_operation(self, name: str) -> Operation:
        """Get a Database Operation.

        :param name: str
          The name of the operation resource.

        :returns: :class:`Operation`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return Operation.from_dict(res)

    def get_database_project(self, name: str) -> DatabaseProject:
        """Get a Database Project.

        :param name: str
          The name of the Database Project to retrieve. Format: projects/{project_id}

        :returns: :class:`DatabaseProject`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return DatabaseProject.from_dict(res)

    def list_database_branches(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[DatabaseBranch]:
        """List Database Branches.

        :param parent: str
          The Database Project, which owns this collection of branches. Format: projects/{project_id}
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Database Branches. Requests first page if absent.

        :returns: Iterator over :class:`DatabaseBranch`
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
            if "database_branches" in json:
                for v in json["database_branches"]:
                    yield DatabaseBranch.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_database_endpoints(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[DatabaseEndpoint]:
        """List Database Endpoints.

        :param parent: str
          The Database Branch, which owns this collection of endpoints. Format:
          projects/{project_id}/branches/{branch_id}
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Database Branches. Requests first page if absent.

        :returns: Iterator over :class:`DatabaseEndpoint`
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
            if "database_endpoints" in json:
                for v in json["database_endpoints"]:
                    yield DatabaseEndpoint.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_database_projects(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[DatabaseProject]:
        """List Database Projects.

        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Database Projects. Requests first page if absent.

        :returns: Iterator over :class:`DatabaseProject`
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
            if "database_projects" in json:
                for v in json["database_projects"]:
                    yield DatabaseProject.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def restart_database_endpoint(self, name: str) -> RestartDatabaseEndpointOperation:
        """Restart a Database Endpoint.

        :param name: str
          The name of the Database Endpoint to restart. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}

        :returns: :class:`Operation`
        """

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", f"/api/2.0/postgres/{name}", headers=headers)
        operation = Operation.from_dict(res)
        return RestartDatabaseEndpointOperation(self, operation)

    def update_database_branch(
        self, name: str, database_branch: DatabaseBranch, update_mask: str
    ) -> UpdateDatabaseBranchOperation:
        """Update a Database Branch.

        :param name: str
          The resource name of the branch. Format: projects/{project_id}/branches/{branch_id}
        :param database_branch: :class:`DatabaseBranch`
          The Database Branch to update.

          The branch's `name` field is used to identify the branch to update. Format:
          projects/{project_id}/branches/{branch_id}
        :param update_mask: str
          The list of fields to update. If unspecified, all fields will be updated when possible.

        :returns: :class:`Operation`
        """

        body = database_branch.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.0/postgres/{name}", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return UpdateDatabaseBranchOperation(self, operation)

    def update_database_endpoint(
        self, name: str, database_endpoint: DatabaseEndpoint, update_mask: str
    ) -> UpdateDatabaseEndpointOperation:
        """Update a Database Endpoint.

        :param name: str
          The resource name of the endpoint. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}
        :param database_endpoint: :class:`DatabaseEndpoint`
          The Database Endpoint to update.

          The endpoints's `name` field is used to identify the endpoint to update. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}
        :param update_mask: str
          The list of fields to update. If unspecified, all fields will be updated when possible.

        :returns: :class:`Operation`
        """

        body = database_endpoint.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.0/postgres/{name}", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return UpdateDatabaseEndpointOperation(self, operation)

    def update_database_project(
        self, name: str, database_project: DatabaseProject, update_mask: str
    ) -> UpdateDatabaseProjectOperation:
        """Update a Database Project.

        :param name: str
          The resource name of the project. Format: projects/{project_id}
        :param database_project: :class:`DatabaseProject`
          The Database Project to update.

          The project's `name` field is used to identify the project to update. Format: projects/{project_id}
        :param update_mask: str
          The list of fields to update. If unspecified, all fields will be updated when possible.

        :returns: :class:`Operation`
        """

        body = database_project.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.0/postgres/{name}", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return UpdateDatabaseProjectOperation(self, operation)


class CreateDatabaseBranchOperation:
    """Long-running operation for create_database_branch"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> DatabaseBranch:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`DatabaseBranch`
        """

        def poll_operation():
            operation = self._impl.get_database_operation(name=self._operation.name)

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

            database_branch = DatabaseBranch.from_dict(operation.response)

            return database_branch, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> DatabaseBranchOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`DatabaseBranchOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return DatabaseBranchOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_database_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class CreateDatabaseEndpointOperation:
    """Long-running operation for create_database_endpoint"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> DatabaseEndpoint:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`DatabaseEndpoint`
        """

        def poll_operation():
            operation = self._impl.get_database_operation(name=self._operation.name)

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

            database_endpoint = DatabaseEndpoint.from_dict(operation.response)

            return database_endpoint, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> DatabaseEndpointOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`DatabaseEndpointOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return DatabaseEndpointOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_database_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class CreateDatabaseProjectOperation:
    """Long-running operation for create_database_project"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> DatabaseProject:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`DatabaseProject`
        """

        def poll_operation():
            operation = self._impl.get_database_operation(name=self._operation.name)

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

            database_project = DatabaseProject.from_dict(operation.response)

            return database_project, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> DatabaseProjectOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`DatabaseProjectOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return DatabaseProjectOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_database_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class RestartDatabaseEndpointOperation:
    """Long-running operation for restart_database_endpoint"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> DatabaseEndpoint:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`DatabaseEndpoint`
        """

        def poll_operation():
            operation = self._impl.get_database_operation(name=self._operation.name)

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

            database_endpoint = DatabaseEndpoint.from_dict(operation.response)

            return database_endpoint, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> DatabaseEndpointOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`DatabaseEndpointOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return DatabaseEndpointOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_database_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class UpdateDatabaseBranchOperation:
    """Long-running operation for update_database_branch"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> DatabaseBranch:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`DatabaseBranch`
        """

        def poll_operation():
            operation = self._impl.get_database_operation(name=self._operation.name)

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

            database_branch = DatabaseBranch.from_dict(operation.response)

            return database_branch, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> DatabaseBranchOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`DatabaseBranchOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return DatabaseBranchOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_database_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class UpdateDatabaseEndpointOperation:
    """Long-running operation for update_database_endpoint"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> DatabaseEndpoint:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`DatabaseEndpoint`
        """

        def poll_operation():
            operation = self._impl.get_database_operation(name=self._operation.name)

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

            database_endpoint = DatabaseEndpoint.from_dict(operation.response)

            return database_endpoint, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> DatabaseEndpointOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`DatabaseEndpointOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return DatabaseEndpointOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_database_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class UpdateDatabaseProjectOperation:
    """Long-running operation for update_database_project"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> DatabaseProject:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`DatabaseProject`
        """

        def poll_operation():
            operation = self._impl.get_database_operation(name=self._operation.name)

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

            database_project = DatabaseProject.from_dict(operation.response)

            return database_project, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> DatabaseProjectOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`DatabaseProjectOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return DatabaseProjectOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_database_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done

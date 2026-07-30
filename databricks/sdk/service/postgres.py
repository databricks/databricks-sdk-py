# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.
# ruff: noqa: F811, F841
# F401 is intentionally NOT covered: `make fmt` uses `ruff check --fix-only`
# to strip the fat-import header below; ignoring F401 would defeat that.

from __future__ import annotations

import logging
import uuid
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List, Optional

from google.protobuf.duration_pb2 import Duration
from google.protobuf.timestamp_pb2 import Timestamp

from databricks.sdk.common import lro
from databricks.sdk.common.types.fieldmask import FieldMask
from databricks.sdk.retries import RetryError, poll
from databricks.sdk.service._internal import (
    _duration,
    _enum,
    _from_dict,
    _repeated_dict,
    _repeated_enum,
    _timestamp,
)

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class Branch:
    branch_id: Optional[str] = None
    """The part of the name, chosen by the user when the resource was created."""

    create_time: Optional[Timestamp] = None
    """A timestamp indicating when the branch was created."""

    name: Optional[str] = None
    """Output only. The full resource path of the branch. Format:
    projects/{project_id}/branches/{branch_id}"""

    parent: Optional[str] = None
    """The project containing this branch (API resource hierarchy). Format: projects/{project_id}
    
    Note: This field indicates where the branch exists in the resource hierarchy. For point-in-time
    branching from another branch, see ``status.source_branch``."""

    spec: Optional[BranchSpec] = None
    """The spec contains the branch configuration."""

    status: Optional[BranchStatus] = None
    """The current status of a Branch."""

    uid: Optional[str] = None
    """System-generated unique ID for the branch."""

    update_time: Optional[Timestamp] = None
    """A timestamp indicating when the branch was last updated."""

    def as_dict(self) -> dict:
        """Serializes the Branch into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.branch_id is not None:
            body["branch_id"] = self.branch_id
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.spec:
            body["spec"] = self.spec.as_dict()
        if self.status:
            body["status"] = self.status.as_dict()
        if self.uid is not None:
            body["uid"] = self.uid
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Branch into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.branch_id is not None:
            body["branch_id"] = self.branch_id
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.spec:
            body["spec"] = self.spec
        if self.status:
            body["status"] = self.status
        if self.uid is not None:
            body["uid"] = self.uid
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Branch:
        """Deserializes the Branch from a dictionary."""
        return cls(
            branch_id=d.get("branch_id", None),
            create_time=_timestamp(d, "create_time"),
            name=d.get("name", None),
            parent=d.get("parent", None),
            spec=_from_dict(d, "spec", BranchSpec),
            status=_from_dict(d, "status", BranchStatus),
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


@dataclass
class BranchSpec:
    expire_time: Optional[Timestamp] = None
    """Absolute expiration timestamp. When set, the branch will expire at this time. Mutually exclusive
    with ``ttl`` and ``no_expiry``. When updating, use ``spec.expiration`` in the update_mask."""

    is_protected: Optional[bool] = None
    """When set to true, protects the branch from deletion and reset. Associated compute endpoints and
    the project cannot be deleted while the branch is protected."""

    no_expiry: Optional[bool] = None
    """Explicitly disable expiration. When set to true, the branch will not expire. If set to false,
    the request is invalid; provide either ttl or expire_time instead. Mutually exclusive with
    ``expire_time`` and ``ttl``. When updating, use ``spec.expiration`` in the update_mask."""

    source_branch: Optional[str] = None
    """The name of the source branch from which this branch was created (data lineage for point-in-time
    recovery). If not specified, defaults to the project's default branch. Format:
    projects/{project_id}/branches/{branch_id}"""

    source_branch_lsn: Optional[str] = None
    """The Log Sequence Number (LSN) on the source branch from which this branch was created."""

    source_branch_time: Optional[Timestamp] = None
    """The point in time on the source branch from which this branch was created."""

    ttl: Optional[Duration] = None
    """Relative time-to-live duration. When set, the branch will expire at creation_time + ttl.
    Mutually exclusive with ``expire_time`` and ``no_expiry``. When updating, use
    ``spec.expiration`` in the update_mask."""

    def as_dict(self) -> dict:
        """Serializes the BranchSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.expire_time is not None:
            body["expire_time"] = self.expire_time.ToJsonString()
        if self.is_protected is not None:
            body["is_protected"] = self.is_protected
        if self.no_expiry is not None:
            body["no_expiry"] = self.no_expiry
        if self.source_branch is not None:
            body["source_branch"] = self.source_branch
        if self.source_branch_lsn is not None:
            body["source_branch_lsn"] = self.source_branch_lsn
        if self.source_branch_time is not None:
            body["source_branch_time"] = self.source_branch_time.ToJsonString()
        if self.ttl is not None:
            body["ttl"] = self.ttl.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the BranchSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.expire_time is not None:
            body["expire_time"] = self.expire_time
        if self.is_protected is not None:
            body["is_protected"] = self.is_protected
        if self.no_expiry is not None:
            body["no_expiry"] = self.no_expiry
        if self.source_branch is not None:
            body["source_branch"] = self.source_branch
        if self.source_branch_lsn is not None:
            body["source_branch_lsn"] = self.source_branch_lsn
        if self.source_branch_time is not None:
            body["source_branch_time"] = self.source_branch_time
        if self.ttl is not None:
            body["ttl"] = self.ttl
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> BranchSpec:
        """Deserializes the BranchSpec from a dictionary."""
        return cls(
            expire_time=_timestamp(d, "expire_time"),
            is_protected=d.get("is_protected", None),
            no_expiry=d.get("no_expiry", None),
            source_branch=d.get("source_branch", None),
            source_branch_lsn=d.get("source_branch_lsn", None),
            source_branch_time=_timestamp(d, "source_branch_time"),
            ttl=_duration(d, "ttl"),
        )


@dataclass
class BranchStatus:
    branch_id: Optional[str] = None
    """Part of the resource name."""

    current_state: Optional[BranchStatusState] = None
    """The branch's state, indicating if it is initializing, ready for use, or archived."""

    default: Optional[bool] = None
    """Whether the branch is the project's default branch."""

    delete_time: Optional[Timestamp] = None
    """A timestamp indicating when the branch was deleted. Empty if the branch is not deleted."""

    expire_time: Optional[Timestamp] = None
    """Absolute expiration time for the branch. Empty if expiration is disabled."""

    is_protected: Optional[bool] = None
    """Whether the branch is protected."""

    logical_size_bytes: Optional[int] = None
    """The logical size of the branch."""

    pending_state: Optional[BranchStatusState] = None
    """The pending state of the branch, if a state transition is in progress."""

    purge_time: Optional[Timestamp] = None
    """A timestamp indicating when the branch is scheduled to be purged. Empty if the branch is not
    deleted, otherwise set to a timestamp in the future."""

    source_branch: Optional[str] = None
    """The name of the source branch from which this branch was created. Format:
    projects/{project_id}/branches/{branch_id}"""

    source_branch_lsn: Optional[str] = None
    """The Log Sequence Number (LSN) on the source branch from which this branch was created."""

    source_branch_time: Optional[Timestamp] = None
    """The point in time on the source branch from which this branch was created."""

    source_recovery_branch: Optional[str] = None
    """If this branch is a child of a recovery branch, this field identifies that recovery source. For
    non-recovery-derived branches this is unset. Format:
    projects/{project_id}/preview/recovery-branches/{recovery_branch_id}"""

    state_change_time: Optional[Timestamp] = None
    """A timestamp indicating when the ``current_state`` began."""

    def as_dict(self) -> dict:
        """Serializes the BranchStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.branch_id is not None:
            body["branch_id"] = self.branch_id
        if self.current_state is not None:
            body["current_state"] = self.current_state.value
        if self.default is not None:
            body["default"] = self.default
        if self.delete_time is not None:
            body["delete_time"] = self.delete_time.ToJsonString()
        if self.expire_time is not None:
            body["expire_time"] = self.expire_time.ToJsonString()
        if self.is_protected is not None:
            body["is_protected"] = self.is_protected
        if self.logical_size_bytes is not None:
            body["logical_size_bytes"] = self.logical_size_bytes
        if self.pending_state is not None:
            body["pending_state"] = self.pending_state.value
        if self.purge_time is not None:
            body["purge_time"] = self.purge_time.ToJsonString()
        if self.source_branch is not None:
            body["source_branch"] = self.source_branch
        if self.source_branch_lsn is not None:
            body["source_branch_lsn"] = self.source_branch_lsn
        if self.source_branch_time is not None:
            body["source_branch_time"] = self.source_branch_time.ToJsonString()
        if self.source_recovery_branch is not None:
            body["source_recovery_branch"] = self.source_recovery_branch
        if self.state_change_time is not None:
            body["state_change_time"] = self.state_change_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the BranchStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.branch_id is not None:
            body["branch_id"] = self.branch_id
        if self.current_state is not None:
            body["current_state"] = self.current_state
        if self.default is not None:
            body["default"] = self.default
        if self.delete_time is not None:
            body["delete_time"] = self.delete_time
        if self.expire_time is not None:
            body["expire_time"] = self.expire_time
        if self.is_protected is not None:
            body["is_protected"] = self.is_protected
        if self.logical_size_bytes is not None:
            body["logical_size_bytes"] = self.logical_size_bytes
        if self.pending_state is not None:
            body["pending_state"] = self.pending_state
        if self.purge_time is not None:
            body["purge_time"] = self.purge_time
        if self.source_branch is not None:
            body["source_branch"] = self.source_branch
        if self.source_branch_lsn is not None:
            body["source_branch_lsn"] = self.source_branch_lsn
        if self.source_branch_time is not None:
            body["source_branch_time"] = self.source_branch_time
        if self.source_recovery_branch is not None:
            body["source_recovery_branch"] = self.source_recovery_branch
        if self.state_change_time is not None:
            body["state_change_time"] = self.state_change_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> BranchStatus:
        """Deserializes the BranchStatus from a dictionary."""
        return cls(
            branch_id=d.get("branch_id", None),
            current_state=_enum(d, "current_state", BranchStatusState),
            default=d.get("default", None),
            delete_time=_timestamp(d, "delete_time"),
            expire_time=_timestamp(d, "expire_time"),
            is_protected=d.get("is_protected", None),
            logical_size_bytes=d.get("logical_size_bytes", None),
            pending_state=_enum(d, "pending_state", BranchStatusState),
            purge_time=_timestamp(d, "purge_time"),
            source_branch=d.get("source_branch", None),
            source_branch_lsn=d.get("source_branch_lsn", None),
            source_branch_time=_timestamp(d, "source_branch_time"),
            source_recovery_branch=d.get("source_recovery_branch", None),
            state_change_time=_timestamp(d, "state_change_time"),
        )


class BranchStatusState(Enum):
    """The state of the branch."""

    ARCHIVED = "ARCHIVED"
    DELETED = "DELETED"
    IMPORTING = "IMPORTING"
    INIT = "INIT"
    READY = "READY"
    RESETTING = "RESETTING"


@dataclass
class Catalog:
    catalog_id: Optional[str] = None
    """The part of the name, chosen by the user when the resource was created."""

    create_time: Optional[Timestamp] = None
    """A timestamp indicating when the catalog was created."""

    name: Optional[str] = None
    """Output only. The full resource path of the catalog.
    
    Format: "catalogs/{catalog_id}"."""

    spec: Optional[CatalogCatalogSpec] = None
    """The desired state of the Catalog."""

    status: Optional[CatalogCatalogStatus] = None
    """The observed state of the Catalog."""

    uid: Optional[str] = None
    """System-generated unique identifier for the catalog."""

    update_time: Optional[Timestamp] = None
    """A timestamp indicating when the catalog was last updated."""

    def as_dict(self) -> dict:
        """Serializes the Catalog into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.catalog_id is not None:
            body["catalog_id"] = self.catalog_id
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.name is not None:
            body["name"] = self.name
        if self.spec:
            body["spec"] = self.spec.as_dict()
        if self.status:
            body["status"] = self.status.as_dict()
        if self.uid is not None:
            body["uid"] = self.uid
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Catalog into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.catalog_id is not None:
            body["catalog_id"] = self.catalog_id
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.name is not None:
            body["name"] = self.name
        if self.spec:
            body["spec"] = self.spec
        if self.status:
            body["status"] = self.status
        if self.uid is not None:
            body["uid"] = self.uid
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Catalog:
        """Deserializes the Catalog from a dictionary."""
        return cls(
            catalog_id=d.get("catalog_id", None),
            create_time=_timestamp(d, "create_time"),
            name=d.get("name", None),
            spec=_from_dict(d, "spec", CatalogCatalogSpec),
            status=_from_dict(d, "status", CatalogCatalogStatus),
            uid=d.get("uid", None),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class CatalogCatalogSpec:
    """The desired state of the Catalog."""

    postgres_database: str
    """The name of the Postgres database inside the specified Lakebase project and branch to be
    associated with the UC catalog. This database must already exist, unless
    create_database_if_missing is set to true on creation.
    
    A database can only be registered with one UC catalog at a time. To re-register a database with
    a different catalog, the existing catalog must be deleted first.
    
    A child branch inherits the fact of parent's registration. This means the same-named database in
    a child branch cannot be registered with a second catalog while the parent's registration
    exists. To allow registering the database of a child branch, drop and recreate the database on
    the child branch. This removes the fact of parent's registration from this branch only.
    
    Doing Point In Time Restore (PITR) prior to the moment before the Postgres DB was registered in
    the Catalog drops the fact of registration of the database. So the user should avoid doing so."""

    branch: Optional[str] = None
    """The resource path of the branch associated with the catalog.
    
    Format: projects/{project_id}/branches/{branch_id}."""

    create_database_if_missing: Optional[bool] = None
    """If set to true, the specified postgres_database is created on behalf of the calling user if it
    does not already exist. In this case, the calling user has a role created for them in Postgres
    if they do not already have one.
    
    Defaults to false, meaning that the request fails if the specified postgres_database does not
    already exist."""

    def as_dict(self) -> dict:
        """Serializes the CatalogCatalogSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.branch is not None:
            body["branch"] = self.branch
        if self.create_database_if_missing is not None:
            body["create_database_if_missing"] = self.create_database_if_missing
        if self.postgres_database is not None:
            body["postgres_database"] = self.postgres_database
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CatalogCatalogSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.branch is not None:
            body["branch"] = self.branch
        if self.create_database_if_missing is not None:
            body["create_database_if_missing"] = self.create_database_if_missing
        if self.postgres_database is not None:
            body["postgres_database"] = self.postgres_database
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CatalogCatalogSpec:
        """Deserializes the CatalogCatalogSpec from a dictionary."""
        return cls(
            branch=d.get("branch", None),
            create_database_if_missing=d.get("create_database_if_missing", None),
            postgres_database=d.get("postgres_database", None),
        )


@dataclass
class CatalogCatalogStatus:
    """The observed state of the Catalog."""

    branch: Optional[str] = None
    """The resource path of the branch associated with the catalog.
    
    Format: projects/{project_id}/branches/{branch_id}."""

    postgres_database: Optional[str] = None
    """The name of the Postgres database associated with the catalog."""

    project: Optional[str] = None
    """The resource path of the project associated with the catalog.
    
    Format: projects/{project_id}."""

    def as_dict(self) -> dict:
        """Serializes the CatalogCatalogStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.branch is not None:
            body["branch"] = self.branch
        if self.postgres_database is not None:
            body["postgres_database"] = self.postgres_database
        if self.project is not None:
            body["project"] = self.project
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CatalogCatalogStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.branch is not None:
            body["branch"] = self.branch
        if self.postgres_database is not None:
            body["postgres_database"] = self.postgres_database
        if self.project is not None:
            body["project"] = self.project
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CatalogCatalogStatus:
        """Deserializes the CatalogCatalogStatus from a dictionary."""
        return cls(
            branch=d.get("branch", None),
            postgres_database=d.get("postgres_database", None),
            project=d.get("project", None),
        )


@dataclass
class CatalogOperationMetadata:
    def as_dict(self) -> dict:
        """Serializes the CatalogOperationMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CatalogOperationMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CatalogOperationMetadata:
        """Deserializes the CatalogOperationMetadata from a dictionary."""
        return cls()


@dataclass
class CdfConfig:
    """A Lakebase CDF configuration (CdfConfig): one per Postgres schema per database, replicating that
    schema's tables into a Unity Catalog schema. Immutable once created."""

    catalog: str
    """The Unity Catalog catalog that replicated tables are written into. Set at creation; the
    CdfConfig is immutable."""

    schema: str
    """The Unity Catalog schema that replicated tables are written into. Set at creation; the CdfConfig
    is immutable."""

    postgres_schema: str
    """The Postgres schema this CdfConfig replicates from. Unique within the parent database. Set at
    creation; the CdfConfig is immutable."""

    cdf_config_id: Optional[str] = None
    """The user-specified id; equals the final segment of ``name``. Defaults to the Postgres schema
    name for configs without an explicit id."""

    create_time: Optional[Timestamp] = None
    """When the CdfConfig was created."""

    name: Optional[str] = None
    """Output only. The full resource name of the CdfConfig. Format:
    projects/{project}/branches/{branch}/databases/{database}/cdf-configs/{cdf_config}"""

    def as_dict(self) -> dict:
        """Serializes the CdfConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.catalog is not None:
            body["catalog"] = self.catalog
        if self.cdf_config_id is not None:
            body["cdf_config_id"] = self.cdf_config_id
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.name is not None:
            body["name"] = self.name
        if self.postgres_schema is not None:
            body["postgres_schema"] = self.postgres_schema
        if self.schema is not None:
            body["schema"] = self.schema
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CdfConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.catalog is not None:
            body["catalog"] = self.catalog
        if self.cdf_config_id is not None:
            body["cdf_config_id"] = self.cdf_config_id
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.name is not None:
            body["name"] = self.name
        if self.postgres_schema is not None:
            body["postgres_schema"] = self.postgres_schema
        if self.schema is not None:
            body["schema"] = self.schema
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CdfConfig:
        """Deserializes the CdfConfig from a dictionary."""
        return cls(
            catalog=d.get("catalog", None),
            cdf_config_id=d.get("cdf_config_id", None),
            create_time=_timestamp(d, "create_time"),
            name=d.get("name", None),
            postgres_schema=d.get("postgres_schema", None),
            schema=d.get("schema", None),
        )


@dataclass
class CdfConfigOperationMetadata:
    """Metadata for CdfConfig long-running operations. Intentionally empty today; fields (e.g.
    progress) may be added as the operation contract grows."""

    def as_dict(self) -> dict:
        """Serializes the CdfConfigOperationMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CdfConfigOperationMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CdfConfigOperationMetadata:
        """Deserializes the CdfConfigOperationMetadata from a dictionary."""
        return cls()


class CdfState(Enum):
    """The replication state of a single replicated table (CdfStatus)."""

    CDF_STATE_SKIPPED = "CDF_STATE_SKIPPED"
    CDF_STATE_SNAPSHOTTING = "CDF_STATE_SNAPSHOTTING"
    CDF_STATE_STREAMING = "CDF_STATE_STREAMING"
    CDF_STATE_TERMINATED = "CDF_STATE_TERMINATED"


@dataclass
class CdfStatus:
    """The read-only replication status of a single Postgres table replicated under a CdfConfig. One
    status exists per replicated table. It is created automatically and cannot be modified."""

    committed_lsn: Optional[str] = None
    """The high-watermark Log Sequence Number (LSN) committed to Delta Lake."""

    create_time: Optional[Timestamp] = None
    """When replication for this table was first established."""

    last_sync_time: Optional[Timestamp] = None
    """The last time changes for this table were written to Delta Lake."""

    name: Optional[str] = None
    """Output only. The full resource name of the CdfStatus. Format:
    projects/{project}/branches/{branch}/databases/{database}/cdf-configs/{cdf_config}/cdf-statuses/{cdf_status}
    The {cdf_status} segment is the Postgres table name."""

    postgres_table: Optional[str] = None
    """The Postgres table being replicated."""

    state: Optional[CdfState] = None
    """The current replication state of this table."""

    status_detail: Optional[str] = None
    """Human-readable detail for the current state (e.g. the skip/error reason). Empty for healthy
    states."""

    uc_table: Optional[str] = None
    """The Unity Catalog table receiving replicated data."""

    def as_dict(self) -> dict:
        """Serializes the CdfStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.committed_lsn is not None:
            body["committed_lsn"] = self.committed_lsn
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.last_sync_time is not None:
            body["last_sync_time"] = self.last_sync_time.ToJsonString()
        if self.name is not None:
            body["name"] = self.name
        if self.postgres_table is not None:
            body["postgres_table"] = self.postgres_table
        if self.state is not None:
            body["state"] = self.state.value
        if self.status_detail is not None:
            body["status_detail"] = self.status_detail
        if self.uc_table is not None:
            body["uc_table"] = self.uc_table
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CdfStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.committed_lsn is not None:
            body["committed_lsn"] = self.committed_lsn
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.last_sync_time is not None:
            body["last_sync_time"] = self.last_sync_time
        if self.name is not None:
            body["name"] = self.name
        if self.postgres_table is not None:
            body["postgres_table"] = self.postgres_table
        if self.state is not None:
            body["state"] = self.state
        if self.status_detail is not None:
            body["status_detail"] = self.status_detail
        if self.uc_table is not None:
            body["uc_table"] = self.uc_table
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CdfStatus:
        """Deserializes the CdfStatus from a dictionary."""
        return cls(
            committed_lsn=d.get("committed_lsn", None),
            create_time=_timestamp(d, "create_time"),
            last_sync_time=_timestamp(d, "last_sync_time"),
            name=d.get("name", None),
            postgres_table=d.get("postgres_table", None),
            state=_enum(d, "state", CdfState),
            status_detail=d.get("status_detail", None),
            uc_table=d.get("uc_table", None),
        )


@dataclass
class ComputeInstance:
    name: str
    """The fully qualified name for this compute instance. Format:
    projects/*/branches/*/endpoints/*/compute-instances/*"""

    compute_instance_id: str
    """The unique ID for this compute."""

    compute_host: Optional[str] = None
    """A host scoped directly to the enclosing compute. This host is guaranteed to resolve to the
    specific compute instance."""

    current_state: Optional[ComputeInstanceComputeState] = None
    """The current state of the compute."""

    pending_state: Optional[ComputeInstanceComputeState] = None
    """The desired pending state of the compute, if a state transition is in progress."""

    role: Optional[ComputeInstanceComputeType] = None
    """The role of this compute within the endpoint."""

    start_time: Optional[Timestamp] = None
    """A timestamp indicating when the compute was last started."""

    suspend_time: Optional[Timestamp] = None
    """A timestamp indicating when the compute was last suspended."""

    def as_dict(self) -> dict:
        """Serializes the ComputeInstance into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.compute_host is not None:
            body["compute_host"] = self.compute_host
        if self.compute_instance_id is not None:
            body["compute_instance_id"] = self.compute_instance_id
        if self.current_state is not None:
            body["current_state"] = self.current_state.value
        if self.name is not None:
            body["name"] = self.name
        if self.pending_state is not None:
            body["pending_state"] = self.pending_state.value
        if self.role is not None:
            body["role"] = self.role.value
        if self.start_time is not None:
            body["start_time"] = self.start_time.ToJsonString()
        if self.suspend_time is not None:
            body["suspend_time"] = self.suspend_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ComputeInstance into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.compute_host is not None:
            body["compute_host"] = self.compute_host
        if self.compute_instance_id is not None:
            body["compute_instance_id"] = self.compute_instance_id
        if self.current_state is not None:
            body["current_state"] = self.current_state
        if self.name is not None:
            body["name"] = self.name
        if self.pending_state is not None:
            body["pending_state"] = self.pending_state
        if self.role is not None:
            body["role"] = self.role
        if self.start_time is not None:
            body["start_time"] = self.start_time
        if self.suspend_time is not None:
            body["suspend_time"] = self.suspend_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ComputeInstance:
        """Deserializes the ComputeInstance from a dictionary."""
        return cls(
            compute_host=d.get("compute_host", None),
            compute_instance_id=d.get("compute_instance_id", None),
            current_state=_enum(d, "current_state", ComputeInstanceComputeState),
            name=d.get("name", None),
            pending_state=_enum(d, "pending_state", ComputeInstanceComputeState),
            role=_enum(d, "role", ComputeInstanceComputeType),
            start_time=_timestamp(d, "start_time"),
            suspend_time=_timestamp(d, "suspend_time"),
        )


class ComputeInstanceComputeState(Enum):
    ACTIVE = "ACTIVE"
    IDLE = "IDLE"
    INIT = "INIT"


class ComputeInstanceComputeType(Enum):
    HOT_STANDBY = "HOT_STANDBY"
    READ_ONLY = "READ_ONLY"
    READ_WRITE = "READ_WRITE"


@dataclass
class DailySchedule:
    """Take a snapshot once per day, at the configured hour."""

    hour: Optional[int] = None
    """The hour of the day, in UTC, at which to take the snapshot, in [0, 23]."""

    def as_dict(self) -> dict:
        """Serializes the DailySchedule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.hour is not None:
            body["hour"] = self.hour
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DailySchedule into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.hour is not None:
            body["hour"] = self.hour
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DailySchedule:
        """Deserializes the DailySchedule from a dictionary."""
        return cls(hour=d.get("hour", None))


@dataclass
class DataApi:
    """DataApi represents the Data API (PostgREST) configuration for a Database. At most one DataApi
    per database. Create enables Data API, Delete disables it."""

    create_time: Optional[Timestamp] = None
    """A timestamp indicating when the Data API was first enabled."""

    name: Optional[str] = None
    """Resource name: projects/{project_id}/branches/{branch_id}/databases/{database_id}/data-api"""

    parent: Optional[str] = None
    """The database containing this Data API configuration. Format:
    projects/{project_id}/branches/{branch_id}/databases/{database_id}"""

    spec: Optional[DataApiDataApiSpec] = None
    """The desired Data API configuration."""

    status: Optional[DataApiDataApiStatus] = None
    """The observed Data API state (read-only)."""

    update_time: Optional[Timestamp] = None
    """A timestamp indicating when the Data API configuration was last updated."""

    def as_dict(self) -> dict:
        """Serializes the DataApi into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.spec:
            body["spec"] = self.spec.as_dict()
        if self.status:
            body["status"] = self.status.as_dict()
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DataApi into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.spec:
            body["spec"] = self.spec
        if self.status:
            body["status"] = self.status
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DataApi:
        """Deserializes the DataApi from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            name=d.get("name", None),
            parent=d.get("parent", None),
            spec=_from_dict(d, "spec", DataApiDataApiSpec),
            status=_from_dict(d, "status", DataApiDataApiStatus),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class DataApiDataApiSpec:
    """Desired PostgREST configuration (input)."""

    db_aggregates_enabled: Optional[bool] = None
    """Enable aggregate functions (count, sum, avg, etc.) in Data API responses. Default: true."""

    db_anon_role: Optional[str] = None
    """The PostgreSQL role used for unauthenticated (anonymous) requests. Must be a valid PostgreSQL
    role name (1-63 chars, [a-zA-Z_][a-zA-Z0-9_$]*). Default: "anonymous"."""

    db_extra_search_path: Optional[List[str]] = None
    """Additional schemas to include in the PostgreSQL search path. Each entry must be a valid
    PostgreSQL schema name."""

    db_max_rows: Optional[int] = None
    """Maximum number of rows returned in a single Data API response. Must be a positive integer."""

    db_schemas: Optional[List[str]] = None
    """Database schemas exposed through the Data API. Each entry must be a valid PostgreSQL schema name
    (1-63 chars, [a-zA-Z_][a-zA-Z0-9_$]*). Maximum 100 entries. Default: ["public"]."""

    jwt_cache_max_lifetime: Optional[Duration] = None
    """Maximum lifetime for cached JWT tokens. Zero duration disables caching."""

    jwt_role_claim_key: Optional[str] = None
    """JSON path to the role claim in JWT tokens (e.g., ".sub"). Default: ".sub"."""

    openapi_mode: Optional[OpenApiMode] = None
    """OpenAPI documentation mode for the Data API endpoint."""

    server_cors_allowed_origins: Optional[List[str]] = None
    """Allowed origins for CORS requests. Each entry should be a valid origin URL, or use "*" to allow
    all origins."""

    server_timing_enabled: Optional[bool] = None
    """Enable the Server-Timing header in Data API responses."""

    def as_dict(self) -> dict:
        """Serializes the DataApiDataApiSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.db_aggregates_enabled is not None:
            body["db_aggregates_enabled"] = self.db_aggregates_enabled
        if self.db_anon_role is not None:
            body["db_anon_role"] = self.db_anon_role
        if self.db_extra_search_path:
            body["db_extra_search_path"] = [v for v in self.db_extra_search_path]
        if self.db_max_rows is not None:
            body["db_max_rows"] = self.db_max_rows
        if self.db_schemas:
            body["db_schemas"] = [v for v in self.db_schemas]
        if self.jwt_cache_max_lifetime is not None:
            body["jwt_cache_max_lifetime"] = self.jwt_cache_max_lifetime.ToJsonString()
        if self.jwt_role_claim_key is not None:
            body["jwt_role_claim_key"] = self.jwt_role_claim_key
        if self.openapi_mode is not None:
            body["openapi_mode"] = self.openapi_mode.value
        if self.server_cors_allowed_origins:
            body["server_cors_allowed_origins"] = [v for v in self.server_cors_allowed_origins]
        if self.server_timing_enabled is not None:
            body["server_timing_enabled"] = self.server_timing_enabled
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DataApiDataApiSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.db_aggregates_enabled is not None:
            body["db_aggregates_enabled"] = self.db_aggregates_enabled
        if self.db_anon_role is not None:
            body["db_anon_role"] = self.db_anon_role
        if self.db_extra_search_path:
            body["db_extra_search_path"] = self.db_extra_search_path
        if self.db_max_rows is not None:
            body["db_max_rows"] = self.db_max_rows
        if self.db_schemas:
            body["db_schemas"] = self.db_schemas
        if self.jwt_cache_max_lifetime is not None:
            body["jwt_cache_max_lifetime"] = self.jwt_cache_max_lifetime
        if self.jwt_role_claim_key is not None:
            body["jwt_role_claim_key"] = self.jwt_role_claim_key
        if self.openapi_mode is not None:
            body["openapi_mode"] = self.openapi_mode
        if self.server_cors_allowed_origins:
            body["server_cors_allowed_origins"] = self.server_cors_allowed_origins
        if self.server_timing_enabled is not None:
            body["server_timing_enabled"] = self.server_timing_enabled
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DataApiDataApiSpec:
        """Deserializes the DataApiDataApiSpec from a dictionary."""
        return cls(
            db_aggregates_enabled=d.get("db_aggregates_enabled", None),
            db_anon_role=d.get("db_anon_role", None),
            db_extra_search_path=d.get("db_extra_search_path", None),
            db_max_rows=d.get("db_max_rows", None),
            db_schemas=d.get("db_schemas", None),
            jwt_cache_max_lifetime=_duration(d, "jwt_cache_max_lifetime"),
            jwt_role_claim_key=d.get("jwt_role_claim_key", None),
            openapi_mode=_enum(d, "openapi_mode", OpenApiMode),
            server_cors_allowed_origins=d.get("server_cors_allowed_origins", None),
            server_timing_enabled=d.get("server_timing_enabled", None),
        )


@dataclass
class DataApiDataApiStatus:
    """Observed state (output-only)."""

    available_schemas: Optional[List[str]] = None
    """Schemas available in the database (for reference when configuring db_schemas)."""

    db_aggregates_enabled: Optional[bool] = None
    """Actual aggregate function setting read from the database."""

    db_anon_role: Optional[str] = None
    """Actual anonymous role name read from the database."""

    db_extra_search_path: Optional[List[str]] = None
    """Actual extra search path schemas read from the database."""

    db_max_rows: Optional[int] = None
    """Actual max rows setting read from the database."""

    db_schemas: Optional[List[str]] = None
    """Actual exposed schemas read from the database."""

    jwt_cache_max_lifetime: Optional[Duration] = None
    """Actual JWT cache max lifetime read from the database."""

    jwt_role_claim_key: Optional[str] = None
    """Actual JWT role claim key read from the database."""

    openapi_mode: Optional[OpenApiMode] = None
    """Actual OpenAPI mode read from the database."""

    server_cors_allowed_origins: Optional[List[str]] = None
    """Actual CORS allowed origins read from the database."""

    server_timing_enabled: Optional[bool] = None
    """Actual Server-Timing header setting read from the database."""

    url: Optional[str] = None
    """Data API endpoint URL."""

    def as_dict(self) -> dict:
        """Serializes the DataApiDataApiStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.available_schemas:
            body["available_schemas"] = [v for v in self.available_schemas]
        if self.db_aggregates_enabled is not None:
            body["db_aggregates_enabled"] = self.db_aggregates_enabled
        if self.db_anon_role is not None:
            body["db_anon_role"] = self.db_anon_role
        if self.db_extra_search_path:
            body["db_extra_search_path"] = [v for v in self.db_extra_search_path]
        if self.db_max_rows is not None:
            body["db_max_rows"] = self.db_max_rows
        if self.db_schemas:
            body["db_schemas"] = [v for v in self.db_schemas]
        if self.jwt_cache_max_lifetime is not None:
            body["jwt_cache_max_lifetime"] = self.jwt_cache_max_lifetime.ToJsonString()
        if self.jwt_role_claim_key is not None:
            body["jwt_role_claim_key"] = self.jwt_role_claim_key
        if self.openapi_mode is not None:
            body["openapi_mode"] = self.openapi_mode.value
        if self.server_cors_allowed_origins:
            body["server_cors_allowed_origins"] = [v for v in self.server_cors_allowed_origins]
        if self.server_timing_enabled is not None:
            body["server_timing_enabled"] = self.server_timing_enabled
        if self.url is not None:
            body["url"] = self.url
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DataApiDataApiStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.available_schemas:
            body["available_schemas"] = self.available_schemas
        if self.db_aggregates_enabled is not None:
            body["db_aggregates_enabled"] = self.db_aggregates_enabled
        if self.db_anon_role is not None:
            body["db_anon_role"] = self.db_anon_role
        if self.db_extra_search_path:
            body["db_extra_search_path"] = self.db_extra_search_path
        if self.db_max_rows is not None:
            body["db_max_rows"] = self.db_max_rows
        if self.db_schemas:
            body["db_schemas"] = self.db_schemas
        if self.jwt_cache_max_lifetime is not None:
            body["jwt_cache_max_lifetime"] = self.jwt_cache_max_lifetime
        if self.jwt_role_claim_key is not None:
            body["jwt_role_claim_key"] = self.jwt_role_claim_key
        if self.openapi_mode is not None:
            body["openapi_mode"] = self.openapi_mode
        if self.server_cors_allowed_origins:
            body["server_cors_allowed_origins"] = self.server_cors_allowed_origins
        if self.server_timing_enabled is not None:
            body["server_timing_enabled"] = self.server_timing_enabled
        if self.url is not None:
            body["url"] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DataApiDataApiStatus:
        """Deserializes the DataApiDataApiStatus from a dictionary."""
        return cls(
            available_schemas=d.get("available_schemas", None),
            db_aggregates_enabled=d.get("db_aggregates_enabled", None),
            db_anon_role=d.get("db_anon_role", None),
            db_extra_search_path=d.get("db_extra_search_path", None),
            db_max_rows=d.get("db_max_rows", None),
            db_schemas=d.get("db_schemas", None),
            jwt_cache_max_lifetime=_duration(d, "jwt_cache_max_lifetime"),
            jwt_role_claim_key=d.get("jwt_role_claim_key", None),
            openapi_mode=_enum(d, "openapi_mode", OpenApiMode),
            server_cors_allowed_origins=d.get("server_cors_allowed_origins", None),
            server_timing_enabled=d.get("server_timing_enabled", None),
            url=d.get("url", None),
        )


@dataclass
class DataApiOperationMetadata:
    def as_dict(self) -> dict:
        """Serializes the DataApiOperationMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DataApiOperationMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DataApiOperationMetadata:
        """Deserializes the DataApiOperationMetadata from a dictionary."""
        return cls()


@dataclass
class Database:
    """Database represents a Postgres database within a Branch."""

    create_time: Optional[Timestamp] = None
    """A timestamp indicating when the database was created."""

    database_id: Optional[str] = None
    """The part of the name, chosen by the user when the resource was created."""

    name: Optional[str] = None
    """The resource name of the database. Format:
    projects/{project_id}/branches/{branch_id}/databases/{database_id}"""

    parent: Optional[str] = None
    """The branch containing this database. Format: projects/{project_id}/branches/{branch_id}"""

    spec: Optional[DatabaseDatabaseSpec] = None
    """The desired state of the Database."""

    status: Optional[DatabaseDatabaseStatus] = None
    """The observed state of the Database."""

    update_time: Optional[Timestamp] = None
    """A timestamp indicating when the database was last updated."""

    def as_dict(self) -> dict:
        """Serializes the Database into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.database_id is not None:
            body["database_id"] = self.database_id
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.spec:
            body["spec"] = self.spec.as_dict()
        if self.status:
            body["status"] = self.status.as_dict()
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Database into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.database_id is not None:
            body["database_id"] = self.database_id
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.spec:
            body["spec"] = self.spec
        if self.status:
            body["status"] = self.status
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Database:
        """Deserializes the Database from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            database_id=d.get("database_id", None),
            name=d.get("name", None),
            parent=d.get("parent", None),
            spec=_from_dict(d, "spec", DatabaseDatabaseSpec),
            status=_from_dict(d, "status", DatabaseDatabaseStatus),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class DatabaseCredential:
    expire_time: Optional[Timestamp] = None
    """Timestamp in UTC of when this credential expires."""

    token: Optional[str] = None
    """The OAuth token that can be used as a password when connecting to a database."""

    def as_dict(self) -> dict:
        """Serializes the DatabaseCredential into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.expire_time is not None:
            body["expire_time"] = self.expire_time.ToJsonString()
        if self.token is not None:
            body["token"] = self.token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabaseCredential into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.expire_time is not None:
            body["expire_time"] = self.expire_time
        if self.token is not None:
            body["token"] = self.token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabaseCredential:
        """Deserializes the DatabaseCredential from a dictionary."""
        return cls(expire_time=_timestamp(d, "expire_time"), token=d.get("token", None))


@dataclass
class DatabaseDatabaseSpec:
    role: str
    """The name of the role that owns the database. Format:
    projects/{project_id}/branches/{branch_id}/roles/{role_id}
    
    To change the owner, pass valid existing Role name when updating the Database
    
    A database always has an owner."""

    postgres_database: Optional[str] = None
    """The name of the Postgres database.
    
    This expects a valid Postgres identifier as specified in the link below.
    https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS Required
    when creating the Database.
    
    To rename, pass a valid postgres identifier when updating the Database."""

    def as_dict(self) -> dict:
        """Serializes the DatabaseDatabaseSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.postgres_database is not None:
            body["postgres_database"] = self.postgres_database
        if self.role is not None:
            body["role"] = self.role
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabaseDatabaseSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.postgres_database is not None:
            body["postgres_database"] = self.postgres_database
        if self.role is not None:
            body["role"] = self.role
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabaseDatabaseSpec:
        """Deserializes the DatabaseDatabaseSpec from a dictionary."""
        return cls(postgres_database=d.get("postgres_database", None), role=d.get("role", None))


@dataclass
class DatabaseDatabaseStatus:
    database_id: Optional[str] = None
    """Part of the resource name."""

    postgres_database: Optional[str] = None
    """The name of the Postgres database."""

    role: Optional[str] = None
    """The name of the role that owns the database. Format:
    projects/{project_id}/branches/{branch_id}/roles/{role_id}"""

    def as_dict(self) -> dict:
        """Serializes the DatabaseDatabaseStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.database_id is not None:
            body["database_id"] = self.database_id
        if self.postgres_database is not None:
            body["postgres_database"] = self.postgres_database
        if self.role is not None:
            body["role"] = self.role
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabaseDatabaseStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.database_id is not None:
            body["database_id"] = self.database_id
        if self.postgres_database is not None:
            body["postgres_database"] = self.postgres_database
        if self.role is not None:
            body["role"] = self.role
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabaseDatabaseStatus:
        """Deserializes the DatabaseDatabaseStatus from a dictionary."""
        return cls(
            database_id=d.get("database_id", None),
            postgres_database=d.get("postgres_database", None),
            role=d.get("role", None),
        )


@dataclass
class DatabaseOperationMetadata:
    def as_dict(self) -> dict:
        """Serializes the DatabaseOperationMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabaseOperationMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabaseOperationMetadata:
        """Deserializes the DatabaseOperationMetadata from a dictionary."""
        return cls()


@dataclass
class DatabricksServiceExceptionWithDetailsProto:
    """Databricks Error that is returned by all Databricks APIs."""

    details: Optional[List[dict]] = None

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


class DayOfWeek(Enum):
    """The day of the week on which a weekly snapshot is taken."""

    FRIDAY = "FRIDAY"
    MONDAY = "MONDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"
    THURSDAY = "THURSDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"


@dataclass
class DeleteForwardEtlConfigurationResponse:
    """Response to delete Forward ETL configuration."""

    deleted_configs: Optional[int] = None
    """Number of configuration rows deleted (0 or 1)."""

    deleted_mappings: Optional[int] = None
    """Number of table mapping rows deleted."""

    def as_dict(self) -> dict:
        """Serializes the DeleteForwardEtlConfigurationResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.deleted_configs is not None:
            body["deleted_configs"] = self.deleted_configs
        if self.deleted_mappings is not None:
            body["deleted_mappings"] = self.deleted_mappings
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DeleteForwardEtlConfigurationResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.deleted_configs is not None:
            body["deleted_configs"] = self.deleted_configs
        if self.deleted_mappings is not None:
            body["deleted_mappings"] = self.deleted_mappings
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DeleteForwardEtlConfigurationResponse:
        """Deserializes the DeleteForwardEtlConfigurationResponse from a dictionary."""
        return cls(deleted_configs=d.get("deleted_configs", None), deleted_mappings=d.get("deleted_mappings", None))


@dataclass
class DeltaTableSyncInfo:
    delta_commit_time: Optional[Timestamp] = None
    """The timestamp when the above Delta version was committed in the source Delta table. Note: This
    is the Delta commit time, not the time the data was written to the synced table."""

    delta_commit_version: Optional[int] = None
    """The Delta Lake commit version that was last successfully synced."""

    def as_dict(self) -> dict:
        """Serializes the DeltaTableSyncInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.delta_commit_time is not None:
            body["delta_commit_time"] = self.delta_commit_time.ToJsonString()
        if self.delta_commit_version is not None:
            body["delta_commit_version"] = self.delta_commit_version
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DeltaTableSyncInfo into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.delta_commit_time is not None:
            body["delta_commit_time"] = self.delta_commit_time
        if self.delta_commit_version is not None:
            body["delta_commit_version"] = self.delta_commit_version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DeltaTableSyncInfo:
        """Deserializes the DeltaTableSyncInfo from a dictionary."""
        return cls(
            delta_commit_time=_timestamp(d, "delta_commit_time"),
            delta_commit_version=d.get("delta_commit_version", None),
        )


@dataclass
class DisableForwardEtlResponse:
    """Response to disable Forward ETL"""

    disabled: Optional[bool] = None
    """Whether Forward ETL was successfully disabled."""

    def as_dict(self) -> dict:
        """Serializes the DisableForwardEtlResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.disabled is not None:
            body["disabled"] = self.disabled
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DisableForwardEtlResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.disabled is not None:
            body["disabled"] = self.disabled
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DisableForwardEtlResponse:
        """Deserializes the DisableForwardEtlResponse from a dictionary."""
        return cls(disabled=d.get("disabled", None))


@dataclass
class Endpoint:
    create_time: Optional[Timestamp] = None
    """A timestamp indicating when the compute endpoint was created."""

    endpoint_id: Optional[str] = None
    """The part of the name, chosen by the user when the resource was created."""

    name: Optional[str] = None
    """Output only. The full resource path of the endpoint. Format:
    projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}"""

    parent: Optional[str] = None
    """The branch containing this endpoint (API resource hierarchy). Format:
    projects/{project_id}/branches/{branch_id}"""

    spec: Optional[EndpointSpec] = None
    """The spec contains the compute endpoint configuration, including autoscaling limits, suspend
    timeout, and disabled state."""

    status: Optional[EndpointStatus] = None
    """Current operational status of the compute endpoint."""

    uid: Optional[str] = None
    """System-generated unique ID for the endpoint."""

    update_time: Optional[Timestamp] = None
    """A timestamp indicating when the compute endpoint was last updated."""

    def as_dict(self) -> dict:
        """Serializes the Endpoint into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.endpoint_id is not None:
            body["endpoint_id"] = self.endpoint_id
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.spec:
            body["spec"] = self.spec.as_dict()
        if self.status:
            body["status"] = self.status.as_dict()
        if self.uid is not None:
            body["uid"] = self.uid
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Endpoint into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.endpoint_id is not None:
            body["endpoint_id"] = self.endpoint_id
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.spec:
            body["spec"] = self.spec
        if self.status:
            body["status"] = self.status
        if self.uid is not None:
            body["uid"] = self.uid
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Endpoint:
        """Deserializes the Endpoint from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            endpoint_id=d.get("endpoint_id", None),
            name=d.get("name", None),
            parent=d.get("parent", None),
            spec=_from_dict(d, "spec", EndpointSpec),
            status=_from_dict(d, "status", EndpointStatus),
            uid=d.get("uid", None),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class EndpointGroupSpec:
    min: int
    """The minimum number of computes in the endpoint group. Currently, this must be equal to max. This
    must be greater than or equal to 1."""

    max: int
    """The maximum number of computes in the endpoint group. Currently, this must be equal to min. Set
    to 1 for single compute endpoints, to disable HA. To manually suspend all computes in an
    endpoint group, set disabled to true on the EndpointSpec."""

    enable_readable_secondaries: Optional[bool] = None
    """Whether to allow read-only connections to read-write endpoints. Only relevant for read-write
    endpoints where size.max > 1."""

    def as_dict(self) -> dict:
        """Serializes the EndpointGroupSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.enable_readable_secondaries is not None:
            body["enable_readable_secondaries"] = self.enable_readable_secondaries
        if self.max is not None:
            body["max"] = self.max
        if self.min is not None:
            body["min"] = self.min
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointGroupSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.enable_readable_secondaries is not None:
            body["enable_readable_secondaries"] = self.enable_readable_secondaries
        if self.max is not None:
            body["max"] = self.max
        if self.min is not None:
            body["min"] = self.min
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> EndpointGroupSpec:
        """Deserializes the EndpointGroupSpec from a dictionary."""
        return cls(
            enable_readable_secondaries=d.get("enable_readable_secondaries", None),
            max=d.get("max", None),
            min=d.get("min", None),
        )


@dataclass
class EndpointGroupStatus:
    min: int
    """The minimum number of computes in the endpoint group. Currently, this must be equal to max. This
    must be greater than or equal to 1."""

    max: int
    """The maximum number of computes in the endpoint group. Currently, this must be equal to min. Set
    to 1 for single compute endpoints, to disable HA. To manually suspend all computes in an
    endpoint group, set disabled to true on the EndpointSpec."""

    enable_readable_secondaries: Optional[bool] = None
    """Whether read-only connections to read-write endpoints are allowed. Only relevant if read
    replicas are configured by specifying size.max > 1."""

    def as_dict(self) -> dict:
        """Serializes the EndpointGroupStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.enable_readable_secondaries is not None:
            body["enable_readable_secondaries"] = self.enable_readable_secondaries
        if self.max is not None:
            body["max"] = self.max
        if self.min is not None:
            body["min"] = self.min
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointGroupStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.enable_readable_secondaries is not None:
            body["enable_readable_secondaries"] = self.enable_readable_secondaries
        if self.max is not None:
            body["max"] = self.max
        if self.min is not None:
            body["min"] = self.min
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> EndpointGroupStatus:
        """Deserializes the EndpointGroupStatus from a dictionary."""
        return cls(
            enable_readable_secondaries=d.get("enable_readable_secondaries", None),
            max=d.get("max", None),
            min=d.get("min", None),
        )


@dataclass
class EndpointHosts:
    """Encapsulates various hostnames (r/w or r/o, pooled or not) for an endpoint."""

    host: Optional[str] = None
    """The hostname to connect to this endpoint. For read-write endpoints, this is a read-write
    hostname which connects to the primary compute. For read-only endpoints, this is a read-only
    hostname which allows read-only operations."""

    read_only_host: Optional[str] = None
    """An optionally defined read-only host for the endpoint, without pooling. For read-only endpoints,
    this attribute is always defined and is equivalent to host. For read-write endpoints, this
    attribute is defined if the enclosing endpoint is a group with greater than 1 computes
    configured, and has readable secondaries enabled."""

    read_only_pooled_host: Optional[str] = None
    """The read-only hostname of the compute endpoint, with pooling. This attribute is always defined
    for read-only endpoints, and may be defined for read-write endpoints if configured with read
    replicas and allow read-only connections."""

    read_write_pooled_host: Optional[str] = None
    """The read-write hostname of the compute endpoint, with pooling. This attribute is only defined
    for read-write endpoints."""

    def as_dict(self) -> dict:
        """Serializes the EndpointHosts into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.host is not None:
            body["host"] = self.host
        if self.read_only_host is not None:
            body["read_only_host"] = self.read_only_host
        if self.read_only_pooled_host is not None:
            body["read_only_pooled_host"] = self.read_only_pooled_host
        if self.read_write_pooled_host is not None:
            body["read_write_pooled_host"] = self.read_write_pooled_host
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointHosts into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.host is not None:
            body["host"] = self.host
        if self.read_only_host is not None:
            body["read_only_host"] = self.read_only_host
        if self.read_only_pooled_host is not None:
            body["read_only_pooled_host"] = self.read_only_pooled_host
        if self.read_write_pooled_host is not None:
            body["read_write_pooled_host"] = self.read_write_pooled_host
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> EndpointHosts:
        """Deserializes the EndpointHosts from a dictionary."""
        return cls(
            host=d.get("host", None),
            read_only_host=d.get("read_only_host", None),
            read_only_pooled_host=d.get("read_only_pooled_host", None),
            read_write_pooled_host=d.get("read_write_pooled_host", None),
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


@dataclass
class EndpointSettings:
    """A collection of settings for a compute endpoint."""

    pg_settings: Optional[Dict[str, str]] = None
    """A raw representation of Postgres settings."""

    def as_dict(self) -> dict:
        """Serializes the EndpointSettings into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.pg_settings:
            body["pg_settings"] = self.pg_settings
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointSettings into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.pg_settings:
            body["pg_settings"] = self.pg_settings
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> EndpointSettings:
        """Deserializes the EndpointSettings from a dictionary."""
        return cls(pg_settings=d.get("pg_settings", None))


@dataclass
class EndpointSpec:
    endpoint_type: EndpointType
    """The endpoint type. A branch can only have one READ_WRITE endpoint."""

    autoscaling_limit_max_cu: Optional[float] = None
    """The maximum number of Compute Units. The maximum value is 64. The difference between the minimum
    and maximum Compute Units (max - min) must not exceed 16."""

    autoscaling_limit_min_cu: Optional[float] = None
    """The minimum number of Compute Units. Minimum value is 0.5."""

    disabled: Optional[bool] = None
    """Whether to restrict connections to the compute endpoint. Enabling this option schedules a
    suspend compute operation. A disabled compute endpoint cannot be enabled by a connection or
    console action."""

    group: Optional[EndpointGroupSpec] = None
    """Settings for optional HA configuration of the endpoint. If unspecified, the endpoint defaults to
    non HA settings, with a single compute backing the endpoint (and no readable secondaries for
    Read/Write endpoints)."""

    no_suspension: Optional[bool] = None
    """When set to true, explicitly disables automatic suspension (never suspend). Should be set to
    true when provided. Mutually exclusive with ``suspend_timeout_duration``. When updating, use
    ``spec.suspension`` in the update_mask."""

    settings: Optional[EndpointSettings] = None

    suspend_timeout_duration: Optional[Duration] = None
    """Duration of inactivity after which the compute endpoint is automatically suspended. If specified
    should be between 60s and 604800s (1 minute to 1 week). Mutually exclusive with
    ``no_suspension``. When updating, use ``spec.suspension`` in the update_mask."""

    def as_dict(self) -> dict:
        """Serializes the EndpointSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.autoscaling_limit_max_cu is not None:
            body["autoscaling_limit_max_cu"] = self.autoscaling_limit_max_cu
        if self.autoscaling_limit_min_cu is not None:
            body["autoscaling_limit_min_cu"] = self.autoscaling_limit_min_cu
        if self.disabled is not None:
            body["disabled"] = self.disabled
        if self.endpoint_type is not None:
            body["endpoint_type"] = self.endpoint_type.value
        if self.group:
            body["group"] = self.group.as_dict()
        if self.no_suspension is not None:
            body["no_suspension"] = self.no_suspension
        if self.settings:
            body["settings"] = self.settings.as_dict()
        if self.suspend_timeout_duration is not None:
            body["suspend_timeout_duration"] = self.suspend_timeout_duration.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.autoscaling_limit_max_cu is not None:
            body["autoscaling_limit_max_cu"] = self.autoscaling_limit_max_cu
        if self.autoscaling_limit_min_cu is not None:
            body["autoscaling_limit_min_cu"] = self.autoscaling_limit_min_cu
        if self.disabled is not None:
            body["disabled"] = self.disabled
        if self.endpoint_type is not None:
            body["endpoint_type"] = self.endpoint_type
        if self.group:
            body["group"] = self.group
        if self.no_suspension is not None:
            body["no_suspension"] = self.no_suspension
        if self.settings:
            body["settings"] = self.settings
        if self.suspend_timeout_duration is not None:
            body["suspend_timeout_duration"] = self.suspend_timeout_duration
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> EndpointSpec:
        """Deserializes the EndpointSpec from a dictionary."""
        return cls(
            autoscaling_limit_max_cu=d.get("autoscaling_limit_max_cu", None),
            autoscaling_limit_min_cu=d.get("autoscaling_limit_min_cu", None),
            disabled=d.get("disabled", None),
            endpoint_type=_enum(d, "endpoint_type", EndpointType),
            group=_from_dict(d, "group", EndpointGroupSpec),
            no_suspension=d.get("no_suspension", None),
            settings=_from_dict(d, "settings", EndpointSettings),
            suspend_timeout_duration=_duration(d, "suspend_timeout_duration"),
        )


@dataclass
class EndpointStatus:
    autoscaling_limit_max_cu: Optional[float] = None
    """The maximum number of Compute Units. The maximum value is 64. The difference between the minimum
    and maximum Compute Units (max - min) must not exceed 16."""

    autoscaling_limit_min_cu: Optional[float] = None
    """The minimum number of Compute Units."""

    current_state: Optional[EndpointStatusState] = None

    disabled: Optional[bool] = None
    """Whether to restrict connections to the compute endpoint. Enabling this option schedules a
    suspend compute operation. A disabled compute endpoint cannot be enabled by a connection or
    console action."""

    endpoint_id: Optional[str] = None
    """Part of the resource name."""

    endpoint_type: Optional[EndpointType] = None
    """The endpoint type. A branch can only have one READ_WRITE endpoint."""

    group: Optional[EndpointGroupStatus] = None
    """Details on the HA configuration of the endpoint."""

    hosts: Optional[EndpointHosts] = None
    """Contains host information for connecting to the endpoint."""

    last_active_time: Optional[Timestamp] = None
    """A timestamp indicating when the compute endpoint was last active."""

    pending_state: Optional[EndpointStatusState] = None

    settings: Optional[EndpointSettings] = None

    suspend_timeout_duration: Optional[Duration] = None
    """Duration of inactivity after which the compute endpoint is automatically suspended."""

    def as_dict(self) -> dict:
        """Serializes the EndpointStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.autoscaling_limit_max_cu is not None:
            body["autoscaling_limit_max_cu"] = self.autoscaling_limit_max_cu
        if self.autoscaling_limit_min_cu is not None:
            body["autoscaling_limit_min_cu"] = self.autoscaling_limit_min_cu
        if self.current_state is not None:
            body["current_state"] = self.current_state.value
        if self.disabled is not None:
            body["disabled"] = self.disabled
        if self.endpoint_id is not None:
            body["endpoint_id"] = self.endpoint_id
        if self.endpoint_type is not None:
            body["endpoint_type"] = self.endpoint_type.value
        if self.group:
            body["group"] = self.group.as_dict()
        if self.hosts:
            body["hosts"] = self.hosts.as_dict()
        if self.last_active_time is not None:
            body["last_active_time"] = self.last_active_time.ToJsonString()
        if self.pending_state is not None:
            body["pending_state"] = self.pending_state.value
        if self.settings:
            body["settings"] = self.settings.as_dict()
        if self.suspend_timeout_duration is not None:
            body["suspend_timeout_duration"] = self.suspend_timeout_duration.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.autoscaling_limit_max_cu is not None:
            body["autoscaling_limit_max_cu"] = self.autoscaling_limit_max_cu
        if self.autoscaling_limit_min_cu is not None:
            body["autoscaling_limit_min_cu"] = self.autoscaling_limit_min_cu
        if self.current_state is not None:
            body["current_state"] = self.current_state
        if self.disabled is not None:
            body["disabled"] = self.disabled
        if self.endpoint_id is not None:
            body["endpoint_id"] = self.endpoint_id
        if self.endpoint_type is not None:
            body["endpoint_type"] = self.endpoint_type
        if self.group:
            body["group"] = self.group
        if self.hosts:
            body["hosts"] = self.hosts
        if self.last_active_time is not None:
            body["last_active_time"] = self.last_active_time
        if self.pending_state is not None:
            body["pending_state"] = self.pending_state
        if self.settings:
            body["settings"] = self.settings
        if self.suspend_timeout_duration is not None:
            body["suspend_timeout_duration"] = self.suspend_timeout_duration
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> EndpointStatus:
        """Deserializes the EndpointStatus from a dictionary."""
        return cls(
            autoscaling_limit_max_cu=d.get("autoscaling_limit_max_cu", None),
            autoscaling_limit_min_cu=d.get("autoscaling_limit_min_cu", None),
            current_state=_enum(d, "current_state", EndpointStatusState),
            disabled=d.get("disabled", None),
            endpoint_id=d.get("endpoint_id", None),
            endpoint_type=_enum(d, "endpoint_type", EndpointType),
            group=_from_dict(d, "group", EndpointGroupStatus),
            hosts=_from_dict(d, "hosts", EndpointHosts),
            last_active_time=_timestamp(d, "last_active_time"),
            pending_state=_enum(d, "pending_state", EndpointStatusState),
            settings=_from_dict(d, "settings", EndpointSettings),
            suspend_timeout_duration=_duration(d, "suspend_timeout_duration"),
        )


class EndpointStatusState(Enum):
    """The state of the compute endpoint."""

    ACTIVE = "ACTIVE"
    DEGRADED = "DEGRADED"
    IDLE = "IDLE"
    INIT = "INIT"


class EndpointType(Enum):
    """The compute endpoint type. Either ``read_write`` or ``read_only``."""

    ENDPOINT_TYPE_READ_ONLY = "ENDPOINT_TYPE_READ_ONLY"
    ENDPOINT_TYPE_READ_WRITE = "ENDPOINT_TYPE_READ_WRITE"


class ErrorCode(Enum):
    """Error codes returned by Databricks APIs to indicate specific failure conditions."""

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
class ForwardEtlConfig:
    """Forward ETL configuration"""

    create_time_millis: Optional[int] = None
    """Configuration creation timestamp in milliseconds since epoch."""

    enabled: Optional[bool] = None
    """Whether Forward ETL is enabled."""

    pg_database_oid: Optional[int] = None
    """PostgreSQL database OID."""

    pg_schema_oid: Optional[int] = None
    """PostgreSQL schema OID."""

    tenant_id: Optional[str] = None
    """Tenant ID (dashless UUID format)."""

    timeline_id: Optional[str] = None
    """Timeline ID (dashless UUID format)."""

    uc_catalog_id: Optional[str] = None
    """Unity Catalog catalog ID."""

    uc_schema_id: Optional[str] = None
    """Unity Catalog schema ID."""

    update_time_millis: Optional[int] = None
    """Configuration last update timestamp in milliseconds since epoch."""

    workspace_id: Optional[int] = None
    """Workspace ID."""

    def as_dict(self) -> dict:
        """Serializes the ForwardEtlConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time_millis is not None:
            body["create_time_millis"] = self.create_time_millis
        if self.enabled is not None:
            body["enabled"] = self.enabled
        if self.pg_database_oid is not None:
            body["pg_database_oid"] = self.pg_database_oid
        if self.pg_schema_oid is not None:
            body["pg_schema_oid"] = self.pg_schema_oid
        if self.tenant_id is not None:
            body["tenant_id"] = self.tenant_id
        if self.timeline_id is not None:
            body["timeline_id"] = self.timeline_id
        if self.uc_catalog_id is not None:
            body["uc_catalog_id"] = self.uc_catalog_id
        if self.uc_schema_id is not None:
            body["uc_schema_id"] = self.uc_schema_id
        if self.update_time_millis is not None:
            body["update_time_millis"] = self.update_time_millis
        if self.workspace_id is not None:
            body["workspace_id"] = self.workspace_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ForwardEtlConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time_millis is not None:
            body["create_time_millis"] = self.create_time_millis
        if self.enabled is not None:
            body["enabled"] = self.enabled
        if self.pg_database_oid is not None:
            body["pg_database_oid"] = self.pg_database_oid
        if self.pg_schema_oid is not None:
            body["pg_schema_oid"] = self.pg_schema_oid
        if self.tenant_id is not None:
            body["tenant_id"] = self.tenant_id
        if self.timeline_id is not None:
            body["timeline_id"] = self.timeline_id
        if self.uc_catalog_id is not None:
            body["uc_catalog_id"] = self.uc_catalog_id
        if self.uc_schema_id is not None:
            body["uc_schema_id"] = self.uc_schema_id
        if self.update_time_millis is not None:
            body["update_time_millis"] = self.update_time_millis
        if self.workspace_id is not None:
            body["workspace_id"] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ForwardEtlConfig:
        """Deserializes the ForwardEtlConfig from a dictionary."""
        return cls(
            create_time_millis=d.get("create_time_millis", None),
            enabled=d.get("enabled", None),
            pg_database_oid=d.get("pg_database_oid", None),
            pg_schema_oid=d.get("pg_schema_oid", None),
            tenant_id=d.get("tenant_id", None),
            timeline_id=d.get("timeline_id", None),
            uc_catalog_id=d.get("uc_catalog_id", None),
            uc_schema_id=d.get("uc_schema_id", None),
            update_time_millis=d.get("update_time_millis", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class ForwardEtlDatabase:
    """Database metadata"""

    name: Optional[str] = None
    """Database name."""

    oid: Optional[int] = None
    """PostgreSQL database OID."""

    def as_dict(self) -> dict:
        """Serializes the ForwardEtlDatabase into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.oid is not None:
            body["oid"] = self.oid
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ForwardEtlDatabase into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.oid is not None:
            body["oid"] = self.oid
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ForwardEtlDatabase:
        """Deserializes the ForwardEtlDatabase from a dictionary."""
        return cls(name=d.get("name", None), oid=d.get("oid", None))


@dataclass
class ForwardEtlMetadata:
    """Forward ETL metadata response"""

    databases: Optional[List[ForwardEtlDatabase]] = None
    """List of databases with their PostgreSQL OIDs."""

    schemas: Optional[List[ForwardEtlSchema]] = None
    """List of schemas with their PostgreSQL OIDs."""

    def as_dict(self) -> dict:
        """Serializes the ForwardEtlMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.databases:
            body["databases"] = [v.as_dict() for v in self.databases]
        if self.schemas:
            body["schemas"] = [v.as_dict() for v in self.schemas]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ForwardEtlMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.databases:
            body["databases"] = self.databases
        if self.schemas:
            body["schemas"] = self.schemas
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ForwardEtlMetadata:
        """Deserializes the ForwardEtlMetadata from a dictionary."""
        return cls(
            databases=_repeated_dict(d, "databases", ForwardEtlDatabase),
            schemas=_repeated_dict(d, "schemas", ForwardEtlSchema),
        )


@dataclass
class ForwardEtlSchema:
    """Schema metadata"""

    name: Optional[str] = None
    """Schema name."""

    oid: Optional[int] = None
    """PostgreSQL schema OID."""

    def as_dict(self) -> dict:
        """Serializes the ForwardEtlSchema into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.oid is not None:
            body["oid"] = self.oid
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ForwardEtlSchema into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.oid is not None:
            body["oid"] = self.oid
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ForwardEtlSchema:
        """Deserializes the ForwardEtlSchema from a dictionary."""
        return cls(name=d.get("name", None), oid=d.get("oid", None))


@dataclass
class ForwardEtlStatus:
    """Forward ETL status response"""

    configurations: Optional[List[ForwardEtlConfig]] = None
    """List of Forward ETL configurations."""

    table_mappings: Optional[List[ForwardEtlTableMapping]] = None
    """Per-table replication mappings."""

    def as_dict(self) -> dict:
        """Serializes the ForwardEtlStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.configurations:
            body["configurations"] = [v.as_dict() for v in self.configurations]
        if self.table_mappings:
            body["table_mappings"] = [v.as_dict() for v in self.table_mappings]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ForwardEtlStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.configurations:
            body["configurations"] = self.configurations
        if self.table_mappings:
            body["table_mappings"] = self.table_mappings
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ForwardEtlStatus:
        """Deserializes the ForwardEtlStatus from a dictionary."""
        return cls(
            configurations=_repeated_dict(d, "configurations", ForwardEtlConfig),
            table_mappings=_repeated_dict(d, "table_mappings", ForwardEtlTableMapping),
        )


@dataclass
class ForwardEtlTableMapping:
    """Per-table replication mapping"""

    enabled: Optional[bool] = None
    """Whether replication is enabled for this table."""

    last_synced_lsn: Optional[str] = None
    """Last synced LSN (Log Sequence Number) for this table."""

    pg_table_name: Optional[str] = None
    """PostgreSQL table name."""

    pg_table_oid: Optional[int] = None
    """PostgreSQL table OID."""

    uc_table_id: Optional[str] = None
    """Unity Catalog table ID."""

    uc_table_name: Optional[str] = None
    """Unity Catalog table name."""

    def as_dict(self) -> dict:
        """Serializes the ForwardEtlTableMapping into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.enabled is not None:
            body["enabled"] = self.enabled
        if self.last_synced_lsn is not None:
            body["last_synced_lsn"] = self.last_synced_lsn
        if self.pg_table_name is not None:
            body["pg_table_name"] = self.pg_table_name
        if self.pg_table_oid is not None:
            body["pg_table_oid"] = self.pg_table_oid
        if self.uc_table_id is not None:
            body["uc_table_id"] = self.uc_table_id
        if self.uc_table_name is not None:
            body["uc_table_name"] = self.uc_table_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ForwardEtlTableMapping into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.enabled is not None:
            body["enabled"] = self.enabled
        if self.last_synced_lsn is not None:
            body["last_synced_lsn"] = self.last_synced_lsn
        if self.pg_table_name is not None:
            body["pg_table_name"] = self.pg_table_name
        if self.pg_table_oid is not None:
            body["pg_table_oid"] = self.pg_table_oid
        if self.uc_table_id is not None:
            body["uc_table_id"] = self.uc_table_id
        if self.uc_table_name is not None:
            body["uc_table_name"] = self.uc_table_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ForwardEtlTableMapping:
        """Deserializes the ForwardEtlTableMapping from a dictionary."""
        return cls(
            enabled=d.get("enabled", None),
            last_synced_lsn=d.get("last_synced_lsn", None),
            pg_table_name=d.get("pg_table_name", None),
            pg_table_oid=d.get("pg_table_oid", None),
            uc_table_id=d.get("uc_table_id", None),
            uc_table_name=d.get("uc_table_name", None),
        )


@dataclass
class InitialBranchSpec:
    """Configuration for the initial default branch created during project creation."""

    is_protected: Optional[bool] = None
    """Whether the initial default branch should be protected from deletion."""

    def as_dict(self) -> dict:
        """Serializes the InitialBranchSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.is_protected is not None:
            body["is_protected"] = self.is_protected
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the InitialBranchSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.is_protected is not None:
            body["is_protected"] = self.is_protected
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> InitialBranchSpec:
        """Deserializes the InitialBranchSpec from a dictionary."""
        return cls(is_protected=d.get("is_protected", None))


@dataclass
class InitialDatabaseSpec:
    """Configuration for the initial Postgres database created inside the initial branch for a newly
    created project. If omitted, the initial branch still gets an initial database with name
    ``databricks_postgres``. The initial database is always owned by the initial Postgres role
    (whether caller-provided via ``initial_role_spec`` or defaulted to the caller's identity)."""

    postgres_database: Optional[str] = None
    """The name of the Postgres database.
    
    This expects a valid Postgres identifier as specified in the link below.
    https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS"""

    def as_dict(self) -> dict:
        """Serializes the InitialDatabaseSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.postgres_database is not None:
            body["postgres_database"] = self.postgres_database
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the InitialDatabaseSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.postgres_database is not None:
            body["postgres_database"] = self.postgres_database
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> InitialDatabaseSpec:
        """Deserializes the InitialDatabaseSpec from a dictionary."""
        return cls(postgres_database=d.get("postgres_database", None))


@dataclass
class InitialEndpointSpec:
    """Configuration for the initial Read/Write endpoint created during project creation."""

    autoscaling_limit_max_cu: Optional[float] = None
    """The maximum number of Compute Units for the initial endpoint."""

    autoscaling_limit_min_cu: Optional[float] = None
    """The minimum number of Compute Units for the initial endpoint."""

    group: Optional[EndpointGroupSpec] = None
    """Settings for HA configuration of the endpoint."""

    no_suspension: Optional[bool] = None
    """When set to true, explicitly disables automatic suspension (never suspend). Should be set to
    true when provided. Mutually exclusive with ``suspend_timeout_duration``."""

    suspend_timeout_duration: Optional[Duration] = None
    """Duration of inactivity after which the initial endpoint is automatically suspended. If
    specified, should be between 60s and 604800s (1 minute to 1 week). Mutually exclusive with
    ``no_suspension``."""

    def as_dict(self) -> dict:
        """Serializes the InitialEndpointSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.autoscaling_limit_max_cu is not None:
            body["autoscaling_limit_max_cu"] = self.autoscaling_limit_max_cu
        if self.autoscaling_limit_min_cu is not None:
            body["autoscaling_limit_min_cu"] = self.autoscaling_limit_min_cu
        if self.group:
            body["group"] = self.group.as_dict()
        if self.no_suspension is not None:
            body["no_suspension"] = self.no_suspension
        if self.suspend_timeout_duration is not None:
            body["suspend_timeout_duration"] = self.suspend_timeout_duration.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the InitialEndpointSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.autoscaling_limit_max_cu is not None:
            body["autoscaling_limit_max_cu"] = self.autoscaling_limit_max_cu
        if self.autoscaling_limit_min_cu is not None:
            body["autoscaling_limit_min_cu"] = self.autoscaling_limit_min_cu
        if self.group:
            body["group"] = self.group
        if self.no_suspension is not None:
            body["no_suspension"] = self.no_suspension
        if self.suspend_timeout_duration is not None:
            body["suspend_timeout_duration"] = self.suspend_timeout_duration
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> InitialEndpointSpec:
        """Deserializes the InitialEndpointSpec from a dictionary."""
        return cls(
            autoscaling_limit_max_cu=d.get("autoscaling_limit_max_cu", None),
            autoscaling_limit_min_cu=d.get("autoscaling_limit_min_cu", None),
            group=_from_dict(d, "group", EndpointGroupSpec),
            no_suspension=d.get("no_suspension", None),
            suspend_timeout_duration=_duration(d, "suspend_timeout_duration"),
        )


@dataclass
class InitialRoleSpec:
    """Configuration for the initial Postgres role created inside the initial branch for a newly
    created project. If omitted, the default branch still gets an initial Postgres role
    corresponding to the caller of the API endpoint."""

    attributes: Optional[RoleAttributes] = None
    """The desired API-exposed Postgres role attribute to associate with the role. Optional."""

    auth_method: Optional[RoleAuthMethod] = None
    """Controls how the Postgres role authenticates when a client opens a database connection.
    Supported values:
    
    - LAKEBASE_OAUTH_V1: the role authenticates by presenting a Databricks OAuth access token
      derived from the backing managed identity (the Databricks user, service principal, or group
      named by the role's ``postgres_role``). No static password exists for roles using this method.
    - PG_PASSWORD_SCRAM_SHA_256: the role authenticates with a Postgres password verified
      server-side using the SCRAM-SHA-256 mechanism. Lakebase generates a password for the role.
    - NO_LOGIN: the role cannot open a Postgres session at all. Useful for roles that exist only to
      own objects or to aggregate privileges that are then granted to other, loginable roles.
    
    If auth_method is left unspecified, a meaningful authentication method is derived from the
    identity_type:
    
    - For the managed identities, OAUTH is used.
    - For the regular postgres roles, authentication based on postgres passwords is used.
    
    NOTE: for the Databricks identity type GROUP, LAKEBASE_OAUTH_V1 is the default auth method
    (group can login as well)."""

    identity_type: Optional[RoleIdentityType] = None
    """The type of role. When specifying a managed-identity, the chosen role_id must be a valid:
    
    - application ID for SERVICE_PRINCIPAL
    - user email for USER
    - group name for GROUP"""

    membership_roles: Optional[List[RoleMembershipRole]] = None
    """An enum value for a standard role that this role is a member of."""

    postgres_role: Optional[str] = None
    """The name of the Postgres role.
    
    This expects a valid Postgres identifier as specified in the link below.
    https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS
    
    If you wish to create a Postgres Role backed by a managed Databricks identity, then
    postgres_role must be one of the following:
    
    1. user email for IdentityType.USER
    2. app ID for IdentityType.SERVICE_PRINCIPAL
    3. group name for IdentityType.GROUP"""

    def as_dict(self) -> dict:
        """Serializes the InitialRoleSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.attributes:
            body["attributes"] = self.attributes.as_dict()
        if self.auth_method is not None:
            body["auth_method"] = self.auth_method.value
        if self.identity_type is not None:
            body["identity_type"] = self.identity_type.value
        if self.membership_roles:
            body["membership_roles"] = [v.value for v in self.membership_roles]
        if self.postgres_role is not None:
            body["postgres_role"] = self.postgres_role
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the InitialRoleSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.attributes:
            body["attributes"] = self.attributes
        if self.auth_method is not None:
            body["auth_method"] = self.auth_method
        if self.identity_type is not None:
            body["identity_type"] = self.identity_type
        if self.membership_roles:
            body["membership_roles"] = self.membership_roles
        if self.postgres_role is not None:
            body["postgres_role"] = self.postgres_role
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> InitialRoleSpec:
        """Deserializes the InitialRoleSpec from a dictionary."""
        return cls(
            attributes=_from_dict(d, "attributes", RoleAttributes),
            auth_method=_enum(d, "auth_method", RoleAuthMethod),
            identity_type=_enum(d, "identity_type", RoleIdentityType),
            membership_roles=_repeated_enum(d, "membership_roles", RoleMembershipRole),
            postgres_role=d.get("postgres_role", None),
        )


@dataclass
class ListBranchesResponse:
    branches: Optional[List[Branch]] = None
    """List of branches in the project."""

    next_page_token: Optional[str] = None
    """Token to request the next page of branches."""

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
class ListCdfConfigsResponse:
    """Response to a ListCdfConfigs request, containing a page of CdfConfigs and a token for fetching
    the next page."""

    cdf_configs: Optional[List[CdfConfig]] = None
    """The CdfConfigs under the parent database."""

    next_page_token: Optional[str] = None
    """Token to retrieve the next page of results; empty when there are no more."""

    def as_dict(self) -> dict:
        """Serializes the ListCdfConfigsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.cdf_configs:
            body["cdf_configs"] = [v.as_dict() for v in self.cdf_configs]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListCdfConfigsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.cdf_configs:
            body["cdf_configs"] = self.cdf_configs
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListCdfConfigsResponse:
        """Deserializes the ListCdfConfigsResponse from a dictionary."""
        return cls(
            cdf_configs=_repeated_dict(d, "cdf_configs", CdfConfig), next_page_token=d.get("next_page_token", None)
        )


@dataclass
class ListCdfStatusesResponse:
    """Response to a ListCdfStatuses request, containing a page of replicated table statuses and a
    token for fetching the next page."""

    cdf_statuses: Optional[List[CdfStatus]] = None
    """The replicated tables under the parent CdfConfig."""

    next_page_token: Optional[str] = None
    """Token to retrieve the next page of results; empty when there are no more."""

    def as_dict(self) -> dict:
        """Serializes the ListCdfStatusesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.cdf_statuses:
            body["cdf_statuses"] = [v.as_dict() for v in self.cdf_statuses]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListCdfStatusesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.cdf_statuses:
            body["cdf_statuses"] = self.cdf_statuses
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListCdfStatusesResponse:
        """Deserializes the ListCdfStatusesResponse from a dictionary."""
        return cls(
            cdf_statuses=_repeated_dict(d, "cdf_statuses", CdfStatus), next_page_token=d.get("next_page_token", None)
        )


@dataclass
class ListComputeInstancesResponse:
    compute_instances: Optional[List[ComputeInstance]] = None
    """The compute instances from the specified endpoint."""

    next_page_token: Optional[str] = None
    """A token, which can be sent as ``page_token`` to retrieve the next page. If this field is
    omitted, there are no subsequent pages."""

    def as_dict(self) -> dict:
        """Serializes the ListComputeInstancesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.compute_instances:
            body["compute_instances"] = [v.as_dict() for v in self.compute_instances]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListComputeInstancesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.compute_instances:
            body["compute_instances"] = self.compute_instances
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListComputeInstancesResponse:
        """Deserializes the ListComputeInstancesResponse from a dictionary."""
        return cls(
            compute_instances=_repeated_dict(d, "compute_instances", ComputeInstance),
            next_page_token=d.get("next_page_token", None),
        )


@dataclass
class ListDatabasesResponse:
    databases: Optional[List[Database]] = None
    """List of databases."""

    next_page_token: Optional[str] = None
    """Pagination token to request the next page of databases."""

    def as_dict(self) -> dict:
        """Serializes the ListDatabasesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.databases:
            body["databases"] = [v.as_dict() for v in self.databases]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListDatabasesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.databases:
            body["databases"] = self.databases
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListDatabasesResponse:
        """Deserializes the ListDatabasesResponse from a dictionary."""
        return cls(databases=_repeated_dict(d, "databases", Database), next_page_token=d.get("next_page_token", None))


@dataclass
class ListEndpointsResponse:
    endpoints: Optional[List[Endpoint]] = None
    """List of compute endpoints in the branch."""

    next_page_token: Optional[str] = None
    """Token to request the next page of compute endpoints."""

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
    """Token to request the next page of projects."""

    projects: Optional[List[Project]] = None
    """List of all projects in the workspace that the user has permission to access."""

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
class ListRecoveryBranchPreviewsResponse:
    next_page_token: Optional[str] = None

    recovery_branch_previews: Optional[List[RecoveryBranchPreview]] = None

    def as_dict(self) -> dict:
        """Serializes the ListRecoveryBranchPreviewsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.recovery_branch_previews:
            body["recovery_branch_previews"] = [v.as_dict() for v in self.recovery_branch_previews]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListRecoveryBranchPreviewsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.recovery_branch_previews:
            body["recovery_branch_previews"] = self.recovery_branch_previews
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListRecoveryBranchPreviewsResponse:
        """Deserializes the ListRecoveryBranchPreviewsResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            recovery_branch_previews=_repeated_dict(d, "recovery_branch_previews", RecoveryBranchPreview),
        )


@dataclass
class ListReplicationGroupPreviewsResponse:
    next_page_token: Optional[str] = None

    replication_group_previews: Optional[List[ReplicationGroupPreview]] = None

    def as_dict(self) -> dict:
        """Serializes the ListReplicationGroupPreviewsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.replication_group_previews:
            body["replication_group_previews"] = [v.as_dict() for v in self.replication_group_previews]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListReplicationGroupPreviewsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.replication_group_previews:
            body["replication_group_previews"] = self.replication_group_previews
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListReplicationGroupPreviewsResponse:
        """Deserializes the ListReplicationGroupPreviewsResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            replication_group_previews=_repeated_dict(d, "replication_group_previews", ReplicationGroupPreview),
        )


@dataclass
class ListRolesResponse:
    next_page_token: Optional[str] = None
    """Token to request the next page of Postgres roles."""

    roles: Optional[List[Role]] = None
    """List of Postgres roles in the branch."""

    def as_dict(self) -> dict:
        """Serializes the ListRolesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.roles:
            body["roles"] = [v.as_dict() for v in self.roles]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListRolesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.roles:
            body["roles"] = self.roles
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListRolesResponse:
        """Deserializes the ListRolesResponse from a dictionary."""
        return cls(next_page_token=d.get("next_page_token", None), roles=_repeated_dict(d, "roles", Role))


@dataclass
class ListSnapshotsResponse:
    next_page_token: Optional[str] = None
    """Token to retrieve the next page; empty if there are no more pages."""

    snapshots: Optional[List[Snapshot]] = None
    """The snapshots in the project."""

    def as_dict(self) -> dict:
        """Serializes the ListSnapshotsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.snapshots:
            body["snapshots"] = [v.as_dict() for v in self.snapshots]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListSnapshotsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.snapshots:
            body["snapshots"] = self.snapshots
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListSnapshotsResponse:
        """Deserializes the ListSnapshotsResponse from a dictionary."""
        return cls(next_page_token=d.get("next_page_token", None), snapshots=_repeated_dict(d, "snapshots", Snapshot))


@dataclass
class MonthlySchedule:
    """Take a snapshot once per month, on the configured day at the configured hour."""

    day: int
    """The day of the month on which to take the snapshot, in [1, 31]. In shorter months the snapshot
    is taken on the last day instead (day 31 runs on Feb 28 or 29, and on Apr 30), so every month
    gets exactly one snapshot."""

    hour: Optional[int] = None
    """The hour of the day, in UTC, at which to take the snapshot, in [0, 23]."""

    def as_dict(self) -> dict:
        """Serializes the MonthlySchedule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.day is not None:
            body["day"] = self.day
        if self.hour is not None:
            body["hour"] = self.hour
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the MonthlySchedule into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.day is not None:
            body["day"] = self.day
        if self.hour is not None:
            body["hour"] = self.hour
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> MonthlySchedule:
        """Deserializes the MonthlySchedule from a dictionary."""
        return cls(day=d.get("day", None), hour=d.get("hour", None))


@dataclass
class NewPipelineSpec:
    budget_policy_id: Optional[str] = None
    """Budget policy to set on the newly created pipeline."""

    pipeline_channel: Optional[NewPipelineSpecPipelineChannel] = None
    """Release channel of the underlying pipeline's runtime. Some source table configurations (e.g.,
    read-time CDF) require PREVIEW. Defaults to CURRENT if not specified."""

    storage_catalog: Optional[str] = None
    """UC catalog for the pipeline to store intermediate files (checkpoints, event logs etc). This
    needs to be a standard catalog where the user has permissions to create Delta tables."""

    storage_schema: Optional[str] = None
    """UC schema for the pipeline to store intermediate files (checkpoints, event logs etc). This needs
    to be in the standard catalog where the user has permissions to create Delta tables."""

    def as_dict(self) -> dict:
        """Serializes the NewPipelineSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.budget_policy_id is not None:
            body["budget_policy_id"] = self.budget_policy_id
        if self.pipeline_channel is not None:
            body["pipeline_channel"] = self.pipeline_channel.value
        if self.storage_catalog is not None:
            body["storage_catalog"] = self.storage_catalog
        if self.storage_schema is not None:
            body["storage_schema"] = self.storage_schema
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the NewPipelineSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.budget_policy_id is not None:
            body["budget_policy_id"] = self.budget_policy_id
        if self.pipeline_channel is not None:
            body["pipeline_channel"] = self.pipeline_channel
        if self.storage_catalog is not None:
            body["storage_catalog"] = self.storage_catalog
        if self.storage_schema is not None:
            body["storage_schema"] = self.storage_schema
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> NewPipelineSpec:
        """Deserializes the NewPipelineSpec from a dictionary."""
        return cls(
            budget_policy_id=d.get("budget_policy_id", None),
            pipeline_channel=_enum(d, "pipeline_channel", NewPipelineSpecPipelineChannel),
            storage_catalog=d.get("storage_catalog", None),
            storage_schema=d.get("storage_schema", None),
        )


class NewPipelineSpecPipelineChannel(Enum):
    """Release channel of the underlying pipeline's runtime. PREVIEW provides early access to the
    latest features but may be less stable. Some source table configurations (e.g., read-time CDF)
    require PREVIEW. Defaults to CURRENT if not specified."""

    CURRENT = "CURRENT"
    PREVIEW = "PREVIEW"


class OpenApiMode(Enum):
    """Controls how the Data API exposes the OpenAPI documentation endpoint. Only IGNORE_PRIVILEGES and
    DISABLED are supported today; "follow-privileges" is not implemented yet (it may be added later
    as value 3 — adding new enum values is backward-compatible)."""

    OPEN_API_MODE_DISABLED = "OPEN_API_MODE_DISABLED"
    OPEN_API_MODE_IGNORE_PRIVILEGES = "OPEN_API_MODE_IGNORE_PRIVILEGES"


@dataclass
class Operation:
    """This resource represents a long-running operation that is the result of a network API call."""

    done: Optional[bool] = None
    """If the value is ``false``, it means the operation is still in progress. If ``true``, the
    operation is completed, and either ``error`` or ``response`` is available."""

    error: Optional[DatabricksServiceExceptionWithDetailsProto] = None
    """The error result of the operation in case of failure or cancellation."""

    metadata: Optional[dict] = None
    """Service-specific metadata associated with the operation. It typically contains progress
    information and common metadata such as create time. Some services might not provide such
    metadata."""

    name: Optional[str] = None
    """The server-assigned name, which is only unique within the same service that originally returns
    it. If you use the default HTTP mapping, the ``name`` should be a resource name ending with
    ``operations/{unique_id}``."""

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
    create_time: Optional[Timestamp] = None
    """A timestamp indicating when the project was created."""

    delete_time: Optional[Timestamp] = None
    """A timestamp indicating when the project was soft-deleted. Empty if the project is not deleted,
    otherwise set to a timestamp in the past."""

    initial_branch_spec: Optional[InitialBranchSpec] = None
    """Configuration for the initial default branch created as part of project creation. Allows
    overriding branch protection. These settings only apply at creation time and do not affect
    resources created after project creation."""

    initial_database_spec: Optional[InitialDatabaseSpec] = None
    """Configuration for the initial Postgres database created inside the initial branch for this
    project. If omitted, the initial branch still gets an initial database with name
    ``databricks_postgres``. The initial database is always owned by the initial role
    (caller-provided via ``initial_role_spec`` or defaulted to the caller's identity). This field is
    input-only; to change databases after project creation, use the standalone Database API."""

    initial_endpoint_spec: Optional[InitialEndpointSpec] = None
    """Configuration settings for the initial Read/Write endpoint created inside the initial branch for
    a newly created project. If omitted, the initial endpoint created will have default settings,
    without high availability configured. This field does not apply to any endpoints created after
    project creation. Use spec.default_endpoint_settings to configure default settings for endpoints
    created after project creation."""

    initial_role_spec: Optional[InitialRoleSpec] = None
    """Configuration for the initial Postgres role created inside the initial branch for this project.
    If omitted, the initial branch gets an initial role corresponding to the caller of the API
    endpoint. This field is input-only; to change roles after project creation, use the standalone
    Role API."""

    name: Optional[str] = None
    """Output only. The full resource path of the project. Format: projects/{project_id}"""

    project_id: Optional[str] = None
    """The part of the name, chosen by the user when the resource was created."""

    purge_time: Optional[Timestamp] = None
    """A timestamp indicating when the project is scheduled for permanent deletion. Empty if the
    project is not deleted, otherwise set to a timestamp in the future."""

    spec: Optional[ProjectSpec] = None
    """The spec contains the project configuration, including display_name, pg_version (Postgres
    version), history_retention_duration, and default_endpoint_settings."""

    status: Optional[ProjectStatus] = None
    """The current status of a Project."""

    uid: Optional[str] = None
    """System-generated unique ID for the project."""

    update_time: Optional[Timestamp] = None
    """A timestamp indicating when the project was last updated."""

    def as_dict(self) -> dict:
        """Serializes the Project into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.delete_time is not None:
            body["delete_time"] = self.delete_time.ToJsonString()
        if self.initial_branch_spec:
            body["initial_branch_spec"] = self.initial_branch_spec.as_dict()
        if self.initial_database_spec:
            body["initial_database_spec"] = self.initial_database_spec.as_dict()
        if self.initial_endpoint_spec:
            body["initial_endpoint_spec"] = self.initial_endpoint_spec.as_dict()
        if self.initial_role_spec:
            body["initial_role_spec"] = self.initial_role_spec.as_dict()
        if self.name is not None:
            body["name"] = self.name
        if self.project_id is not None:
            body["project_id"] = self.project_id
        if self.purge_time is not None:
            body["purge_time"] = self.purge_time.ToJsonString()
        if self.spec:
            body["spec"] = self.spec.as_dict()
        if self.status:
            body["status"] = self.status.as_dict()
        if self.uid is not None:
            body["uid"] = self.uid
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Project into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.delete_time is not None:
            body["delete_time"] = self.delete_time
        if self.initial_branch_spec:
            body["initial_branch_spec"] = self.initial_branch_spec
        if self.initial_database_spec:
            body["initial_database_spec"] = self.initial_database_spec
        if self.initial_endpoint_spec:
            body["initial_endpoint_spec"] = self.initial_endpoint_spec
        if self.initial_role_spec:
            body["initial_role_spec"] = self.initial_role_spec
        if self.name is not None:
            body["name"] = self.name
        if self.project_id is not None:
            body["project_id"] = self.project_id
        if self.purge_time is not None:
            body["purge_time"] = self.purge_time
        if self.spec:
            body["spec"] = self.spec
        if self.status:
            body["status"] = self.status
        if self.uid is not None:
            body["uid"] = self.uid
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Project:
        """Deserializes the Project from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            delete_time=_timestamp(d, "delete_time"),
            initial_branch_spec=_from_dict(d, "initial_branch_spec", InitialBranchSpec),
            initial_database_spec=_from_dict(d, "initial_database_spec", InitialDatabaseSpec),
            initial_endpoint_spec=_from_dict(d, "initial_endpoint_spec", InitialEndpointSpec),
            initial_role_spec=_from_dict(d, "initial_role_spec", InitialRoleSpec),
            name=d.get("name", None),
            project_id=d.get("project_id", None),
            purge_time=_timestamp(d, "purge_time"),
            spec=_from_dict(d, "spec", ProjectSpec),
            status=_from_dict(d, "status", ProjectStatus),
            uid=d.get("uid", None),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class ProjectCustomTag:
    key: Optional[str] = None
    """The key of the custom tag."""

    value: Optional[str] = None
    """The value of the custom tag."""

    def as_dict(self) -> dict:
        """Serializes the ProjectCustomTag into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.key is not None:
            body["key"] = self.key
        if self.value is not None:
            body["value"] = self.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ProjectCustomTag into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.key is not None:
            body["key"] = self.key
        if self.value is not None:
            body["value"] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ProjectCustomTag:
        """Deserializes the ProjectCustomTag from a dictionary."""
        return cls(key=d.get("key", None), value=d.get("value", None))


@dataclass
class ProjectDefaultEndpointSettings:
    """A collection of settings for a compute endpoint."""

    autoscaling_limit_max_cu: Optional[float] = None
    """The maximum number of Compute Units. Minimum value is 0.5."""

    autoscaling_limit_min_cu: Optional[float] = None
    """The minimum number of Compute Units. Minimum value is 0.5."""

    no_suspension: Optional[bool] = None
    """When set to true, explicitly disables automatic suspension (never suspend). Should be set to
    true when provided. Mutually exclusive with ``suspend_timeout_duration``. When updating, use
    ``spec.project_default_settings.suspension`` in the update_mask."""

    pg_settings: Optional[Dict[str, str]] = None
    """A raw representation of Postgres settings."""

    suspend_timeout_duration: Optional[Duration] = None
    """Duration of inactivity after which the compute endpoint is automatically suspended. If specified
    should be between 60s and 604800s (1 minute to 1 week). Mutually exclusive with
    ``no_suspension``. When updating, use ``spec.project_default_settings.suspension`` in the
    update_mask."""

    def as_dict(self) -> dict:
        """Serializes the ProjectDefaultEndpointSettings into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.autoscaling_limit_max_cu is not None:
            body["autoscaling_limit_max_cu"] = self.autoscaling_limit_max_cu
        if self.autoscaling_limit_min_cu is not None:
            body["autoscaling_limit_min_cu"] = self.autoscaling_limit_min_cu
        if self.no_suspension is not None:
            body["no_suspension"] = self.no_suspension
        if self.pg_settings:
            body["pg_settings"] = self.pg_settings
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
        if self.no_suspension is not None:
            body["no_suspension"] = self.no_suspension
        if self.pg_settings:
            body["pg_settings"] = self.pg_settings
        if self.suspend_timeout_duration is not None:
            body["suspend_timeout_duration"] = self.suspend_timeout_duration
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ProjectDefaultEndpointSettings:
        """Deserializes the ProjectDefaultEndpointSettings from a dictionary."""
        return cls(
            autoscaling_limit_max_cu=d.get("autoscaling_limit_max_cu", None),
            autoscaling_limit_min_cu=d.get("autoscaling_limit_min_cu", None),
            no_suspension=d.get("no_suspension", None),
            pg_settings=d.get("pg_settings", None),
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
class ProjectSpec:
    budget_policy_id: Optional[str] = None
    """The desired budget policy to associate with the project. See status.budget_policy_id for the
    policy that is actually applied to the project."""

    compute_provisioner: Optional[str] = None
    """The compute provisioner used to provision endpoints in this project. Overrides the default
    provisioner when set."""

    custom_tags: Optional[List[ProjectCustomTag]] = None
    """Custom tags to associate with the project. Forwarded to LBM for billing and cost tracking. To
    update tags, provide the new tag list and include "spec.custom_tags" in the update_mask. To
    clear all tags, provide an empty list and include "spec.custom_tags" in the update_mask. To
    preserve existing tags, omit this field from the update_mask (or use wildcard "*" which
    auto-excludes empty tags)."""

    default_branch: Optional[str] = None
    """The full resource path for the default branch of the project Format:
    projects/{project_id}/branches/{branch_id}"""

    default_endpoint_settings: Optional[ProjectDefaultEndpointSettings] = None

    display_name: Optional[str] = None
    """Human-readable project name. Length should be between 1 and 256 characters."""

    enable_pg_native_login: Optional[bool] = None
    """Whether to enable PG native password login on all endpoints in this project. Defaults to false."""

    history_retention_duration: Optional[Duration] = None
    """The number of seconds to retain the shared history for point in time recovery for all branches
    in this project. Value should be between 172800s (2 days) and 3024000s (35 days)."""

    pg_version: Optional[int] = None
    """The major Postgres version number. The set of supported versions may vary; consult the API
    documentation for currently accepted values."""

    def as_dict(self) -> dict:
        """Serializes the ProjectSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.budget_policy_id is not None:
            body["budget_policy_id"] = self.budget_policy_id
        if self.compute_provisioner is not None:
            body["compute_provisioner"] = self.compute_provisioner
        if self.custom_tags:
            body["custom_tags"] = [v.as_dict() for v in self.custom_tags]
        if self.default_branch is not None:
            body["default_branch"] = self.default_branch
        if self.default_endpoint_settings:
            body["default_endpoint_settings"] = self.default_endpoint_settings.as_dict()
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.enable_pg_native_login is not None:
            body["enable_pg_native_login"] = self.enable_pg_native_login
        if self.history_retention_duration is not None:
            body["history_retention_duration"] = self.history_retention_duration.ToJsonString()
        if self.pg_version is not None:
            body["pg_version"] = self.pg_version
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ProjectSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.budget_policy_id is not None:
            body["budget_policy_id"] = self.budget_policy_id
        if self.compute_provisioner is not None:
            body["compute_provisioner"] = self.compute_provisioner
        if self.custom_tags:
            body["custom_tags"] = self.custom_tags
        if self.default_branch is not None:
            body["default_branch"] = self.default_branch
        if self.default_endpoint_settings:
            body["default_endpoint_settings"] = self.default_endpoint_settings
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.enable_pg_native_login is not None:
            body["enable_pg_native_login"] = self.enable_pg_native_login
        if self.history_retention_duration is not None:
            body["history_retention_duration"] = self.history_retention_duration
        if self.pg_version is not None:
            body["pg_version"] = self.pg_version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ProjectSpec:
        """Deserializes the ProjectSpec from a dictionary."""
        return cls(
            budget_policy_id=d.get("budget_policy_id", None),
            compute_provisioner=d.get("compute_provisioner", None),
            custom_tags=_repeated_dict(d, "custom_tags", ProjectCustomTag),
            default_branch=d.get("default_branch", None),
            default_endpoint_settings=_from_dict(d, "default_endpoint_settings", ProjectDefaultEndpointSettings),
            display_name=d.get("display_name", None),
            enable_pg_native_login=d.get("enable_pg_native_login", None),
            history_retention_duration=_duration(d, "history_retention_duration"),
            pg_version=d.get("pg_version", None),
        )


@dataclass
class ProjectStatus:
    branch_logical_size_limit_bytes: Optional[int] = None
    """The logical size limit for a branch."""

    budget_policy_id: Optional[str] = None
    """The budget policy that is applied to the project."""

    compute_last_active_time: Optional[Timestamp] = None
    """The most recent time when any endpoint of this project was active."""

    compute_provisioner: Optional[str] = None
    """The effective compute provisioner backing this project's endpoints."""

    custom_tags: Optional[List[ProjectCustomTag]] = None
    """The effective custom tags associated with the project."""

    default_branch: Optional[str] = None
    """The full resource path of the default branch of the project"""

    default_endpoint_settings: Optional[ProjectDefaultEndpointSettings] = None
    """The effective default endpoint settings."""

    display_name: Optional[str] = None
    """The effective human-readable project name."""

    enable_pg_native_login: Optional[bool] = None
    """Whether to enable PG native password login on all endpoints in this project."""

    history_retention_duration: Optional[Duration] = None
    """The effective number of seconds to retain the shared history for point in time recovery."""

    owner: Optional[str] = None
    """The email of the project owner."""

    pg_version: Optional[int] = None
    """The effective major Postgres version number."""

    project_id: Optional[str] = None
    """Part of the resource name."""

    replication_role: Optional[ReplicationRolePreview] = None
    """The replication role of the project in this workspace. Populated only when cross-workspace
    replication is configured."""

    synthetic_storage_size_bytes: Optional[int] = None
    """The current space occupied by the project in storage."""

    def as_dict(self) -> dict:
        """Serializes the ProjectStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.branch_logical_size_limit_bytes is not None:
            body["branch_logical_size_limit_bytes"] = self.branch_logical_size_limit_bytes
        if self.budget_policy_id is not None:
            body["budget_policy_id"] = self.budget_policy_id
        if self.compute_last_active_time is not None:
            body["compute_last_active_time"] = self.compute_last_active_time.ToJsonString()
        if self.compute_provisioner is not None:
            body["compute_provisioner"] = self.compute_provisioner
        if self.custom_tags:
            body["custom_tags"] = [v.as_dict() for v in self.custom_tags]
        if self.default_branch is not None:
            body["default_branch"] = self.default_branch
        if self.default_endpoint_settings:
            body["default_endpoint_settings"] = self.default_endpoint_settings.as_dict()
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.enable_pg_native_login is not None:
            body["enable_pg_native_login"] = self.enable_pg_native_login
        if self.history_retention_duration is not None:
            body["history_retention_duration"] = self.history_retention_duration.ToJsonString()
        if self.owner is not None:
            body["owner"] = self.owner
        if self.pg_version is not None:
            body["pg_version"] = self.pg_version
        if self.project_id is not None:
            body["project_id"] = self.project_id
        if self.replication_role is not None:
            body["replication_role"] = self.replication_role.value
        if self.synthetic_storage_size_bytes is not None:
            body["synthetic_storage_size_bytes"] = self.synthetic_storage_size_bytes
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ProjectStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.branch_logical_size_limit_bytes is not None:
            body["branch_logical_size_limit_bytes"] = self.branch_logical_size_limit_bytes
        if self.budget_policy_id is not None:
            body["budget_policy_id"] = self.budget_policy_id
        if self.compute_last_active_time is not None:
            body["compute_last_active_time"] = self.compute_last_active_time
        if self.compute_provisioner is not None:
            body["compute_provisioner"] = self.compute_provisioner
        if self.custom_tags:
            body["custom_tags"] = self.custom_tags
        if self.default_branch is not None:
            body["default_branch"] = self.default_branch
        if self.default_endpoint_settings:
            body["default_endpoint_settings"] = self.default_endpoint_settings
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.enable_pg_native_login is not None:
            body["enable_pg_native_login"] = self.enable_pg_native_login
        if self.history_retention_duration is not None:
            body["history_retention_duration"] = self.history_retention_duration
        if self.owner is not None:
            body["owner"] = self.owner
        if self.pg_version is not None:
            body["pg_version"] = self.pg_version
        if self.project_id is not None:
            body["project_id"] = self.project_id
        if self.replication_role is not None:
            body["replication_role"] = self.replication_role
        if self.synthetic_storage_size_bytes is not None:
            body["synthetic_storage_size_bytes"] = self.synthetic_storage_size_bytes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ProjectStatus:
        """Deserializes the ProjectStatus from a dictionary."""
        return cls(
            branch_logical_size_limit_bytes=d.get("branch_logical_size_limit_bytes", None),
            budget_policy_id=d.get("budget_policy_id", None),
            compute_last_active_time=_timestamp(d, "compute_last_active_time"),
            compute_provisioner=d.get("compute_provisioner", None),
            custom_tags=_repeated_dict(d, "custom_tags", ProjectCustomTag),
            default_branch=d.get("default_branch", None),
            default_endpoint_settings=_from_dict(d, "default_endpoint_settings", ProjectDefaultEndpointSettings),
            display_name=d.get("display_name", None),
            enable_pg_native_login=d.get("enable_pg_native_login", None),
            history_retention_duration=_duration(d, "history_retention_duration"),
            owner=d.get("owner", None),
            pg_version=d.get("pg_version", None),
            project_id=d.get("project_id", None),
            replication_role=_enum(d, "replication_role", ReplicationRolePreview),
            synthetic_storage_size_bytes=d.get("synthetic_storage_size_bytes", None),
        )


class ProvisioningInfoState(Enum):
    ACTIVE = "ACTIVE"
    DEGRADED = "DEGRADED"
    DELETING = "DELETING"
    FAILED = "FAILED"
    PROVISIONING = "PROVISIONING"
    UPDATING = "UPDATING"


class ProvisioningPhase(Enum):
    """The current phase of the data synchronization pipeline."""

    PROVISIONING_PHASE_INDEX_SCAN = "PROVISIONING_PHASE_INDEX_SCAN"
    PROVISIONING_PHASE_INDEX_SORT = "PROVISIONING_PHASE_INDEX_SORT"
    PROVISIONING_PHASE_MAIN = "PROVISIONING_PHASE_MAIN"


@dataclass
class RecoveryBranchPreview:
    create_time: Optional[Timestamp] = None

    name: Optional[str] = None
    """The resource name of the recovery branch. Format:
    projects/{project_id}/preview/recovery-branches/{recovery_branch_id}"""

    parent: Optional[str] = None
    """The project containing this recovery branch. Format: projects/{project_id}"""

    status: Optional[RecoveryBranchPreviewStatus] = None

    uid: Optional[str] = None

    update_time: Optional[Timestamp] = None

    def as_dict(self) -> dict:
        """Serializes the RecoveryBranchPreview into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.status:
            body["status"] = self.status.as_dict()
        if self.uid is not None:
            body["uid"] = self.uid
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RecoveryBranchPreview into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.status:
            body["status"] = self.status
        if self.uid is not None:
            body["uid"] = self.uid
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RecoveryBranchPreview:
        """Deserializes the RecoveryBranchPreview from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            name=d.get("name", None),
            parent=d.get("parent", None),
            status=_from_dict(d, "status", RecoveryBranchPreviewStatus),
            uid=d.get("uid", None),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class RecoveryBranchPreviewStatus:
    current_state: Optional[RecoveryBranchPreviewStatusState] = None

    divergent: Optional[bool] = None

    end_lsn: Optional[str] = None
    """The Log Sequence Number (LSN) up to which the recovery branch's timeline holds data."""

    expire_time: Optional[Timestamp] = None

    failover_child_lsn: Optional[str] = None
    """The Log Sequence Number (LSN) at which a local child timeline was branched off this recovery
    branch's timeline during recovery branch creation."""

    home_workspace: Optional[str] = None
    """The workspace that owns the source branch and where reconciliation completes. Format: a
    workspace identifier."""

    is_foreign: Optional[bool] = None

    origin_branch: Optional[str] = None
    """The normal branch from which this recovery branch originated. Format:
    projects/{project_id}/branches/{branch_id}"""

    def as_dict(self) -> dict:
        """Serializes the RecoveryBranchPreviewStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.current_state is not None:
            body["current_state"] = self.current_state.value
        if self.divergent is not None:
            body["divergent"] = self.divergent
        if self.end_lsn is not None:
            body["end_lsn"] = self.end_lsn
        if self.expire_time is not None:
            body["expire_time"] = self.expire_time.ToJsonString()
        if self.failover_child_lsn is not None:
            body["failover_child_lsn"] = self.failover_child_lsn
        if self.home_workspace is not None:
            body["home_workspace"] = self.home_workspace
        if self.is_foreign is not None:
            body["is_foreign"] = self.is_foreign
        if self.origin_branch is not None:
            body["origin_branch"] = self.origin_branch
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RecoveryBranchPreviewStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.current_state is not None:
            body["current_state"] = self.current_state
        if self.divergent is not None:
            body["divergent"] = self.divergent
        if self.end_lsn is not None:
            body["end_lsn"] = self.end_lsn
        if self.expire_time is not None:
            body["expire_time"] = self.expire_time
        if self.failover_child_lsn is not None:
            body["failover_child_lsn"] = self.failover_child_lsn
        if self.home_workspace is not None:
            body["home_workspace"] = self.home_workspace
        if self.is_foreign is not None:
            body["is_foreign"] = self.is_foreign
        if self.origin_branch is not None:
            body["origin_branch"] = self.origin_branch
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RecoveryBranchPreviewStatus:
        """Deserializes the RecoveryBranchPreviewStatus from a dictionary."""
        return cls(
            current_state=_enum(d, "current_state", RecoveryBranchPreviewStatusState),
            divergent=d.get("divergent", None),
            end_lsn=d.get("end_lsn", None),
            expire_time=_timestamp(d, "expire_time"),
            failover_child_lsn=d.get("failover_child_lsn", None),
            home_workspace=d.get("home_workspace", None),
            is_foreign=d.get("is_foreign", None),
            origin_branch=d.get("origin_branch", None),
        )


class RecoveryBranchPreviewStatusState(Enum):
    PENDING_HOME_SYNC = "PENDING_HOME_SYNC"
    READY_FOR_INSPECTION = "READY_FOR_INSPECTION"
    RECONCILED = "RECONCILED"


@dataclass
class ReplicationGroupPreview:
    replication_mode: ReplicationModePreview
    """The selected replication mode."""

    workspaces: List[str]
    """The workspaces participating in this replication group. Phase 1 requires exactly 2 entries."""

    create_time: Optional[Timestamp] = None
    """Server-generated timestamps."""

    etag: Optional[str] = None
    """Optional optimistic concurrency token for update and delete."""

    name: Optional[str] = None
    """The resource name of the replication group. Format:
    projects/{project_id}/preview/replication-groups/{replication_group_id}"""

    observed_metrics: Optional[ReplicationMetricsPreview] = None
    """The latest observed replication metrics for this group."""

    parent: Optional[str] = None
    """The parent project that owns this replication group. Format: projects/{project_id}"""

    primary_workspace: Optional[str] = None
    """The workspace currently serving writes. Server-owned."""

    state: Optional[ReplicationGroupPreviewState] = None
    """The lifecycle state of the replication group."""

    update_time: Optional[Timestamp] = None

    def as_dict(self) -> dict:
        """Serializes the ReplicationGroupPreview into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.etag is not None:
            body["etag"] = self.etag
        if self.name is not None:
            body["name"] = self.name
        if self.observed_metrics:
            body["observed_metrics"] = self.observed_metrics.as_dict()
        if self.parent is not None:
            body["parent"] = self.parent
        if self.primary_workspace is not None:
            body["primary_workspace"] = self.primary_workspace
        if self.replication_mode is not None:
            body["replication_mode"] = self.replication_mode.value
        if self.state is not None:
            body["state"] = self.state.value
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        if self.workspaces:
            body["workspaces"] = [v for v in self.workspaces]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ReplicationGroupPreview into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.etag is not None:
            body["etag"] = self.etag
        if self.name is not None:
            body["name"] = self.name
        if self.observed_metrics:
            body["observed_metrics"] = self.observed_metrics
        if self.parent is not None:
            body["parent"] = self.parent
        if self.primary_workspace is not None:
            body["primary_workspace"] = self.primary_workspace
        if self.replication_mode is not None:
            body["replication_mode"] = self.replication_mode
        if self.state is not None:
            body["state"] = self.state
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.workspaces:
            body["workspaces"] = self.workspaces
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ReplicationGroupPreview:
        """Deserializes the ReplicationGroupPreview from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            etag=d.get("etag", None),
            name=d.get("name", None),
            observed_metrics=_from_dict(d, "observed_metrics", ReplicationMetricsPreview),
            parent=d.get("parent", None),
            primary_workspace=d.get("primary_workspace", None),
            replication_mode=_enum(d, "replication_mode", ReplicationModePreview),
            state=_enum(d, "state", ReplicationGroupPreviewState),
            update_time=_timestamp(d, "update_time"),
            workspaces=d.get("workspaces", None),
        )


@dataclass
class ReplicationGroupPreviewOperationMetadata:
    """Empty placeholder; required by every LRO ``metadata_type``. Mirrors BranchOperationMetadata /
    RoleOperationMetadata."""

    def as_dict(self) -> dict:
        """Serializes the ReplicationGroupPreviewOperationMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ReplicationGroupPreviewOperationMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ReplicationGroupPreviewOperationMetadata:
        """Deserializes the ReplicationGroupPreviewOperationMetadata from a dictionary."""
        return cls()


class ReplicationGroupPreviewState(Enum):
    REPLICATION_GROUP_PREVIEW_STATE_DEGRADED = "REPLICATION_GROUP_PREVIEW_STATE_DEGRADED"
    REPLICATION_GROUP_PREVIEW_STATE_DELETING = "REPLICATION_GROUP_PREVIEW_STATE_DELETING"
    REPLICATION_GROUP_PREVIEW_STATE_FAILING_OVER = "REPLICATION_GROUP_PREVIEW_STATE_FAILING_OVER"
    REPLICATION_GROUP_PREVIEW_STATE_PROVISIONING = "REPLICATION_GROUP_PREVIEW_STATE_PROVISIONING"
    REPLICATION_GROUP_PREVIEW_STATE_READY = "REPLICATION_GROUP_PREVIEW_STATE_READY"
    REPLICATION_GROUP_PREVIEW_STATE_SWITCHING_OVER = "REPLICATION_GROUP_PREVIEW_STATE_SWITCHING_OVER"


@dataclass
class ReplicationMetricsPreview:
    as_of_time: Optional[Timestamp] = None
    """The time at which these metrics were sampled."""

    bytes_lag: Optional[int] = None
    """The most recent observed byte lag."""

    throughput_bytes_per_second: Optional[int] = None
    """The most recent observed replication throughput."""

    time_lag: Optional[Duration] = None
    """The most recent observed time lag."""

    def as_dict(self) -> dict:
        """Serializes the ReplicationMetricsPreview into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.as_of_time is not None:
            body["as_of_time"] = self.as_of_time.ToJsonString()
        if self.bytes_lag is not None:
            body["bytes_lag"] = self.bytes_lag
        if self.throughput_bytes_per_second is not None:
            body["throughput_bytes_per_second"] = self.throughput_bytes_per_second
        if self.time_lag is not None:
            body["time_lag"] = self.time_lag.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ReplicationMetricsPreview into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.as_of_time is not None:
            body["as_of_time"] = self.as_of_time
        if self.bytes_lag is not None:
            body["bytes_lag"] = self.bytes_lag
        if self.throughput_bytes_per_second is not None:
            body["throughput_bytes_per_second"] = self.throughput_bytes_per_second
        if self.time_lag is not None:
            body["time_lag"] = self.time_lag
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ReplicationMetricsPreview:
        """Deserializes the ReplicationMetricsPreview from a dictionary."""
        return cls(
            as_of_time=_timestamp(d, "as_of_time"),
            bytes_lag=d.get("bytes_lag", None),
            throughput_bytes_per_second=d.get("throughput_bytes_per_second", None),
            time_lag=_duration(d, "time_lag"),
        )


class ReplicationModePreview(Enum):
    """How changes are propagated from the primary workspace to its secondaries in a replication group:
    on a fixed schedule or continuously as they occur."""

    REPLICATION_MODE_PREVIEW_LIVE = "REPLICATION_MODE_PREVIEW_LIVE"
    REPLICATION_MODE_PREVIEW_PERIODIC = "REPLICATION_MODE_PREVIEW_PERIODIC"


class ReplicationRolePreview(Enum):
    """The replication role of the project in its current workspace. Populated only when
    cross-workspace replication is configured for the project."""

    REPLICATION_ROLE_PREVIEW_DEMOTING = "REPLICATION_ROLE_PREVIEW_DEMOTING"
    REPLICATION_ROLE_PREVIEW_PRIMARY = "REPLICATION_ROLE_PREVIEW_PRIMARY"
    REPLICATION_ROLE_PREVIEW_SECONDARY = "REPLICATION_ROLE_PREVIEW_SECONDARY"


@dataclass
class RequestedClaims:
    permission_set: Optional[RequestedClaimsPermissionSet] = None

    resources: Optional[List[RequestedResource]] = None

    def as_dict(self) -> dict:
        """Serializes the RequestedClaims into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permission_set is not None:
            body["permission_set"] = self.permission_set.value
        if self.resources:
            body["resources"] = [v.as_dict() for v in self.resources]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RequestedClaims into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.permission_set is not None:
            body["permission_set"] = self.permission_set
        if self.resources:
            body["resources"] = self.resources
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RequestedClaims:
        """Deserializes the RequestedClaims from a dictionary."""
        return cls(
            permission_set=_enum(d, "permission_set", RequestedClaimsPermissionSet),
            resources=_repeated_dict(d, "resources", RequestedResource),
        )


class RequestedClaimsPermissionSet(Enum):
    READ_ONLY = "READ_ONLY"


@dataclass
class RequestedResource:
    table_name: Optional[str] = None
    """The full Unity Catalog table name."""

    def as_dict(self) -> dict:
        """Serializes the RequestedResource into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.table_name is not None:
            body["table_name"] = self.table_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RequestedResource into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.table_name is not None:
            body["table_name"] = self.table_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RequestedResource:
        """Deserializes the RequestedResource from a dictionary."""
        return cls(table_name=d.get("table_name", None))


@dataclass
class Role:
    """Role represents a Postgres role within a Branch."""

    create_time: Optional[Timestamp] = None

    name: Optional[str] = None
    """Output only. The full resource path of the role. Format:
    projects/{project_id}/branches/{branch_id}/roles/{role_id}"""

    parent: Optional[str] = None
    """The Branch where this Role exists. Format: projects/{project_id}/branches/{branch_id}"""

    role_id: Optional[str] = None
    """The part of the name, chosen by the user when the resource was created."""

    spec: Optional[RoleRoleSpec] = None
    """The spec contains the role configuration, including identity type, authentication method, and
    role attributes."""

    status: Optional[RoleRoleStatus] = None
    """Current status of the role, including its identity type, authentication method, and role
    attributes."""

    update_time: Optional[Timestamp] = None

    def as_dict(self) -> dict:
        """Serializes the Role into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.role_id is not None:
            body["role_id"] = self.role_id
        if self.spec:
            body["spec"] = self.spec.as_dict()
        if self.status:
            body["status"] = self.status.as_dict()
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Role into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.role_id is not None:
            body["role_id"] = self.role_id
        if self.spec:
            body["spec"] = self.spec
        if self.status:
            body["status"] = self.status
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Role:
        """Deserializes the Role from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            name=d.get("name", None),
            parent=d.get("parent", None),
            role_id=d.get("role_id", None),
            spec=_from_dict(d, "spec", RoleRoleSpec),
            status=_from_dict(d, "status", RoleRoleStatus),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class RoleAttributes:
    """Attributes that can be granted to a Postgres role. We are only implementing a subset for now,
    see xref: https://www.postgresql.org/docs/16/sql-createrole.html The values follow Postgres
    keyword naming e.g. CREATEDB, BYPASSRLS, etc. which is why they don't include typical
    underscores between words."""

    bypassrls: Optional[bool] = None

    createdb: Optional[bool] = None

    createrole: Optional[bool] = None

    def as_dict(self) -> dict:
        """Serializes the RoleAttributes into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.bypassrls is not None:
            body["bypassrls"] = self.bypassrls
        if self.createdb is not None:
            body["createdb"] = self.createdb
        if self.createrole is not None:
            body["createrole"] = self.createrole
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RoleAttributes into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.bypassrls is not None:
            body["bypassrls"] = self.bypassrls
        if self.createdb is not None:
            body["createdb"] = self.createdb
        if self.createrole is not None:
            body["createrole"] = self.createrole
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RoleAttributes:
        """Deserializes the RoleAttributes from a dictionary."""
        return cls(
            bypassrls=d.get("bypassrls", None), createdb=d.get("createdb", None), createrole=d.get("createrole", None)
        )


class RoleAuthMethod(Enum):
    """How the role is authenticated when connecting to Postgres."""

    LAKEBASE_OAUTH_V1 = "LAKEBASE_OAUTH_V1"
    NO_LOGIN = "NO_LOGIN"
    PG_PASSWORD_SCRAM_SHA_256 = "PG_PASSWORD_SCRAM_SHA_256"


class RoleIdentityType(Enum):
    """The type of the Databricks managed identity that this Role represents. Leave empty if you wish
    to create a regular Postgres role not associated with a Databricks identity."""

    GROUP = "GROUP"
    SERVICE_PRINCIPAL = "SERVICE_PRINCIPAL"
    USER = "USER"


class RoleMembershipRole(Enum):
    """Roles that the DatabaseInstanceRole can be a member of."""

    DATABRICKS_SUPERUSER = "DATABRICKS_SUPERUSER"


@dataclass
class RoleOperationMetadata:
    def as_dict(self) -> dict:
        """Serializes the RoleOperationMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RoleOperationMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RoleOperationMetadata:
        """Deserializes the RoleOperationMetadata from a dictionary."""
        return cls()


@dataclass
class RoleRoleSpec:
    attributes: Optional[RoleAttributes] = None
    """The desired API-exposed Postgres role attribute to associate with the role. Optional."""

    auth_method: Optional[RoleAuthMethod] = None
    """Controls how the Postgres role authenticates when a client opens a database connection.
    Supported values:
    
    - LAKEBASE_OAUTH_V1: the role authenticates by presenting a Databricks OAuth access token
      derived from the backing managed identity (the Databricks user, service principal, or group
      named by the role's ``postgres_role``). No static password exists for roles using this method.
    - PG_PASSWORD_SCRAM_SHA_256: the role authenticates with a Postgres password verified
      server-side using the SCRAM-SHA-256 mechanism. Lakebase generates a password for the role.
    - NO_LOGIN: the role cannot open a Postgres session at all. Useful for roles that exist only to
      own objects or to aggregate privileges that are then granted to other, loginable roles.
    
    If auth_method is left unspecified, a meaningful authentication method is derived from the
    identity_type:
    
    - For the managed identities, OAUTH is used.
    - For the regular postgres roles, authentication based on postgres passwords is used.
    
    NOTE: for the Databricks identity type GROUP, LAKEBASE_OAUTH_V1 is the default auth method
    (group can login as well)."""

    identity_type: Optional[RoleIdentityType] = None
    """The type of role. When specifying a managed-identity, the chosen role_id must be a valid:
    
    - application ID for SERVICE_PRINCIPAL
    - user email for USER
    - group name for GROUP"""

    membership_roles: Optional[List[RoleMembershipRole]] = None
    """An enum value for a standard role that this role is a member of."""

    postgres_role: Optional[str] = None
    """The name of the Postgres role.
    
    This expects a valid Postgres identifier as specified in the link below.
    https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS
    
    Required when creating the Role.
    
    If you wish to create a Postgres Role backed by a managed Databricks identity, then
    postgres_role must be one of the following:
    
    1. user email for IdentityType.USER
    2. app ID for IdentityType.SERVICE_PRINCIPAL
    3. group name for IdentityType.GROUP"""

    def as_dict(self) -> dict:
        """Serializes the RoleRoleSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.attributes:
            body["attributes"] = self.attributes.as_dict()
        if self.auth_method is not None:
            body["auth_method"] = self.auth_method.value
        if self.identity_type is not None:
            body["identity_type"] = self.identity_type.value
        if self.membership_roles:
            body["membership_roles"] = [v.value for v in self.membership_roles]
        if self.postgres_role is not None:
            body["postgres_role"] = self.postgres_role
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RoleRoleSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.attributes:
            body["attributes"] = self.attributes
        if self.auth_method is not None:
            body["auth_method"] = self.auth_method
        if self.identity_type is not None:
            body["identity_type"] = self.identity_type
        if self.membership_roles:
            body["membership_roles"] = self.membership_roles
        if self.postgres_role is not None:
            body["postgres_role"] = self.postgres_role
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RoleRoleSpec:
        """Deserializes the RoleRoleSpec from a dictionary."""
        return cls(
            attributes=_from_dict(d, "attributes", RoleAttributes),
            auth_method=_enum(d, "auth_method", RoleAuthMethod),
            identity_type=_enum(d, "identity_type", RoleIdentityType),
            membership_roles=_repeated_enum(d, "membership_roles", RoleMembershipRole),
            postgres_role=d.get("postgres_role", None),
        )


@dataclass
class RoleRoleStatus:
    attributes: Optional[RoleAttributes] = None
    """The PG role attributes associated with the role."""

    auth_method: Optional[RoleAuthMethod] = None

    identity_type: Optional[RoleIdentityType] = None
    """The type of the role."""

    membership_roles: Optional[List[RoleMembershipRole]] = None
    """An enum value for a standard role that this role is a member of."""

    postgres_role: Optional[str] = None
    """The name of the Postgres role."""

    role_id: Optional[str] = None
    """Part of the resource name."""

    def as_dict(self) -> dict:
        """Serializes the RoleRoleStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.attributes:
            body["attributes"] = self.attributes.as_dict()
        if self.auth_method is not None:
            body["auth_method"] = self.auth_method.value
        if self.identity_type is not None:
            body["identity_type"] = self.identity_type.value
        if self.membership_roles:
            body["membership_roles"] = [v.value for v in self.membership_roles]
        if self.postgres_role is not None:
            body["postgres_role"] = self.postgres_role
        if self.role_id is not None:
            body["role_id"] = self.role_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RoleRoleStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.attributes:
            body["attributes"] = self.attributes
        if self.auth_method is not None:
            body["auth_method"] = self.auth_method
        if self.identity_type is not None:
            body["identity_type"] = self.identity_type
        if self.membership_roles:
            body["membership_roles"] = self.membership_roles
        if self.postgres_role is not None:
            body["postgres_role"] = self.postgres_role
        if self.role_id is not None:
            body["role_id"] = self.role_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RoleRoleStatus:
        """Deserializes the RoleRoleStatus from a dictionary."""
        return cls(
            attributes=_from_dict(d, "attributes", RoleAttributes),
            auth_method=_enum(d, "auth_method", RoleAuthMethod),
            identity_type=_enum(d, "identity_type", RoleIdentityType),
            membership_roles=_repeated_enum(d, "membership_roles", RoleMembershipRole),
            postgres_role=d.get("postgres_role", None),
            role_id=d.get("role_id", None),
        )


@dataclass
class ScheduleCadence:
    """One cadence at which automatic snapshots are taken."""

    retention: Duration
    """How long snapshots from this cadence are kept before automatic deletion. Must be at least 1
    hour. Applied when a snapshot is taken; not retroactive, so changing it affects only later
    snapshots."""

    daily_schedule: Optional[DailySchedule] = None
    """Take a snapshot once per day."""

    monthly_schedule: Optional[MonthlySchedule] = None
    """Take a snapshot once per month."""

    weekly_schedule: Optional[WeeklySchedule] = None
    """Take a snapshot once per week."""

    def as_dict(self) -> dict:
        """Serializes the ScheduleCadence into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.daily_schedule:
            body["daily_schedule"] = self.daily_schedule.as_dict()
        if self.monthly_schedule:
            body["monthly_schedule"] = self.monthly_schedule.as_dict()
        if self.retention is not None:
            body["retention"] = self.retention.ToJsonString()
        if self.weekly_schedule:
            body["weekly_schedule"] = self.weekly_schedule.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ScheduleCadence into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.daily_schedule:
            body["daily_schedule"] = self.daily_schedule
        if self.monthly_schedule:
            body["monthly_schedule"] = self.monthly_schedule
        if self.retention is not None:
            body["retention"] = self.retention
        if self.weekly_schedule:
            body["weekly_schedule"] = self.weekly_schedule
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ScheduleCadence:
        """Deserializes the ScheduleCadence from a dictionary."""
        return cls(
            daily_schedule=_from_dict(d, "daily_schedule", DailySchedule),
            monthly_schedule=_from_dict(d, "monthly_schedule", MonthlySchedule),
            retention=_duration(d, "retention"),
            weekly_schedule=_from_dict(d, "weekly_schedule", WeeklySchedule),
        )


@dataclass
class Snapshot:
    """An immutable, point-in-time copy of a branch's data within a project. It remains available after
    the source branch is deleted."""

    create_time: Optional[Timestamp] = None
    """When the snapshot was created."""

    name: Optional[str] = None
    """The resource name of the snapshot. Format: projects/{project_id}/snapshots/{snapshot_id}"""

    snapshot_id: Optional[str] = None
    """The user-chosen ID; the final segment of ``name``."""

    spec: Optional[SnapshotSpec] = None
    """Client-provided configuration of the snapshot."""

    status: Optional[SnapshotStatus] = None
    """Server-observed state of the snapshot."""

    uid: Optional[str] = None
    """Unique system-generated ID for the snapshot."""

    update_time: Optional[Timestamp] = None
    """When the snapshot was last updated."""

    def as_dict(self) -> dict:
        """Serializes the Snapshot into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.name is not None:
            body["name"] = self.name
        if self.snapshot_id is not None:
            body["snapshot_id"] = self.snapshot_id
        if self.spec:
            body["spec"] = self.spec.as_dict()
        if self.status:
            body["status"] = self.status.as_dict()
        if self.uid is not None:
            body["uid"] = self.uid
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Snapshot into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.name is not None:
            body["name"] = self.name
        if self.snapshot_id is not None:
            body["snapshot_id"] = self.snapshot_id
        if self.spec:
            body["spec"] = self.spec
        if self.status:
            body["status"] = self.status
        if self.uid is not None:
            body["uid"] = self.uid
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Snapshot:
        """Deserializes the Snapshot from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            name=d.get("name", None),
            snapshot_id=d.get("snapshot_id", None),
            spec=_from_dict(d, "spec", SnapshotSpec),
            status=_from_dict(d, "status", SnapshotStatus),
            uid=d.get("uid", None),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class SnapshotOperationMetadata:
    """Metadata for the long-running snapshot Create, Update, and Delete operations."""

    def as_dict(self) -> dict:
        """Serializes the SnapshotOperationMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SnapshotOperationMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SnapshotOperationMetadata:
        """Deserializes the SnapshotOperationMetadata from a dictionary."""
        return cls()


@dataclass
class SnapshotSchedule:
    """The automatic snapshot cadences for a branch. There is exactly one schedule per branch
    (singleton); it is configured in place, not created or deleted.

    Name: projects/{project_id}/branches/{branch_id}/snapshot-schedule"""

    name: Optional[str] = None
    """The resource name of the branch's snapshot schedule. Format:
    projects/{project_id}/branches/{branch_id}/snapshot-schedule"""

    schedule: Optional[List[ScheduleCadence]] = None
    """The cadences at which automatic snapshots are taken. Update replaces the whole set; an empty set
    disables automatic snapshots. Order is not significant. When several cadences fire together, one
    snapshot is taken, retained for the longest of their retentions."""

    def as_dict(self) -> dict:
        """Serializes the SnapshotSchedule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.schedule:
            body["schedule"] = [v.as_dict() for v in self.schedule]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SnapshotSchedule into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.schedule:
            body["schedule"] = self.schedule
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SnapshotSchedule:
        """Deserializes the SnapshotSchedule from a dictionary."""
        return cls(name=d.get("name", None), schedule=_repeated_dict(d, "schedule", ScheduleCadence))


@dataclass
class SnapshotSpec:
    """Client-provided configuration of the snapshot."""

    source_branch: str
    """The source branch to snapshot. Format: projects/{project_id}/branches/{branch_id}"""

    expire_time: Optional[Timestamp] = None
    """Absolute time at which the snapshot is deleted. Mutually exclusive with ``ttl`` and
    ``no_expiry``."""

    no_expiry: Optional[bool] = None
    """If true, the snapshot never expires. Mutually exclusive with ``ttl`` and ``expire_time``."""

    source_branch_lsn: Optional[str] = None
    """LSN to snapshot from, e.g. ``16/B374D848``. Mutually exclusive with ``source_branch_time``."""

    source_branch_time: Optional[Timestamp] = None
    """Timestamp to snapshot from. Mutually exclusive with ``source_branch_lsn``."""

    ttl: Optional[Duration] = None
    """Time-to-live. The snapshot expires this long after it is created. Mutually exclusive with
    ``expire_time`` and ``no_expiry``."""

    def as_dict(self) -> dict:
        """Serializes the SnapshotSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.expire_time is not None:
            body["expire_time"] = self.expire_time.ToJsonString()
        if self.no_expiry is not None:
            body["no_expiry"] = self.no_expiry
        if self.source_branch is not None:
            body["source_branch"] = self.source_branch
        if self.source_branch_lsn is not None:
            body["source_branch_lsn"] = self.source_branch_lsn
        if self.source_branch_time is not None:
            body["source_branch_time"] = self.source_branch_time.ToJsonString()
        if self.ttl is not None:
            body["ttl"] = self.ttl.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SnapshotSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.expire_time is not None:
            body["expire_time"] = self.expire_time
        if self.no_expiry is not None:
            body["no_expiry"] = self.no_expiry
        if self.source_branch is not None:
            body["source_branch"] = self.source_branch
        if self.source_branch_lsn is not None:
            body["source_branch_lsn"] = self.source_branch_lsn
        if self.source_branch_time is not None:
            body["source_branch_time"] = self.source_branch_time
        if self.ttl is not None:
            body["ttl"] = self.ttl
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SnapshotSpec:
        """Deserializes the SnapshotSpec from a dictionary."""
        return cls(
            expire_time=_timestamp(d, "expire_time"),
            no_expiry=d.get("no_expiry", None),
            source_branch=d.get("source_branch", None),
            source_branch_lsn=d.get("source_branch_lsn", None),
            source_branch_time=_timestamp(d, "source_branch_time"),
            ttl=_duration(d, "ttl"),
        )


@dataclass
class SnapshotStatus:
    """Server-observed state of a snapshot."""

    current_state: Optional[SnapshotStatusState] = None
    """The snapshot's current state."""

    diff_size_bytes: Optional[int] = None
    """Incremental storage size in bytes since the previous snapshot. Unset when the snapshot is not
    billed on incremental usage."""

    expire_time: Optional[Timestamp] = None
    """Absolute time at which the snapshot is deleted."""

    full_size_bytes: Optional[int] = None
    """Full logical size of the snapshot, in bytes."""

    no_expiry: Optional[bool] = None
    """True if the snapshot never expires."""

    source_branch: Optional[str] = None
    """The source branch the snapshot was taken from. Format:
    projects/{project_id}/branches/{branch_id}"""

    source_branch_lsn: Optional[str] = None
    """The LSN at which the snapshot was taken."""

    source_branch_time: Optional[Timestamp] = None
    """The point in time at which the snapshot was taken."""

    def as_dict(self) -> dict:
        """Serializes the SnapshotStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.current_state is not None:
            body["current_state"] = self.current_state.value
        if self.diff_size_bytes is not None:
            body["diff_size_bytes"] = self.diff_size_bytes
        if self.expire_time is not None:
            body["expire_time"] = self.expire_time.ToJsonString()
        if self.full_size_bytes is not None:
            body["full_size_bytes"] = self.full_size_bytes
        if self.no_expiry is not None:
            body["no_expiry"] = self.no_expiry
        if self.source_branch is not None:
            body["source_branch"] = self.source_branch
        if self.source_branch_lsn is not None:
            body["source_branch_lsn"] = self.source_branch_lsn
        if self.source_branch_time is not None:
            body["source_branch_time"] = self.source_branch_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SnapshotStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.current_state is not None:
            body["current_state"] = self.current_state
        if self.diff_size_bytes is not None:
            body["diff_size_bytes"] = self.diff_size_bytes
        if self.expire_time is not None:
            body["expire_time"] = self.expire_time
        if self.full_size_bytes is not None:
            body["full_size_bytes"] = self.full_size_bytes
        if self.no_expiry is not None:
            body["no_expiry"] = self.no_expiry
        if self.source_branch is not None:
            body["source_branch"] = self.source_branch
        if self.source_branch_lsn is not None:
            body["source_branch_lsn"] = self.source_branch_lsn
        if self.source_branch_time is not None:
            body["source_branch_time"] = self.source_branch_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SnapshotStatus:
        """Deserializes the SnapshotStatus from a dictionary."""
        return cls(
            current_state=_enum(d, "current_state", SnapshotStatusState),
            diff_size_bytes=d.get("diff_size_bytes", None),
            expire_time=_timestamp(d, "expire_time"),
            full_size_bytes=d.get("full_size_bytes", None),
            no_expiry=d.get("no_expiry", None),
            source_branch=d.get("source_branch", None),
            source_branch_lsn=d.get("source_branch_lsn", None),
            source_branch_time=_timestamp(d, "source_branch_time"),
        )


class SnapshotStatusState(Enum):
    """The state of the snapshot."""

    AVAILABLE = "AVAILABLE"
    CREATING = "CREATING"
    DELETING = "DELETING"
    FAILED = "FAILED"


@dataclass
class SyncedTable:
    create_time: Optional[Timestamp] = None

    name: Optional[str] = None
    """Output only. The Full resource name of the synced table in Postgres where (catalog, schema,
    table) are the UC entity names.
    
    Format "synced_tables/{catalog}.{schema}.{table}"
    
    For the corresponding source table in the Unity catalog look for the "source_table_full_name"
    attribute."""

    spec: Optional[SyncedTableSyncedTableSpec] = None
    """Configuration details of the synced table, such as the source table, scheduling policy, etc.
    This attribute is specified at creation time and most fields are returned as is on subsequent
    queries."""

    status: Optional[SyncedTableSyncedTableStatus] = None
    """Synced Table data synchronization status."""

    synced_table_id: Optional[str] = None
    """The part of the name, chosen by the user when the resource was created."""

    uid: Optional[str] = None
    """The Unity Catalog table ID for this synced table."""

    def as_dict(self) -> dict:
        """Serializes the SyncedTable into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.name is not None:
            body["name"] = self.name
        if self.spec:
            body["spec"] = self.spec.as_dict()
        if self.status:
            body["status"] = self.status.as_dict()
        if self.synced_table_id is not None:
            body["synced_table_id"] = self.synced_table_id
        if self.uid is not None:
            body["uid"] = self.uid
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncedTable into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.name is not None:
            body["name"] = self.name
        if self.spec:
            body["spec"] = self.spec
        if self.status:
            body["status"] = self.status
        if self.synced_table_id is not None:
            body["synced_table_id"] = self.synced_table_id
        if self.uid is not None:
            body["uid"] = self.uid
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncedTable:
        """Deserializes the SyncedTable from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            name=d.get("name", None),
            spec=_from_dict(d, "spec", SyncedTableSyncedTableSpec),
            status=_from_dict(d, "status", SyncedTableSyncedTableStatus),
            synced_table_id=d.get("synced_table_id", None),
            uid=d.get("uid", None),
        )


@dataclass
class SyncedTableOperationMetadata:
    """Metadata for SyncedTable long-running operations."""

    def as_dict(self) -> dict:
        """Serializes the SyncedTableOperationMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncedTableOperationMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncedTableOperationMetadata:
        """Deserializes the SyncedTableOperationMetadata from a dictionary."""
        return cls()


@dataclass
class SyncedTablePipelineProgress:
    """Progress information of the Synced Table data synchronization pipeline."""

    estimated_completion_time_seconds: Optional[float] = None
    """The estimated time remaining to complete this update in seconds."""

    latest_version_currently_processing: Optional[int] = None
    """The source table Delta version that was last processed by the pipeline. The pipeline may not
    have completely processed this version yet."""

    sync_progress_completion: Optional[float] = None
    """The completion ratio of this update. This is a number between 0 and 1."""

    synced_row_count: Optional[int] = None
    """The number of rows that have been synced in this update."""

    total_row_count: Optional[int] = None
    """The total number of rows that need to be synced in this update. This number may be an estimate."""

    def as_dict(self) -> dict:
        """Serializes the SyncedTablePipelineProgress into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.estimated_completion_time_seconds is not None:
            body["estimated_completion_time_seconds"] = self.estimated_completion_time_seconds
        if self.latest_version_currently_processing is not None:
            body["latest_version_currently_processing"] = self.latest_version_currently_processing
        if self.sync_progress_completion is not None:
            body["sync_progress_completion"] = self.sync_progress_completion
        if self.synced_row_count is not None:
            body["synced_row_count"] = self.synced_row_count
        if self.total_row_count is not None:
            body["total_row_count"] = self.total_row_count
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncedTablePipelineProgress into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.estimated_completion_time_seconds is not None:
            body["estimated_completion_time_seconds"] = self.estimated_completion_time_seconds
        if self.latest_version_currently_processing is not None:
            body["latest_version_currently_processing"] = self.latest_version_currently_processing
        if self.sync_progress_completion is not None:
            body["sync_progress_completion"] = self.sync_progress_completion
        if self.synced_row_count is not None:
            body["synced_row_count"] = self.synced_row_count
        if self.total_row_count is not None:
            body["total_row_count"] = self.total_row_count
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncedTablePipelineProgress:
        """Deserializes the SyncedTablePipelineProgress from a dictionary."""
        return cls(
            estimated_completion_time_seconds=d.get("estimated_completion_time_seconds", None),
            latest_version_currently_processing=d.get("latest_version_currently_processing", None),
            sync_progress_completion=d.get("sync_progress_completion", None),
            synced_row_count=d.get("synced_row_count", None),
            total_row_count=d.get("total_row_count", None),
        )


@dataclass
class SyncedTablePosition:
    delta_table_sync_info: Optional[DeltaTableSyncInfo] = None

    sync_end_time: Optional[Timestamp] = None
    """The end timestamp of the most recent successful synchronization. This is the time when the data
    is available in the synced table."""

    sync_start_time: Optional[Timestamp] = None
    """The starting timestamp of the most recent successful synchronization from the source table to
    the destination (synced) table. Note this is the starting timestamp of the sync operation, not
    the end time. E.g., for a batch, this is the time when the sync operation started."""

    def as_dict(self) -> dict:
        """Serializes the SyncedTablePosition into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.delta_table_sync_info:
            body["delta_table_sync_info"] = self.delta_table_sync_info.as_dict()
        if self.sync_end_time is not None:
            body["sync_end_time"] = self.sync_end_time.ToJsonString()
        if self.sync_start_time is not None:
            body["sync_start_time"] = self.sync_start_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncedTablePosition into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.delta_table_sync_info:
            body["delta_table_sync_info"] = self.delta_table_sync_info
        if self.sync_end_time is not None:
            body["sync_end_time"] = self.sync_end_time
        if self.sync_start_time is not None:
            body["sync_start_time"] = self.sync_start_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncedTablePosition:
        """Deserializes the SyncedTablePosition from a dictionary."""
        return cls(
            delta_table_sync_info=_from_dict(d, "delta_table_sync_info", DeltaTableSyncInfo),
            sync_end_time=_timestamp(d, "sync_end_time"),
            sync_start_time=_timestamp(d, "sync_start_time"),
        )


class SyncedTableState(Enum):
    """The state of a synced table."""

    SYNCED_TABLE_OFFLINE = "SYNCED_TABLE_OFFLINE"
    SYNCED_TABLE_OFFLINE_FAILED = "SYNCED_TABLE_OFFLINE_FAILED"
    SYNCED_TABLE_ONLINE = "SYNCED_TABLE_ONLINE"
    SYNCED_TABLE_ONLINE_CONTINUOUS_UPDATE = "SYNCED_TABLE_ONLINE_CONTINUOUS_UPDATE"
    SYNCED_TABLE_ONLINE_NO_PENDING_UPDATE = "SYNCED_TABLE_ONLINE_NO_PENDING_UPDATE"
    SYNCED_TABLE_ONLINE_PIPELINE_FAILED = "SYNCED_TABLE_ONLINE_PIPELINE_FAILED"
    SYNCED_TABLE_ONLINE_TRIGGERED_UPDATE = "SYNCED_TABLE_ONLINE_TRIGGERED_UPDATE"
    SYNCED_TABLE_ONLINE_UPDATING_PIPELINE_RESOURCES = "SYNCED_TABLE_ONLINE_UPDATING_PIPELINE_RESOURCES"
    SYNCED_TABLE_PROVISIONING = "SYNCED_TABLE_PROVISIONING"
    SYNCED_TABLE_PROVISIONING_INITIAL_SNAPSHOT = "SYNCED_TABLE_PROVISIONING_INITIAL_SNAPSHOT"
    SYNCED_TABLE_PROVISIONING_PIPELINE_RESOURCES = "SYNCED_TABLE_PROVISIONING_PIPELINE_RESOURCES"


@dataclass
class SyncedTableSyncedTableSpec:
    accelerated_sync: Optional[bool] = None
    """When true, enables accelerated sync mode for the initial data load. This significantly improves
    performance for large tables. Requires workspace-level enablement through Lakebase Accelerated
    Sync preview."""

    branch: Optional[str] = None
    """The full resource name the branch associated with the table.
    
    Format: "projects/{project_id}/branches/{branch_id}"."""

    create_database_objects_if_missing: Optional[bool] = None
    """If true, the synced table's logical database and schema resources in PG will be created if they
    do not already exist. The request will fail if this is false and the database/schema do not
    exist.
    
    Defaults to true if omitted."""

    existing_pipeline_id: Optional[str] = None
    """ID of an existing pipeline to bin-pack this synced table into. At most one of
    existing_pipeline_id and new_pipeline_spec should be defined.
    
    The pipeline used for the synced table is returned via the top level pipeline_id attribute."""

    extra_columns: Optional[List[SyncedTableSyncedTableSpecExtraColumn]] = None
    """Extra PostgreSQL-only columns to add to the synced table."""

    extra_index_definitions: Optional[List[SyncedTableSyncedTableSpecSecondaryIndex]] = None
    """Secondary indexes to create on the synced table."""

    new_pipeline_spec: Optional[NewPipelineSpec] = None
    """Specification for creating a new pipeline. At most one of existing_pipeline_id and
    new_pipeline_spec should be defined.
    
    The pipeline used for the synced table is returned via the top level pipeline_id attribute."""

    postgres_database: Optional[str] = None
    """The Postgres database name where the synced table will be created in.
    
    If this synced table is created inside a Lakebase Catalog, this attribute can be omitted on
    creation and is inferred from the postgres_database associated with the Lakebase Catalog. If
    specified when inside a Lakebase Catalog, the value must match.
    
    A value must be specified when creating a synced table inside a Standard Catalog."""

    primary_key_columns: Optional[List[str]] = None
    """Primary Key columns to be used for data insert/update in the destination."""

    scheduling_policy: Optional[SyncedTableSyncedTableSpecSyncedTableSchedulingPolicy] = None
    """Scheduling policy of the underlying pipeline."""

    source_table_full_name: Optional[str] = None
    """Three-part (catalog, schema, table) name of the source Delta table.
    
    For the corresponding destination table, use any of the two:
    
    - synced_table_id used at the creation of the SyncedTable
    - "name" consisting of "synced_tables/" prefix and the full name of the destination table."""

    timeseries_key: Optional[str] = None
    """Time series key to deduplicate (tie-break) rows with the same primary key."""

    type_overrides: Optional[List[SyncedTableSyncedTableSpecTypeOverride]] = None
    """Override the default Delta->PG type mapping for specific columns. A TypeOverride with
    PG_SPECIFIC_TYPE_UNSPECIFIED is rejected; a valid pg_type must be set."""

    def as_dict(self) -> dict:
        """Serializes the SyncedTableSyncedTableSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.accelerated_sync is not None:
            body["accelerated_sync"] = self.accelerated_sync
        if self.branch is not None:
            body["branch"] = self.branch
        if self.create_database_objects_if_missing is not None:
            body["create_database_objects_if_missing"] = self.create_database_objects_if_missing
        if self.existing_pipeline_id is not None:
            body["existing_pipeline_id"] = self.existing_pipeline_id
        if self.extra_columns:
            body["extra_columns"] = [v.as_dict() for v in self.extra_columns]
        if self.extra_index_definitions:
            body["extra_index_definitions"] = [v.as_dict() for v in self.extra_index_definitions]
        if self.new_pipeline_spec:
            body["new_pipeline_spec"] = self.new_pipeline_spec.as_dict()
        if self.postgres_database is not None:
            body["postgres_database"] = self.postgres_database
        if self.primary_key_columns:
            body["primary_key_columns"] = [v for v in self.primary_key_columns]
        if self.scheduling_policy is not None:
            body["scheduling_policy"] = self.scheduling_policy.value
        if self.source_table_full_name is not None:
            body["source_table_full_name"] = self.source_table_full_name
        if self.timeseries_key is not None:
            body["timeseries_key"] = self.timeseries_key
        if self.type_overrides:
            body["type_overrides"] = [v.as_dict() for v in self.type_overrides]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncedTableSyncedTableSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.accelerated_sync is not None:
            body["accelerated_sync"] = self.accelerated_sync
        if self.branch is not None:
            body["branch"] = self.branch
        if self.create_database_objects_if_missing is not None:
            body["create_database_objects_if_missing"] = self.create_database_objects_if_missing
        if self.existing_pipeline_id is not None:
            body["existing_pipeline_id"] = self.existing_pipeline_id
        if self.extra_columns:
            body["extra_columns"] = self.extra_columns
        if self.extra_index_definitions:
            body["extra_index_definitions"] = self.extra_index_definitions
        if self.new_pipeline_spec:
            body["new_pipeline_spec"] = self.new_pipeline_spec
        if self.postgres_database is not None:
            body["postgres_database"] = self.postgres_database
        if self.primary_key_columns:
            body["primary_key_columns"] = self.primary_key_columns
        if self.scheduling_policy is not None:
            body["scheduling_policy"] = self.scheduling_policy
        if self.source_table_full_name is not None:
            body["source_table_full_name"] = self.source_table_full_name
        if self.timeseries_key is not None:
            body["timeseries_key"] = self.timeseries_key
        if self.type_overrides:
            body["type_overrides"] = self.type_overrides
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncedTableSyncedTableSpec:
        """Deserializes the SyncedTableSyncedTableSpec from a dictionary."""
        return cls(
            accelerated_sync=d.get("accelerated_sync", None),
            branch=d.get("branch", None),
            create_database_objects_if_missing=d.get("create_database_objects_if_missing", None),
            existing_pipeline_id=d.get("existing_pipeline_id", None),
            extra_columns=_repeated_dict(d, "extra_columns", SyncedTableSyncedTableSpecExtraColumn),
            extra_index_definitions=_repeated_dict(
                d, "extra_index_definitions", SyncedTableSyncedTableSpecSecondaryIndex
            ),
            new_pipeline_spec=_from_dict(d, "new_pipeline_spec", NewPipelineSpec),
            postgres_database=d.get("postgres_database", None),
            primary_key_columns=d.get("primary_key_columns", None),
            scheduling_policy=_enum(d, "scheduling_policy", SyncedTableSyncedTableSpecSyncedTableSchedulingPolicy),
            source_table_full_name=d.get("source_table_full_name", None),
            timeseries_key=d.get("timeseries_key", None),
            type_overrides=_repeated_dict(d, "type_overrides", SyncedTableSyncedTableSpecTypeOverride),
        )


@dataclass
class SyncedTableSyncedTableSpecExtraColumn:
    """An extra PostgreSQL column to add to the synced table."""

    column_name: str
    """Name of the column."""

    column_type: str
    """PostgreSQL type of the column, for example "tsvector" or "vector(1024)"."""

    compute: Optional[str] = None
    """SQL expression used to compute the column's value, for example "to_tsvector('english',
    content)"."""

    maintenance: Optional[SyncedTableSyncedTableSpecExtraColumnMaintenance] = None

    def as_dict(self) -> dict:
        """Serializes the SyncedTableSyncedTableSpecExtraColumn into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.column_name is not None:
            body["column_name"] = self.column_name
        if self.column_type is not None:
            body["column_type"] = self.column_type
        if self.compute is not None:
            body["compute"] = self.compute
        if self.maintenance is not None:
            body["maintenance"] = self.maintenance.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncedTableSyncedTableSpecExtraColumn into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.column_name is not None:
            body["column_name"] = self.column_name
        if self.column_type is not None:
            body["column_type"] = self.column_type
        if self.compute is not None:
            body["compute"] = self.compute
        if self.maintenance is not None:
            body["maintenance"] = self.maintenance
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncedTableSyncedTableSpecExtraColumn:
        """Deserializes the SyncedTableSyncedTableSpecExtraColumn from a dictionary."""
        return cls(
            column_name=d.get("column_name", None),
            column_type=d.get("column_type", None),
            compute=d.get("compute", None),
            maintenance=_enum(d, "maintenance", SyncedTableSyncedTableSpecExtraColumnMaintenance),
        )


class SyncedTableSyncedTableSpecExtraColumnMaintenance(Enum):
    """How the column's value is populated and kept up to date."""

    DEFAULT_VALUE = "DEFAULT_VALUE"
    STORED_GENERATED = "STORED_GENERATED"


class SyncedTableSyncedTableSpecPgSpecificType(Enum):
    """PostgreSQL-specific target types that can override the default Delta-to-PG mapping."""

    PG_SPECIFIC_TYPE_HALFVEC = "PG_SPECIFIC_TYPE_HALFVEC"
    PG_SPECIFIC_TYPE_VARCHAR = "PG_SPECIFIC_TYPE_VARCHAR"
    PG_SPECIFIC_TYPE_VECTOR = "PG_SPECIFIC_TYPE_VECTOR"


@dataclass
class SyncedTableSyncedTableSpecSecondaryIndex:
    """Definition of a secondary index to create on the synced table."""

    name: str
    """Name of the index as it will appear in PostgreSQL."""

    definition: str
    """The definition portion of a CREATE INDEX statement, placed after ON table_name. For example:
    USING hnsw (embedding vector_cosine_ops) WITH (m = 16, ef_construction = 64)."""

    creation_point: Optional[SyncedTableSyncedTableSpecSecondaryIndexCreationPoint] = None
    """When the index should be created relative to the initial data load."""

    def as_dict(self) -> dict:
        """Serializes the SyncedTableSyncedTableSpecSecondaryIndex into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.creation_point is not None:
            body["creation_point"] = self.creation_point.value
        if self.definition is not None:
            body["definition"] = self.definition
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncedTableSyncedTableSpecSecondaryIndex into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.creation_point is not None:
            body["creation_point"] = self.creation_point
        if self.definition is not None:
            body["definition"] = self.definition
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncedTableSyncedTableSpecSecondaryIndex:
        """Deserializes the SyncedTableSyncedTableSpecSecondaryIndex from a dictionary."""
        return cls(
            creation_point=_enum(d, "creation_point", SyncedTableSyncedTableSpecSecondaryIndexCreationPoint),
            definition=d.get("definition", None),
            name=d.get("name", None),
        )


class SyncedTableSyncedTableSpecSecondaryIndexCreationPoint(Enum):
    """Controls when the index is created relative to the initial data load."""

    CREATION_POINT_AFTER_DATA_LOAD = "CREATION_POINT_AFTER_DATA_LOAD"


class SyncedTableSyncedTableSpecSyncedTableSchedulingPolicy(Enum):
    """Scheduling policy of the synced table's underlying pipeline."""

    CONTINUOUS = "CONTINUOUS"
    SNAPSHOT = "SNAPSHOT"
    TRIGGERED = "TRIGGERED"


@dataclass
class SyncedTableSyncedTableSpecTypeOverride:
    """Overrides the default Delta-to-PostgreSQL type mapping for a single column."""

    column_name: str
    """Name of the source column whose target PostgreSQL type should be overridden."""

    pg_type: SyncedTableSyncedTableSpecPgSpecificType
    """PostgreSQL-specific target type to use for the column."""

    size: Optional[int] = None
    """Size parameter for the target type, for types that take one (e.g. vector dimension, varchar
    length). Required when the chosen pg_type needs a size."""

    def as_dict(self) -> dict:
        """Serializes the SyncedTableSyncedTableSpecTypeOverride into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.column_name is not None:
            body["column_name"] = self.column_name
        if self.pg_type is not None:
            body["pg_type"] = self.pg_type.value
        if self.size is not None:
            body["size"] = self.size
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncedTableSyncedTableSpecTypeOverride into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.column_name is not None:
            body["column_name"] = self.column_name
        if self.pg_type is not None:
            body["pg_type"] = self.pg_type
        if self.size is not None:
            body["size"] = self.size
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncedTableSyncedTableSpecTypeOverride:
        """Deserializes the SyncedTableSyncedTableSpecTypeOverride from a dictionary."""
        return cls(
            column_name=d.get("column_name", None),
            pg_type=_enum(d, "pg_type", SyncedTableSyncedTableSpecPgSpecificType),
            size=d.get("size", None),
        )


@dataclass
class SyncedTableSyncedTableStatus:
    detailed_state: Optional[SyncedTableState] = None
    """The state of the synced table."""

    last_processed_commit_version: Optional[int] = None
    """The last source table Delta version that was successfully synced to the synced table."""

    last_sync: Optional[SyncedTablePosition] = None
    """Summary of the last successful synchronization from source to destination."""

    last_sync_time: Optional[Timestamp] = None
    """The end timestamp of the last time any data was synchronized from the source table to the synced
    table. This is when the data is available in the synced table."""

    message: Optional[str] = None
    """A text description of the current state of the synced table."""

    ongoing_sync_progress: Optional[SyncedTablePipelineProgress] = None

    pipeline_id: Optional[str] = None
    """ID of the associated pipeline."""

    project: Optional[str] = None
    """The full resource name of the project associated with the table.
    
    Format: "projects/{project_id}"."""

    provisioning_phase: Optional[ProvisioningPhase] = None
    """The current phase of the data synchronization pipeline."""

    unity_catalog_provisioning_state: Optional[ProvisioningInfoState] = None
    """The provisioning state of the synced table entity in Unity Catalog."""

    def as_dict(self) -> dict:
        """Serializes the SyncedTableSyncedTableStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.detailed_state is not None:
            body["detailed_state"] = self.detailed_state.value
        if self.last_processed_commit_version is not None:
            body["last_processed_commit_version"] = self.last_processed_commit_version
        if self.last_sync:
            body["last_sync"] = self.last_sync.as_dict()
        if self.last_sync_time is not None:
            body["last_sync_time"] = self.last_sync_time.ToJsonString()
        if self.message is not None:
            body["message"] = self.message
        if self.ongoing_sync_progress:
            body["ongoing_sync_progress"] = self.ongoing_sync_progress.as_dict()
        if self.pipeline_id is not None:
            body["pipeline_id"] = self.pipeline_id
        if self.project is not None:
            body["project"] = self.project
        if self.provisioning_phase is not None:
            body["provisioning_phase"] = self.provisioning_phase.value
        if self.unity_catalog_provisioning_state is not None:
            body["unity_catalog_provisioning_state"] = self.unity_catalog_provisioning_state.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncedTableSyncedTableStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.detailed_state is not None:
            body["detailed_state"] = self.detailed_state
        if self.last_processed_commit_version is not None:
            body["last_processed_commit_version"] = self.last_processed_commit_version
        if self.last_sync:
            body["last_sync"] = self.last_sync
        if self.last_sync_time is not None:
            body["last_sync_time"] = self.last_sync_time
        if self.message is not None:
            body["message"] = self.message
        if self.ongoing_sync_progress:
            body["ongoing_sync_progress"] = self.ongoing_sync_progress
        if self.pipeline_id is not None:
            body["pipeline_id"] = self.pipeline_id
        if self.project is not None:
            body["project"] = self.project
        if self.provisioning_phase is not None:
            body["provisioning_phase"] = self.provisioning_phase
        if self.unity_catalog_provisioning_state is not None:
            body["unity_catalog_provisioning_state"] = self.unity_catalog_provisioning_state
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncedTableSyncedTableStatus:
        """Deserializes the SyncedTableSyncedTableStatus from a dictionary."""
        return cls(
            detailed_state=_enum(d, "detailed_state", SyncedTableState),
            last_processed_commit_version=d.get("last_processed_commit_version", None),
            last_sync=_from_dict(d, "last_sync", SyncedTablePosition),
            last_sync_time=_timestamp(d, "last_sync_time"),
            message=d.get("message", None),
            ongoing_sync_progress=_from_dict(d, "ongoing_sync_progress", SyncedTablePipelineProgress),
            pipeline_id=d.get("pipeline_id", None),
            project=d.get("project", None),
            provisioning_phase=_enum(d, "provisioning_phase", ProvisioningPhase),
            unity_catalog_provisioning_state=_enum(d, "unity_catalog_provisioning_state", ProvisioningInfoState),
        )


@dataclass
class Table:
    """Table represents a non-synced database table in a Lakebase project. Unlike SyncedTable, this
    does not have a data synchronization pipeline."""

    name: str
    """Full three-part (catalog, schema, table) name of the table."""

    database: str
    """The project and branch scoped database to which this table belongs. Of the format:
    projects/{project_id}/branches/{branch_id}/databases/{database_id} where database_id is the name
    of the logical database in Postgres."""

    branch: Optional[str] = None
    """The id of the database branch associated with the table. Of the format
    projects/{project_id}/branches/{branch_id}."""

    project: Optional[str] = None
    """The id of the database project associated with the table. Of the format projects/{project_id}."""

    table_serving_url: Optional[str] = None
    """REST API URL for serving data from this table."""

    def as_dict(self) -> dict:
        """Serializes the Table into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.branch is not None:
            body["branch"] = self.branch
        if self.database is not None:
            body["database"] = self.database
        if self.name is not None:
            body["name"] = self.name
        if self.project is not None:
            body["project"] = self.project
        if self.table_serving_url is not None:
            body["table_serving_url"] = self.table_serving_url
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Table into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.branch is not None:
            body["branch"] = self.branch
        if self.database is not None:
            body["database"] = self.database
        if self.name is not None:
            body["name"] = self.name
        if self.project is not None:
            body["project"] = self.project
        if self.table_serving_url is not None:
            body["table_serving_url"] = self.table_serving_url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Table:
        """Deserializes the Table from a dictionary."""
        return cls(
            branch=d.get("branch", None),
            database=d.get("database", None),
            name=d.get("name", None),
            project=d.get("project", None),
            table_serving_url=d.get("table_serving_url", None),
        )


@dataclass
class WeeklySchedule:
    """Take a snapshot once per week, on the configured day at the configured hour."""

    day_of_week: DayOfWeek
    """The day of the week on which to take the snapshot."""

    hour: Optional[int] = None
    """The hour of the day, in UTC, at which to take the snapshot, in [0, 23]."""

    def as_dict(self) -> dict:
        """Serializes the WeeklySchedule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.day_of_week is not None:
            body["day_of_week"] = self.day_of_week.value
        if self.hour is not None:
            body["hour"] = self.hour
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the WeeklySchedule into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.day_of_week is not None:
            body["day_of_week"] = self.day_of_week
        if self.hour is not None:
            body["hour"] = self.hour
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> WeeklySchedule:
        """Deserializes the WeeklySchedule from a dictionary."""
        return cls(day_of_week=_enum(d, "day_of_week", DayOfWeek), hour=d.get("hour", None))


class PostgresAPI:
    """Use the Postgres API to create and manage Lakebase Autoscaling Postgres infrastructure, including
    projects, branches, compute endpoints, and roles.

    This API manages database infrastructure only. To query or modify data, use the Data API or direct SQL
    connections.

    **About resource IDs and names**

    Resources are identified by hierarchical resource names like
    ``projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}``. The ``name`` field on each
    resource contains this full path and is output-only. Note that ``name`` refers to this resource path, not
    the user-visible ``display_name``."""

    def __init__(self, api_client):
        self._api = api_client

    def create_branch(
        self, parent: str, branch: Branch, branch_id: str, *, replace_existing: Optional[bool] = None
    ) -> CreateBranchOperation:
        """Creates a new database branch in the project.

        :param parent: str
          The Project where this Branch will be created. Format: projects/{project_id}
        :param branch: :class:`Branch`
          The Branch to create.
        :param branch_id: str
          The ID to use for the Branch. This becomes the final component of the branch's resource name. The ID
          is required and must be 1-63 characters long, start with a lowercase letter, and contain only
          lowercase letters, numbers, and hyphens. For example, ``development`` becomes
          ``projects/my-app/branches/development``.
        :param replace_existing: bool (optional)
          If true, update the branch if it already exists instead of returning an error.

        :returns: :class:`Operation`
        """

        body = branch.as_dict()
        query = {}
        if branch_id is not None:
            query["branch_id"] = branch_id
        if replace_existing is not None:
            query["replace_existing"] = replace_existing
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/postgres/{parent}/branches", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return CreateBranchOperation(self, operation)

    def create_catalog(self, catalog: Catalog, catalog_id: str) -> CreateCatalogOperation:
        """Register a Postgres database in the Unity Catalog.

        :param catalog: :class:`Catalog`
        :param catalog_id: str
          The ID in the Unity Catalog. It becomes the full resource name, for example "my_catalog" becomes
          "catalogs/my_catalog".

        :returns: :class:`Operation`
        """

        body = catalog.as_dict()
        query = {}
        if catalog_id is not None:
            query["catalog_id"] = catalog_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/postgres/catalogs", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return CreateCatalogOperation(self, operation)

    def create_cdf_config(
        self, parent: str, cdf_config: CdfConfig, *, cdf_config_id: Optional[str] = None
    ) -> CreateCdfConfigOperation:
        """Create a CDF configuration that materializes the change data feed for all tables in a Postgres schema
        as open-format Delta tables in Unity Catalog. Once created, each table's change history is
        continuously written to its corresponding Lakehouse table.

        :param parent: str
          The parent database under which to create the CdfConfig. Format:
          projects/{project}/branches/{branch}/databases/{database}
        :param cdf_config: :class:`CdfConfig`
          The CdfConfig to create. The catalog, schema, and postgres_schema fields are required; all other
          fields are output only and ignored on input.
        :param cdf_config_id: str (optional)
          The user-specified id for the CdfConfig, forming the final segment of its resource name. Must match
          the pattern ``[a-z][a-z0-9_]{0,62}``. Defaults to the Postgres schema name when omitted.

        :returns: :class:`Operation`
        """

        body = cdf_config.as_dict()
        query = {}
        if cdf_config_id is not None:
            query["cdf_config_id"] = cdf_config_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/postgres/{parent}/cdf-configs", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return CreateCdfConfigOperation(self, operation)

    def create_data_api(self, parent: str, data_api: DataApi) -> CreateDataApiOperation:
        """Enable Data API for a database.

        :param parent: str
          Parent database: projects/{project_id}/branches/{branch_id}/databases/{database_id}
        :param data_api: :class:`DataApi`
          The Data API configuration to create.

        :returns: :class:`Operation`
        """

        body = data_api.as_dict()
        query = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/postgres/{parent}/data-api", body=body, headers=headers)
        operation = Operation.from_dict(res)
        return CreateDataApiOperation(self, operation)

    def create_database(
        self,
        parent: str,
        database: Database,
        *,
        database_id: Optional[str] = None,
        replace_existing: Optional[bool] = None,
    ) -> CreateDatabaseOperation:
        """Create a Database.

        Creates a database in the specified branch. A branch can have multiple databases.

        :param parent: str
          The Branch where this Database will be created. Format: projects/{project_id}/branches/{branch_id}
        :param database: :class:`Database`
          The desired specification of a Database.
        :param database_id: str (optional)
          The ID to use for the Database, which will become the final component of the database's resource
          name. This ID becomes the database name in postgres.

          This value should be 4-63 characters, and only use characters available in DNS names, as defined by
          RFC-1123

          If database_id is not specified in the request, it is generated automatically.
        :param replace_existing: bool (optional)
          If true, update the database if it already exists instead of returning an error.

        :returns: :class:`Operation`
        """

        body = database.as_dict()
        query = {}
        if database_id is not None:
            query["database_id"] = database_id
        if replace_existing is not None:
            query["replace_existing"] = replace_existing
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/postgres/{parent}/databases", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return CreateDatabaseOperation(self, operation)

    def create_endpoint(
        self, parent: str, endpoint: Endpoint, endpoint_id: str, *, replace_existing: Optional[bool] = None
    ) -> CreateEndpointOperation:
        """Creates a new compute endpoint in the branch.

        :param parent: str
          The Branch where this Endpoint will be created. Format: projects/{project_id}/branches/{branch_id}
        :param endpoint: :class:`Endpoint`
          The Endpoint to create.
        :param endpoint_id: str
          The ID to use for the Endpoint. This becomes the final component of the endpoint's resource name.
          The ID is required and must be 1-63 characters long, start with a lowercase letter, and contain only
          lowercase letters, numbers, and hyphens. For example, ``primary`` becomes
          ``projects/my-app/branches/development/endpoints/primary``.
        :param replace_existing: bool (optional)
          If true, update the endpoint if it already exists instead of returning an error.

        :returns: :class:`Operation`
        """

        body = endpoint.as_dict()
        query = {}
        if endpoint_id is not None:
            query["endpoint_id"] = endpoint_id
        if replace_existing is not None:
            query["replace_existing"] = replace_existing
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/postgres/{parent}/endpoints", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return CreateEndpointOperation(self, operation)

    def create_project(self, project: Project, project_id: str) -> CreateProjectOperation:
        """Creates a new Lakebase Autoscaling Postgres database project, which contains branches and compute
        endpoints.

        :param project: :class:`Project`
          The Project to create.
        :param project_id: str
          The ID to use for the Project. This becomes the final component of the project's resource name. The
          ID is required and must be 1-63 characters long, start with a lowercase letter, and contain only
          lowercase letters, numbers, and hyphens. For example, ``my-app`` becomes ``projects/my-app``.

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

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/postgres/projects", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return CreateProjectOperation(self, operation)

    def create_replication_group_preview(
        self,
        parent: str,
        replication_group_preview: ReplicationGroupPreview,
        replication_group_preview_id: str,
        *,
        request_id: Optional[str] = None,
    ) -> CreateReplicationGroupPreviewOperation:
        """Creates a new replication group for the project.

        :param parent: str
        :param replication_group_preview: :class:`ReplicationGroupPreview`
        :param replication_group_preview_id: str
        :param request_id: str (optional)

        :returns: :class:`Operation`
        """

        if request_id is None or request_id == "":
            request_id = str(uuid.uuid4())
        body = replication_group_preview.as_dict()
        query = {}
        if replication_group_preview_id is not None:
            query["replication_group_preview_id"] = replication_group_preview_id
        if request_id is not None:
            query["request_id"] = request_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "POST", f"/api/2.0/postgres/{parent}/preview/replication-groups", query=query, body=body, headers=headers
        )
        operation = Operation.from_dict(res)
        return CreateReplicationGroupPreviewOperation(self, operation)

    def create_role(
        self, parent: str, role: Role, *, replace_existing: Optional[bool] = None, role_id: Optional[str] = None
    ) -> CreateRoleOperation:
        """Creates a new Postgres role in the branch.

        :param parent: str
          The Branch where this Role is created. Format: projects/{project_id}/branches/{branch_id}
        :param role: :class:`Role`
          The desired specification of a Role.
        :param replace_existing: bool (optional)
          If true, update the role if it already exists instead of returning an error.

          When the role already exists, the provided ``role`` spec fully replaces the existing one:
          ``membership_roles`` is overwritten, not merged. Leaving ``membership_roles`` empty clears all of
          the role's existing memberships, including ``DATABRICKS_SUPERUSER``. Always send the complete
          desired list of memberships when using this field.
        :param role_id: str (optional)
          The ID to use for the Role, which will become the final component of the role's resource name. This
          ID becomes the role in Postgres.

          This value should be 4-63 characters, and valid characters are lowercase letters, numbers, and
          hyphens, as defined by RFC 1123.

          If role_id is not specified in the request, it is generated automatically.

        :returns: :class:`Operation`
        """

        body = role.as_dict()
        query = {}
        if replace_existing is not None:
            query["replace_existing"] = replace_existing
        if role_id is not None:
            query["role_id"] = role_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/postgres/{parent}/roles", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return CreateRoleOperation(self, operation)

    def create_snapshot(
        self, parent: str, snapshot: Snapshot, *, snapshot_id: Optional[str] = None
    ) -> CreateSnapshotOperation:
        """Creates a snapshot, an immutable point-in-time copy of a branch's data, within the project.

        :param parent: str
          The project in which to create the snapshot. Format: projects/{project_id}
        :param snapshot: :class:`Snapshot`
          The snapshot to create.
        :param snapshot_id: str (optional)
          Client-chosen ID for the snapshot. If omitted, the server generates one.

        :returns: :class:`Operation`
        """

        body = snapshot.as_dict()
        query = {}
        if snapshot_id is not None:
            query["snapshot_id"] = snapshot_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/postgres/{parent}/snapshots", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return CreateSnapshotOperation(self, operation)

    def create_synced_table(self, synced_table: SyncedTable, synced_table_id: str) -> CreateSyncedTableOperation:
        """Create a Synced Table.

        :param synced_table: :class:`SyncedTable`
        :param synced_table_id: str
          The ID to use for the Synced Table. This becomes the final component of the SyncedTable's resource
          name. ID is required and is the synced table name, containing (catalog, schema, table) tuple.
          Elements of the tuple are the UC entity names.

          Example: "{catalog}.{schema}.{table}"

          synced_table_id represents both of the following:

          1. An online VIEW virtual table in the Unity Catalog accessible via the Lakehouse Federation.
          2. Postgres table named "{table}" in schema "{schema}" in the connected Postgres database

        :returns: :class:`Operation`
        """

        body = synced_table.as_dict()
        query = {}
        if synced_table_id is not None:
            query["synced_table_id"] = synced_table_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/postgres/synced_tables", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return CreateSyncedTableOperation(self, operation)

    def create_table(self, table: Table) -> Table:
        """Create a Table (non-synced database table for Autoscaling v2 Lakebase projects).

        :param table: :class:`Table`

        :returns: :class:`Table`
        """

        body = table.as_dict()
        query = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/postgres/tables", body=body, headers=headers)
        return Table.from_dict(res)

    def delete_branch(
        self, name: str, *, allow_missing: Optional[bool] = None, purge: Optional[bool] = None
    ) -> DeleteBranchOperation:
        """Deletes the specified database branch.

        :param name: str
          The full resource path of the branch to delete. Format: projects/{project_id}/branches/{branch_id}
        :param allow_missing: bool (optional)
          If true, if branch does not exists, the request will succeed and no action will be taken. If false
          (default value) and branch does not exists, the request will fail with NOT_FOUND error.
        :param purge: bool (optional)
          If true, permanently delete the branch; if false, soft delete.

        :returns: :class:`Operation`
        """

        query = {}
        if allow_missing is not None:
            query["allow_missing"] = allow_missing
        if purge is not None:
            query["purge"] = purge
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("DELETE", f"/api/2.0/postgres/{name}", query=query, headers=headers)
        operation = Operation.from_dict(res)
        return DeleteBranchOperation(self, operation)

    def delete_catalog(self, name: str) -> DeleteCatalogOperation:
        """Delete a Database Catalog.

        :param name: str
          The full resource path of the catalog to delete.

          Format: "catalogs/{catalog_id}".

        :returns: :class:`Operation`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("DELETE", f"/api/2.0/postgres/{name}", headers=headers)
        operation = Operation.from_dict(res)
        return DeleteCatalogOperation(self, operation)

    def delete_cdf_config(self, name: str, *, force: Optional[bool] = None) -> DeleteCdfConfigOperation:
        """Delete a CDF configuration and stop materializing the change data feed. When force=true, also drops
        the Delta tables in Unity Catalog. When force=false (default), the existing tables are preserved at
        their last state.

        :param name: str
          The resource name of the CdfConfig to delete. Format:
          projects/{project}/branches/{branch}/databases/{database}/cdf-configs/{cdf_config}
        :param force: bool (optional)
          When true, also drops the replicated Delta tables in Unity Catalog. When false (the default), the
          replicated tables are preserved at their last synced state.

        :returns: :class:`Operation`
        """

        query = {}
        if force is not None:
            query["force"] = force
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("DELETE", f"/api/2.0/postgres/{name}", query=query, headers=headers)
        operation = Operation.from_dict(res)
        return DeleteCdfConfigOperation(self, operation)

    def delete_data_api(self, name: str) -> DeleteDataApiOperation:
        """Disable Data API for a database.

        :param name: str
          Resource name: projects/{project_id}/branches/{branch_id}/databases/{database_id}/data-api

        :returns: :class:`Operation`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("DELETE", f"/api/2.0/postgres/{name}", headers=headers)
        operation = Operation.from_dict(res)
        return DeleteDataApiOperation(self, operation)

    def delete_database(self, name: str) -> DeleteDatabaseOperation:
        """Delete a Database.

        :param name: str
          The resource name of the postgres database. Format:
          projects/{project_id}/branches/{branch_id}/databases/{database_id}

        :returns: :class:`Operation`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("DELETE", f"/api/2.0/postgres/{name}", headers=headers)
        operation = Operation.from_dict(res)
        return DeleteDatabaseOperation(self, operation)

    def delete_endpoint(self, name: str) -> DeleteEndpointOperation:
        """Deletes the specified compute endpoint.

        :param name: str
          The full resource path of the endpoint to delete. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}

        :returns: :class:`Operation`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("DELETE", f"/api/2.0/postgres/{name}", headers=headers)
        operation = Operation.from_dict(res)
        return DeleteEndpointOperation(self, operation)

    def delete_forward_etl_configuration(
        self,
        parent: str,
        *,
        pg_database_oid: Optional[int] = None,
        pg_schema_oid: Optional[int] = None,
        tenant_id: Optional[str] = None,
        timeline_id: Optional[str] = None,
    ) -> DeleteForwardEtlConfigurationResponse:
        """Hard delete a Forward ETL configuration and all associated table mappings. Unlike DisableForwardEtl,
        this permanently removes the config and mapping rows.

        :param parent: str
          The Branch to delete Forward ETL configuration for. Format:
          projects/{project_id}/branches/{branch_id}
        :param pg_database_oid: int (optional)
          PostgreSQL database OID to delete configuration for.
        :param pg_schema_oid: int (optional)
          PostgreSQL schema OID to delete configuration for.
        :param tenant_id: str (optional)
          Tenant ID (dashless UUID format).
        :param timeline_id: str (optional)
          Timeline ID (dashless UUID format).

        :returns: :class:`DeleteForwardEtlConfigurationResponse`
        """

        query = {}
        if pg_database_oid is not None:
            query["pg_database_oid"] = pg_database_oid
        if pg_schema_oid is not None:
            query["pg_schema_oid"] = pg_schema_oid
        if tenant_id is not None:
            query["tenant_id"] = tenant_id
        if timeline_id is not None:
            query["timeline_id"] = timeline_id
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "DELETE", f"/api/2.0/postgres/{parent}/forward-etl/configuration", query=query, headers=headers
        )
        return DeleteForwardEtlConfigurationResponse.from_dict(res)

    def delete_project(self, name: str, *, purge: Optional[bool] = None) -> DeleteProjectOperation:
        """Deletes the specified database project.

        :param name: str
          The full resource path of the project to delete. Format: projects/{project_id}
        :param purge: bool (optional)
          If true, permanently deletes the project (hard delete). If false or unset, performs a soft delete.

        :returns: :class:`Operation`
        """

        query = {}
        if purge is not None:
            query["purge"] = purge
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("DELETE", f"/api/2.0/postgres/{name}", query=query, headers=headers)
        operation = Operation.from_dict(res)
        return DeleteProjectOperation(self, operation)

    def delete_recovery_branch_preview(
        self, name: str, *, request_id: Optional[str] = None
    ) -> DeleteRecoveryBranchPreviewOperation:
        """Deletes the specified recovery branch after reconciliation is complete.

        :param name: str
        :param request_id: str (optional)

        :returns: :class:`Operation`
        """

        if request_id is None or request_id == "":
            request_id = str(uuid.uuid4())

        query = {}
        if request_id is not None:
            query["request_id"] = request_id
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("DELETE", f"/api/2.0/postgres/{name}", query=query, headers=headers)
        operation = Operation.from_dict(res)
        return DeleteRecoveryBranchPreviewOperation(self, operation)

    def delete_replication_group_preview(
        self, name: str, *, etag: Optional[str] = None, request_id: Optional[str] = None
    ) -> DeleteReplicationGroupPreviewOperation:
        """Deletes the specified replication group.

        :param name: str
        :param etag: str (optional)
        :param request_id: str (optional)

        :returns: :class:`Operation`
        """

        if request_id is None or request_id == "":
            request_id = str(uuid.uuid4())

        query = {}
        if etag is not None:
            query["etag"] = etag
        if request_id is not None:
            query["request_id"] = request_id
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("DELETE", f"/api/2.0/postgres/{name}", query=query, headers=headers)
        operation = Operation.from_dict(res)
        return DeleteReplicationGroupPreviewOperation(self, operation)

    def delete_role(self, name: str, *, reassign_owned_to: Optional[str] = None) -> DeleteRoleOperation:
        """Deletes the specified Postgres role.

        :param name: str
          The full resource path of the role to delete. Format:
          projects/{project_id}/branches/{branch_id}/roles/{role_id}
        :param reassign_owned_to: str (optional)
          Reassign objects. If this is set, all objects owned by the role are reassigned to the role specified
          in this parameter.

          NOTE: setting this requires spinning up a compute to succeed, since it involves running SQL queries.

        :returns: :class:`Operation`
        """

        query = {}
        if reassign_owned_to is not None:
            query["reassign_owned_to"] = reassign_owned_to
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("DELETE", f"/api/2.0/postgres/{name}", query=query, headers=headers)
        operation = Operation.from_dict(res)
        return DeleteRoleOperation(self, operation)

    def delete_snapshot(self, name: str) -> DeleteSnapshotOperation:
        """Deletes the specified snapshot.

        :param name: str
          The resource name of the snapshot to delete. Format: projects/{project_id}/snapshots/{snapshot_id}

        :returns: :class:`Operation`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("DELETE", f"/api/2.0/postgres/{name}", headers=headers)
        operation = Operation.from_dict(res)
        return DeleteSnapshotOperation(self, operation)

    def delete_synced_table(self, name: str) -> DeleteSyncedTableOperation:
        """Delete a Synced Table.

        :param name: str
          The Full resource name of the synced table, of the format
          "synced_tables/{catalog}.{schema}.{table}", where (catalog, schema, table) are the UC entity names.

        :returns: :class:`Operation`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("DELETE", f"/api/2.0/postgres/{name}", headers=headers)
        operation = Operation.from_dict(res)
        return DeleteSyncedTableOperation(self, operation)

    def delete_table(self, name: str):
        """Delete a Table (non-synced database table for Autoscaling v2 Lakebase projects).

        :param name: str
          Full three-part (catalog, schema, table) name of the table.


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/postgres/tables/{name}", headers=headers)

    def disable_forward_etl(
        self,
        parent: str,
        *,
        pg_database_oid: Optional[int] = None,
        pg_schema_oid: Optional[int] = None,
        tenant_id: Optional[str] = None,
        timeline_id: Optional[str] = None,
    ) -> DisableForwardEtlResponse:
        """Disable Forward ETL for a branch.

        :param parent: str
          The Branch to disable Forward ETL for. Format: projects/{project_id}/branches/{branch_id}
        :param pg_database_oid: int (optional)
          PostgreSQL database OID to disable.
        :param pg_schema_oid: int (optional)
          PostgreSQL schema OID to disable.
        :param tenant_id: str (optional)
          Tenant ID (dashless UUID format).
        :param timeline_id: str (optional)
          Timeline ID (dashless UUID format).

        :returns: :class:`DisableForwardEtlResponse`
        """

        query = {}
        if pg_database_oid is not None:
            query["pg_database_oid"] = pg_database_oid
        if pg_schema_oid is not None:
            query["pg_schema_oid"] = pg_schema_oid
        if tenant_id is not None:
            query["tenant_id"] = tenant_id
        if timeline_id is not None:
            query["timeline_id"] = timeline_id
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("DELETE", f"/api/2.0/postgres/{parent}/forward-etl", query=query, headers=headers)
        return DisableForwardEtlResponse.from_dict(res)

    def failover_replication_group_preview(
        self, name: str, target_workspace: str, *, etag: Optional[str] = None, request_id: Optional[str] = None
    ) -> FailoverReplicationGroupPreviewOperation:
        """Fails over the replication group to a target workspace, promoting the secondary to primary.

        :param name: str
        :param target_workspace: str
        :param etag: str (optional)
        :param request_id: str (optional)

        :returns: :class:`Operation`
        """

        if request_id is None or request_id == "":
            request_id = str(uuid.uuid4())
        body = {}
        if etag is not None:
            body["etag"] = etag
        if request_id is not None:
            body["request_id"] = request_id
        if target_workspace is not None:
            body["target_workspace"] = target_workspace
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/postgres/{name}/failover", body=body, headers=headers)
        operation = Operation.from_dict(res)
        return FailoverReplicationGroupPreviewOperation(self, operation)

    def generate_database_credential(
        self,
        endpoint: str,
        *,
        claims: Optional[List[RequestedClaims]] = None,
        expire_time: Optional[Timestamp] = None,
        group_name: Optional[str] = None,
        ttl: Optional[Duration] = None,
    ) -> DatabaseCredential:
        """Generate OAuth credentials for a Postgres database.

        :param endpoint: str
          The endpoint resource name for which this credential will be generated. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}
        :param claims: List[:class:`RequestedClaims`] (optional)
          The returned token will be scoped to UC tables with the specified permissions.
        :param expire_time: Timestamp (optional)
          Timestamp in UTC of when this credential should expire. Must be at least 300 seconds (5 minutes) and
          at most 1 hour from the current time.
        :param group_name: str (optional)
          Databricks workspace group name. When provided, credentials are generated with permissions scoped to
          this group.
        :param ttl: Duration (optional)
          The requested time-to-live for the generated credential token. Must be at least 300 seconds (5
          minutes) and at most 3600 seconds (1 hour).

        :returns: :class:`DatabaseCredential`
        """

        body = {}
        if claims is not None:
            body["claims"] = [v.as_dict() for v in claims]
        if endpoint is not None:
            body["endpoint"] = endpoint
        if expire_time is not None:
            body["expire_time"] = expire_time.ToJsonString()
        if group_name is not None:
            body["group_name"] = group_name
        if ttl is not None:
            body["ttl"] = ttl.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/postgres/credentials", body=body, headers=headers)
        return DatabaseCredential.from_dict(res)

    def get_branch(self, name: str) -> Branch:
        """Retrieves information about the specified database branch.

        :param name: str
          The full resource path of the branch to retrieve. Format: projects/{project_id}/branches/{branch_id}

        :returns: :class:`Branch`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return Branch.from_dict(res)

    def get_catalog(self, name: str) -> Catalog:
        """Get a Database Catalog.

        :param name: str
          The full resource path of the catalog to retrieve.

          Format: "catalogs/{catalog_id}".

        :returns: :class:`Catalog`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return Catalog.from_dict(res)

    def get_cdf_config(self, name: str) -> CdfConfig:
        """Get a single Lakebase CDF configuration, including the source Postgres schema, target Unity Catalog
        schema, and the identity under which writes are authorized.

        :param name: str
          The resource name of the CdfConfig to retrieve. Format:
          projects/{project}/branches/{branch}/databases/{database}/cdf-configs/{cdf_config}

        :returns: :class:`CdfConfig`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return CdfConfig.from_dict(res)

    def get_cdf_status(self, name: str) -> CdfStatus:
        """Get the CDF status of a single table within a Lakebase CDF configuration, including its current state
        and the last committed position in the feed.

        :param name: str
          The resource name of the CdfStatus to retrieve. Format:
          projects/{project}/branches/{branch}/databases/{database}/cdf-configs/{cdf_config}/cdf-statuses/{cdf_status}

        :returns: :class:`CdfStatus`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return CdfStatus.from_dict(res)

    def get_compute_instance(self, name: str) -> ComputeInstance:
        """Lists the specific compute instance under an endpoint. Note: ComputeInstances are managed via the
        parent Endpoint resource, and cannot be created, updated, or deleted directly.

        :param name: str
          The full resource path of the compute instance to retrieve. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}/compute-instances/{compute_instance_id}

        :returns: :class:`ComputeInstance`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return ComputeInstance.from_dict(res)

    def get_data_api(self, name: str) -> DataApi:
        """Get Data API configuration for a database.

        :param name: str
          Resource name: projects/{project_id}/branches/{branch_id}/databases/{database_id}/data-api

        :returns: :class:`DataApi`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return DataApi.from_dict(res)

    def get_database(self, name: str) -> Database:
        """Get a Database.

        :param name: str
          The name of the Database to retrieve. Format:
          projects/{project_id}/branches/{branch_id}/databases/{database_id}

        :returns: :class:`Database`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return Database.from_dict(res)

    def get_endpoint(self, name: str) -> Endpoint:
        """Retrieves information about the specified compute endpoint, including its connection details and
        operational state.

        :param name: str
          The full resource path of the endpoint to retrieve. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}

        :returns: :class:`Endpoint`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return Endpoint.from_dict(res)

    def get_forward_etl_metadata(
        self, parent: str, *, tenant_id: Optional[str] = None, timeline_id: Optional[str] = None
    ) -> ForwardEtlMetadata:
        """Get Forward ETL metadata (database and schema OIDs).

        :param parent: str
          The Branch to get metadata for. Format: projects/{project_id}/branches/{branch_id}
        :param tenant_id: str (optional)
          Tenant ID (dashless UUID format).
        :param timeline_id: str (optional)
          Timeline ID (dashless UUID format).

        :returns: :class:`ForwardEtlMetadata`
        """

        query = {}
        if tenant_id is not None:
            query["tenant_id"] = tenant_id
        if timeline_id is not None:
            query["timeline_id"] = timeline_id
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/{parent}/forward-etl/metadata", query=query, headers=headers)
        return ForwardEtlMetadata.from_dict(res)

    def get_forward_etl_status(
        self, parent: str, *, tenant_id: Optional[str] = None, timeline_id: Optional[str] = None
    ) -> ForwardEtlStatus:
        """Get Forward ETL configuration and status for a branch.

        :param parent: str
          The Branch to get Forward ETL status for. Format: projects/{project_id}/branches/{branch_id}
        :param tenant_id: str (optional)
          Tenant ID (dashless UUID format).
        :param timeline_id: str (optional)
          Timeline ID (dashless UUID format).

        :returns: :class:`ForwardEtlStatus`
        """

        query = {}
        if tenant_id is not None:
            query["tenant_id"] = tenant_id
        if timeline_id is not None:
            query["timeline_id"] = timeline_id
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/{parent}/forward-etl", query=query, headers=headers)
        return ForwardEtlStatus.from_dict(res)

    def get_operation(self, name: str) -> Operation:
        """Retrieves the status of a long-running operation.

        :param name: str
          The name of the operation resource.

        :returns: :class:`Operation`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return Operation.from_dict(res)

    def get_project(self, name: str) -> Project:
        """Retrieves information about the specified database project.

        :param name: str
          The full resource path of the project to retrieve. Format: projects/{project_id}

        :returns: :class:`Project`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return Project.from_dict(res)

    def get_recovery_branch_preview(self, name: str) -> RecoveryBranchPreview:
        """Retrieves information about the specified recovery branch.

        :param name: str

        :returns: :class:`RecoveryBranchPreview`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return RecoveryBranchPreview.from_dict(res)

    def get_replication_group_preview(self, name: str) -> ReplicationGroupPreview:
        """Retrieves information about the specified replication group.

        :param name: str

        :returns: :class:`ReplicationGroupPreview`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return ReplicationGroupPreview.from_dict(res)

    def get_role(self, name: str) -> Role:
        """Retrieves information about the specified Postgres role, including its authentication method and
        permissions.

        :param name: str
          The full resource path of the role to retrieve. Format:
          projects/{project_id}/branches/{branch_id}/roles/{role_id}

        :returns: :class:`Role`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return Role.from_dict(res)

    def get_snapshot(self, name: str) -> Snapshot:
        """Retrieves information about the specified snapshot.

        :param name: str
          The resource name of the snapshot to retrieve. Format: projects/{project_id}/snapshots/{snapshot_id}

        :returns: :class:`Snapshot`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return Snapshot.from_dict(res)

    def get_snapshot_schedule(self, name: str) -> SnapshotSchedule:
        """Retrieves the snapshot schedule for a branch. A branch with no configured schedule returns an empty
        schedule (not NOT_FOUND).

        :param name: str
          The resource name of the branch's snapshot schedule. Format:
          projects/{project_id}/branches/{branch_id}/snapshot-schedule

        :returns: :class:`SnapshotSchedule`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return SnapshotSchedule.from_dict(res)

    def get_synced_table(self, name: str) -> SyncedTable:
        """Get a Synced Table.

        :param name: str
          The Full resource name of the synced table. Format: "synced_tables/{catalog}.{schema}.{table}",
          where (catalog, schema, table) are the entity names in the Unity Catalog.

        :returns: :class:`SyncedTable`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/{name}", headers=headers)
        return SyncedTable.from_dict(res)

    def get_table(self, name: str) -> Table:
        """Get a Table (non-synced database table for Autoscaling v2 Lakebase projects).

        :param name: str
          Full three-part (catalog, schema, table) name of the table.

        :returns: :class:`Table`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/postgres/tables/{name}", headers=headers)
        return Table.from_dict(res)

    def inspect_recovery_branch_preview(
        self, name: str, branch_id: str, *, request_id: Optional[str] = None
    ) -> InspectRecoveryBranchPreviewOperation:
        """Materializes a temporary inspection branch from the specified recovery branch for data examination.

        :param name: str
          The recovery branch from which to create the inspection branch.
        :param branch_id: str
          Caller-supplied id for the inspection Branch this custom method materializes.
        :param request_id: str (optional)

        :returns: :class:`Operation`
        """

        if request_id is None or request_id == "":
            request_id = str(uuid.uuid4())
        body = {}
        if branch_id is not None:
            body["branch_id"] = branch_id
        if request_id is not None:
            body["request_id"] = request_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/postgres/{name}/inspect", body=body, headers=headers)
        operation = Operation.from_dict(res)
        return InspectRecoveryBranchPreviewOperation(self, operation)

    def list_branches(
        self,
        parent: str,
        *,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        show_deleted: Optional[bool] = None,
    ) -> Iterator[Branch]:
        """Returns a paginated list of database branches in the project.

        :param parent: str
          The Project that owns this collection of branches. Format: projects/{project_id}
        :param page_size: int (optional)
          Upper bound for items returned. Cannot be negative.
        :param page_token: str (optional)
          Page token from a previous response. If not provided, returns the first page.
        :param show_deleted: bool (optional)
          Whether to include soft-deleted branches in the response. When true, deleted branches are included
          alongside active branches. Purged branches are never returned.

        :returns: Iterator over :class:`Branch`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        if show_deleted is not None:
            query["show_deleted"] = show_deleted
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", f"/api/2.0/postgres/{parent}/branches", query=query, headers=headers)
            if "branches" in json:
                for v in json["branches"]:
                    yield Branch.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_cdf_configs(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[CdfConfig]:
        """List all CDF configurations for a Lakebase database. Each configuration maps a Postgres schema to a
        Unity Catalog schema where the change data feed is materialized.

        :param parent: str
          The parent database to list CdfConfigs for. Format:
          projects/{project}/branches/{branch}/databases/{database}
        :param page_size: int (optional)
          Maximum number of CdfConfigs to return.
        :param page_token: str (optional)
          Pagination token returned by a previous ListCdfConfigs call. Empty on the first page.

        :returns: Iterator over :class:`CdfConfig`
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
            json = self._api.do("GET", f"/api/2.0/postgres/{parent}/cdf-configs", query=query, headers=headers)
            if "cdf_configs" in json:
                for v in json["cdf_configs"]:
                    yield CdfConfig.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_cdf_statuses(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[CdfStatus]:
        """List the per-table CDF statuses within a Lakebase CDF configuration. Each status shows whether a
        table's change data feed is snapshotting, streaming, or skipped.

        :param parent: str
          The parent CdfConfig to list CdfStatuses for. Format:
          projects/{project}/branches/{branch}/databases/{database}/cdf-configs/{cdf_config}
        :param page_size: int (optional)
          Maximum number of CdfStatuses to return.
        :param page_token: str (optional)
          Pagination token returned by a previous ListCdfStatuses call. Empty on the first page.

        :returns: Iterator over :class:`CdfStatus`
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
            json = self._api.do("GET", f"/api/2.0/postgres/{parent}/cdf-statuses", query=query, headers=headers)
            if "cdf_statuses" in json:
                for v in json["cdf_statuses"]:
                    yield CdfStatus.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_compute_instances(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[ComputeInstance]:
        """Lists all compute instances that have been created under the specified endpoint. Note:
        ComputeInstances are managed via the parent Endpoint resource, and cannot be created, updated, or
        deleted directly.

        :param parent: str
          The parent, which owns the compute instances.
        :param page_size: int (optional)
          The maximum number of compute instances to return. The service may return fewer than this value.

          If unspecified, at most 50 compute instances will be returned. The maximum value is 1000; values
          above 1000 will be coerced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous ``ListInstances`` call. Provide this to retrieve the
          subsequent page.

          When paginating, all other parameters provided to ``ListInstances`` must match the call that
          provided the page token.

        :returns: Iterator over :class:`ComputeInstance`
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
            json = self._api.do("GET", f"/api/2.0/postgres/{parent}/compute-instances", query=query, headers=headers)
            if "compute_instances" in json:
                for v in json["compute_instances"]:
                    yield ComputeInstance.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_databases(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Database]:
        """List Databases.

        :param parent: str
          The Branch that owns this collection of databases. Format:
          projects/{project_id}/branches/{branch_id}
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Databases. Requests first page if absent.

        :returns: Iterator over :class:`Database`
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
            json = self._api.do("GET", f"/api/2.0/postgres/{parent}/databases", query=query, headers=headers)
            if "databases" in json:
                for v in json["databases"]:
                    yield Database.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_endpoints(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Endpoint]:
        """Returns a paginated list of compute endpoints in the branch.

        :param parent: str
          The Branch that owns this collection of endpoints. Format:
          projects/{project_id}/branches/{branch_id}
        :param page_size: int (optional)
          Upper bound for items returned. Cannot be negative.
        :param page_token: str (optional)
          Page token from a previous response. If not provided, returns the first page.

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

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", f"/api/2.0/postgres/{parent}/endpoints", query=query, headers=headers)
            if "endpoints" in json:
                for v in json["endpoints"]:
                    yield Endpoint.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_projects(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None, show_deleted: Optional[bool] = None
    ) -> Iterator[Project]:
        """Returns a paginated list of database projects in the workspace that the user has permission to access.

        :param page_size: int (optional)
          Upper bound for items returned. Cannot be negative. The maximum value is 100.
        :param page_token: str (optional)
          Page token from a previous response. If not provided, returns the first page.
        :param show_deleted: bool (optional)
          Whether to include soft-deleted projects in the response. When true, soft-deleted projects are
          included alongside active projects. Hard-deleted and already-purged projects are never returned.

        :returns: Iterator over :class:`Project`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        if show_deleted is not None:
            query["show_deleted"] = show_deleted
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", "/api/2.0/postgres/projects", query=query, headers=headers)
            if "projects" in json:
                for v in json["projects"]:
                    yield Project.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_recovery_branch_previews(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[RecoveryBranchPreview]:
        """Returns a paginated list of recovery branches for the project.

        :param parent: str
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`RecoveryBranchPreview`
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
            json = self._api.do(
                "GET", f"/api/2.0/postgres/{parent}/preview/recovery-branches", query=query, headers=headers
            )
            if "recovery_branch_previews" in json:
                for v in json["recovery_branch_previews"]:
                    yield RecoveryBranchPreview.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_replication_group_previews(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[ReplicationGroupPreview]:
        """Returns a paginated list of replication groups for the project.

        :param parent: str
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`ReplicationGroupPreview`
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
            json = self._api.do(
                "GET", f"/api/2.0/postgres/{parent}/preview/replication-groups", query=query, headers=headers
            )
            if "replication_group_previews" in json:
                for v in json["replication_group_previews"]:
                    yield ReplicationGroupPreview.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_roles(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Role]:
        """Returns a paginated list of Postgres roles in the branch.

        :param parent: str
          The Branch that owns this collection of roles. Format: projects/{project_id}/branches/{branch_id}
        :param page_size: int (optional)
          Upper bound for items returned. Cannot be negative.
        :param page_token: str (optional)
          Page token from a previous response. If not provided, returns the first page.

        :returns: Iterator over :class:`Role`
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
            json = self._api.do("GET", f"/api/2.0/postgres/{parent}/roles", query=query, headers=headers)
            if "roles" in json:
                for v in json["roles"]:
                    yield Role.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_snapshots(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Snapshot]:
        """Returns a paginated list of snapshots in the project.

        :param parent: str
          The project that owns the snapshots. Format: projects/{project_id}
        :param page_size: int (optional)
          Maximum number of snapshots to return per page.
        :param page_token: str (optional)
          Page token from a previous response; omit for the first page.

        :returns: Iterator over :class:`Snapshot`
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
            json = self._api.do("GET", f"/api/2.0/postgres/{parent}/snapshots", query=query, headers=headers)
            if "snapshots" in json:
                for v in json["snapshots"]:
                    yield Snapshot.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def switchover_replication_group_preview(
        self, name: str, target_workspace: str, *, etag: Optional[str] = None, request_id: Optional[str] = None
    ) -> SwitchoverReplicationGroupPreviewOperation:
        """Switches over the replication group to a target workspace with a coordinated failover.

        :param name: str
        :param target_workspace: str
        :param etag: str (optional)
        :param request_id: str (optional)

        :returns: :class:`Operation`
        """

        if request_id is None or request_id == "":
            request_id = str(uuid.uuid4())
        body = {}
        if etag is not None:
            body["etag"] = etag
        if request_id is not None:
            body["request_id"] = request_id
        if target_workspace is not None:
            body["target_workspace"] = target_workspace
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/postgres/{name}/switchover", body=body, headers=headers)
        operation = Operation.from_dict(res)
        return SwitchoverReplicationGroupPreviewOperation(self, operation)

    def undelete_branch(self, name: str) -> UndeleteBranchOperation:
        """Undeletes the specified database branch.

        :param name: str
          The full resource path of the branch to undelete. Format: projects/{project_id}/branches/{branch_id}

        :returns: :class:`Operation`
        """

        body = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/postgres/{name}/undelete", body=body, headers=headers)
        operation = Operation.from_dict(res)
        return UndeleteBranchOperation(self, operation)

    def undelete_project(self, name: str) -> UndeleteProjectOperation:
        """Undeletes a soft-deleted project.

        :param name: str
          The full resource path of the project to undelete. Format: projects/{project_id}

        :returns: :class:`Operation`
        """

        body = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/postgres/{name}/undelete", body=body, headers=headers)
        operation = Operation.from_dict(res)
        return UndeleteProjectOperation(self, operation)

    def update_branch(self, name: str, branch: Branch, update_mask: FieldMask) -> UpdateBranchOperation:
        """Updates the specified database branch. You can set this branch as the project's default branch, or
        protect/unprotect it.

        :param name: str
          Output only. The full resource path of the branch. Format:
          projects/{project_id}/branches/{branch_id}
        :param branch: :class:`Branch`
          The Branch to update.

          The branch's ``name`` field is used to identify the branch to update. Format:
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

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/postgres/{name}", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return UpdateBranchOperation(self, operation)

    def update_data_api(self, name: str, data_api: DataApi, update_mask: FieldMask) -> UpdateDataApiOperation:
        """Update Data API configuration for a database.

        :param name: str
          Resource name: projects/{project_id}/branches/{branch_id}/databases/{database_id}/data-api
        :param data_api: :class:`DataApi`
          The Data API configuration to update. The data_api's ``name`` field identifies the resource.
        :param update_mask: FieldMask
          The list of fields to update. If unspecified, all fields will be updated when possible.

        :returns: :class:`Operation`
        """

        body = data_api.as_dict()
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

        res = self._api.do("PATCH", f"/api/2.0/postgres/{name}", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return UpdateDataApiOperation(self, operation)

    def update_database(self, name: str, database: Database, update_mask: FieldMask) -> UpdateDatabaseOperation:
        """Update a Database.

        :param name: str
          The resource name of the database. Format:
          projects/{project_id}/branches/{branch_id}/databases/{database_id}
        :param database: :class:`Database`
          The Database to update.

          The database's ``name`` field is used to identify the database to update. Format:
          projects/{project_id}/branches/{branch_id}/databases/{database_id}
        :param update_mask: FieldMask
          The list of fields to update. If unspecified, all fields will be updated when possible.

        :returns: :class:`Operation`
        """

        body = database.as_dict()
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

        res = self._api.do("PATCH", f"/api/2.0/postgres/{name}", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return UpdateDatabaseOperation(self, operation)

    def update_endpoint(self, name: str, endpoint: Endpoint, update_mask: FieldMask) -> UpdateEndpointOperation:
        """Updates the specified compute endpoint. You can update autoscaling limits, suspend timeout, or
        enable/disable the compute endpoint.

        :param name: str
          Output only. The full resource path of the endpoint. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}
        :param endpoint: :class:`Endpoint`
          The Endpoint to update.

          The endpoint's ``name`` field is used to identify the endpoint to update. Format:
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

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/postgres/{name}", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return UpdateEndpointOperation(self, operation)

    def update_project(self, name: str, project: Project, update_mask: FieldMask) -> UpdateProjectOperation:
        """Updates the specified database project.

        :param name: str
          Output only. The full resource path of the project. Format: projects/{project_id}
        :param project: :class:`Project`
          The Project to update.

          The project's ``name`` field is used to identify the project to update. Format:
          projects/{project_id}
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

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/postgres/{name}", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return UpdateProjectOperation(self, operation)

    def update_replication_group_preview(
        self,
        name: str,
        replication_group_preview: ReplicationGroupPreview,
        update_mask: FieldMask,
        *,
        request_id: Optional[str] = None,
    ) -> UpdateReplicationGroupPreviewOperation:
        """Updates the specified replication group.

        :param name: str
          The resource name of the replication group. Format:
          projects/{project_id}/preview/replication-groups/{replication_group_id}
        :param replication_group_preview: :class:`ReplicationGroupPreview`
        :param update_mask: FieldMask
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g.,
          ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of ``*`` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using ``*`` wildcards, as it can lead to unintended results if the
          API changes in the future.
        :param request_id: str (optional)

        :returns: :class:`Operation`
        """

        if request_id is None or request_id == "":
            request_id = str(uuid.uuid4())
        body = replication_group_preview.as_dict()
        query = {}
        if request_id is not None:
            query["request_id"] = request_id
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/postgres/{name}", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return UpdateReplicationGroupPreviewOperation(self, operation)

    def update_role(self, name: str, role: Role, update_mask: FieldMask) -> UpdateRoleOperation:
        """Update a role for a branch.

        :param name: str
          Output only. The full resource path of the role. Format:
          projects/{project_id}/branches/{branch_id}/roles/{role_id}
        :param role: :class:`Role`
          The Postgres Role to update.

          The role's ``name`` field is used to identify the role to update. Format:
          projects/{project_id}/branches/{branch_id}/roles/{role_id}
        :param update_mask: FieldMask
          The list of fields to update in Postgres Role. If unspecified, all fields will be updated when
          possible.

        :returns: :class:`Operation`
        """

        body = role.as_dict()
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

        res = self._api.do("PATCH", f"/api/2.0/postgres/{name}", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return UpdateRoleOperation(self, operation)

    def update_snapshot(self, name: str, snapshot: Snapshot, update_mask: FieldMask) -> UpdateSnapshotOperation:
        """Updates the specified snapshot. You can change or disable its expiration policy.

        :param name: str
          The resource name of the snapshot. Format: projects/{project_id}/snapshots/{snapshot_id}
        :param snapshot: :class:`Snapshot`
          The snapshot to update. Its ``name`` identifies the snapshot. Format:
          projects/{project_id}/snapshots/{snapshot_id}
        :param update_mask: FieldMask
          Fields to update. The only updatable path is ``spec.expiration``.

        :returns: :class:`Operation`
        """

        body = snapshot.as_dict()
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

        res = self._api.do("PATCH", f"/api/2.0/postgres/{name}", query=query, body=body, headers=headers)
        operation = Operation.from_dict(res)
        return UpdateSnapshotOperation(self, operation)

    def update_snapshot_schedule(
        self, name: str, snapshot_schedule: SnapshotSchedule, update_mask: FieldMask
    ) -> SnapshotSchedule:
        """Sets the snapshot schedule for a branch. The ``schedule`` field is replaced wholesale; an empty
        schedule disables automatic snapshots.

        :param name: str
          The resource name of the branch's snapshot schedule. Format:
          projects/{project_id}/branches/{branch_id}/snapshot-schedule
        :param snapshot_schedule: :class:`SnapshotSchedule`
          The snapshot schedule to set. Its ``name`` identifies the branch. Format:
          projects/{project_id}/branches/{branch_id}/snapshot-schedule
        :param update_mask: FieldMask
          Fields to update. The only updatable path is ``schedule``, which replaces the entire set of
          cadences.

        :returns: :class:`SnapshotSchedule`
        """

        body = snapshot_schedule.as_dict()
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

        res = self._api.do("PATCH", f"/api/2.0/postgres/{name}", query=query, body=body, headers=headers)
        return SnapshotSchedule.from_dict(res)


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


class CreateCatalogOperation:
    """Long-running operation for create_catalog"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> Catalog:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Catalog`
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

            catalog = Catalog.from_dict(operation.response)

            return catalog, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> CatalogOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`CatalogOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return CatalogOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class CreateCdfConfigOperation:
    """Long-running operation for create_cdf_config"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> CdfConfig:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`CdfConfig`
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

            cdf_config = CdfConfig.from_dict(operation.response)

            return cdf_config, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> CdfConfigOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`CdfConfigOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return CdfConfigOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class CreateDataApiOperation:
    """Long-running operation for create_data_api"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> DataApi:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`DataApi`
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

            data_api = DataApi.from_dict(operation.response)

            return data_api, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> DataApiOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`DataApiOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return DataApiOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class CreateDatabaseOperation:
    """Long-running operation for create_database"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> Database:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Database`
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

            database = Database.from_dict(operation.response)

            return database, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> DatabaseOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`DatabaseOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return DatabaseOperationMetadata.from_dict(self._operation.metadata)

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


class CreateReplicationGroupPreviewOperation:
    """Long-running operation for create_replication_group_preview"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> ReplicationGroupPreview:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`ReplicationGroupPreview`
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

            replication_group_preview = ReplicationGroupPreview.from_dict(operation.response)

            return replication_group_preview, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> ReplicationGroupPreviewOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`ReplicationGroupPreviewOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return ReplicationGroupPreviewOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class CreateRoleOperation:
    """Long-running operation for create_role"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> Role:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Role`
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

            role = Role.from_dict(operation.response)

            return role, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> RoleOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`RoleOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return RoleOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class CreateSnapshotOperation:
    """Long-running operation for create_snapshot"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> Snapshot:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Snapshot`
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

            snapshot = Snapshot.from_dict(operation.response)

            return snapshot, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> SnapshotOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`SnapshotOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return SnapshotOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class CreateSyncedTableOperation:
    """Long-running operation for create_synced_table"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> SyncedTable:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`SyncedTable`
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

            synced_table = SyncedTable.from_dict(operation.response)

            return synced_table, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> SyncedTableOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`SyncedTableOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return SyncedTableOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class DeleteBranchOperation:
    """Long-running operation for delete_branch"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None):
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Any /* MISSING TYPE */`
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

            return {}, None

        poll(poll_operation, timeout=opts.timeout if opts is not None else None)

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


class DeleteCatalogOperation:
    """Long-running operation for delete_catalog"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None):
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Any /* MISSING TYPE */`
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

            return {}, None

        poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> CatalogOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`CatalogOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return CatalogOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class DeleteCdfConfigOperation:
    """Long-running operation for delete_cdf_config"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None):
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Any /* MISSING TYPE */`
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

            return {}, None

        poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> CdfConfigOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`CdfConfigOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return CdfConfigOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class DeleteDataApiOperation:
    """Long-running operation for delete_data_api"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None):
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Any /* MISSING TYPE */`
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

            return {}, None

        poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> DataApiOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`DataApiOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return DataApiOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class DeleteDatabaseOperation:
    """Long-running operation for delete_database"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None):
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Any /* MISSING TYPE */`
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

            return {}, None

        poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> DatabaseOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`DatabaseOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return DatabaseOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class DeleteEndpointOperation:
    """Long-running operation for delete_endpoint"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None):
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Any /* MISSING TYPE */`
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

            return {}, None

        poll(poll_operation, timeout=opts.timeout if opts is not None else None)

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


class DeleteProjectOperation:
    """Long-running operation for delete_project"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None):
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Any /* MISSING TYPE */`
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

            return {}, None

        poll(poll_operation, timeout=opts.timeout if opts is not None else None)

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


class DeleteRecoveryBranchPreviewOperation:
    """Long-running operation for delete_recovery_branch_preview"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None):
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Any /* MISSING TYPE */`
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

            return {}, None

        poll(poll_operation, timeout=opts.timeout if opts is not None else None)

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


class DeleteReplicationGroupPreviewOperation:
    """Long-running operation for delete_replication_group_preview"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None):
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Any /* MISSING TYPE */`
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

            return {}, None

        poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> ReplicationGroupPreviewOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`ReplicationGroupPreviewOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return ReplicationGroupPreviewOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class DeleteRoleOperation:
    """Long-running operation for delete_role"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None):
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Any /* MISSING TYPE */`
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

            return {}, None

        poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> RoleOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`RoleOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return RoleOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class DeleteSnapshotOperation:
    """Long-running operation for delete_snapshot"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None):
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Any /* MISSING TYPE */`
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

            return {}, None

        poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> SnapshotOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`SnapshotOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return SnapshotOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class DeleteSyncedTableOperation:
    """Long-running operation for delete_synced_table"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None):
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Any /* MISSING TYPE */`
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

            return {}, None

        poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> SyncedTableOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`SyncedTableOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return SyncedTableOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class FailoverReplicationGroupPreviewOperation:
    """Long-running operation for failover_replication_group_preview"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> ReplicationGroupPreview:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`ReplicationGroupPreview`
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

            replication_group_preview = ReplicationGroupPreview.from_dict(operation.response)

            return replication_group_preview, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> ReplicationGroupPreviewOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`ReplicationGroupPreviewOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return ReplicationGroupPreviewOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class InspectRecoveryBranchPreviewOperation:
    """Long-running operation for inspect_recovery_branch_preview"""

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


class SwitchoverReplicationGroupPreviewOperation:
    """Long-running operation for switchover_replication_group_preview"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> ReplicationGroupPreview:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`ReplicationGroupPreview`
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

            replication_group_preview = ReplicationGroupPreview.from_dict(operation.response)

            return replication_group_preview, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> ReplicationGroupPreviewOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`ReplicationGroupPreviewOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return ReplicationGroupPreviewOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class UndeleteBranchOperation:
    """Long-running operation for undelete_branch"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None):
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Any /* MISSING TYPE */`
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

            return {}, None

        poll(poll_operation, timeout=opts.timeout if opts is not None else None)

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


class UndeleteProjectOperation:
    """Long-running operation for undelete_project"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None):
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Any /* MISSING TYPE */`
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

            return {}, None

        poll(poll_operation, timeout=opts.timeout if opts is not None else None)

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


class UpdateDataApiOperation:
    """Long-running operation for update_data_api"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> DataApi:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`DataApi`
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

            data_api = DataApi.from_dict(operation.response)

            return data_api, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> DataApiOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`DataApiOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return DataApiOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class UpdateDatabaseOperation:
    """Long-running operation for update_database"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> Database:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Database`
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

            database = Database.from_dict(operation.response)

            return database, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> DatabaseOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`DatabaseOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return DatabaseOperationMetadata.from_dict(self._operation.metadata)

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


class UpdateReplicationGroupPreviewOperation:
    """Long-running operation for update_replication_group_preview"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> ReplicationGroupPreview:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`ReplicationGroupPreview`
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

            replication_group_preview = ReplicationGroupPreview.from_dict(operation.response)

            return replication_group_preview, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> ReplicationGroupPreviewOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`ReplicationGroupPreviewOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return ReplicationGroupPreviewOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class UpdateRoleOperation:
    """Long-running operation for update_role"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> Role:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Role`
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

            role = Role.from_dict(operation.response)

            return role, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> RoleOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`RoleOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return RoleOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class UpdateSnapshotOperation:
    """Long-running operation for update_snapshot"""

    def __init__(self, impl: PostgresAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> Snapshot:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`Snapshot`
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

            snapshot = Snapshot.from_dict(operation.response)

            return snapshot, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> SnapshotOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`SnapshotOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return SnapshotOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done

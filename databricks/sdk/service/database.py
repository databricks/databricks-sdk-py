# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List, Optional

from ._internal import _enum, _from_dict, _repeated_dict

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class DatabaseCatalog:
    name: str
    """The name of the catalog in UC."""

    database_instance_name: str
    """The name of the DatabaseInstance housing the database."""

    database_name: str
    """The name of the database (in a instance) associated with the catalog."""

    create_database_if_not_exists: Optional[bool] = None

    uid: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the DatabaseCatalog into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_database_if_not_exists is not None:
            body["create_database_if_not_exists"] = self.create_database_if_not_exists
        if self.database_instance_name is not None:
            body["database_instance_name"] = self.database_instance_name
        if self.database_name is not None:
            body["database_name"] = self.database_name
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
        if self.database_instance_name is not None:
            body["database_instance_name"] = self.database_instance_name
        if self.database_name is not None:
            body["database_name"] = self.database_name
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
            database_instance_name=d.get("database_instance_name", None),
            database_name=d.get("database_name", None),
            name=d.get("name", None),
            uid=d.get("uid", None),
        )


@dataclass
class DatabaseCredential:
    token: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the DatabaseCredential into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.token is not None:
            body["token"] = self.token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabaseCredential into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.token is not None:
            body["token"] = self.token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabaseCredential:
        """Deserializes the DatabaseCredential from a dictionary."""
        return cls(token=d.get("token", None))


@dataclass
class DatabaseInstance:
    """A DatabaseInstance represents a logical Postgres instance, comprised of both compute and
    storage."""

    name: str
    """The name of the instance. This is the unique identifier for the instance."""

    capacity: Optional[str] = None
    """The sku of the instance. Valid values are "CU_1", "CU_2", "CU_4", "CU_8"."""

    creation_time: Optional[str] = None
    """The timestamp when the instance was created."""

    creator: Optional[str] = None
    """The email of the creator of the instance."""

    pg_version: Optional[str] = None
    """The version of Postgres running on the instance."""

    read_write_dns: Optional[str] = None
    """The DNS endpoint to connect to the instance for read+write access."""

    state: Optional[DatabaseInstanceState] = None
    """The current state of the instance."""

    stopped: Optional[bool] = None
    """Whether the instance is stopped."""

    uid: Optional[str] = None
    """An immutable UUID identifier for the instance."""

    def as_dict(self) -> dict:
        """Serializes the DatabaseInstance into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.capacity is not None:
            body["capacity"] = self.capacity
        if self.creation_time is not None:
            body["creation_time"] = self.creation_time
        if self.creator is not None:
            body["creator"] = self.creator
        if self.name is not None:
            body["name"] = self.name
        if self.pg_version is not None:
            body["pg_version"] = self.pg_version
        if self.read_write_dns is not None:
            body["read_write_dns"] = self.read_write_dns
        if self.state is not None:
            body["state"] = self.state.value
        if self.stopped is not None:
            body["stopped"] = self.stopped
        if self.uid is not None:
            body["uid"] = self.uid
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabaseInstance into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.capacity is not None:
            body["capacity"] = self.capacity
        if self.creation_time is not None:
            body["creation_time"] = self.creation_time
        if self.creator is not None:
            body["creator"] = self.creator
        if self.name is not None:
            body["name"] = self.name
        if self.pg_version is not None:
            body["pg_version"] = self.pg_version
        if self.read_write_dns is not None:
            body["read_write_dns"] = self.read_write_dns
        if self.state is not None:
            body["state"] = self.state
        if self.stopped is not None:
            body["stopped"] = self.stopped
        if self.uid is not None:
            body["uid"] = self.uid
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabaseInstance:
        """Deserializes the DatabaseInstance from a dictionary."""
        return cls(
            capacity=d.get("capacity", None),
            creation_time=d.get("creation_time", None),
            creator=d.get("creator", None),
            name=d.get("name", None),
            pg_version=d.get("pg_version", None),
            read_write_dns=d.get("read_write_dns", None),
            state=_enum(d, "state", DatabaseInstanceState),
            stopped=d.get("stopped", None),
            uid=d.get("uid", None),
        )


class DatabaseInstanceState(Enum):

    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"
    FAILING_OVER = "FAILING_OVER"
    STARTING = "STARTING"
    STOPPED = "STOPPED"
    UPDATING = "UPDATING"


@dataclass
class DatabaseTable:
    """Next field marker: 13"""

    name: str
    """Full three-part (catalog, schema, table) name of the table."""

    database_instance_name: Optional[str] = None
    """Name of the target database instance. This is required when creating database tables in standard
    catalogs. This is optional when creating database tables in registered catalogs. If this field
    is specified when creating database tables in registered catalogs, the database instance name
    MUST match that of the registered catalog (or the request will be rejected)."""

    logical_database_name: Optional[str] = None
    """Target Postgres database object (logical database) name for this table. This field is optional
    in all scenarios.
    
    When creating a table in a registered Postgres catalog, the target Postgres database name is
    inferred to be that of the registered catalog. If this field is specified in this scenario, the
    Postgres database name MUST match that of the registered catalog (or the request will be
    rejected).
    
    When creating a table in a standard catalog, the target database name is inferred to be that of
    the standard catalog. In this scenario, specifying this field will allow targeting an arbitrary
    postgres database. Note that this has implications for the `create_database_objects_is_missing`
    field in `spec`."""

    table_serving_url: Optional[str] = None
    """Data serving REST API URL for this table"""

    def as_dict(self) -> dict:
        """Serializes the DatabaseTable into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.database_instance_name is not None:
            body["database_instance_name"] = self.database_instance_name
        if self.logical_database_name is not None:
            body["logical_database_name"] = self.logical_database_name
        if self.name is not None:
            body["name"] = self.name
        if self.table_serving_url is not None:
            body["table_serving_url"] = self.table_serving_url
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabaseTable into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.database_instance_name is not None:
            body["database_instance_name"] = self.database_instance_name
        if self.logical_database_name is not None:
            body["logical_database_name"] = self.logical_database_name
        if self.name is not None:
            body["name"] = self.name
        if self.table_serving_url is not None:
            body["table_serving_url"] = self.table_serving_url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabaseTable:
        """Deserializes the DatabaseTable from a dictionary."""
        return cls(
            database_instance_name=d.get("database_instance_name", None),
            logical_database_name=d.get("logical_database_name", None),
            name=d.get("name", None),
            table_serving_url=d.get("table_serving_url", None),
        )


@dataclass
class DeleteDatabaseCatalogResponse:
    def as_dict(self) -> dict:
        """Serializes the DeleteDatabaseCatalogResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DeleteDatabaseCatalogResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DeleteDatabaseCatalogResponse:
        """Deserializes the DeleteDatabaseCatalogResponse from a dictionary."""
        return cls()


@dataclass
class DeleteDatabaseInstanceResponse:
    def as_dict(self) -> dict:
        """Serializes the DeleteDatabaseInstanceResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DeleteDatabaseInstanceResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DeleteDatabaseInstanceResponse:
        """Deserializes the DeleteDatabaseInstanceResponse from a dictionary."""
        return cls()


@dataclass
class DeleteDatabaseTableResponse:
    def as_dict(self) -> dict:
        """Serializes the DeleteDatabaseTableResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DeleteDatabaseTableResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DeleteDatabaseTableResponse:
        """Deserializes the DeleteDatabaseTableResponse from a dictionary."""
        return cls()


@dataclass
class DeleteSyncedDatabaseTableResponse:
    def as_dict(self) -> dict:
        """Serializes the DeleteSyncedDatabaseTableResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DeleteSyncedDatabaseTableResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DeleteSyncedDatabaseTableResponse:
        """Deserializes the DeleteSyncedDatabaseTableResponse from a dictionary."""
        return cls()


@dataclass
class GenerateDatabaseCredentialRequest:
    """Generates a credential that can be used to access database instances"""

    instance_names: Optional[List[str]] = None
    """Instances to which the token will be scoped."""

    request_id: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the GenerateDatabaseCredentialRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.instance_names:
            body["instance_names"] = [v for v in self.instance_names]
        if self.request_id is not None:
            body["request_id"] = self.request_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenerateDatabaseCredentialRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.instance_names:
            body["instance_names"] = self.instance_names
        if self.request_id is not None:
            body["request_id"] = self.request_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenerateDatabaseCredentialRequest:
        """Deserializes the GenerateDatabaseCredentialRequest from a dictionary."""
        return cls(instance_names=d.get("instance_names", None), request_id=d.get("request_id", None))


@dataclass
class ListDatabaseInstancesResponse:
    database_instances: Optional[List[DatabaseInstance]] = None
    """List of instances."""

    next_page_token: Optional[str] = None
    """Pagination token to request the next page of instances."""

    def as_dict(self) -> dict:
        """Serializes the ListDatabaseInstancesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.database_instances:
            body["database_instances"] = [v.as_dict() for v in self.database_instances]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListDatabaseInstancesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.database_instances:
            body["database_instances"] = self.database_instances
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListDatabaseInstancesResponse:
        """Deserializes the ListDatabaseInstancesResponse from a dictionary."""
        return cls(
            database_instances=_repeated_dict(d, "database_instances", DatabaseInstance),
            next_page_token=d.get("next_page_token", None),
        )


@dataclass
class NewPipelineSpec:
    """Custom fields that user can set for pipeline while creating SyncedDatabaseTable. Note that other
    fields of pipeline are still inferred by table def internally"""

    storage_catalog: Optional[str] = None
    """UC catalog for the pipeline to store intermediate files (checkpoints, event logs etc). This
    needs to be a standard catalog where the user has permissions to create Delta tables."""

    storage_schema: Optional[str] = None
    """UC schema for the pipeline to store intermediate files (checkpoints, event logs etc). This needs
    to be in the standard catalog where the user has permissions to create Delta tables."""

    def as_dict(self) -> dict:
        """Serializes the NewPipelineSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.storage_catalog is not None:
            body["storage_catalog"] = self.storage_catalog
        if self.storage_schema is not None:
            body["storage_schema"] = self.storage_schema
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the NewPipelineSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.storage_catalog is not None:
            body["storage_catalog"] = self.storage_catalog
        if self.storage_schema is not None:
            body["storage_schema"] = self.storage_schema
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> NewPipelineSpec:
        """Deserializes the NewPipelineSpec from a dictionary."""
        return cls(storage_catalog=d.get("storage_catalog", None), storage_schema=d.get("storage_schema", None))


class ProvisioningInfoState(Enum):

    ACTIVE = "ACTIVE"
    DEGRADED = "DEGRADED"
    DELETING = "DELETING"
    FAILED = "FAILED"
    PROVISIONING = "PROVISIONING"
    UPDATING = "UPDATING"


@dataclass
class SyncedDatabaseTable:
    """Next field marker: 12"""

    name: str
    """Full three-part (catalog, schema, table) name of the table."""

    data_synchronization_status: Optional[SyncedTableStatus] = None
    """Synced Table data synchronization status"""

    database_instance_name: Optional[str] = None
    """Name of the target database instance. This is required when creating synced database tables in
    standard catalogs. This is optional when creating synced database tables in registered catalogs.
    If this field is specified when creating synced database tables in registered catalogs, the
    database instance name MUST match that of the registered catalog (or the request will be
    rejected)."""

    logical_database_name: Optional[str] = None
    """Target Postgres database object (logical database) name for this table. This field is optional
    in all scenarios.
    
    When creating a synced table in a registered Postgres catalog, the target Postgres database name
    is inferred to be that of the registered catalog. If this field is specified in this scenario,
    the Postgres database name MUST match that of the registered catalog (or the request will be
    rejected).
    
    When creating a synced table in a standard catalog, the target database name is inferred to be
    that of the standard catalog. In this scenario, specifying this field will allow targeting an
    arbitrary postgres database."""

    spec: Optional[SyncedTableSpec] = None
    """Specification of a synced database table."""

    table_serving_url: Optional[str] = None
    """Data serving REST API URL for this table"""

    unity_catalog_provisioning_state: Optional[ProvisioningInfoState] = None
    """The provisioning state of the synced table entity in Unity Catalog. This is distinct from the
    state of the data synchronization pipeline (i.e. the table may be in "ACTIVE" but the pipeline
    may be in "PROVISIONING" as it runs asynchronously)."""

    def as_dict(self) -> dict:
        """Serializes the SyncedDatabaseTable into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.data_synchronization_status:
            body["data_synchronization_status"] = self.data_synchronization_status.as_dict()
        if self.database_instance_name is not None:
            body["database_instance_name"] = self.database_instance_name
        if self.logical_database_name is not None:
            body["logical_database_name"] = self.logical_database_name
        if self.name is not None:
            body["name"] = self.name
        if self.spec:
            body["spec"] = self.spec.as_dict()
        if self.table_serving_url is not None:
            body["table_serving_url"] = self.table_serving_url
        if self.unity_catalog_provisioning_state is not None:
            body["unity_catalog_provisioning_state"] = self.unity_catalog_provisioning_state.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncedDatabaseTable into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.data_synchronization_status:
            body["data_synchronization_status"] = self.data_synchronization_status
        if self.database_instance_name is not None:
            body["database_instance_name"] = self.database_instance_name
        if self.logical_database_name is not None:
            body["logical_database_name"] = self.logical_database_name
        if self.name is not None:
            body["name"] = self.name
        if self.spec:
            body["spec"] = self.spec
        if self.table_serving_url is not None:
            body["table_serving_url"] = self.table_serving_url
        if self.unity_catalog_provisioning_state is not None:
            body["unity_catalog_provisioning_state"] = self.unity_catalog_provisioning_state
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncedDatabaseTable:
        """Deserializes the SyncedDatabaseTable from a dictionary."""
        return cls(
            data_synchronization_status=_from_dict(d, "data_synchronization_status", SyncedTableStatus),
            database_instance_name=d.get("database_instance_name", None),
            logical_database_name=d.get("logical_database_name", None),
            name=d.get("name", None),
            spec=_from_dict(d, "spec", SyncedTableSpec),
            table_serving_url=d.get("table_serving_url", None),
            unity_catalog_provisioning_state=_enum(d, "unity_catalog_provisioning_state", ProvisioningInfoState),
        )


@dataclass
class SyncedTableContinuousUpdateStatus:
    """Detailed status of a synced table. Shown if the synced table is in the SYNCED_CONTINUOUS_UPDATE
    or the SYNCED_UPDATING_PIPELINE_RESOURCES state."""

    initial_pipeline_sync_progress: Optional[SyncedTablePipelineProgress] = None
    """Progress of the initial data synchronization."""

    last_processed_commit_version: Optional[int] = None
    """The last source table Delta version that was synced to the synced table. Note that this Delta
    version may not be completely synced to the synced table yet."""

    timestamp: Optional[str] = None
    """The timestamp of the last time any data was synchronized from the source table to the synced
    table."""

    def as_dict(self) -> dict:
        """Serializes the SyncedTableContinuousUpdateStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.initial_pipeline_sync_progress:
            body["initial_pipeline_sync_progress"] = self.initial_pipeline_sync_progress.as_dict()
        if self.last_processed_commit_version is not None:
            body["last_processed_commit_version"] = self.last_processed_commit_version
        if self.timestamp is not None:
            body["timestamp"] = self.timestamp
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncedTableContinuousUpdateStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.initial_pipeline_sync_progress:
            body["initial_pipeline_sync_progress"] = self.initial_pipeline_sync_progress
        if self.last_processed_commit_version is not None:
            body["last_processed_commit_version"] = self.last_processed_commit_version
        if self.timestamp is not None:
            body["timestamp"] = self.timestamp
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncedTableContinuousUpdateStatus:
        """Deserializes the SyncedTableContinuousUpdateStatus from a dictionary."""
        return cls(
            initial_pipeline_sync_progress=_from_dict(d, "initial_pipeline_sync_progress", SyncedTablePipelineProgress),
            last_processed_commit_version=d.get("last_processed_commit_version", None),
            timestamp=d.get("timestamp", None),
        )


@dataclass
class SyncedTableFailedStatus:
    """Detailed status of a synced table. Shown if the synced table is in the OFFLINE_FAILED or the
    SYNCED_PIPELINE_FAILED state."""

    last_processed_commit_version: Optional[int] = None
    """The last source table Delta version that was synced to the synced table. Note that this Delta
    version may only be partially synced to the synced table. Only populated if the table is still
    synced and available for serving."""

    timestamp: Optional[str] = None
    """The timestamp of the last time any data was synchronized from the source table to the synced
    table. Only populated if the table is still synced and available for serving."""

    def as_dict(self) -> dict:
        """Serializes the SyncedTableFailedStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.last_processed_commit_version is not None:
            body["last_processed_commit_version"] = self.last_processed_commit_version
        if self.timestamp is not None:
            body["timestamp"] = self.timestamp
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncedTableFailedStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.last_processed_commit_version is not None:
            body["last_processed_commit_version"] = self.last_processed_commit_version
        if self.timestamp is not None:
            body["timestamp"] = self.timestamp
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncedTableFailedStatus:
        """Deserializes the SyncedTableFailedStatus from a dictionary."""
        return cls(
            last_processed_commit_version=d.get("last_processed_commit_version", None),
            timestamp=d.get("timestamp", None),
        )


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
class SyncedTableProvisioningStatus:
    """Detailed status of a synced table. Shown if the synced table is in the
    PROVISIONING_PIPELINE_RESOURCES or the PROVISIONING_INITIAL_SNAPSHOT state."""

    initial_pipeline_sync_progress: Optional[SyncedTablePipelineProgress] = None
    """Details about initial data synchronization. Only populated when in the
    PROVISIONING_INITIAL_SNAPSHOT state."""

    def as_dict(self) -> dict:
        """Serializes the SyncedTableProvisioningStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.initial_pipeline_sync_progress:
            body["initial_pipeline_sync_progress"] = self.initial_pipeline_sync_progress.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncedTableProvisioningStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.initial_pipeline_sync_progress:
            body["initial_pipeline_sync_progress"] = self.initial_pipeline_sync_progress
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncedTableProvisioningStatus:
        """Deserializes the SyncedTableProvisioningStatus from a dictionary."""
        return cls(
            initial_pipeline_sync_progress=_from_dict(d, "initial_pipeline_sync_progress", SyncedTablePipelineProgress)
        )


class SyncedTableSchedulingPolicy(Enum):

    CONTINUOUS = "CONTINUOUS"
    SNAPSHOT = "SNAPSHOT"
    TRIGGERED = "TRIGGERED"


@dataclass
class SyncedTableSpec:
    """Specification of a synced database table."""

    create_database_objects_if_missing: Optional[bool] = None
    """If true, the synced table's logical database and schema resources in PG will be created if they
    do not already exist."""

    new_pipeline_spec: Optional[NewPipelineSpec] = None
    """Spec of new pipeline. Should be empty if pipeline_id is set"""

    pipeline_id: Optional[str] = None
    """ID of the associated pipeline. Should be empty if new_pipeline_spec is set"""

    primary_key_columns: Optional[List[str]] = None
    """Primary Key columns to be used for data insert/update in the destination."""

    scheduling_policy: Optional[SyncedTableSchedulingPolicy] = None
    """Scheduling policy of the underlying pipeline."""

    source_table_full_name: Optional[str] = None
    """Three-part (catalog, schema, table) name of the source Delta table."""

    timeseries_key: Optional[str] = None
    """Time series key to deduplicate (tie-break) rows with the same primary key."""

    def as_dict(self) -> dict:
        """Serializes the SyncedTableSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_database_objects_if_missing is not None:
            body["create_database_objects_if_missing"] = self.create_database_objects_if_missing
        if self.new_pipeline_spec:
            body["new_pipeline_spec"] = self.new_pipeline_spec.as_dict()
        if self.pipeline_id is not None:
            body["pipeline_id"] = self.pipeline_id
        if self.primary_key_columns:
            body["primary_key_columns"] = [v for v in self.primary_key_columns]
        if self.scheduling_policy is not None:
            body["scheduling_policy"] = self.scheduling_policy.value
        if self.source_table_full_name is not None:
            body["source_table_full_name"] = self.source_table_full_name
        if self.timeseries_key is not None:
            body["timeseries_key"] = self.timeseries_key
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncedTableSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_database_objects_if_missing is not None:
            body["create_database_objects_if_missing"] = self.create_database_objects_if_missing
        if self.new_pipeline_spec:
            body["new_pipeline_spec"] = self.new_pipeline_spec
        if self.pipeline_id is not None:
            body["pipeline_id"] = self.pipeline_id
        if self.primary_key_columns:
            body["primary_key_columns"] = self.primary_key_columns
        if self.scheduling_policy is not None:
            body["scheduling_policy"] = self.scheduling_policy
        if self.source_table_full_name is not None:
            body["source_table_full_name"] = self.source_table_full_name
        if self.timeseries_key is not None:
            body["timeseries_key"] = self.timeseries_key
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncedTableSpec:
        """Deserializes the SyncedTableSpec from a dictionary."""
        return cls(
            create_database_objects_if_missing=d.get("create_database_objects_if_missing", None),
            new_pipeline_spec=_from_dict(d, "new_pipeline_spec", NewPipelineSpec),
            pipeline_id=d.get("pipeline_id", None),
            primary_key_columns=d.get("primary_key_columns", None),
            scheduling_policy=_enum(d, "scheduling_policy", SyncedTableSchedulingPolicy),
            source_table_full_name=d.get("source_table_full_name", None),
            timeseries_key=d.get("timeseries_key", None),
        )


class SyncedTableState(Enum):
    """The state of a synced table."""

    SYNCED_TABLED_OFFLINE = "SYNCED_TABLED_OFFLINE"
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
class SyncedTableStatus:
    """Status of a synced table."""

    continuous_update_status: Optional[SyncedTableContinuousUpdateStatus] = None
    """Detailed status of a synced table. Shown if the synced table is in the SYNCED_CONTINUOUS_UPDATE
    or the SYNCED_UPDATING_PIPELINE_RESOURCES state."""

    detailed_state: Optional[SyncedTableState] = None
    """The state of the synced table."""

    failed_status: Optional[SyncedTableFailedStatus] = None
    """Detailed status of a synced table. Shown if the synced table is in the OFFLINE_FAILED or the
    SYNCED_PIPELINE_FAILED state."""

    message: Optional[str] = None
    """A text description of the current state of the synced table."""

    provisioning_status: Optional[SyncedTableProvisioningStatus] = None
    """Detailed status of a synced table. Shown if the synced table is in the
    PROVISIONING_PIPELINE_RESOURCES or the PROVISIONING_INITIAL_SNAPSHOT state."""

    triggered_update_status: Optional[SyncedTableTriggeredUpdateStatus] = None
    """Detailed status of a synced table. Shown if the synced table is in the SYNCED_TRIGGERED_UPDATE
    or the SYNCED_NO_PENDING_UPDATE state."""

    def as_dict(self) -> dict:
        """Serializes the SyncedTableStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.continuous_update_status:
            body["continuous_update_status"] = self.continuous_update_status.as_dict()
        if self.detailed_state is not None:
            body["detailed_state"] = self.detailed_state.value
        if self.failed_status:
            body["failed_status"] = self.failed_status.as_dict()
        if self.message is not None:
            body["message"] = self.message
        if self.provisioning_status:
            body["provisioning_status"] = self.provisioning_status.as_dict()
        if self.triggered_update_status:
            body["triggered_update_status"] = self.triggered_update_status.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncedTableStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.continuous_update_status:
            body["continuous_update_status"] = self.continuous_update_status
        if self.detailed_state is not None:
            body["detailed_state"] = self.detailed_state
        if self.failed_status:
            body["failed_status"] = self.failed_status
        if self.message is not None:
            body["message"] = self.message
        if self.provisioning_status:
            body["provisioning_status"] = self.provisioning_status
        if self.triggered_update_status:
            body["triggered_update_status"] = self.triggered_update_status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncedTableStatus:
        """Deserializes the SyncedTableStatus from a dictionary."""
        return cls(
            continuous_update_status=_from_dict(d, "continuous_update_status", SyncedTableContinuousUpdateStatus),
            detailed_state=_enum(d, "detailed_state", SyncedTableState),
            failed_status=_from_dict(d, "failed_status", SyncedTableFailedStatus),
            message=d.get("message", None),
            provisioning_status=_from_dict(d, "provisioning_status", SyncedTableProvisioningStatus),
            triggered_update_status=_from_dict(d, "triggered_update_status", SyncedTableTriggeredUpdateStatus),
        )


@dataclass
class SyncedTableTriggeredUpdateStatus:
    """Detailed status of a synced table. Shown if the synced table is in the SYNCED_TRIGGERED_UPDATE
    or the SYNCED_NO_PENDING_UPDATE state."""

    last_processed_commit_version: Optional[int] = None
    """The last source table Delta version that was synced to the synced table. Note that this Delta
    version may not be completely synced to the synced table yet."""

    timestamp: Optional[str] = None
    """The timestamp of the last time any data was synchronized from the source table to the synced
    table."""

    triggered_update_progress: Optional[SyncedTablePipelineProgress] = None
    """Progress of the active data synchronization pipeline."""

    def as_dict(self) -> dict:
        """Serializes the SyncedTableTriggeredUpdateStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.last_processed_commit_version is not None:
            body["last_processed_commit_version"] = self.last_processed_commit_version
        if self.timestamp is not None:
            body["timestamp"] = self.timestamp
        if self.triggered_update_progress:
            body["triggered_update_progress"] = self.triggered_update_progress.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncedTableTriggeredUpdateStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.last_processed_commit_version is not None:
            body["last_processed_commit_version"] = self.last_processed_commit_version
        if self.timestamp is not None:
            body["timestamp"] = self.timestamp
        if self.triggered_update_progress:
            body["triggered_update_progress"] = self.triggered_update_progress
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncedTableTriggeredUpdateStatus:
        """Deserializes the SyncedTableTriggeredUpdateStatus from a dictionary."""
        return cls(
            last_processed_commit_version=d.get("last_processed_commit_version", None),
            timestamp=d.get("timestamp", None),
            triggered_update_progress=_from_dict(d, "triggered_update_progress", SyncedTablePipelineProgress),
        )


class DatabaseAPI:
    """Database Instances provide access to a database via REST API or direct SQL."""

    def __init__(self, api_client):
        self._api = api_client

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

        res = self._api.do("POST", "/api/2.0/database/catalogs", body=body, headers=headers)
        return DatabaseCatalog.from_dict(res)

    def create_database_instance(self, database_instance: DatabaseInstance) -> DatabaseInstance:
        """Create a Database Instance.

        :param database_instance: :class:`DatabaseInstance`
          A DatabaseInstance represents a logical Postgres instance, comprised of both compute and storage.

        :returns: :class:`DatabaseInstance`
        """
        body = database_instance.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/database/instances", body=body, headers=headers)
        return DatabaseInstance.from_dict(res)

    def create_database_table(self, table: DatabaseTable) -> DatabaseTable:
        """Create a Database Table.

        :param table: :class:`DatabaseTable`
          Next field marker: 13

        :returns: :class:`DatabaseTable`
        """
        body = table.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/database/tables", body=body, headers=headers)
        return DatabaseTable.from_dict(res)

    def create_synced_database_table(self, synced_table: SyncedDatabaseTable) -> SyncedDatabaseTable:
        """Create a Synced Database Table.

        :param synced_table: :class:`SyncedDatabaseTable`
          Next field marker: 12

        :returns: :class:`SyncedDatabaseTable`
        """
        body = synced_table.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/database/synced_tables", body=body, headers=headers)
        return SyncedDatabaseTable.from_dict(res)

    def delete_database_catalog(self, name: str):
        """Delete a Database Catalog.

        :param name: str


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/database/catalogs/{name}", headers=headers)

    def delete_database_instance(self, name: str, *, force: Optional[bool] = None, purge: Optional[bool] = None):
        """Delete a Database Instance.

        :param name: str
          Name of the instance to delete.
        :param force: bool (optional)
          By default, a instance cannot be deleted if it has descendant instances created via PITR. If this
          flag is specified as true, all descendent instances will be deleted as well.
        :param purge: bool (optional)
          If false, the database instance is soft deleted. Soft deleted instances behave as if they are
          deleted, and cannot be used for CRUD operations nor connected to. However they can be undeleted by
          calling the undelete API for a limited time. If true, the database instance is hard deleted and
          cannot be undeleted.


        """

        query = {}
        if force is not None:
            query["force"] = force
        if purge is not None:
            query["purge"] = purge
        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/database/instances/{name}", query=query, headers=headers)

    def delete_database_table(self, name: str):
        """Delete a Database Table.

        :param name: str


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/database/tables/{name}", headers=headers)

    def delete_synced_database_table(self, name: str):
        """Delete a Synced Database Table.

        :param name: str


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/database/synced_tables/{name}", headers=headers)

    def find_database_instance_by_uid(self, *, uid: Optional[str] = None) -> DatabaseInstance:
        """Find a Database Instance by uid.

        :param uid: str (optional)
          UID of the cluster to get.

        :returns: :class:`DatabaseInstance`
        """

        query = {}
        if uid is not None:
            query["uid"] = uid
        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", "/api/2.0/database/instances:findByUid", query=query, headers=headers)
        return DatabaseInstance.from_dict(res)

    def generate_database_credential(
        self, *, instance_names: Optional[List[str]] = None, request_id: Optional[str] = None
    ) -> DatabaseCredential:
        """Generates a credential that can be used to access database instances.

        :param instance_names: List[str] (optional)
          Instances to which the token will be scoped.
        :param request_id: str (optional)

        :returns: :class:`DatabaseCredential`
        """
        body = {}
        if instance_names is not None:
            body["instance_names"] = [v for v in instance_names]
        if request_id is not None:
            body["request_id"] = request_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/database/credentials", body=body, headers=headers)
        return DatabaseCredential.from_dict(res)

    def get_database_catalog(self, name: str) -> DatabaseCatalog:
        """Get a Database Catalog.

        :param name: str

        :returns: :class:`DatabaseCatalog`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/database/catalogs/{name}", headers=headers)
        return DatabaseCatalog.from_dict(res)

    def get_database_instance(self, name: str) -> DatabaseInstance:
        """Get a Database Instance.

        :param name: str
          Name of the cluster to get.

        :returns: :class:`DatabaseInstance`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/database/instances/{name}", headers=headers)
        return DatabaseInstance.from_dict(res)

    def get_database_table(self, name: str) -> DatabaseTable:
        """Get a Database Table.

        :param name: str

        :returns: :class:`DatabaseTable`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/database/tables/{name}", headers=headers)
        return DatabaseTable.from_dict(res)

    def get_synced_database_table(self, name: str) -> SyncedDatabaseTable:
        """Get a Synced Database Table.

        :param name: str

        :returns: :class:`SyncedDatabaseTable`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/database/synced_tables/{name}", headers=headers)
        return SyncedDatabaseTable.from_dict(res)

    def list_database_instances(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[DatabaseInstance]:
        """List Database Instances.

        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Database Instances. Requests first page if absent.

        :returns: Iterator over :class:`DatabaseInstance`
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
            json = self._api.do("GET", "/api/2.0/database/instances", query=query, headers=headers)
            if "database_instances" in json:
                for v in json["database_instances"]:
                    yield DatabaseInstance.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def update_database_instance(
        self, name: str, database_instance: DatabaseInstance, update_mask: str
    ) -> DatabaseInstance:
        """Update a Database Instance.

        :param name: str
          The name of the instance. This is the unique identifier for the instance.
        :param database_instance: :class:`DatabaseInstance`
          A DatabaseInstance represents a logical Postgres instance, comprised of both compute and storage.
        :param update_mask: str
          The list of fields to update.

        :returns: :class:`DatabaseInstance`
        """
        body = database_instance.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.0/database/instances/{name}", query=query, body=body, headers=headers)
        return DatabaseInstance.from_dict(res)

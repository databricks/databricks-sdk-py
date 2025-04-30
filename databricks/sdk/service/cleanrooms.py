# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List, Optional

from ._internal import _enum, _from_dict, _repeated_dict

_LOG = logging.getLogger("databricks.sdk")


from databricks.sdk.service import catalog, jobs, settings, sharing

# all definitions in this file are in alphabetical order


@dataclass
class CleanRoom:
    access_restricted: Optional[CleanRoomAccessRestricted] = None
    """Whether clean room access is restricted due to [CSP]
    
    [CSP]: https://docs.databricks.com/en/security/privacy/security-profile.html"""

    comment: Optional[str] = None

    created_at: Optional[int] = None
    """When the clean room was created, in epoch milliseconds."""

    local_collaborator_alias: Optional[str] = None
    """The alias of the collaborator tied to the local clean room."""

    name: Optional[str] = None
    """The name of the clean room. It should follow [UC securable naming requirements].
    
    [UC securable naming requirements]: https://docs.databricks.com/en/data-governance/unity-catalog/index.html#securable-object-naming-requirements"""

    output_catalog: Optional[CleanRoomOutputCatalog] = None
    """Output catalog of the clean room. It is an output only field. Output catalog is manipulated
    using the separate CreateCleanRoomOutputCatalog API."""

    owner: Optional[str] = None
    """This is Databricks username of the owner of the local clean room securable for permission
    management."""

    remote_detailed_info: Optional[CleanRoomRemoteDetail] = None
    """Central clean room details. During creation, users need to specify cloud_vendor, region, and
    collaborators.global_metastore_id. This field will not be filled in the ListCleanRooms call."""

    status: Optional[CleanRoomStatusEnum] = None
    """Clean room status."""

    updated_at: Optional[int] = None
    """When the clean room was last updated, in epoch milliseconds."""

    def as_dict(self) -> dict:
        """Serializes the CleanRoom into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_restricted is not None:
            body["access_restricted"] = self.access_restricted.value
        if self.comment is not None:
            body["comment"] = self.comment
        if self.created_at is not None:
            body["created_at"] = self.created_at
        if self.local_collaborator_alias is not None:
            body["local_collaborator_alias"] = self.local_collaborator_alias
        if self.name is not None:
            body["name"] = self.name
        if self.output_catalog:
            body["output_catalog"] = self.output_catalog.as_dict()
        if self.owner is not None:
            body["owner"] = self.owner
        if self.remote_detailed_info:
            body["remote_detailed_info"] = self.remote_detailed_info.as_dict()
        if self.status is not None:
            body["status"] = self.status.value
        if self.updated_at is not None:
            body["updated_at"] = self.updated_at
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CleanRoom into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.access_restricted is not None:
            body["access_restricted"] = self.access_restricted
        if self.comment is not None:
            body["comment"] = self.comment
        if self.created_at is not None:
            body["created_at"] = self.created_at
        if self.local_collaborator_alias is not None:
            body["local_collaborator_alias"] = self.local_collaborator_alias
        if self.name is not None:
            body["name"] = self.name
        if self.output_catalog:
            body["output_catalog"] = self.output_catalog
        if self.owner is not None:
            body["owner"] = self.owner
        if self.remote_detailed_info:
            body["remote_detailed_info"] = self.remote_detailed_info
        if self.status is not None:
            body["status"] = self.status
        if self.updated_at is not None:
            body["updated_at"] = self.updated_at
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CleanRoom:
        """Deserializes the CleanRoom from a dictionary."""
        return cls(
            access_restricted=_enum(d, "access_restricted", CleanRoomAccessRestricted),
            comment=d.get("comment", None),
            created_at=d.get("created_at", None),
            local_collaborator_alias=d.get("local_collaborator_alias", None),
            name=d.get("name", None),
            output_catalog=_from_dict(d, "output_catalog", CleanRoomOutputCatalog),
            owner=d.get("owner", None),
            remote_detailed_info=_from_dict(d, "remote_detailed_info", CleanRoomRemoteDetail),
            status=_enum(d, "status", CleanRoomStatusEnum),
            updated_at=d.get("updated_at", None),
        )


class CleanRoomAccessRestricted(Enum):

    CSP_MISMATCH = "CSP_MISMATCH"
    NO_RESTRICTION = "NO_RESTRICTION"


@dataclass
class CleanRoomAsset:
    """Metadata of the clean room asset"""

    added_at: Optional[int] = None
    """When the asset is added to the clean room, in epoch milliseconds."""

    asset_type: Optional[CleanRoomAssetAssetType] = None
    """The type of the asset."""

    foreign_table: Optional[CleanRoomAssetForeignTable] = None
    """Foreign table details available to all collaborators of the clean room. Present if and only if
    **asset_type** is **FOREIGN_TABLE**"""

    foreign_table_local_details: Optional[CleanRoomAssetForeignTableLocalDetails] = None
    """Local details for a foreign that are only available to its owner. Present if and only if
    **asset_type** is **FOREIGN_TABLE**"""

    name: Optional[str] = None
    """A fully qualified name that uniquely identifies the asset within the clean room. This is also
    the name displayed in the clean room UI.
    
    For UC securable assets (tables, volumes, etc.), the format is
    *shared_catalog*.*shared_schema*.*asset_name*
    
    For notebooks, the name is the notebook file name."""

    notebook: Optional[CleanRoomAssetNotebook] = None
    """Notebook details available to all collaborators of the clean room. Present if and only if
    **asset_type** is **NOTEBOOK_FILE**"""

    owner_collaborator_alias: Optional[str] = None
    """The alias of the collaborator who owns this asset"""

    status: Optional[CleanRoomAssetStatusEnum] = None
    """Status of the asset"""

    table: Optional[CleanRoomAssetTable] = None
    """Table details available to all collaborators of the clean room. Present if and only if
    **asset_type** is **TABLE**"""

    table_local_details: Optional[CleanRoomAssetTableLocalDetails] = None
    """Local details for a table that are only available to its owner. Present if and only if
    **asset_type** is **TABLE**"""

    view: Optional[CleanRoomAssetView] = None
    """View details available to all collaborators of the clean room. Present if and only if
    **asset_type** is **VIEW**"""

    view_local_details: Optional[CleanRoomAssetViewLocalDetails] = None
    """Local details for a view that are only available to its owner. Present if and only if
    **asset_type** is **VIEW**"""

    volume_local_details: Optional[CleanRoomAssetVolumeLocalDetails] = None
    """Local details for a volume that are only available to its owner. Present if and only if
    **asset_type** is **VOLUME**"""

    def as_dict(self) -> dict:
        """Serializes the CleanRoomAsset into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.added_at is not None:
            body["added_at"] = self.added_at
        if self.asset_type is not None:
            body["asset_type"] = self.asset_type.value
        if self.foreign_table:
            body["foreign_table"] = self.foreign_table.as_dict()
        if self.foreign_table_local_details:
            body["foreign_table_local_details"] = self.foreign_table_local_details.as_dict()
        if self.name is not None:
            body["name"] = self.name
        if self.notebook:
            body["notebook"] = self.notebook.as_dict()
        if self.owner_collaborator_alias is not None:
            body["owner_collaborator_alias"] = self.owner_collaborator_alias
        if self.status is not None:
            body["status"] = self.status.value
        if self.table:
            body["table"] = self.table.as_dict()
        if self.table_local_details:
            body["table_local_details"] = self.table_local_details.as_dict()
        if self.view:
            body["view"] = self.view.as_dict()
        if self.view_local_details:
            body["view_local_details"] = self.view_local_details.as_dict()
        if self.volume_local_details:
            body["volume_local_details"] = self.volume_local_details.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CleanRoomAsset into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.added_at is not None:
            body["added_at"] = self.added_at
        if self.asset_type is not None:
            body["asset_type"] = self.asset_type
        if self.foreign_table:
            body["foreign_table"] = self.foreign_table
        if self.foreign_table_local_details:
            body["foreign_table_local_details"] = self.foreign_table_local_details
        if self.name is not None:
            body["name"] = self.name
        if self.notebook:
            body["notebook"] = self.notebook
        if self.owner_collaborator_alias is not None:
            body["owner_collaborator_alias"] = self.owner_collaborator_alias
        if self.status is not None:
            body["status"] = self.status
        if self.table:
            body["table"] = self.table
        if self.table_local_details:
            body["table_local_details"] = self.table_local_details
        if self.view:
            body["view"] = self.view
        if self.view_local_details:
            body["view_local_details"] = self.view_local_details
        if self.volume_local_details:
            body["volume_local_details"] = self.volume_local_details
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CleanRoomAsset:
        """Deserializes the CleanRoomAsset from a dictionary."""
        return cls(
            added_at=d.get("added_at", None),
            asset_type=_enum(d, "asset_type", CleanRoomAssetAssetType),
            foreign_table=_from_dict(d, "foreign_table", CleanRoomAssetForeignTable),
            foreign_table_local_details=_from_dict(
                d, "foreign_table_local_details", CleanRoomAssetForeignTableLocalDetails
            ),
            name=d.get("name", None),
            notebook=_from_dict(d, "notebook", CleanRoomAssetNotebook),
            owner_collaborator_alias=d.get("owner_collaborator_alias", None),
            status=_enum(d, "status", CleanRoomAssetStatusEnum),
            table=_from_dict(d, "table", CleanRoomAssetTable),
            table_local_details=_from_dict(d, "table_local_details", CleanRoomAssetTableLocalDetails),
            view=_from_dict(d, "view", CleanRoomAssetView),
            view_local_details=_from_dict(d, "view_local_details", CleanRoomAssetViewLocalDetails),
            volume_local_details=_from_dict(d, "volume_local_details", CleanRoomAssetVolumeLocalDetails),
        )


class CleanRoomAssetAssetType(Enum):

    FOREIGN_TABLE = "FOREIGN_TABLE"
    NOTEBOOK_FILE = "NOTEBOOK_FILE"
    TABLE = "TABLE"
    VIEW = "VIEW"
    VOLUME = "VOLUME"


@dataclass
class CleanRoomAssetForeignTable:
    columns: Optional[List[catalog.ColumnInfo]] = None
    """The metadata information of the columns in the foreign table"""

    def as_dict(self) -> dict:
        """Serializes the CleanRoomAssetForeignTable into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.columns:
            body["columns"] = [v.as_dict() for v in self.columns]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CleanRoomAssetForeignTable into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.columns:
            body["columns"] = self.columns
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CleanRoomAssetForeignTable:
        """Deserializes the CleanRoomAssetForeignTable from a dictionary."""
        return cls(columns=_repeated_dict(d, "columns", catalog.ColumnInfo))


@dataclass
class CleanRoomAssetForeignTableLocalDetails:
    local_name: Optional[str] = None
    """The fully qualified name of the foreign table in its owner's local metastore, in the format of
    *catalog*.*schema*.*foreign_table_name*"""

    def as_dict(self) -> dict:
        """Serializes the CleanRoomAssetForeignTableLocalDetails into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.local_name is not None:
            body["local_name"] = self.local_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CleanRoomAssetForeignTableLocalDetails into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.local_name is not None:
            body["local_name"] = self.local_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CleanRoomAssetForeignTableLocalDetails:
        """Deserializes the CleanRoomAssetForeignTableLocalDetails from a dictionary."""
        return cls(local_name=d.get("local_name", None))


@dataclass
class CleanRoomAssetNotebook:
    etag: Optional[str] = None
    """Server generated etag that represents the notebook version."""

    notebook_content: Optional[str] = None
    """Base 64 representation of the notebook contents. This is the same format as returned by
    :method:workspace/export with the format of **HTML**."""

    def as_dict(self) -> dict:
        """Serializes the CleanRoomAssetNotebook into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.etag is not None:
            body["etag"] = self.etag
        if self.notebook_content is not None:
            body["notebook_content"] = self.notebook_content
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CleanRoomAssetNotebook into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.etag is not None:
            body["etag"] = self.etag
        if self.notebook_content is not None:
            body["notebook_content"] = self.notebook_content
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CleanRoomAssetNotebook:
        """Deserializes the CleanRoomAssetNotebook from a dictionary."""
        return cls(etag=d.get("etag", None), notebook_content=d.get("notebook_content", None))


class CleanRoomAssetStatusEnum(Enum):

    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    PERMISSION_DENIED = "PERMISSION_DENIED"


@dataclass
class CleanRoomAssetTable:
    columns: Optional[List[catalog.ColumnInfo]] = None
    """The metadata information of the columns in the table"""

    def as_dict(self) -> dict:
        """Serializes the CleanRoomAssetTable into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.columns:
            body["columns"] = [v.as_dict() for v in self.columns]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CleanRoomAssetTable into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.columns:
            body["columns"] = self.columns
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CleanRoomAssetTable:
        """Deserializes the CleanRoomAssetTable from a dictionary."""
        return cls(columns=_repeated_dict(d, "columns", catalog.ColumnInfo))


@dataclass
class CleanRoomAssetTableLocalDetails:
    local_name: Optional[str] = None
    """The fully qualified name of the table in its owner's local metastore, in the format of
    *catalog*.*schema*.*table_name*"""

    partitions: Optional[List[sharing.Partition]] = None
    """Partition filtering specification for a shared table."""

    def as_dict(self) -> dict:
        """Serializes the CleanRoomAssetTableLocalDetails into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.local_name is not None:
            body["local_name"] = self.local_name
        if self.partitions:
            body["partitions"] = [v.as_dict() for v in self.partitions]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CleanRoomAssetTableLocalDetails into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.local_name is not None:
            body["local_name"] = self.local_name
        if self.partitions:
            body["partitions"] = self.partitions
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CleanRoomAssetTableLocalDetails:
        """Deserializes the CleanRoomAssetTableLocalDetails from a dictionary."""
        return cls(local_name=d.get("local_name", None), partitions=_repeated_dict(d, "partitions", sharing.Partition))


@dataclass
class CleanRoomAssetView:
    columns: Optional[List[catalog.ColumnInfo]] = None
    """The metadata information of the columns in the view"""

    def as_dict(self) -> dict:
        """Serializes the CleanRoomAssetView into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.columns:
            body["columns"] = [v.as_dict() for v in self.columns]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CleanRoomAssetView into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.columns:
            body["columns"] = self.columns
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CleanRoomAssetView:
        """Deserializes the CleanRoomAssetView from a dictionary."""
        return cls(columns=_repeated_dict(d, "columns", catalog.ColumnInfo))


@dataclass
class CleanRoomAssetViewLocalDetails:
    local_name: Optional[str] = None
    """The fully qualified name of the view in its owner's local metastore, in the format of
    *catalog*.*schema*.*view_name*"""

    def as_dict(self) -> dict:
        """Serializes the CleanRoomAssetViewLocalDetails into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.local_name is not None:
            body["local_name"] = self.local_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CleanRoomAssetViewLocalDetails into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.local_name is not None:
            body["local_name"] = self.local_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CleanRoomAssetViewLocalDetails:
        """Deserializes the CleanRoomAssetViewLocalDetails from a dictionary."""
        return cls(local_name=d.get("local_name", None))


@dataclass
class CleanRoomAssetVolumeLocalDetails:
    local_name: Optional[str] = None
    """The fully qualified name of the volume in its owner's local metastore, in the format of
    *catalog*.*schema*.*volume_name*"""

    def as_dict(self) -> dict:
        """Serializes the CleanRoomAssetVolumeLocalDetails into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.local_name is not None:
            body["local_name"] = self.local_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CleanRoomAssetVolumeLocalDetails into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.local_name is not None:
            body["local_name"] = self.local_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CleanRoomAssetVolumeLocalDetails:
        """Deserializes the CleanRoomAssetVolumeLocalDetails from a dictionary."""
        return cls(local_name=d.get("local_name", None))


@dataclass
class CleanRoomCollaborator:
    """Publicly visible clean room collaborator."""

    collaborator_alias: str
    """Collaborator alias specified by the clean room creator. It is unique across all collaborators of
    this clean room, and used to derive multiple values internally such as catalog alias and clean
    room name for single metastore clean rooms. It should follow [UC securable naming requirements].
    
    [UC securable naming requirements]: https://docs.databricks.com/en/data-governance/unity-catalog/index.html#securable-object-naming-requirements"""

    display_name: Optional[str] = None
    """Generated display name for the collaborator. In the case of a single metastore clean room, it is
    the clean room name. For x-metastore clean rooms, it is the organization name of the metastore.
    It is not restricted to these values and could change in the future"""

    global_metastore_id: Optional[str] = None
    """The global Unity Catalog metastore id of the collaborator. The identifier is of format
    cloud:region:metastore-uuid."""

    invite_recipient_email: Optional[str] = None
    """Email of the user who is receiving the clean room "invitation". It should be empty for the
    creator of the clean room, and non-empty for the invitees of the clean room. It is only returned
    in the output when clean room creator calls GET"""

    invite_recipient_workspace_id: Optional[int] = None
    """Workspace ID of the user who is receiving the clean room "invitation". Must be specified if
    invite_recipient_email is specified. It should be empty when the collaborator is the creator of
    the clean room."""

    organization_name: Optional[str] = None
    """[Organization name](:method:metastores/list#metastores-delta_sharing_organization_name)
    configured in the metastore"""

    def as_dict(self) -> dict:
        """Serializes the CleanRoomCollaborator into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.collaborator_alias is not None:
            body["collaborator_alias"] = self.collaborator_alias
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.global_metastore_id is not None:
            body["global_metastore_id"] = self.global_metastore_id
        if self.invite_recipient_email is not None:
            body["invite_recipient_email"] = self.invite_recipient_email
        if self.invite_recipient_workspace_id is not None:
            body["invite_recipient_workspace_id"] = self.invite_recipient_workspace_id
        if self.organization_name is not None:
            body["organization_name"] = self.organization_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CleanRoomCollaborator into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.collaborator_alias is not None:
            body["collaborator_alias"] = self.collaborator_alias
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.global_metastore_id is not None:
            body["global_metastore_id"] = self.global_metastore_id
        if self.invite_recipient_email is not None:
            body["invite_recipient_email"] = self.invite_recipient_email
        if self.invite_recipient_workspace_id is not None:
            body["invite_recipient_workspace_id"] = self.invite_recipient_workspace_id
        if self.organization_name is not None:
            body["organization_name"] = self.organization_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CleanRoomCollaborator:
        """Deserializes the CleanRoomCollaborator from a dictionary."""
        return cls(
            collaborator_alias=d.get("collaborator_alias", None),
            display_name=d.get("display_name", None),
            global_metastore_id=d.get("global_metastore_id", None),
            invite_recipient_email=d.get("invite_recipient_email", None),
            invite_recipient_workspace_id=d.get("invite_recipient_workspace_id", None),
            organization_name=d.get("organization_name", None),
        )


@dataclass
class CleanRoomNotebookTaskRun:
    """Stores information about a single task run."""

    collaborator_job_run_info: Optional[CollaboratorJobRunInfo] = None
    """Job run info of the task in the runner's local workspace. This field is only included in the
    LIST API. if the task was run within the same workspace the API is being called. If the task run
    was in a different workspace under the same metastore, only the workspace_id is included."""

    notebook_job_run_state: Optional[jobs.CleanRoomTaskRunState] = None
    """State of the task run."""

    notebook_name: Optional[str] = None
    """Asset name of the notebook executed in this task run."""

    output_schema_expiration_time: Optional[int] = None
    """Expiration time of the output schema of the task run (if any), in epoch milliseconds."""

    output_schema_name: Optional[str] = None
    """Name of the output schema associated with the clean rooms notebook task run."""

    run_duration: Optional[int] = None
    """Duration of the task run, in milliseconds."""

    start_time: Optional[int] = None
    """When the task run started, in epoch milliseconds."""

    def as_dict(self) -> dict:
        """Serializes the CleanRoomNotebookTaskRun into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.collaborator_job_run_info:
            body["collaborator_job_run_info"] = self.collaborator_job_run_info.as_dict()
        if self.notebook_job_run_state:
            body["notebook_job_run_state"] = self.notebook_job_run_state.as_dict()
        if self.notebook_name is not None:
            body["notebook_name"] = self.notebook_name
        if self.output_schema_expiration_time is not None:
            body["output_schema_expiration_time"] = self.output_schema_expiration_time
        if self.output_schema_name is not None:
            body["output_schema_name"] = self.output_schema_name
        if self.run_duration is not None:
            body["run_duration"] = self.run_duration
        if self.start_time is not None:
            body["start_time"] = self.start_time
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CleanRoomNotebookTaskRun into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.collaborator_job_run_info:
            body["collaborator_job_run_info"] = self.collaborator_job_run_info
        if self.notebook_job_run_state:
            body["notebook_job_run_state"] = self.notebook_job_run_state
        if self.notebook_name is not None:
            body["notebook_name"] = self.notebook_name
        if self.output_schema_expiration_time is not None:
            body["output_schema_expiration_time"] = self.output_schema_expiration_time
        if self.output_schema_name is not None:
            body["output_schema_name"] = self.output_schema_name
        if self.run_duration is not None:
            body["run_duration"] = self.run_duration
        if self.start_time is not None:
            body["start_time"] = self.start_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CleanRoomNotebookTaskRun:
        """Deserializes the CleanRoomNotebookTaskRun from a dictionary."""
        return cls(
            collaborator_job_run_info=_from_dict(d, "collaborator_job_run_info", CollaboratorJobRunInfo),
            notebook_job_run_state=_from_dict(d, "notebook_job_run_state", jobs.CleanRoomTaskRunState),
            notebook_name=d.get("notebook_name", None),
            output_schema_expiration_time=d.get("output_schema_expiration_time", None),
            output_schema_name=d.get("output_schema_name", None),
            run_duration=d.get("run_duration", None),
            start_time=d.get("start_time", None),
        )


@dataclass
class CleanRoomOutputCatalog:
    catalog_name: Optional[str] = None
    """The name of the output catalog in UC. It should follow [UC securable naming requirements]. The
    field will always exist if status is CREATED.
    
    [UC securable naming requirements]: https://docs.databricks.com/en/data-governance/unity-catalog/index.html#securable-object-naming-requirements"""

    status: Optional[CleanRoomOutputCatalogOutputCatalogStatus] = None

    def as_dict(self) -> dict:
        """Serializes the CleanRoomOutputCatalog into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.catalog_name is not None:
            body["catalog_name"] = self.catalog_name
        if self.status is not None:
            body["status"] = self.status.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CleanRoomOutputCatalog into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.catalog_name is not None:
            body["catalog_name"] = self.catalog_name
        if self.status is not None:
            body["status"] = self.status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CleanRoomOutputCatalog:
        """Deserializes the CleanRoomOutputCatalog from a dictionary."""
        return cls(
            catalog_name=d.get("catalog_name", None),
            status=_enum(d, "status", CleanRoomOutputCatalogOutputCatalogStatus),
        )


class CleanRoomOutputCatalogOutputCatalogStatus(Enum):

    CREATED = "CREATED"
    NOT_CREATED = "NOT_CREATED"
    NOT_ELIGIBLE = "NOT_ELIGIBLE"


@dataclass
class CleanRoomRemoteDetail:
    """Publicly visible central clean room details."""

    central_clean_room_id: Optional[str] = None
    """Central clean room ID."""

    cloud_vendor: Optional[str] = None
    """Cloud vendor (aws,azure,gcp) of the central clean room."""

    collaborators: Optional[List[CleanRoomCollaborator]] = None
    """Collaborators in the central clean room. There should one and only one collaborator in the list
    that satisfies the owner condition:
    
    1. It has the creator's global_metastore_id (determined by caller of CreateCleanRoom).
    
    2. Its invite_recipient_email is empty."""

    compliance_security_profile: Optional[ComplianceSecurityProfile] = None
    """The compliance security profile used to process regulated data following compliance standards."""

    creator: Optional[CleanRoomCollaborator] = None
    """Collaborator who creates the clean room."""

    egress_network_policy: Optional[settings.EgressNetworkPolicy] = None
    """Egress network policy to apply to the central clean room workspace."""

    region: Optional[str] = None
    """Region of the central clean room."""

    def as_dict(self) -> dict:
        """Serializes the CleanRoomRemoteDetail into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.central_clean_room_id is not None:
            body["central_clean_room_id"] = self.central_clean_room_id
        if self.cloud_vendor is not None:
            body["cloud_vendor"] = self.cloud_vendor
        if self.collaborators:
            body["collaborators"] = [v.as_dict() for v in self.collaborators]
        if self.compliance_security_profile:
            body["compliance_security_profile"] = self.compliance_security_profile.as_dict()
        if self.creator:
            body["creator"] = self.creator.as_dict()
        if self.egress_network_policy:
            body["egress_network_policy"] = self.egress_network_policy.as_dict()
        if self.region is not None:
            body["region"] = self.region
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CleanRoomRemoteDetail into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.central_clean_room_id is not None:
            body["central_clean_room_id"] = self.central_clean_room_id
        if self.cloud_vendor is not None:
            body["cloud_vendor"] = self.cloud_vendor
        if self.collaborators:
            body["collaborators"] = self.collaborators
        if self.compliance_security_profile:
            body["compliance_security_profile"] = self.compliance_security_profile
        if self.creator:
            body["creator"] = self.creator
        if self.egress_network_policy:
            body["egress_network_policy"] = self.egress_network_policy
        if self.region is not None:
            body["region"] = self.region
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CleanRoomRemoteDetail:
        """Deserializes the CleanRoomRemoteDetail from a dictionary."""
        return cls(
            central_clean_room_id=d.get("central_clean_room_id", None),
            cloud_vendor=d.get("cloud_vendor", None),
            collaborators=_repeated_dict(d, "collaborators", CleanRoomCollaborator),
            compliance_security_profile=_from_dict(d, "compliance_security_profile", ComplianceSecurityProfile),
            creator=_from_dict(d, "creator", CleanRoomCollaborator),
            egress_network_policy=_from_dict(d, "egress_network_policy", settings.EgressNetworkPolicy),
            region=d.get("region", None),
        )


class CleanRoomStatusEnum(Enum):

    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    FAILED = "FAILED"
    PROVISIONING = "PROVISIONING"


@dataclass
class CollaboratorJobRunInfo:
    collaborator_alias: Optional[str] = None
    """Alias of the collaborator that triggered the task run."""

    collaborator_job_id: Optional[int] = None
    """Job ID of the task run in the collaborator's workspace."""

    collaborator_job_run_id: Optional[int] = None
    """Job run ID of the task run in the collaborator's workspace."""

    collaborator_task_run_id: Optional[int] = None
    """Task run ID of the task run in the collaborator's workspace."""

    collaborator_workspace_id: Optional[int] = None
    """ID of the collaborator's workspace that triggered the task run."""

    def as_dict(self) -> dict:
        """Serializes the CollaboratorJobRunInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.collaborator_alias is not None:
            body["collaborator_alias"] = self.collaborator_alias
        if self.collaborator_job_id is not None:
            body["collaborator_job_id"] = self.collaborator_job_id
        if self.collaborator_job_run_id is not None:
            body["collaborator_job_run_id"] = self.collaborator_job_run_id
        if self.collaborator_task_run_id is not None:
            body["collaborator_task_run_id"] = self.collaborator_task_run_id
        if self.collaborator_workspace_id is not None:
            body["collaborator_workspace_id"] = self.collaborator_workspace_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CollaboratorJobRunInfo into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.collaborator_alias is not None:
            body["collaborator_alias"] = self.collaborator_alias
        if self.collaborator_job_id is not None:
            body["collaborator_job_id"] = self.collaborator_job_id
        if self.collaborator_job_run_id is not None:
            body["collaborator_job_run_id"] = self.collaborator_job_run_id
        if self.collaborator_task_run_id is not None:
            body["collaborator_task_run_id"] = self.collaborator_task_run_id
        if self.collaborator_workspace_id is not None:
            body["collaborator_workspace_id"] = self.collaborator_workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CollaboratorJobRunInfo:
        """Deserializes the CollaboratorJobRunInfo from a dictionary."""
        return cls(
            collaborator_alias=d.get("collaborator_alias", None),
            collaborator_job_id=d.get("collaborator_job_id", None),
            collaborator_job_run_id=d.get("collaborator_job_run_id", None),
            collaborator_task_run_id=d.get("collaborator_task_run_id", None),
            collaborator_workspace_id=d.get("collaborator_workspace_id", None),
        )


@dataclass
class ComplianceSecurityProfile:
    """The compliance security profile used to process regulated data following compliance standards."""

    compliance_standards: Optional[List[settings.ComplianceStandard]] = None
    """The list of compliance standards that the compliance security profile is configured to enforce."""

    is_enabled: Optional[bool] = None
    """Whether the compliance security profile is enabled."""

    def as_dict(self) -> dict:
        """Serializes the ComplianceSecurityProfile into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.compliance_standards:
            body["compliance_standards"] = [v.as_dict() for v in self.compliance_standards]
        if self.is_enabled is not None:
            body["is_enabled"] = self.is_enabled
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ComplianceSecurityProfile into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.compliance_standards:
            body["compliance_standards"] = self.compliance_standards
        if self.is_enabled is not None:
            body["is_enabled"] = self.is_enabled
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ComplianceSecurityProfile:
        """Deserializes the ComplianceSecurityProfile from a dictionary."""
        return cls(
            compliance_standards=_repeated_dict(d, "compliance_standards", settings.ComplianceStandard),
            is_enabled=d.get("is_enabled", None),
        )


@dataclass
class CreateCleanRoomOutputCatalogResponse:
    output_catalog: Optional[CleanRoomOutputCatalog] = None

    def as_dict(self) -> dict:
        """Serializes the CreateCleanRoomOutputCatalogResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.output_catalog:
            body["output_catalog"] = self.output_catalog.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CreateCleanRoomOutputCatalogResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.output_catalog:
            body["output_catalog"] = self.output_catalog
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CreateCleanRoomOutputCatalogResponse:
        """Deserializes the CreateCleanRoomOutputCatalogResponse from a dictionary."""
        return cls(output_catalog=_from_dict(d, "output_catalog", CleanRoomOutputCatalog))


@dataclass
class DeleteCleanRoomAssetResponse:
    """Response for delete clean room request. Using an empty message since the generic Empty proto
    does not externd UnshadedMessageMarker."""

    def as_dict(self) -> dict:
        """Serializes the DeleteCleanRoomAssetResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DeleteCleanRoomAssetResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DeleteCleanRoomAssetResponse:
        """Deserializes the DeleteCleanRoomAssetResponse from a dictionary."""
        return cls()


@dataclass
class DeleteResponse:
    def as_dict(self) -> dict:
        """Serializes the DeleteResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DeleteResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DeleteResponse:
        """Deserializes the DeleteResponse from a dictionary."""
        return cls()


@dataclass
class ListCleanRoomAssetsResponse:
    assets: Optional[List[CleanRoomAsset]] = None
    """Assets in the clean room."""

    next_page_token: Optional[str] = None
    """Opaque token to retrieve the next page of results. Absent if there are no more pages. page_token
    should be set to this value for the next request (for the next page of results)."""

    def as_dict(self) -> dict:
        """Serializes the ListCleanRoomAssetsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.assets:
            body["assets"] = [v.as_dict() for v in self.assets]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListCleanRoomAssetsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.assets:
            body["assets"] = self.assets
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListCleanRoomAssetsResponse:
        """Deserializes the ListCleanRoomAssetsResponse from a dictionary."""
        return cls(assets=_repeated_dict(d, "assets", CleanRoomAsset), next_page_token=d.get("next_page_token", None))


@dataclass
class ListCleanRoomNotebookTaskRunsResponse:
    next_page_token: Optional[str] = None
    """Opaque token to retrieve the next page of results. Absent if there are no more pages. page_token
    should be set to this value for the next request (for the next page of results)."""

    runs: Optional[List[CleanRoomNotebookTaskRun]] = None
    """Name of the clean room."""

    def as_dict(self) -> dict:
        """Serializes the ListCleanRoomNotebookTaskRunsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.runs:
            body["runs"] = [v.as_dict() for v in self.runs]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListCleanRoomNotebookTaskRunsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.runs:
            body["runs"] = self.runs
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListCleanRoomNotebookTaskRunsResponse:
        """Deserializes the ListCleanRoomNotebookTaskRunsResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None), runs=_repeated_dict(d, "runs", CleanRoomNotebookTaskRun)
        )


@dataclass
class ListCleanRoomsResponse:
    clean_rooms: Optional[List[CleanRoom]] = None

    next_page_token: Optional[str] = None
    """Opaque token to retrieve the next page of results. Absent if there are no more pages. page_token
    should be set to this value for the next request (for the next page of results)."""

    def as_dict(self) -> dict:
        """Serializes the ListCleanRoomsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.clean_rooms:
            body["clean_rooms"] = [v.as_dict() for v in self.clean_rooms]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListCleanRoomsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.clean_rooms:
            body["clean_rooms"] = self.clean_rooms
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListCleanRoomsResponse:
        """Deserializes the ListCleanRoomsResponse from a dictionary."""
        return cls(
            clean_rooms=_repeated_dict(d, "clean_rooms", CleanRoom), next_page_token=d.get("next_page_token", None)
        )


@dataclass
class UpdateCleanRoomRequest:
    clean_room: Optional[CleanRoom] = None

    name: Optional[str] = None
    """Name of the clean room."""

    def as_dict(self) -> dict:
        """Serializes the UpdateCleanRoomRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.clean_room:
            body["clean_room"] = self.clean_room.as_dict()
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the UpdateCleanRoomRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.clean_room:
            body["clean_room"] = self.clean_room
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> UpdateCleanRoomRequest:
        """Deserializes the UpdateCleanRoomRequest from a dictionary."""
        return cls(clean_room=_from_dict(d, "clean_room", CleanRoom), name=d.get("name", None))


class CleanRoomAssetsAPI:
    """Clean room assets are data and code objects — Tables, volumes, and notebooks that are shared with the
    clean room."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, clean_room_name: str, asset: CleanRoomAsset) -> CleanRoomAsset:
        """Create an asset.

        Create a clean room asset —share an asset like a notebook or table into the clean room. For each UC
        asset that is added through this method, the clean room owner must also have enough privilege on the
        asset to consume it. The privilege must be maintained indefinitely for the clean room to be able to
        access the asset. Typically, you should use a group as the clean room owner.

        :param clean_room_name: str
          Name of the clean room.
        :param asset: :class:`CleanRoomAsset`
          Metadata of the clean room asset

        :returns: :class:`CleanRoomAsset`
        """
        body = asset.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", f"/api/2.0/clean-rooms/{clean_room_name}/assets", body=body, headers=headers)
        return CleanRoomAsset.from_dict(res)

    def delete(self, clean_room_name: str, asset_type: CleanRoomAssetAssetType, asset_full_name: str):
        """Delete an asset.

        Delete a clean room asset - unshare/remove the asset from the clean room

        :param clean_room_name: str
          Name of the clean room.
        :param asset_type: :class:`CleanRoomAssetAssetType`
          The type of the asset.
        :param asset_full_name: str
          The fully qualified name of the asset, it is same as the name field in CleanRoomAsset.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do(
            "DELETE",
            f"/api/2.0/clean-rooms/{clean_room_name}/assets/{asset_type.value}/{asset_full_name}",
            headers=headers,
        )

    def get(self, clean_room_name: str, asset_type: CleanRoomAssetAssetType, asset_full_name: str) -> CleanRoomAsset:
        """Get an asset.

        Get the details of a clean room asset by its type and full name.

        :param clean_room_name: str
          Name of the clean room.
        :param asset_type: :class:`CleanRoomAssetAssetType`
          The type of the asset.
        :param asset_full_name: str
          The fully qualified name of the asset, it is same as the name field in CleanRoomAsset.

        :returns: :class:`CleanRoomAsset`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET",
            f"/api/2.0/clean-rooms/{clean_room_name}/assets/{asset_type.value}/{asset_full_name}",
            headers=headers,
        )
        return CleanRoomAsset.from_dict(res)

    def list(self, clean_room_name: str, *, page_token: Optional[str] = None) -> Iterator[CleanRoomAsset]:
        """List assets.

        :param clean_room_name: str
          Name of the clean room.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.

        :returns: Iterator over :class:`CleanRoomAsset`
        """

        query = {}
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        while True:
            json = self._api.do("GET", f"/api/2.0/clean-rooms/{clean_room_name}/assets", query=query, headers=headers)
            if "assets" in json:
                for v in json["assets"]:
                    yield CleanRoomAsset.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def update(
        self, clean_room_name: str, asset_type: CleanRoomAssetAssetType, name: str, asset: CleanRoomAsset
    ) -> CleanRoomAsset:
        """Update an asset.

        Update a clean room asset. For example, updating the content of a notebook; changing the shared
        partitions of a table; etc.

        :param clean_room_name: str
          Name of the clean room.
        :param asset_type: :class:`CleanRoomAssetAssetType`
          The type of the asset.
        :param name: str
          A fully qualified name that uniquely identifies the asset within the clean room. This is also the
          name displayed in the clean room UI.

          For UC securable assets (tables, volumes, etc.), the format is
          *shared_catalog*.*shared_schema*.*asset_name*

          For notebooks, the name is the notebook file name.
        :param asset: :class:`CleanRoomAsset`
          Metadata of the clean room asset

        :returns: :class:`CleanRoomAsset`
        """
        body = asset.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "PATCH",
            f"/api/2.0/clean-rooms/{clean_room_name}/assets/{asset_type.value}/{name}",
            body=body,
            headers=headers,
        )
        return CleanRoomAsset.from_dict(res)


class CleanRoomTaskRunsAPI:
    """Clean room task runs are the executions of notebooks in a clean room."""

    def __init__(self, api_client):
        self._api = api_client

    def list(
        self,
        clean_room_name: str,
        *,
        notebook_name: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
    ) -> Iterator[CleanRoomNotebookTaskRun]:
        """List notebook task runs.

        List all the historical notebook task runs in a clean room.

        :param clean_room_name: str
          Name of the clean room.
        :param notebook_name: str (optional)
          Notebook name
        :param page_size: int (optional)
          The maximum number of task runs to return. Currently ignored - all runs will be returned.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.

        :returns: Iterator over :class:`CleanRoomNotebookTaskRun`
        """

        query = {}
        if notebook_name is not None:
            query["notebook_name"] = notebook_name
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        while True:
            json = self._api.do("GET", f"/api/2.0/clean-rooms/{clean_room_name}/runs", query=query, headers=headers)
            if "runs" in json:
                for v in json["runs"]:
                    yield CleanRoomNotebookTaskRun.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]


class CleanRoomsAPI:
    """A clean room uses Delta Sharing and serverless compute to provide a secure and privacy-protecting
    environment where multiple parties can work together on sensitive enterprise data without direct access to
    each other’s data."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, clean_room: CleanRoom) -> CleanRoom:
        """Create a clean room.

        Create a new clean room with the specified collaborators. This method is asynchronous; the returned
        name field inside the clean_room field can be used to poll the clean room status, using the
        :method:cleanrooms/get method. When this method returns, the clean room will be in a PROVISIONING
        state, with only name, owner, comment, created_at and status populated. The clean room will be usable
        once it enters an ACTIVE state.

        The caller must be a metastore admin or have the **CREATE_CLEAN_ROOM** privilege on the metastore.

        :param clean_room: :class:`CleanRoom`

        :returns: :class:`CleanRoom`
        """
        body = clean_room.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/clean-rooms", body=body, headers=headers)
        return CleanRoom.from_dict(res)

    def create_output_catalog(
        self, clean_room_name: str, output_catalog: CleanRoomOutputCatalog
    ) -> CreateCleanRoomOutputCatalogResponse:
        """Create an output catalog.

        Create the output catalog of the clean room.

        :param clean_room_name: str
          Name of the clean room.
        :param output_catalog: :class:`CleanRoomOutputCatalog`

        :returns: :class:`CreateCleanRoomOutputCatalogResponse`
        """
        body = output_catalog.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST", f"/api/2.0/clean-rooms/{clean_room_name}/output-catalogs", body=body, headers=headers
        )
        return CreateCleanRoomOutputCatalogResponse.from_dict(res)

    def delete(self, name: str):
        """Delete a clean room.

        Delete a clean room. After deletion, the clean room will be removed from the metastore. If the other
        collaborators have not deleted the clean room, they will still have the clean room in their metastore,
        but it will be in a DELETED state and no operations other than deletion can be performed on it.

        :param name: str
          Name of the clean room.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/clean-rooms/{name}", headers=headers)

    def get(self, name: str) -> CleanRoom:
        """Get a clean room.

        Get the details of a clean room given its name.

        :param name: str

        :returns: :class:`CleanRoom`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/clean-rooms/{name}", headers=headers)
        return CleanRoom.from_dict(res)

    def list(self, *, page_size: Optional[int] = None, page_token: Optional[str] = None) -> Iterator[CleanRoom]:
        """List clean rooms.

        Get a list of all clean rooms of the metastore. Only clean rooms the caller has access to are
        returned.

        :param page_size: int (optional)
          Maximum number of clean rooms to return (i.e., the page length). Defaults to 100.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.

        :returns: Iterator over :class:`CleanRoom`
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
            json = self._api.do("GET", "/api/2.0/clean-rooms", query=query, headers=headers)
            if "clean_rooms" in json:
                for v in json["clean_rooms"]:
                    yield CleanRoom.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def update(self, name: str, *, clean_room: Optional[CleanRoom] = None) -> CleanRoom:
        """Update a clean room.

        Update a clean room. The caller must be the owner of the clean room, have **MODIFY_CLEAN_ROOM**
        privilege, or be metastore admin.

        When the caller is a metastore admin, only the __owner__ field can be updated.

        :param name: str
          Name of the clean room.
        :param clean_room: :class:`CleanRoom` (optional)

        :returns: :class:`CleanRoom`
        """
        body = {}
        if clean_room is not None:
            body["clean_room"] = clean_room.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.0/clean-rooms/{name}", body=body, headers=headers)
        return CleanRoom.from_dict(res)

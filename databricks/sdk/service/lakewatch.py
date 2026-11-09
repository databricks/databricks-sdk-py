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
class AlertConfig:
    """Per-catalog alert-related config. Singleton. Name format: ``catalogs/{catalog}/alertConfig``."""

    default_security_alert_collation_window: Optional[str] = None
    """Window for collating Signals into security alerts. Duration string — compact
    day/hour/minute/second components, e.g. ``1d``, ``12h`` (see ``Schedule.at_least_every`` in
    common.proto for the grammar). Reads return the value as supplied. When unset or empty, the
    window is ``1h``; the window in effect is reported in
    ``effective_default_security_alert_collation_window``."""

    default_system_alert_collation_window: Optional[str] = None
    """Window for collating SystemEvents into system alerts. Duration string — compact
    day/hour/minute/second components, e.g. ``1d``, ``12h`` (see ``Schedule.at_least_every`` in
    common.proto for the grammar). Reads return the value as supplied. When unset or empty, the
    window is ``1d``; the window in effect is reported in
    ``effective_default_system_alert_collation_window``."""

    effective_default_security_alert_collation_window: Optional[str] = None
    """The security alert collation window in effect: ``default_security_alert_collation_window`` when
    set, otherwise ``1h``."""

    effective_default_system_alert_collation_window: Optional[str] = None
    """The system alert collation window in effect: ``default_system_alert_collation_window`` when set,
    otherwise ``1d``."""

    etag: Optional[str] = None
    """Opaque entity tag for optimistic concurrency. Returned on every read; pass it back as the Update
    request's ``etag`` to make the update conditional on the resource being unchanged."""

    name: Optional[str] = None

    security_alert_export_config: Optional[ExportConfig] = None
    """Export destination for security alerts. When unset, export is off and reads return ``{"enabled":
    false}``."""

    system_alert_export_config: Optional[ExportConfig] = None
    """Export destination for system alerts. When unset, export is off and reads return ``{"enabled":
    false}``."""

    update_time: Optional[Timestamp] = None

    updated_by: Optional[Principal] = None

    version: Optional[int] = None
    """Monotonic version, bumped on each update. Informational; use ``etag`` for optimistic
    concurrency."""

    def as_dict(self) -> dict:
        """Serializes the AlertConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.default_security_alert_collation_window is not None:
            body["default_security_alert_collation_window"] = self.default_security_alert_collation_window
        if self.default_system_alert_collation_window is not None:
            body["default_system_alert_collation_window"] = self.default_system_alert_collation_window
        if self.effective_default_security_alert_collation_window is not None:
            body["effective_default_security_alert_collation_window"] = (
                self.effective_default_security_alert_collation_window
            )
        if self.effective_default_system_alert_collation_window is not None:
            body["effective_default_system_alert_collation_window"] = (
                self.effective_default_system_alert_collation_window
            )
        if self.etag is not None:
            body["etag"] = self.etag
        if self.name is not None:
            body["name"] = self.name
        if self.security_alert_export_config:
            body["security_alert_export_config"] = self.security_alert_export_config.as_dict()
        if self.system_alert_export_config:
            body["system_alert_export_config"] = self.system_alert_export_config.as_dict()
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        if self.updated_by:
            body["updated_by"] = self.updated_by.as_dict()
        if self.version is not None:
            body["version"] = self.version
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AlertConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.default_security_alert_collation_window is not None:
            body["default_security_alert_collation_window"] = self.default_security_alert_collation_window
        if self.default_system_alert_collation_window is not None:
            body["default_system_alert_collation_window"] = self.default_system_alert_collation_window
        if self.effective_default_security_alert_collation_window is not None:
            body["effective_default_security_alert_collation_window"] = (
                self.effective_default_security_alert_collation_window
            )
        if self.effective_default_system_alert_collation_window is not None:
            body["effective_default_system_alert_collation_window"] = (
                self.effective_default_system_alert_collation_window
            )
        if self.etag is not None:
            body["etag"] = self.etag
        if self.name is not None:
            body["name"] = self.name
        if self.security_alert_export_config:
            body["security_alert_export_config"] = self.security_alert_export_config
        if self.system_alert_export_config:
            body["system_alert_export_config"] = self.system_alert_export_config
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.updated_by:
            body["updated_by"] = self.updated_by
        if self.version is not None:
            body["version"] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AlertConfig:
        """Deserializes the AlertConfig from a dictionary."""
        return cls(
            default_security_alert_collation_window=d.get("default_security_alert_collation_window", None),
            default_system_alert_collation_window=d.get("default_system_alert_collation_window", None),
            effective_default_security_alert_collation_window=d.get(
                "effective_default_security_alert_collation_window", None
            ),
            effective_default_system_alert_collation_window=d.get(
                "effective_default_system_alert_collation_window", None
            ),
            etag=d.get("etag", None),
            name=d.get("name", None),
            security_alert_export_config=_from_dict(d, "security_alert_export_config", ExportConfig),
            system_alert_export_config=_from_dict(d, "system_alert_export_config", ExportConfig),
            update_time=_timestamp(d, "update_time"),
            updated_by=_from_dict(d, "updated_by", Principal),
            version=_int64(d, "version"),
        )


@dataclass
class AutoLoader:
    """Ingests files from cloud storage with Auto Loader. Mutually exclusive with
    ``unity_catalog_connection`` and ``existing_table``."""

    format: AutoLoaderFormat
    """File format of the source files. Required."""

    location: str
    """URI of the source files: a path in a Unity Catalog volume or external location, or a cloud
    storage URL such as an Amazon S3 path. Required, including when new files are discovered through
    ``queue_url``. Cannot be changed after creation."""

    raw_table: TableName
    """Table that stores the raw data before parsers schematize it. Every Auto Loader datasource writes
    its raw rows to this table before any parser reads them. The table must be in the datasource's
    catalog and schema; an omitted ``catalog_name`` or ``schema_name`` defaults to them. Cannot be
    changed after creation. Reads return the value as supplied; the table the data is written to is
    reported in ``effective_raw_table``."""

    aws_secret_scope: Optional[str] = None
    """Name of the workspace secret scope that holds the AWS access key ID and secret access key, under
    the keys ``awsAccessKeyId`` and ``awsSecretAccessKey``."""

    effective_include_existing_files: Optional[bool] = None
    """Whether ingestion started with the files already present at ``location``. Populated on get,
    create, and update responses."""

    effective_raw_table: Optional[TableName] = None
    """The table that the raw data is written to: ``raw_table`` in the datasource's catalog and schema,
    under their current Unity Catalog names. Populated on get, create, and update responses."""

    envelope: Optional[Envelope] = None
    """How to unwrap a transport envelope around the source records before parsing. Supported only for
    the JSON and JSONL formats. If unset, each source record is treated as one event."""

    format_options: Optional[Dict[str, str]] = None
    """Format-specific parsing options, passed to Auto Loader. Supported for the CSV, JSON, JSONL, and
    XML formats, each of which accepts a fixed set of options. The XML format requires the
    ``rowTag`` option."""

    include_existing_files: Optional[bool] = None
    """Whether to ingest the files already present at ``location`` when ingestion first starts. Set
    true to ingest the existing files and then every new file. Set false, or leave unset, to ingest
    only files that arrive after the datasource starts. Defaults to false. Cannot be changed after
    creation. Reads return the value as supplied; the setting in effect is reported in
    ``effective_include_existing_files``."""

    override_partition_columns: Optional[List[str]] = None
    """Hive-style partition columns to derive from the source file paths. If unset, no partition
    columns are derived."""

    queue_url: Optional[str] = None
    """URL of a customer-managed Amazon SQS queue that receives file-arrival notifications. Set it to
    discover new files through the queue. If unset, new files are discovered through the file events
    of the source's Unity Catalog external location when it has them configured, and by directory
    listing otherwise. Cannot be changed after creation."""

    service_credentials: Optional[str] = None
    """Name of the Unity Catalog service credential to use."""

    def as_dict(self) -> dict:
        """Serializes the AutoLoader into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.aws_secret_scope is not None:
            body["aws_secret_scope"] = self.aws_secret_scope
        if self.effective_include_existing_files is not None:
            body["effective_include_existing_files"] = self.effective_include_existing_files
        if self.effective_raw_table:
            body["effective_raw_table"] = self.effective_raw_table.as_dict()
        if self.envelope:
            body["envelope"] = self.envelope.as_dict()
        if self.format is not None:
            body["format"] = self.format.value
        if self.format_options:
            body["format_options"] = self.format_options
        if self.include_existing_files is not None:
            body["include_existing_files"] = self.include_existing_files
        if self.location is not None:
            body["location"] = self.location
        if self.override_partition_columns:
            body["override_partition_columns"] = [v for v in self.override_partition_columns]
        if self.queue_url is not None:
            body["queue_url"] = self.queue_url
        if self.raw_table:
            body["raw_table"] = self.raw_table.as_dict()
        if self.service_credentials is not None:
            body["service_credentials"] = self.service_credentials
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AutoLoader into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.aws_secret_scope is not None:
            body["aws_secret_scope"] = self.aws_secret_scope
        if self.effective_include_existing_files is not None:
            body["effective_include_existing_files"] = self.effective_include_existing_files
        if self.effective_raw_table:
            body["effective_raw_table"] = self.effective_raw_table
        if self.envelope:
            body["envelope"] = self.envelope
        if self.format is not None:
            body["format"] = self.format
        if self.format_options:
            body["format_options"] = self.format_options
        if self.include_existing_files is not None:
            body["include_existing_files"] = self.include_existing_files
        if self.location is not None:
            body["location"] = self.location
        if self.override_partition_columns:
            body["override_partition_columns"] = self.override_partition_columns
        if self.queue_url is not None:
            body["queue_url"] = self.queue_url
        if self.raw_table:
            body["raw_table"] = self.raw_table
        if self.service_credentials is not None:
            body["service_credentials"] = self.service_credentials
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AutoLoader:
        """Deserializes the AutoLoader from a dictionary."""
        return cls(
            aws_secret_scope=d.get("aws_secret_scope", None),
            effective_include_existing_files=d.get("effective_include_existing_files", None),
            effective_raw_table=_from_dict(d, "effective_raw_table", TableName),
            envelope=_from_dict(d, "envelope", Envelope),
            format=_enum(d, "format", AutoLoaderFormat),
            format_options=d.get("format_options", None),
            include_existing_files=d.get("include_existing_files", None),
            location=d.get("location", None),
            override_partition_columns=d.get("override_partition_columns", None),
            queue_url=d.get("queue_url", None),
            raw_table=_from_dict(d, "raw_table", TableName),
            service_credentials=d.get("service_credentials", None),
        )


class AutoLoaderFormat(Enum):
    """File format of the source files that Auto Loader reads."""

    AUTOLOADER_FORMAT_CSV = "AUTOLOADER_FORMAT_CSV"
    AUTOLOADER_FORMAT_JSON = "AUTOLOADER_FORMAT_JSON"
    AUTOLOADER_FORMAT_JSONL = "AUTOLOADER_FORMAT_JSONL"
    AUTOLOADER_FORMAT_PARQUET = "AUTOLOADER_FORMAT_PARQUET"
    AUTOLOADER_FORMAT_XML = "AUTOLOADER_FORMAT_XML"


@dataclass
class CloudWatchLogsEnvelope:
    """Unwraps an AWS CloudWatch Logs delivery envelope: each element of ``logEvents`` becomes its own
    row, with the element's ``message`` parsed as the event body."""

    header_retention: Optional[bool] = None
    """Whether to keep the envelope's ``owner``, ``logGroup``, and ``logStream`` values in the
    ``data.lw_header`` field of each unwrapped row. Must be set explicitly to ``true`` or ``false``."""

    def as_dict(self) -> dict:
        """Serializes the CloudWatchLogsEnvelope into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.header_retention is not None:
            body["header_retention"] = self.header_retention
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CloudWatchLogsEnvelope into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.header_retention is not None:
            body["header_retention"] = self.header_retention
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CloudWatchLogsEnvelope:
        """Deserializes the CloudWatchLogsEnvelope from a dictionary."""
        return cls(header_retention=d.get("header_retention", None))


@dataclass
class CommonConfig:
    """Catch-all per-catalog config — settings that don't belong to any one resource family.
    Singleton. Name format: ``catalogs/{catalog}/commonConfig``."""

    custom_content_pack_path: Optional[str] = None
    """UC volume path holding user-authored custom content packs, e.g.
    ``/Volumes/{catalog}/{schema}/{volume}``. User-provided with no default: when unset, custom
    content packs are unavailable (referencing one is rejected) and only built-in content packs
    apply."""

    custom_presets_path: Optional[str] = None
    """UC volume path holding user-authored custom presets, e.g.
    ``/Volumes/{catalog}/{schema}/{volume}``. User-provided with no default: when unset, custom
    presets are unavailable and only built-in presets apply."""

    etag: Optional[str] = None
    """Opaque entity tag for optimistic concurrency. Returned on every read; pass it back as the Update
    request's ``etag`` to make the update conditional on the resource being unchanged."""

    name: Optional[str] = None

    per_resource_permissions_enabled: Optional[bool] = None
    """Whether users may grant permissions on individual resources rather than only at the Folder
    level."""

    update_time: Optional[Timestamp] = None

    updated_by: Optional[Principal] = None

    version: Optional[int] = None
    """Monotonic version, bumped on each update. Informational; use ``etag`` for optimistic
    concurrency."""

    def as_dict(self) -> dict:
        """Serializes the CommonConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.custom_content_pack_path is not None:
            body["custom_content_pack_path"] = self.custom_content_pack_path
        if self.custom_presets_path is not None:
            body["custom_presets_path"] = self.custom_presets_path
        if self.etag is not None:
            body["etag"] = self.etag
        if self.name is not None:
            body["name"] = self.name
        if self.per_resource_permissions_enabled is not None:
            body["per_resource_permissions_enabled"] = self.per_resource_permissions_enabled
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        if self.updated_by:
            body["updated_by"] = self.updated_by.as_dict()
        if self.version is not None:
            body["version"] = self.version
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CommonConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.custom_content_pack_path is not None:
            body["custom_content_pack_path"] = self.custom_content_pack_path
        if self.custom_presets_path is not None:
            body["custom_presets_path"] = self.custom_presets_path
        if self.etag is not None:
            body["etag"] = self.etag
        if self.name is not None:
            body["name"] = self.name
        if self.per_resource_permissions_enabled is not None:
            body["per_resource_permissions_enabled"] = self.per_resource_permissions_enabled
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.updated_by:
            body["updated_by"] = self.updated_by
        if self.version is not None:
            body["version"] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CommonConfig:
        """Deserializes the CommonConfig from a dictionary."""
        return cls(
            custom_content_pack_path=d.get("custom_content_pack_path", None),
            custom_presets_path=d.get("custom_presets_path", None),
            etag=d.get("etag", None),
            name=d.get("name", None),
            per_resource_permissions_enabled=d.get("per_resource_permissions_enabled", None),
            update_time=_timestamp(d, "update_time"),
            updated_by=_from_dict(d, "updated_by", Principal),
            version=_int64(d, "version"),
        )


@dataclass
class ContentPackReference:
    """Reference to the ContentPack (and pack version) a resource was originally installed from."""

    uuid: Optional[str] = None
    """UUID of the content pack."""

    version: Optional[str] = None
    """Pack version the resource was installed from."""

    def as_dict(self) -> dict:
        """Serializes the ContentPackReference into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.uuid is not None:
            body["uuid"] = self.uuid
        if self.version is not None:
            body["version"] = self.version
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ContentPackReference into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.uuid is not None:
            body["uuid"] = self.uuid
        if self.version is not None:
            body["version"] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ContentPackReference:
        """Deserializes the ContentPackReference from a dictionary."""
        return cls(uuid=d.get("uuid", None), version=d.get("version", None))


@dataclass
class Datasource:
    """A Lakewatch datasource: a pipeline that ingests security data and writes it to Unity Catalog
    tables.

    What a datasource ingests is defined by its ingestion method (``autoloader``,
    ``unity_catalog_connection``, or ``existing_table``), which sets how the data arrives, together
    with its ``parsers``, which define the schemas that the arriving data is matched against and
    written as."""

    catalog_name: str
    """Name of the Unity Catalog catalog that contains the datasource. Required on create and cannot be
    changed afterward. Reads return the value as supplied; the catalog's current name is reported in
    ``effective_catalog_name``."""

    schema_name: str
    """Name of the Unity Catalog schema that contains the datasource. Required on create and cannot be
    changed afterward. Reads return the value as supplied; the schema's current name is reported in
    ``effective_schema_name``."""

    datasource_name: str
    """Name of the datasource in Unity Catalog, unique within its schema. Required on create and can be
    updated within the same catalog and schema. Get synchronizes this field with the current Unity
    Catalog name, also reported in ``effective_datasource_name``."""

    schedule: Schedule
    """Schedule on which the datasource's ingestion job runs. A datasource cannot be paused, so a
    request that sets ``schedule.enabled`` to ``false`` is rejected. Continuous schedules are not
    supported for Unity Catalog connection datasources."""

    annotations: Optional[Dict[str, str]] = None
    """Free-form key-value annotations on the datasource, managed by the client."""

    autoloader: Optional[AutoLoader] = None

    compute_mode: Optional[DatasourceComputeMode] = None
    """Compute mode for the datasource's ingestion job. If unset, the ``default_compute_mode`` of the
    catalog's datasource configuration applies, or ``DS_COMPUTE_PERFORMANCE_OPTIMIZED`` if the
    catalog has none."""

    compute_workspace_id: Optional[str] = None
    """ID of the workspace whose compute runs this datasource's ingestion job and owns its associated
    resources, such as the storage the ingested data lands in. Server-assigned."""

    create_time: Optional[Timestamp] = None

    created_by: Optional[Principal] = None

    datasource_id: Optional[str] = None
    """Unity Catalog securable ID (a UUID) of the datasource. It never changes, including when the
    datasource is renamed in Unity Catalog, and is the final segment of ``name``."""

    description: Optional[str] = None
    """Free-form description of the datasource."""

    effective_catalog_name: Optional[str] = None
    """Current name of the Unity Catalog catalog that contains the datasource, which reflects catalog
    renames without a change to ``catalog_name``. Populated on get, create, and update responses;
    list responses omit it."""

    effective_datasource_name: Optional[str] = None
    """Current UC leaf name of the datasource (server-owned). Tracks UC renames so callers can observe
    the live name without having to update the client-owned ``datasource_name``; unset until
    resolved."""

    effective_run_as_principal: Optional[str] = None
    """The identity the datasource runs as: the resolved ``run_as_principal``, or the requester's
    identity if ``run_as_principal`` was omitted on create or cleared on update. Given as a user
    email or service principal application ID, or as the numeric principal ID if the identity can no
    longer be resolved. Populated on get, create, and update responses; list responses omit it."""

    effective_schema_name: Optional[str] = None
    """Current name of the Unity Catalog schema that contains the datasource, which reflects schema
    renames without a change to ``schema_name``. Populated on get, create, and update responses;
    list responses omit it."""

    etag: Optional[str] = None
    """Opaque entity tag for optimistic concurrency control. Returned by get, create, and update
    responses and by list responses in the ``DATASOURCE_VIEW_FULL`` view. To make an update
    conditional on the datasource not having changed since it was read, pass this value as the
    update request's ``etag``. Changes to ``status`` do not change the etag."""

    existing_table: Optional[ExistingTable] = None

    name: Optional[str] = None
    """Resource name of the datasource, in the format ``datasources/{datasource_id}``. Unlike the
    datasource's Unity Catalog location (``catalog_name``, ``schema_name``, and
    ``datasource_name``), the name does not change when the datasource or its catalog or schema is
    renamed in Unity Catalog."""

    owner: Optional[Principal] = None
    """Unity Catalog owner of the datasource, assigned by the server. Create responses omit it."""

    parsers: Optional[List[ParserRef]] = None
    """Parsers that schematize the ingested data. Each record is matched against the parsers in order
    and written to the parsed table of the first parser that it matches. Existing-table and Unity
    Catalog connection datasources require at least one parser; an Auto Loader datasource with no
    parsers writes only its raw table."""

    run_as_principal: Optional[str] = None
    """The user or service principal that the datasource runs as, given as a user email or service
    principal application ID. When it is supplied on create or update, the requester must be
    authorized to run the datasource as that principal, or the request is rejected. When it is
    omitted on create, the datasource runs as the requester. On update, a mask that includes
    ``run_as_principal`` without a value clears it, so the datasource runs as the requester; a mask
    that omits it keeps the current identity. Reads return the value as supplied; the identity the
    datasource runs as is reported in ``effective_run_as_principal``."""

    status: Optional[DatasourceStatus] = None
    """Runtime status of the jobs and pipelines that run this datasource."""

    unity_catalog_connection: Optional[UnityCatalogConnection] = None

    update_time: Optional[Timestamp] = None

    updated_by: Optional[Principal] = None

    version: Optional[int] = None
    """Version number of the datasource, incremented on each update. Informational only; use ``etag``
    for optimistic concurrency control."""

    warehouse_id: Optional[str] = None
    """ID of the SQL warehouse that runs the checks Lakewatch performs to validate a create or update
    request, such as source and destination access checks. Required and non-blank on every create
    and update request except a rename-only PATCH; there is no default warehouse. The requester must
    be able to use the warehouse. It is not stored, is not returned on reads, and does not affect
    the compute that runs the ingestion job."""

    def as_dict(self) -> dict:
        """Serializes the Datasource into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.annotations:
            body["annotations"] = self.annotations
        if self.autoloader:
            body["autoloader"] = self.autoloader.as_dict()
        if self.catalog_name is not None:
            body["catalog_name"] = self.catalog_name
        if self.compute_mode is not None:
            body["compute_mode"] = self.compute_mode.value
        if self.compute_workspace_id is not None:
            body["compute_workspace_id"] = self.compute_workspace_id
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.created_by:
            body["created_by"] = self.created_by.as_dict()
        if self.datasource_id is not None:
            body["datasource_id"] = self.datasource_id
        if self.datasource_name is not None:
            body["datasource_name"] = self.datasource_name
        if self.description is not None:
            body["description"] = self.description
        if self.effective_catalog_name is not None:
            body["effective_catalog_name"] = self.effective_catalog_name
        if self.effective_datasource_name is not None:
            body["effective_datasource_name"] = self.effective_datasource_name
        if self.effective_run_as_principal is not None:
            body["effective_run_as_principal"] = self.effective_run_as_principal
        if self.effective_schema_name is not None:
            body["effective_schema_name"] = self.effective_schema_name
        if self.etag is not None:
            body["etag"] = self.etag
        if self.existing_table:
            body["existing_table"] = self.existing_table.as_dict()
        if self.name is not None:
            body["name"] = self.name
        if self.owner:
            body["owner"] = self.owner.as_dict()
        if self.parsers:
            body["parsers"] = [v.as_dict() for v in self.parsers]
        if self.run_as_principal is not None:
            body["run_as_principal"] = self.run_as_principal
        if self.schedule:
            body["schedule"] = self.schedule.as_dict()
        if self.schema_name is not None:
            body["schema_name"] = self.schema_name
        if self.status:
            body["status"] = self.status.as_dict()
        if self.unity_catalog_connection:
            body["unity_catalog_connection"] = self.unity_catalog_connection.as_dict()
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        if self.updated_by:
            body["updated_by"] = self.updated_by.as_dict()
        if self.version is not None:
            body["version"] = self.version
        if self.warehouse_id is not None:
            body["warehouse_id"] = self.warehouse_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Datasource into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.annotations:
            body["annotations"] = self.annotations
        if self.autoloader:
            body["autoloader"] = self.autoloader
        if self.catalog_name is not None:
            body["catalog_name"] = self.catalog_name
        if self.compute_mode is not None:
            body["compute_mode"] = self.compute_mode
        if self.compute_workspace_id is not None:
            body["compute_workspace_id"] = self.compute_workspace_id
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.created_by:
            body["created_by"] = self.created_by
        if self.datasource_id is not None:
            body["datasource_id"] = self.datasource_id
        if self.datasource_name is not None:
            body["datasource_name"] = self.datasource_name
        if self.description is not None:
            body["description"] = self.description
        if self.effective_catalog_name is not None:
            body["effective_catalog_name"] = self.effective_catalog_name
        if self.effective_datasource_name is not None:
            body["effective_datasource_name"] = self.effective_datasource_name
        if self.effective_run_as_principal is not None:
            body["effective_run_as_principal"] = self.effective_run_as_principal
        if self.effective_schema_name is not None:
            body["effective_schema_name"] = self.effective_schema_name
        if self.etag is not None:
            body["etag"] = self.etag
        if self.existing_table:
            body["existing_table"] = self.existing_table
        if self.name is not None:
            body["name"] = self.name
        if self.owner:
            body["owner"] = self.owner
        if self.parsers:
            body["parsers"] = self.parsers
        if self.run_as_principal is not None:
            body["run_as_principal"] = self.run_as_principal
        if self.schedule:
            body["schedule"] = self.schedule
        if self.schema_name is not None:
            body["schema_name"] = self.schema_name
        if self.status:
            body["status"] = self.status
        if self.unity_catalog_connection:
            body["unity_catalog_connection"] = self.unity_catalog_connection
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.updated_by:
            body["updated_by"] = self.updated_by
        if self.version is not None:
            body["version"] = self.version
        if self.warehouse_id is not None:
            body["warehouse_id"] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Datasource:
        """Deserializes the Datasource from a dictionary."""
        return cls(
            annotations=d.get("annotations", None),
            autoloader=_from_dict(d, "autoloader", AutoLoader),
            catalog_name=d.get("catalog_name", None),
            compute_mode=_enum(d, "compute_mode", DatasourceComputeMode),
            compute_workspace_id=d.get("compute_workspace_id", None),
            create_time=_timestamp(d, "create_time"),
            created_by=_from_dict(d, "created_by", Principal),
            datasource_id=d.get("datasource_id", None),
            datasource_name=d.get("datasource_name", None),
            description=d.get("description", None),
            effective_catalog_name=d.get("effective_catalog_name", None),
            effective_datasource_name=d.get("effective_datasource_name", None),
            effective_run_as_principal=d.get("effective_run_as_principal", None),
            effective_schema_name=d.get("effective_schema_name", None),
            etag=d.get("etag", None),
            existing_table=_from_dict(d, "existing_table", ExistingTable),
            name=d.get("name", None),
            owner=_from_dict(d, "owner", Principal),
            parsers=_repeated_dict(d, "parsers", ParserRef),
            run_as_principal=d.get("run_as_principal", None),
            schedule=_from_dict(d, "schedule", Schedule),
            schema_name=d.get("schema_name", None),
            status=_from_dict(d, "status", DatasourceStatus),
            unity_catalog_connection=_from_dict(d, "unity_catalog_connection", UnityCatalogConnection),
            update_time=_timestamp(d, "update_time"),
            updated_by=_from_dict(d, "updated_by", Principal),
            version=_int64(d, "version"),
            warehouse_id=d.get("warehouse_id", None),
        )


class DatasourceComputeMode(Enum):
    """Compute mode for the datasource's ingestion job."""

    DS_COMPUTE_PERFORMANCE_OPTIMIZED = "DS_COMPUTE_PERFORMANCE_OPTIMIZED"
    DS_COMPUTE_STANDARD = "DS_COMPUTE_STANDARD"


@dataclass
class DatasourceConfig:
    """Per-catalog datasource-related config. Singleton. Name format:
    ``catalogs/{catalog}/datasourceConfig``."""

    default_compute_mode: Optional[DatasourceComputeMode] = None
    """Default compute mode applied to datasource ingestion jobs when the individual datasource doesn't
    override it. v1 ``datasources.defaultComputeMode``."""

    default_folder: Optional[str] = None
    """Schema name of the registered folder (in this catalog) that a new datasource is placed in when
    the request does not specify a schema. Must name a schema registered as a folder. Omit to clear.
    Reads return the value as supplied; the folder's current schema name is reported in
    ``effective_default_folder``."""

    effective_default_folder: Optional[str] = None
    """The current schema name of the ``default_folder`` folder. Tracks UC schema renames. Unset when
    no default is configured, or when the folder's schema no longer exists or is not visible to the
    caller."""

    etag: Optional[str] = None
    """Opaque entity tag for optimistic concurrency. Returned on every read; pass it back as the Update
    request's ``etag`` to make the update conditional on the resource being unchanged."""

    name: Optional[str] = None

    update_time: Optional[Timestamp] = None

    updated_by: Optional[Principal] = None

    version: Optional[int] = None
    """Monotonic version, bumped on each update. Informational; use ``etag`` for optimistic
    concurrency."""

    def as_dict(self) -> dict:
        """Serializes the DatasourceConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.default_compute_mode is not None:
            body["default_compute_mode"] = self.default_compute_mode.value
        if self.default_folder is not None:
            body["default_folder"] = self.default_folder
        if self.effective_default_folder is not None:
            body["effective_default_folder"] = self.effective_default_folder
        if self.etag is not None:
            body["etag"] = self.etag
        if self.name is not None:
            body["name"] = self.name
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        if self.updated_by:
            body["updated_by"] = self.updated_by.as_dict()
        if self.version is not None:
            body["version"] = self.version
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatasourceConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.default_compute_mode is not None:
            body["default_compute_mode"] = self.default_compute_mode
        if self.default_folder is not None:
            body["default_folder"] = self.default_folder
        if self.effective_default_folder is not None:
            body["effective_default_folder"] = self.effective_default_folder
        if self.etag is not None:
            body["etag"] = self.etag
        if self.name is not None:
            body["name"] = self.name
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.updated_by:
            body["updated_by"] = self.updated_by
        if self.version is not None:
            body["version"] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatasourceConfig:
        """Deserializes the DatasourceConfig from a dictionary."""
        return cls(
            default_compute_mode=_enum(d, "default_compute_mode", DatasourceComputeMode),
            default_folder=d.get("default_folder", None),
            effective_default_folder=d.get("effective_default_folder", None),
            etag=d.get("etag", None),
            name=d.get("name", None),
            update_time=_timestamp(d, "update_time"),
            updated_by=_from_dict(d, "updated_by", Principal),
            version=_int64(d, "version"),
        )


@dataclass
class DatasourceStatus:
    """Read-only runtime status of a datasource, with the status of each job and pipeline that runs it."""

    ingestion_job: Optional[ResourceStatus] = None
    """Status of the datasource's ingestion job."""

    ingestion_pipeline: Optional[ResourceStatus] = None
    """Status of the managed ingestion pipeline. Populated only when ``unity_catalog_connection`` is
    set, with ``pipeline_id`` identifying the pipeline."""

    def as_dict(self) -> dict:
        """Serializes the DatasourceStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.ingestion_job:
            body["ingestion_job"] = self.ingestion_job.as_dict()
        if self.ingestion_pipeline:
            body["ingestion_pipeline"] = self.ingestion_pipeline.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatasourceStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.ingestion_job:
            body["ingestion_job"] = self.ingestion_job
        if self.ingestion_pipeline:
            body["ingestion_pipeline"] = self.ingestion_pipeline
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatasourceStatus:
        """Deserializes the DatasourceStatus from a dictionary."""
        return cls(
            ingestion_job=_from_dict(d, "ingestion_job", ResourceStatus),
            ingestion_pipeline=_from_dict(d, "ingestion_pipeline", ResourceStatus),
        )


class DatasourceView(Enum):
    """Which fields list responses return for each datasource."""

    DATASOURCE_VIEW_BASIC = "DATASOURCE_VIEW_BASIC"
    DATASOURCE_VIEW_FULL = "DATASOURCE_VIEW_FULL"


@dataclass
class Envelope:
    """Unwraps a transport envelope from the source data so that each contained event becomes its own
    row. Applied when the source data is read, before parsing."""

    cloud_watch_logs: Optional[CloudWatchLogsEnvelope] = None

    json_array: Optional[JsonArrayEnvelope] = None

    def as_dict(self) -> dict:
        """Serializes the Envelope into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.cloud_watch_logs:
            body["cloud_watch_logs"] = self.cloud_watch_logs.as_dict()
        if self.json_array:
            body["json_array"] = self.json_array.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Envelope into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.cloud_watch_logs:
            body["cloud_watch_logs"] = self.cloud_watch_logs
        if self.json_array:
            body["json_array"] = self.json_array
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Envelope:
        """Deserializes the Envelope from a dictionary."""
        return cls(
            cloud_watch_logs=_from_dict(d, "cloud_watch_logs", CloudWatchLogsEnvelope),
            json_array=_from_dict(d, "json_array", JsonArrayEnvelope),
        )


@dataclass
class ExistingTable:
    """Uses an existing Unity Catalog Delta table or view as the datasource's source. Mutually
    exclusive with ``autoloader`` and ``unity_catalog_connection``."""

    name: str
    """Name of the source table or view. Required on create and cannot be changed. Reads return the
    value as supplied; the table's current name is reported in ``effective_name``."""

    catalog: Optional[str] = None
    """Name of the catalog the existing table lives in. Optional on create and defaults to the
    datasource's own catalog. Cannot be changed. Reads return the value as supplied; the catalog in
    use is reported in ``effective_catalog``."""

    effective_catalog: Optional[str] = None
    """Current Unity Catalog catalog name of the source table, resolved from its stable table ID, so a
    rename of the source table is reported here without changing ``catalog``."""

    effective_name: Optional[str] = None
    """Current Unity Catalog name of the source table, resolved from its stable table ID."""

    effective_schema: Optional[str] = None
    """Current Unity Catalog schema name of the source table, resolved from its stable table ID."""

    include_existing_rows: Optional[bool] = None
    """Whether to ingest the rows already present in the source table when ingestion first starts. Set
    true to ingest the existing rows and then every new commit. Set false, or leave unset, to ingest
    only rows written after the datasource starts. Defaults to false, and must be true for a Delta
    Sharing source table. Takes effect only at first start and cannot be changed. Reads return the
    value as supplied."""

    schema: Optional[str] = None
    """Name of the schema the existing table lives in. Optional, but required when ``catalog`` is set;
    supplying ``catalog`` without ``schema`` is rejected. Defaults to the datasource's own schema.
    Cannot be changed. Reads return the value as supplied; the schema in use is reported in
    ``effective_schema``."""

    def as_dict(self) -> dict:
        """Serializes the ExistingTable into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.catalog is not None:
            body["catalog"] = self.catalog
        if self.effective_catalog is not None:
            body["effective_catalog"] = self.effective_catalog
        if self.effective_name is not None:
            body["effective_name"] = self.effective_name
        if self.effective_schema is not None:
            body["effective_schema"] = self.effective_schema
        if self.include_existing_rows is not None:
            body["include_existing_rows"] = self.include_existing_rows
        if self.name is not None:
            body["name"] = self.name
        if self.schema is not None:
            body["schema"] = self.schema
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ExistingTable into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.catalog is not None:
            body["catalog"] = self.catalog
        if self.effective_catalog is not None:
            body["effective_catalog"] = self.effective_catalog
        if self.effective_name is not None:
            body["effective_name"] = self.effective_name
        if self.effective_schema is not None:
            body["effective_schema"] = self.effective_schema
        if self.include_existing_rows is not None:
            body["include_existing_rows"] = self.include_existing_rows
        if self.name is not None:
            body["name"] = self.name
        if self.schema is not None:
            body["schema"] = self.schema
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ExistingTable:
        """Deserializes the ExistingTable from a dictionary."""
        return cls(
            catalog=d.get("catalog", None),
            effective_catalog=d.get("effective_catalog", None),
            effective_name=d.get("effective_name", None),
            effective_schema=d.get("effective_schema", None),
            include_existing_rows=d.get("include_existing_rows", None),
            name=d.get("name", None),
            schema=d.get("schema", None),
        )


@dataclass
class ExportConfig:
    """Configuration for delivering events / alerts to an external destination.

    Exactly one of the destination variants is set; the server picks it via the ``oneof``."""

    enabled: Optional[bool] = None
    """Whether export is currently active."""

    jira: Optional[JiraExportConfig] = None

    service_now: Optional[ServiceNowExportConfig] = None

    slack: Optional[SlackExportConfig] = None

    tines: Optional[TinesExportConfig] = None

    webhook: Optional[WebhookExportConfig] = None

    workspace_id: Optional[str] = None
    """Deprecated and ignored: exports always egress through the request's own workspace. Kept so
    configs stored by older builds still round-trip."""

    def as_dict(self) -> dict:
        """Serializes the ExportConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.enabled is not None:
            body["enabled"] = self.enabled
        if self.jira:
            body["jira"] = self.jira.as_dict()
        if self.service_now:
            body["service_now"] = self.service_now.as_dict()
        if self.slack:
            body["slack"] = self.slack.as_dict()
        if self.tines:
            body["tines"] = self.tines.as_dict()
        if self.webhook:
            body["webhook"] = self.webhook.as_dict()
        if self.workspace_id is not None:
            body["workspace_id"] = self.workspace_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ExportConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.enabled is not None:
            body["enabled"] = self.enabled
        if self.jira:
            body["jira"] = self.jira
        if self.service_now:
            body["service_now"] = self.service_now
        if self.slack:
            body["slack"] = self.slack
        if self.tines:
            body["tines"] = self.tines
        if self.webhook:
            body["webhook"] = self.webhook
        if self.workspace_id is not None:
            body["workspace_id"] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ExportConfig:
        """Deserializes the ExportConfig from a dictionary."""
        return cls(
            enabled=d.get("enabled", None),
            jira=_from_dict(d, "jira", JiraExportConfig),
            service_now=_from_dict(d, "service_now", ServiceNowExportConfig),
            slack=_from_dict(d, "slack", SlackExportConfig),
            tines=_from_dict(d, "tines", TinesExportConfig),
            webhook=_from_dict(d, "webhook", WebhookExportConfig),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class JiraExportConfig:
    instance_url: str
    """Jira instance URL (e.g. ``https://acme.atlassian.net``)."""

    project_key: str
    """Jira project key the exported issues are created under."""

    user_email: str
    """User email paired with the API token for Jira Cloud basic auth."""

    default_issue_type: str
    """Default issue type for created tickets (e.g. ``Task``, ``Incident``). Jira issue creation
    requires an issue type, so it is validated at config-save time rather than failing the export at
    Jira later."""

    api_token_uc_secret: str
    """Three-level Unity Catalog name (``catalog.schema.secret``) of the secret holding the Jira API
    token, paired with ``user_email`` as the Jira Cloud basic-auth credential (``email:token``).
    Only the name is stored; the token is read when an alert is exported, so rotating the secret
    takes effect without editing this config."""

    def as_dict(self) -> dict:
        """Serializes the JiraExportConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.api_token_uc_secret is not None:
            body["api_token_uc_secret"] = self.api_token_uc_secret
        if self.default_issue_type is not None:
            body["default_issue_type"] = self.default_issue_type
        if self.instance_url is not None:
            body["instance_url"] = self.instance_url
        if self.project_key is not None:
            body["project_key"] = self.project_key
        if self.user_email is not None:
            body["user_email"] = self.user_email
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the JiraExportConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.api_token_uc_secret is not None:
            body["api_token_uc_secret"] = self.api_token_uc_secret
        if self.default_issue_type is not None:
            body["default_issue_type"] = self.default_issue_type
        if self.instance_url is not None:
            body["instance_url"] = self.instance_url
        if self.project_key is not None:
            body["project_key"] = self.project_key
        if self.user_email is not None:
            body["user_email"] = self.user_email
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> JiraExportConfig:
        """Deserializes the JiraExportConfig from a dictionary."""
        return cls(
            api_token_uc_secret=d.get("api_token_uc_secret", None),
            default_issue_type=d.get("default_issue_type", None),
            instance_url=d.get("instance_url", None),
            project_key=d.get("project_key", None),
            user_email=d.get("user_email", None),
        )


@dataclass
class JsonArrayEnvelope:
    """Unwraps a JSON array of events into one row per array element."""

    path: str
    """Name of the root-level key that holds the array of events, for example ``Records``. Nested paths
    are not supported."""

    def as_dict(self) -> dict:
        """Serializes the JsonArrayEnvelope into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.path is not None:
            body["path"] = self.path
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the JsonArrayEnvelope into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.path is not None:
            body["path"] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> JsonArrayEnvelope:
        """Deserializes the JsonArrayEnvelope from a dictionary."""
        return cls(path=d.get("path", None))


@dataclass
class ListDatasourcesResponse:
    datasources: Optional[List[Datasource]] = None

    next_page_token: Optional[str] = None
    """Opaque token for fetching the next page; pass it as ``page_token`` on the next call. It is empty
    only when there are no more results. Page size is best-effort, so a short or even empty page
    does not mean the end; keep paging until this token is empty, which is the only reliable
    end-of-results signal."""

    def as_dict(self) -> dict:
        """Serializes the ListDatasourcesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.datasources:
            body["datasources"] = [v.as_dict() for v in self.datasources]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListDatasourcesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.datasources:
            body["datasources"] = self.datasources
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListDatasourcesResponse:
        """Deserializes the ListDatasourcesResponse from a dictionary."""
        return cls(
            datasources=_repeated_dict(d, "datasources", Datasource), next_page_token=d.get("next_page_token", None)
        )


@dataclass
class ListRulesResponse:
    next_page_token: Optional[str] = None
    """Token to pass as ``page_token`` in a subsequent ``ListRules`` call to fetch the next page, or
    empty when there are no more results."""

    rules: Optional[List[Rule]] = None
    """The rules in this page of results."""

    def as_dict(self) -> dict:
        """Serializes the ListRulesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.rules:
            body["rules"] = [v.as_dict() for v in self.rules]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListRulesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.rules:
            body["rules"] = self.rules
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListRulesResponse:
        """Deserializes the ListRulesResponse from a dictionary."""
        return cls(next_page_token=d.get("next_page_token", None), rules=_repeated_dict(d, "rules", Rule))


@dataclass
class ParserRef:
    """Reference to a parser that the datasource uses. Each parser defines the schema of the parsed
    table that it writes."""

    id: str
    """Identifier of the parser. Stable across renames, unlike a parser name."""

    version: str
    """Version of the parser to use, given as an explicit version number."""

    effective_target_table: Optional[TableName] = None
    """The table this parser's data is written to: ``target_table`` when supplied, otherwise the table
    derived from the datasource's catalog and schema and the parser name. Fixed once resolved, so a
    later parser rename does not move it. Populated on get, create, and update responses with the
    resolved table."""

    target_table: Optional[TableName] = None
    """Table that this parser's data is written to. The table must be in the datasource's catalog and
    schema. If unset, the table name is derived from the parser name. Reads return the value as
    supplied; the table the data is written to is reported in ``effective_target_table``."""

    def as_dict(self) -> dict:
        """Serializes the ParserRef into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.effective_target_table:
            body["effective_target_table"] = self.effective_target_table.as_dict()
        if self.id is not None:
            body["id"] = self.id
        if self.target_table:
            body["target_table"] = self.target_table.as_dict()
        if self.version is not None:
            body["version"] = self.version
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ParserRef into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.effective_target_table:
            body["effective_target_table"] = self.effective_target_table
        if self.id is not None:
            body["id"] = self.id
        if self.target_table:
            body["target_table"] = self.target_table
        if self.version is not None:
            body["version"] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ParserRef:
        """Deserializes the ParserRef from a dictionary."""
        return cls(
            effective_target_table=_from_dict(d, "effective_target_table", TableName),
            id=d.get("id", None),
            target_table=_from_dict(d, "target_table", TableName),
            version=d.get("version", None),
        )


@dataclass
class Principal:
    """A principal — user or service-principal — used as the value type for ``created_by`` /
    ``updated_by`` / ``assignee`` etc. across v2 resources."""

    display_name: Optional[str] = None
    """Display name (user or SP name)."""

    email: Optional[str] = None
    """Email (regular users only)."""

    id: Optional[str] = None
    """User / service-principal ID."""

    principal_type: Optional[PrincipalType] = None
    """Whether this principal is a regular user, service principal, or system principal."""

    def as_dict(self) -> dict:
        """Serializes the Principal into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.email is not None:
            body["email"] = self.email
        if self.id is not None:
            body["id"] = self.id
        if self.principal_type is not None:
            body["principal_type"] = self.principal_type.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Principal into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.email is not None:
            body["email"] = self.email
        if self.id is not None:
            body["id"] = self.id
        if self.principal_type is not None:
            body["principal_type"] = self.principal_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Principal:
        """Deserializes the Principal from a dictionary."""
        return cls(
            display_name=d.get("display_name", None),
            email=d.get("email", None),
            id=d.get("id", None),
            principal_type=_enum(d, "principal_type", PrincipalType),
        )


class PrincipalType(Enum):
    """Type of a principal (user / SP / system)."""

    REGULAR_USER = "REGULAR_USER"
    SERVICE_PRINCIPAL = "SERVICE_PRINCIPAL"
    SYSTEM_USER = "SYSTEM_USER"


@dataclass
class ResourceStatus:
    """Read-only runtime status of one job or pipeline backing a resource.

    Shared across resources: a Rule's single job, a Datasource's main / health /
    historical-ingestion jobs, and a Datasource's ingestion pipeline (the ``pipeline_id`` field is
    set only for the pipeline). For a datasource's historical ingestion, the shard count is simply
    the number of ``historical_job_statuses`` entries — there is no separate count field.

    Two orthogonal axes are modeled separately (v1 conflated them into a single ``jobStatus`` enum):
    ``lifecycle`` (is it configured / does it still exist) and ``run_state`` (what the most recent
    or in-flight run did).

    Every field that holds a ``ResourceStatus`` is OUTPUT_ONLY at its use site (Datasource
    ingest/health/historical/pipeline statuses, Rule status), so the inner fields don't repeat the
    annotation."""

    create_time: Optional[Timestamp] = None

    job_id: Optional[str] = None
    """Databricks Jobs API job ID. Unset for a pure ingestion pipeline."""

    last_complete_time: Optional[Timestamp] = None
    """When the most recent run completed. Pairs with ``run_state = SUCCEEDED``."""

    last_error_message: Optional[str] = None
    """Most recent error message, if any. Pairs with ``run_state = FAILED``."""

    last_start_time: Optional[Timestamp] = None
    """When the most recent run started. Pairs with ``run_state = RUNNING``."""

    last_status_change_time: Optional[Timestamp] = None

    lifecycle_state: Optional[ResourceStatusLifecycle] = None
    """Scheduling lifecycle of the resource's underlying job/pipeline: whether it is unscheduled,
    scheduled, stopped, or deleted. Distinct from ``run_state``, which reports the outcome of the
    most recent run."""

    pipeline_id: Optional[str] = None
    """DLT ingestion-pipeline ID. Set only when this status represents the datasource's ingestion
    pipeline (unset for job statuses)."""

    run_state: Optional[ResourceStatusRunState] = None

    def as_dict(self) -> dict:
        """Serializes the ResourceStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.job_id is not None:
            body["job_id"] = self.job_id
        if self.last_complete_time is not None:
            body["last_complete_time"] = self.last_complete_time.ToJsonString()
        if self.last_error_message is not None:
            body["last_error_message"] = self.last_error_message
        if self.last_start_time is not None:
            body["last_start_time"] = self.last_start_time.ToJsonString()
        if self.last_status_change_time is not None:
            body["last_status_change_time"] = self.last_status_change_time.ToJsonString()
        if self.lifecycle_state is not None:
            body["lifecycle_state"] = self.lifecycle_state.value
        if self.pipeline_id is not None:
            body["pipeline_id"] = self.pipeline_id
        if self.run_state is not None:
            body["run_state"] = self.run_state.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ResourceStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.job_id is not None:
            body["job_id"] = self.job_id
        if self.last_complete_time is not None:
            body["last_complete_time"] = self.last_complete_time
        if self.last_error_message is not None:
            body["last_error_message"] = self.last_error_message
        if self.last_start_time is not None:
            body["last_start_time"] = self.last_start_time
        if self.last_status_change_time is not None:
            body["last_status_change_time"] = self.last_status_change_time
        if self.lifecycle_state is not None:
            body["lifecycle_state"] = self.lifecycle_state
        if self.pipeline_id is not None:
            body["pipeline_id"] = self.pipeline_id
        if self.run_state is not None:
            body["run_state"] = self.run_state
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ResourceStatus:
        """Deserializes the ResourceStatus from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            job_id=d.get("job_id", None),
            last_complete_time=_timestamp(d, "last_complete_time"),
            last_error_message=d.get("last_error_message", None),
            last_start_time=_timestamp(d, "last_start_time"),
            last_status_change_time=_timestamp(d, "last_status_change_time"),
            lifecycle_state=_enum(d, "lifecycle_state", ResourceStatusLifecycle),
            pipeline_id=d.get("pipeline_id", None),
            run_state=_enum(d, "run_state", ResourceStatusRunState),
        )


class ResourceStatusLifecycle(Enum):
    """Configured scheduling / existence of the job or pipeline."""

    DELETED = "DELETED"
    SCHEDULED = "SCHEDULED"
    STOPPED = "STOPPED"
    UNSCHEDULED = "UNSCHEDULED"


class ResourceStatusRunState(Enum):
    """Outcome / progress of the most recent (or in-flight) run."""

    CANCELED = "CANCELED"
    FAILED = "FAILED"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"


@dataclass
class Rule:
    """A Lakewatch detection rule: a query that evaluates ingested data and generates a signal for each
    match. Each rule is a securable in a Unity Catalog schema."""

    catalog_name: str
    """Name of the Unity Catalog catalog that contains the rule. Required. Cannot be changed after
    creation. Reads return the value as supplied; the catalog's current name is reported in
    ``effective_catalog_name``."""

    schema_name: str
    """Name of the Unity Catalog schema that contains the rule. Required. Cannot be changed after
    creation. Reads return the value as supplied; the schema's current name is reported in
    ``effective_schema_name``."""

    rule_name: str
    """Name of the rule within its Unity Catalog schema. Required on create; can be updated within the
    same catalog and schema. Get synchronizes this field with the current Unity Catalog name, also
    reported in ``effective_rule_name``."""

    severity: str
    """Free-form severity label, such as ``Informational``, ``Medium``, ``High``, or ``Critical``."""

    fidelity: RuleFidelity
    """Signal quality for this rule."""

    schedule: RuleSchedule
    """When the rule executes."""

    output: RuleOutput
    """What to record in each signal."""

    annotations: Optional[Dict[str, str]] = None
    """Free-form client-managed key/value annotations."""

    batch: Optional[RuleInputBatch] = None
    """Batch SQL rule input."""

    category: Optional[str] = None
    """Free-form rule category."""

    compute_workspace_id: Optional[str] = None
    """ID of the workspace whose compute runs this rule's jobs and owns its associated resources, such
    as the SQL warehouse a scheduled rule runs on. Server-assigned; a rule's warehouse can only be
    changed from this workspace."""

    content_resource_id: Optional[str] = None
    """Immutable UUIDv4 identifying the authored content resource installed as this rule."""

    create_time: Optional[Timestamp] = None
    """Time the rule was created."""

    created_by: Optional[Principal] = None
    """Principal that created the rule."""

    deduplication: Optional[RuleDeduplication] = None
    """Signal deduplication mode."""

    deduplication_time_window: Optional[str] = None
    """Time window for deduplication, such as ``1h``, ``24h``, ``7d``, or ``automatic``."""

    description: Optional[str] = None
    """Free-form description."""

    effective_catalog_name: Optional[str] = None
    """Current name of the Unity Catalog catalog that contains the rule. Reflects catalog renames,
    which do not change ``catalog_name``. Unset until resolved."""

    effective_rule_name: Optional[str] = None
    """Current UC leaf name of the rule (server-owned). Tracks UC renames so callers can observe the
    live name without having to update the client-owned ``rule_name``; unset until resolved."""

    effective_run_as_principal: Optional[str] = None
    """The identity this rule's job runs as: the resolved ``run_as_principal``, or the requester's
    identity when it was omitted on create or cleared on update. The value is a user email or
    service-principal application ID, falling back to the numeric principal ID if that identity can
    no longer be resolved. Populated on single-rule reads (get/create/update); list responses omit
    it."""

    effective_schema_name: Optional[str] = None
    """Current name of the Unity Catalog schema that contains the rule. Reflects schema renames, which
    do not change ``schema_name``. Unset until resolved."""

    etag: Optional[str] = None
    """Opaque entity tag for optimistic concurrency. Content-version ETags change on user edits and
    remain stable across runtime status updates."""

    mitre: Optional[List[RuleMitreMapping]] = None
    """Up to 64 MITRE ATT&CK mappings, producing at most 192 flattened alert tags."""

    name: Optional[str] = None
    """Resource name, in the form ``rules/{rule_id}``. Assigned by the server on create; required on
    update."""

    objective: Optional[str] = None
    """Long-form description of what this rule detects."""

    original_content_pack: Optional[ContentPackReference] = None
    """Reference to the content pack this rule was originally installed from."""

    owner: Optional[Principal] = None
    """Unity Catalog owner of the rule. Assigned by the server. Populated by ``GetRule``."""

    references: Optional[List[str]] = None
    """Ordered reference URLs carried from the authored rule metadata. A maximum of three references of
    up to 512 characters each is supported. Requests exceeding these limits are rejected."""

    rule_id: Optional[str] = None
    """Unity Catalog securable UUID of the rule, and the last segment of ``name``. Never changes,
    including when the rule's catalog or schema is renamed."""

    run_as_principal: Optional[str] = None
    """The principal whose identity this rule's job runs as, given as a user email or service-principal
    application ID. When supplied on create/update, Lakewatch resolves the principal, records it on
    the rule, and creates the delegation to run as that principal — the requester must be
    authorized to delegate to it, or the request is rejected. When omitted on create, the
    requester's own identity is used. An update whose mask does not include ``run_as_principal``
    keeps the current identity, and the requester must still be authorized to delegate to it; an
    editor who is not must supply a run_as_principal they can delegate to (for example, their own
    identity), or clear it, either of which reassigns the rule. An update whose mask includes
    ``run_as_principal`` but supplies no value clears it: the rule then runs as the requester,
    exactly as when it is omitted on create. Reads return the value as supplied; the identity the
    rule runs as is reported in ``effective_run_as_principal``."""

    runbook: Optional[str] = None
    """Long-form operational guidance carried from the authored rule metadata. Supports up to 4096
    characters. Requests exceeding this limit are rejected."""

    status: Optional[ResourceStatus] = None
    """Read-only lifecycle status."""

    suppress_until_time: Optional[Timestamp] = None
    """If set, this rule's signals do not open new alerts until the given time."""

    timerange: Optional[RuleTimeRange] = None
    """Time-range configuration for batch rules. If unset, the execution time range is extended by a
    fixed ``15m`` lookback."""

    update_time: Optional[Timestamp] = None
    """Time the rule was last updated."""

    updated_by: Optional[Principal] = None
    """Principal that last updated the rule."""

    version: Optional[int] = None
    """Monotonic version, bumped on each update. Informational; use ``etag`` for optimistic
    concurrency."""

    def as_dict(self) -> dict:
        """Serializes the Rule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.annotations:
            body["annotations"] = self.annotations
        if self.batch:
            body["batch"] = self.batch.as_dict()
        if self.catalog_name is not None:
            body["catalog_name"] = self.catalog_name
        if self.category is not None:
            body["category"] = self.category
        if self.compute_workspace_id is not None:
            body["compute_workspace_id"] = self.compute_workspace_id
        if self.content_resource_id is not None:
            body["content_resource_id"] = self.content_resource_id
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.created_by:
            body["created_by"] = self.created_by.as_dict()
        if self.deduplication is not None:
            body["deduplication"] = self.deduplication.value
        if self.deduplication_time_window is not None:
            body["deduplication_time_window"] = self.deduplication_time_window
        if self.description is not None:
            body["description"] = self.description
        if self.effective_catalog_name is not None:
            body["effective_catalog_name"] = self.effective_catalog_name
        if self.effective_rule_name is not None:
            body["effective_rule_name"] = self.effective_rule_name
        if self.effective_run_as_principal is not None:
            body["effective_run_as_principal"] = self.effective_run_as_principal
        if self.effective_schema_name is not None:
            body["effective_schema_name"] = self.effective_schema_name
        if self.etag is not None:
            body["etag"] = self.etag
        if self.fidelity is not None:
            body["fidelity"] = self.fidelity.value
        if self.mitre:
            body["mitre"] = [v.as_dict() for v in self.mitre]
        if self.name is not None:
            body["name"] = self.name
        if self.objective is not None:
            body["objective"] = self.objective
        if self.original_content_pack:
            body["original_content_pack"] = self.original_content_pack.as_dict()
        if self.output:
            body["output"] = self.output.as_dict()
        if self.owner:
            body["owner"] = self.owner.as_dict()
        if self.references:
            body["references"] = [v for v in self.references]
        if self.rule_id is not None:
            body["rule_id"] = self.rule_id
        if self.rule_name is not None:
            body["rule_name"] = self.rule_name
        if self.run_as_principal is not None:
            body["run_as_principal"] = self.run_as_principal
        if self.runbook is not None:
            body["runbook"] = self.runbook
        if self.schedule:
            body["schedule"] = self.schedule.as_dict()
        if self.schema_name is not None:
            body["schema_name"] = self.schema_name
        if self.severity is not None:
            body["severity"] = self.severity
        if self.status:
            body["status"] = self.status.as_dict()
        if self.suppress_until_time is not None:
            body["suppress_until_time"] = self.suppress_until_time.ToJsonString()
        if self.timerange:
            body["timerange"] = self.timerange.as_dict()
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        if self.updated_by:
            body["updated_by"] = self.updated_by.as_dict()
        if self.version is not None:
            body["version"] = self.version
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Rule into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.annotations:
            body["annotations"] = self.annotations
        if self.batch:
            body["batch"] = self.batch
        if self.catalog_name is not None:
            body["catalog_name"] = self.catalog_name
        if self.category is not None:
            body["category"] = self.category
        if self.compute_workspace_id is not None:
            body["compute_workspace_id"] = self.compute_workspace_id
        if self.content_resource_id is not None:
            body["content_resource_id"] = self.content_resource_id
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.created_by:
            body["created_by"] = self.created_by
        if self.deduplication is not None:
            body["deduplication"] = self.deduplication
        if self.deduplication_time_window is not None:
            body["deduplication_time_window"] = self.deduplication_time_window
        if self.description is not None:
            body["description"] = self.description
        if self.effective_catalog_name is not None:
            body["effective_catalog_name"] = self.effective_catalog_name
        if self.effective_rule_name is not None:
            body["effective_rule_name"] = self.effective_rule_name
        if self.effective_run_as_principal is not None:
            body["effective_run_as_principal"] = self.effective_run_as_principal
        if self.effective_schema_name is not None:
            body["effective_schema_name"] = self.effective_schema_name
        if self.etag is not None:
            body["etag"] = self.etag
        if self.fidelity is not None:
            body["fidelity"] = self.fidelity
        if self.mitre:
            body["mitre"] = self.mitre
        if self.name is not None:
            body["name"] = self.name
        if self.objective is not None:
            body["objective"] = self.objective
        if self.original_content_pack:
            body["original_content_pack"] = self.original_content_pack
        if self.output:
            body["output"] = self.output
        if self.owner:
            body["owner"] = self.owner
        if self.references:
            body["references"] = self.references
        if self.rule_id is not None:
            body["rule_id"] = self.rule_id
        if self.rule_name is not None:
            body["rule_name"] = self.rule_name
        if self.run_as_principal is not None:
            body["run_as_principal"] = self.run_as_principal
        if self.runbook is not None:
            body["runbook"] = self.runbook
        if self.schedule:
            body["schedule"] = self.schedule
        if self.schema_name is not None:
            body["schema_name"] = self.schema_name
        if self.severity is not None:
            body["severity"] = self.severity
        if self.status:
            body["status"] = self.status
        if self.suppress_until_time is not None:
            body["suppress_until_time"] = self.suppress_until_time
        if self.timerange:
            body["timerange"] = self.timerange
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.updated_by:
            body["updated_by"] = self.updated_by
        if self.version is not None:
            body["version"] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Rule:
        """Deserializes the Rule from a dictionary."""
        return cls(
            annotations=d.get("annotations", None),
            batch=_from_dict(d, "batch", RuleInputBatch),
            catalog_name=d.get("catalog_name", None),
            category=d.get("category", None),
            compute_workspace_id=d.get("compute_workspace_id", None),
            content_resource_id=d.get("content_resource_id", None),
            create_time=_timestamp(d, "create_time"),
            created_by=_from_dict(d, "created_by", Principal),
            deduplication=_enum(d, "deduplication", RuleDeduplication),
            deduplication_time_window=d.get("deduplication_time_window", None),
            description=d.get("description", None),
            effective_catalog_name=d.get("effective_catalog_name", None),
            effective_rule_name=d.get("effective_rule_name", None),
            effective_run_as_principal=d.get("effective_run_as_principal", None),
            effective_schema_name=d.get("effective_schema_name", None),
            etag=d.get("etag", None),
            fidelity=_enum(d, "fidelity", RuleFidelity),
            mitre=_repeated_dict(d, "mitre", RuleMitreMapping),
            name=d.get("name", None),
            objective=d.get("objective", None),
            original_content_pack=_from_dict(d, "original_content_pack", ContentPackReference),
            output=_from_dict(d, "output", RuleOutput),
            owner=_from_dict(d, "owner", Principal),
            references=d.get("references", None),
            rule_id=d.get("rule_id", None),
            rule_name=d.get("rule_name", None),
            run_as_principal=d.get("run_as_principal", None),
            runbook=d.get("runbook", None),
            schedule=_from_dict(d, "schedule", RuleSchedule),
            schema_name=d.get("schema_name", None),
            severity=d.get("severity", None),
            status=_from_dict(d, "status", ResourceStatus),
            suppress_until_time=_timestamp(d, "suppress_until_time"),
            timerange=_from_dict(d, "timerange", RuleTimeRange),
            update_time=_timestamp(d, "update_time"),
            updated_by=_from_dict(d, "updated_by", Principal),
            version=_int64(d, "version"),
        )


@dataclass
class RuleConfig:
    """Per-catalog rule-related config. Singleton. Name format: ``catalogs/{catalog}/ruleConfig``."""

    default_folder: Optional[str] = None
    """Schema name of the registered folder (in this catalog) that a new rule is placed in when the
    request does not specify a schema. Must name a schema registered as a folder. Omit to clear.
    Reads return the value as supplied; the folder's current schema name is reported in
    ``effective_default_folder``."""

    default_schedule: Optional[RuleSchedule] = None
    """Default schedule for rules that don't specify one."""

    default_signal_collation_window: Optional[str] = None
    """Default duration string for signal deduplication when a rule doesn't override it — compact
    day/hour/minute/second components, e.g. ``5d``, ``1h``. Reads return the value as supplied;
    there is no server default, so it is unset until set. An empty value clears it."""

    detection_categories: Optional[List[str]] = None
    """Available detection categories a rule can be tagged with. Reads return the value as supplied.
    When empty, rules can be tagged with the default categories: ``Static Signature``, ``Fuzzy
    Signature``, ``Behavioral``, ``Statistical``, and ``Learning (AI/ML)``. The categories in effect
    are reported in ``effective_detection_categories``."""

    effective_default_folder: Optional[str] = None
    """The current schema name of the ``default_folder`` folder. Tracks UC schema renames. Unset when
    no default is configured, or when the folder's schema no longer exists or is not visible to the
    caller."""

    effective_detection_categories: Optional[List[str]] = None
    """The detection categories in effect: ``detection_categories`` when set, otherwise the default
    categories."""

    etag: Optional[str] = None
    """Opaque entity tag for optimistic concurrency. Returned on every read; pass it back as the Update
    request's ``etag`` to make the update conditional on the resource being unchanged."""

    name: Optional[str] = None

    update_time: Optional[Timestamp] = None

    updated_by: Optional[Principal] = None

    version: Optional[int] = None
    """Monotonic version, bumped on each update. Informational; use ``etag`` for optimistic
    concurrency."""

    def as_dict(self) -> dict:
        """Serializes the RuleConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.default_folder is not None:
            body["default_folder"] = self.default_folder
        if self.default_schedule:
            body["default_schedule"] = self.default_schedule.as_dict()
        if self.default_signal_collation_window is not None:
            body["default_signal_collation_window"] = self.default_signal_collation_window
        if self.detection_categories:
            body["detection_categories"] = [v for v in self.detection_categories]
        if self.effective_default_folder is not None:
            body["effective_default_folder"] = self.effective_default_folder
        if self.effective_detection_categories:
            body["effective_detection_categories"] = [v for v in self.effective_detection_categories]
        if self.etag is not None:
            body["etag"] = self.etag
        if self.name is not None:
            body["name"] = self.name
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        if self.updated_by:
            body["updated_by"] = self.updated_by.as_dict()
        if self.version is not None:
            body["version"] = self.version
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RuleConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.default_folder is not None:
            body["default_folder"] = self.default_folder
        if self.default_schedule:
            body["default_schedule"] = self.default_schedule
        if self.default_signal_collation_window is not None:
            body["default_signal_collation_window"] = self.default_signal_collation_window
        if self.detection_categories:
            body["detection_categories"] = self.detection_categories
        if self.effective_default_folder is not None:
            body["effective_default_folder"] = self.effective_default_folder
        if self.effective_detection_categories:
            body["effective_detection_categories"] = self.effective_detection_categories
        if self.etag is not None:
            body["etag"] = self.etag
        if self.name is not None:
            body["name"] = self.name
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.updated_by:
            body["updated_by"] = self.updated_by
        if self.version is not None:
            body["version"] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RuleConfig:
        """Deserializes the RuleConfig from a dictionary."""
        return cls(
            default_folder=d.get("default_folder", None),
            default_schedule=_from_dict(d, "default_schedule", RuleSchedule),
            default_signal_collation_window=d.get("default_signal_collation_window", None),
            detection_categories=d.get("detection_categories", None),
            effective_default_folder=d.get("effective_default_folder", None),
            effective_detection_categories=d.get("effective_detection_categories", None),
            etag=d.get("etag", None),
            name=d.get("name", None),
            update_time=_timestamp(d, "update_time"),
            updated_by=_from_dict(d, "updated_by", Principal),
            version=_int64(d, "version"),
        )


class RuleDeduplication(Enum):
    """Signal deduplication mode for a detection rule."""

    DEDUPLICATION_DEFAULT = "DEDUPLICATION_DEFAULT"
    DEDUPLICATION_DISABLED = "DEDUPLICATION_DISABLED"
    DEDUPLICATION_ENABLED = "DEDUPLICATION_ENABLED"


class RuleFidelity(Enum):
    """Maturity of a detection rule."""

    FIDELITY_DEVELOPMENT = "FIDELITY_DEVELOPMENT"
    FIDELITY_HIGH = "FIDELITY_HIGH"
    FIDELITY_INVESTIGATIVE = "FIDELITY_INVESTIGATIVE"
    FIDELITY_MEDIUM = "FIDELITY_MEDIUM"


@dataclass
class RuleInputBatch:
    """Batch input for a detection rule."""

    custom: Optional[RuleInputCustomNotebook] = None
    """Custom-notebook user function. The output is used as input data for the rule."""

    sql: Optional[RuleInputBatchSql] = None
    """SQL query evaluated as the rule input."""

    warehouse_id: Optional[str] = None
    """SQL warehouse used to run this batch rule."""

    def as_dict(self) -> dict:
        """Serializes the RuleInputBatch into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.custom:
            body["custom"] = self.custom.as_dict()
        if self.sql:
            body["sql"] = self.sql.as_dict()
        if self.warehouse_id is not None:
            body["warehouse_id"] = self.warehouse_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RuleInputBatch into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.custom:
            body["custom"] = self.custom
        if self.sql:
            body["sql"] = self.sql
        if self.warehouse_id is not None:
            body["warehouse_id"] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RuleInputBatch:
        """Deserializes the RuleInputBatch from a dictionary."""
        return cls(
            custom=_from_dict(d, "custom", RuleInputCustomNotebook),
            sql=_from_dict(d, "sql", RuleInputBatchSql),
            warehouse_id=d.get("warehouse_id", None),
        )


@dataclass
class RuleInputBatchSql:
    """Batch SQL input for a detection rule."""

    query: str
    """SQL query evaluated as the rule input."""

    default_catalog_name: Optional[str] = None
    """Default catalog used to resolve unqualified identifiers in ``query``. If unset, the rule's
    ``catalog_name`` is used."""

    default_schema_name: Optional[str] = None
    """Default schema used to resolve unqualified identifiers in ``query``. If unset, the rule's
    ``schema_name`` is used."""

    def as_dict(self) -> dict:
        """Serializes the RuleInputBatchSql into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.default_catalog_name is not None:
            body["default_catalog_name"] = self.default_catalog_name
        if self.default_schema_name is not None:
            body["default_schema_name"] = self.default_schema_name
        if self.query is not None:
            body["query"] = self.query
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RuleInputBatchSql into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.default_catalog_name is not None:
            body["default_catalog_name"] = self.default_catalog_name
        if self.default_schema_name is not None:
            body["default_schema_name"] = self.default_schema_name
        if self.query is not None:
            body["query"] = self.query
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RuleInputBatchSql:
        """Deserializes the RuleInputBatchSql from a dictionary."""
        return cls(
            default_catalog_name=d.get("default_catalog_name", None),
            default_schema_name=d.get("default_schema_name", None),
            query=d.get("query", None),
        )


@dataclass
class RuleInputCustomNotebook:
    """Reference to a custom-user-function notebook for stream or batch input."""

    notebook: str
    """Fully-qualified notebook path, or a path relative to the configured base notebook directory."""

    options: Optional[Dict[str, str]] = None
    """Optional arguments supplied when invoking the custom function."""

    def as_dict(self) -> dict:
        """Serializes the RuleInputCustomNotebook into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.notebook is not None:
            body["notebook"] = self.notebook
        if self.options:
            body["options"] = self.options
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RuleInputCustomNotebook into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.notebook is not None:
            body["notebook"] = self.notebook
        if self.options:
            body["options"] = self.options
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RuleInputCustomNotebook:
        """Deserializes the RuleInputCustomNotebook from a dictionary."""
        return cls(notebook=d.get("notebook", None), options=d.get("options", None))


@dataclass
class RuleMitreMapping:
    """MITRE ATT&CK mapping for a detection rule."""

    sub_technique: Optional[str] = None
    """Human-readable MITRE sub-technique name."""

    sub_technique_id: Optional[str] = None
    """MITRE sub-technique ID, such as ``T1078.001``."""

    tactic: Optional[str] = None
    """Adversary objective during this attack, such as ``Command and Control``."""

    taxonomy: Optional[str] = None
    """Structured framework that organizes adversary behaviors, such as ``mitre-attack``."""

    technique: Optional[str] = None
    """Human-readable MITRE technique name."""

    technique_id: Optional[str] = None
    """MITRE technique ID, such as ``T1078``."""

    def as_dict(self) -> dict:
        """Serializes the RuleMitreMapping into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.sub_technique is not None:
            body["sub_technique"] = self.sub_technique
        if self.sub_technique_id is not None:
            body["sub_technique_id"] = self.sub_technique_id
        if self.tactic is not None:
            body["tactic"] = self.tactic
        if self.taxonomy is not None:
            body["taxonomy"] = self.taxonomy
        if self.technique is not None:
            body["technique"] = self.technique
        if self.technique_id is not None:
            body["technique_id"] = self.technique_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RuleMitreMapping into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.sub_technique is not None:
            body["sub_technique"] = self.sub_technique
        if self.sub_technique_id is not None:
            body["sub_technique_id"] = self.sub_technique_id
        if self.tactic is not None:
            body["tactic"] = self.tactic
        if self.taxonomy is not None:
            body["taxonomy"] = self.taxonomy
        if self.technique is not None:
            body["technique"] = self.technique
        if self.technique_id is not None:
            body["technique_id"] = self.technique_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RuleMitreMapping:
        """Deserializes the RuleMitreMapping from a dictionary."""
        return cls(
            sub_technique=d.get("sub_technique", None),
            sub_technique_id=d.get("sub_technique_id", None),
            tactic=d.get("tactic", None),
            taxonomy=d.get("taxonomy", None),
            technique=d.get("technique", None),
            technique_id=d.get("technique_id", None),
        )


@dataclass
class RuleOutput:
    """What to record in each signal that this rule generates."""

    context: Optional[Dict[str, str]] = None
    """Key/value context to record from the input row. Values may contain SQL expressions in braces."""

    default_context: Optional[bool] = None
    """If true, also record every column of the triggering input row. Custom context wins on key
    collision."""

    event_time_column: Optional[str] = None
    """Column in the rule output that holds the event timestamp."""

    summary: Optional[str] = None
    """Signal summary. May contain SQL expressions in braces that the server substitutes from the input
    row."""

    def as_dict(self) -> dict:
        """Serializes the RuleOutput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.context:
            body["context"] = self.context
        if self.default_context is not None:
            body["default_context"] = self.default_context
        if self.event_time_column is not None:
            body["event_time_column"] = self.event_time_column
        if self.summary is not None:
            body["summary"] = self.summary
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RuleOutput into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.context:
            body["context"] = self.context
        if self.default_context is not None:
            body["default_context"] = self.default_context
        if self.event_time_column is not None:
            body["event_time_column"] = self.event_time_column
        if self.summary is not None:
            body["summary"] = self.summary
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RuleOutput:
        """Deserializes the RuleOutput from a dictionary."""
        return cls(
            context=d.get("context", None),
            default_context=d.get("default_context", None),
            event_time_column=d.get("event_time_column", None),
            summary=d.get("summary", None),
        )


@dataclass
class RuleSchedule:
    """Defines when a detection rule executes.

    A batch rule sets exactly one of ``at_least_every`` or ``cron_expression``. A streaming rule
    runs continuously and sets no timing; it accepts only ``enabled``, and an omitted schedule means
    enabled. The server rejects any other combination. ``enabled`` is orthogonal to the timing."""

    at_least_every: Optional[str] = None
    """Defines the minimum cadence as a duration string. It may contain components for days, hours,
    minutes, and seconds (e.g. ``5d``, ``5d3h``, ``3d2h5m12s``, ``12m16s``)."""

    continuous: Optional[bool] = None
    """Runs the rule continuously. Detection rules do not accept it: batch rules reject it, and
    streaming rules run continuously without it."""

    cron_expression: Optional[str] = None
    """Defines the schedule using a Quartz cron expression."""

    enabled: Optional[bool] = None
    """Sets whether the job is scheduled to run. Defaults to true."""

    def as_dict(self) -> dict:
        """Serializes the RuleSchedule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.at_least_every is not None:
            body["at_least_every"] = self.at_least_every
        if self.continuous is not None:
            body["continuous"] = self.continuous
        if self.cron_expression is not None:
            body["cron_expression"] = self.cron_expression
        if self.enabled is not None:
            body["enabled"] = self.enabled
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RuleSchedule into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.at_least_every is not None:
            body["at_least_every"] = self.at_least_every
        if self.continuous is not None:
            body["continuous"] = self.continuous
        if self.cron_expression is not None:
            body["cron_expression"] = self.cron_expression
        if self.enabled is not None:
            body["enabled"] = self.enabled
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RuleSchedule:
        """Deserializes the RuleSchedule from a dictionary."""
        return cls(
            at_least_every=d.get("at_least_every", None),
            continuous=d.get("continuous", None),
            cron_expression=d.get("cron_expression", None),
            enabled=d.get("enabled", None),
        )


@dataclass
class RuleTimeRange:
    """Time-range configuration for a batch detection rule."""

    extend_lookback: Optional[str] = None
    """Extends the start of the execution time range by a compact duration with integer days, hours,
    minutes, and seconds in that order, such as ``1h30m`` or ``15m``. Zero duration disables
    extension. Unset or empty uses a fixed ``15m`` at execution time. Only the start moves; the end
    is unchanged. Has no effect on batch SQL that does not use ``IN_TIMERANGE``. Values must fit
    signed 64-bit microseconds."""

    def as_dict(self) -> dict:
        """Serializes the RuleTimeRange into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.extend_lookback is not None:
            body["extend_lookback"] = self.extend_lookback
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RuleTimeRange into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.extend_lookback is not None:
            body["extend_lookback"] = self.extend_lookback
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RuleTimeRange:
        """Deserializes the RuleTimeRange from a dictionary."""
        return cls(extend_lookback=d.get("extend_lookback", None))


class RuleView(Enum):
    """Selects how much of each rule a list response returns."""

    RULE_VIEW_BASIC = "RULE_VIEW_BASIC"
    RULE_VIEW_FULL = "RULE_VIEW_FULL"


@dataclass
class Schedule:
    """Defines when a recurring job executes.

    Exactly one of the timing modes (``at_least_every``, ``cron_expression``, ``continuous``) must
    be set; combining them or setting none is rejected by the server. ``compute_group`` and
    ``enabled`` are orthogonal to the timing."""

    at_least_every: Optional[str] = None
    """Duration string defining the minimum cadence. May contain components for days, hours, minutes,
    seconds (e.g. ``5d``, ``5d3h``, ``3d2h5m12s``, ``12m16s``)."""

    compute_group: Optional[str] = None
    """``dedicated``, ``inherited``, ``automatic``, or a custom group name. Reads return the value as
    supplied. A rule whose schedule omits it runs on ``dedicated``."""

    continuous: Optional[bool] = None
    """Run continuously (sentinel — must be ``true`` when set in this branch)."""

    cron_expression: Optional[str] = None
    """Quartz cron expression."""

    enabled: Optional[bool] = None
    """Whether the job is scheduled to run. Defaults to true."""

    def as_dict(self) -> dict:
        """Serializes the Schedule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.at_least_every is not None:
            body["at_least_every"] = self.at_least_every
        if self.compute_group is not None:
            body["compute_group"] = self.compute_group
        if self.continuous is not None:
            body["continuous"] = self.continuous
        if self.cron_expression is not None:
            body["cron_expression"] = self.cron_expression
        if self.enabled is not None:
            body["enabled"] = self.enabled
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Schedule into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.at_least_every is not None:
            body["at_least_every"] = self.at_least_every
        if self.compute_group is not None:
            body["compute_group"] = self.compute_group
        if self.continuous is not None:
            body["continuous"] = self.continuous
        if self.cron_expression is not None:
            body["cron_expression"] = self.cron_expression
        if self.enabled is not None:
            body["enabled"] = self.enabled
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Schedule:
        """Deserializes the Schedule from a dictionary."""
        return cls(
            at_least_every=d.get("at_least_every", None),
            compute_group=d.get("compute_group", None),
            continuous=d.get("continuous", None),
            cron_expression=d.get("cron_expression", None),
            enabled=d.get("enabled", None),
        )


@dataclass
class ServiceNowExportConfig:
    """ServiceNow destination. Alerts are delivered to the instance's Table API, authorized by an OAuth
    2.0 client-credentials token minted from the registered application's client ID and secret."""

    instance_id: str
    """ServiceNow instance ID — the host label only, not the full URL. For an instance reachable at
    ``https://acme.service-now.com``, this is ``acme``."""

    client_id: str
    """OAuth client ID of the registered ServiceNow application. An identifier rather than secret
    material — ServiceNow shows it on the application record — so it is stored and read back
    verbatim."""

    client_secret_uc_secret: str
    """Three-level Unity Catalog name (``catalog.schema.secret``) of the secret holding the OAuth
    client secret. Only the name is stored; the secret is read when an alert is exported, so
    rotating it takes effect without editing this config."""

    def as_dict(self) -> dict:
        """Serializes the ServiceNowExportConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.client_id is not None:
            body["client_id"] = self.client_id
        if self.client_secret_uc_secret is not None:
            body["client_secret_uc_secret"] = self.client_secret_uc_secret
        if self.instance_id is not None:
            body["instance_id"] = self.instance_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServiceNowExportConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.client_id is not None:
            body["client_id"] = self.client_id
        if self.client_secret_uc_secret is not None:
            body["client_secret_uc_secret"] = self.client_secret_uc_secret
        if self.instance_id is not None:
            body["instance_id"] = self.instance_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ServiceNowExportConfig:
        """Deserializes the ServiceNowExportConfig from a dictionary."""
        return cls(
            client_id=d.get("client_id", None),
            client_secret_uc_secret=d.get("client_secret_uc_secret", None),
            instance_id=d.get("instance_id", None),
        )


@dataclass
class SlackExportConfig:
    channel: str
    """Channel the alert is posted to: a channel ID (e.g. ``C0123456789``) or a channel name without
    the leading ``#`` (e.g. ``soc-alerts``). The value is stored as sent, so a leading ``#``,
    surrounding whitespace, or a value naming more than one channel is rejected. For private
    channels, prefer the channel ID — Slack does not guarantee name resolution for those.
    
    The Slack app must be a member of the channel and hold the ``chat:write`` scope."""

    bot_token_uc_secret: str
    """Three-level Unity Catalog name (``catalog.schema.secret``) of the secret holding the Slack bot
    token. Only the name is stored; the token is read when an alert is exported, so rotating the
    secret takes effect without editing this config."""

    def as_dict(self) -> dict:
        """Serializes the SlackExportConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.bot_token_uc_secret is not None:
            body["bot_token_uc_secret"] = self.bot_token_uc_secret
        if self.channel is not None:
            body["channel"] = self.channel
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SlackExportConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.bot_token_uc_secret is not None:
            body["bot_token_uc_secret"] = self.bot_token_uc_secret
        if self.channel is not None:
            body["channel"] = self.channel
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SlackExportConfig:
        """Deserializes the SlackExportConfig from a dictionary."""
        return cls(bot_token_uc_secret=d.get("bot_token_uc_secret", None), channel=d.get("channel", None))


@dataclass
class TableName:
    """A fully-qualified Unity Catalog table reference by catalog / schema / table name."""

    table_name: str
    """Unity Catalog table name."""

    catalog_name: Optional[str] = None
    """Name of the parent Unity Catalog catalog."""

    schema_name: Optional[str] = None
    """Name of the parent Unity Catalog schema."""

    def as_dict(self) -> dict:
        """Serializes the TableName into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.catalog_name is not None:
            body["catalog_name"] = self.catalog_name
        if self.schema_name is not None:
            body["schema_name"] = self.schema_name
        if self.table_name is not None:
            body["table_name"] = self.table_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the TableName into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.catalog_name is not None:
            body["catalog_name"] = self.catalog_name
        if self.schema_name is not None:
            body["schema_name"] = self.schema_name
        if self.table_name is not None:
            body["table_name"] = self.table_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> TableName:
        """Deserializes the TableName from a dictionary."""
        return cls(
            catalog_name=d.get("catalog_name", None),
            schema_name=d.get("schema_name", None),
            table_name=d.get("table_name", None),
        )


@dataclass
class TinesExportConfig:
    """Tines destination. Alerts are delivered to a Tines webhook action, authorized by a secret sent
    in the ``Authorization`` header."""

    webhook_uri: str
    """Tines webhook action URL, typically of the form ``https://<tenant>.tines.com/webhook/<path>``.
    Any HTTPS host is accepted, so that a Tines tenant on a custom domain works.
    
    The secret is sent as a header, so it must not be embedded in the URL: a trailing secret path
    segment (``/webhook/<path>/<secret>``) and a ``secret`` query parameter are both rejected.
    API-path-prefix URLs (``/api/public/...``) are not supported."""

    webhook_secret_uc_secret: str
    """Three-level Unity Catalog name (``catalog.schema.secret``) of the secret holding the Tines
    webhook secret. Only the name is stored; the secret is read when an alert is exported, so
    rotating it takes effect without editing this config. Required: without it the destination would
    be an unauthenticated endpoint."""

    export_updates: Optional[bool] = None
    """Whether a later change to an already-exported alert is delivered too, as a second
    ``lakewatch.alert.updated`` event to the same webhook action (a close is such an update,
    carrying a terminal ``alert_state``). Creation export is unaffected either way.
    
    Opt-in, and unset means off: Tines is an event transport rather than a system whose record is
    edited in place, so an update is an extra event the receiving story has to correlate to the
    alert it already handled. A destination configured before this event existed must not start
    receiving more without its owner asking."""

    def as_dict(self) -> dict:
        """Serializes the TinesExportConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.export_updates is not None:
            body["export_updates"] = self.export_updates
        if self.webhook_secret_uc_secret is not None:
            body["webhook_secret_uc_secret"] = self.webhook_secret_uc_secret
        if self.webhook_uri is not None:
            body["webhook_uri"] = self.webhook_uri
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the TinesExportConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.export_updates is not None:
            body["export_updates"] = self.export_updates
        if self.webhook_secret_uc_secret is not None:
            body["webhook_secret_uc_secret"] = self.webhook_secret_uc_secret
        if self.webhook_uri is not None:
            body["webhook_uri"] = self.webhook_uri
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> TinesExportConfig:
        """Deserializes the TinesExportConfig from a dictionary."""
        return cls(
            export_updates=d.get("export_updates", None),
            webhook_secret_uc_secret=d.get("webhook_secret_uc_secret", None),
            webhook_uri=d.get("webhook_uri", None),
        )


@dataclass
class UnityCatalogConnection:
    """Ingests data through a managed connector that uses a Unity Catalog connection. Mutually
    exclusive with ``autoloader`` and ``existing_table``."""

    connection_name: str
    """Name of the Unity Catalog connection to ingest through."""

    configuration: Optional[Dict[str, str]] = None
    """Free-form key-value configuration for the managed ingestion pipeline."""

    connector: Optional[str] = None
    """Connector type of the connection, such as ``SLACK_AUDIT_LOGS``. Resolved by the server from
    ``connection_name`` through Unity Catalog; not accepted as input."""

    effective_start_time: Optional[Timestamp] = None
    """The start time ingestion uses: the supplied ``start_time``, or the creation time when it was
    omitted. Always populated."""

    start_time: Optional[Timestamp] = None
    """Earliest source event time to ingest. Leave unset to start at creation time, with no history
    backfilled. Rejected if in the future, beyond the connector's history window, or for a connector
    without start-time support. Takes effect only at first start and cannot be changed. Reads return
    the value as supplied; the start time ingestion uses is reported in ``effective_start_time``."""

    def as_dict(self) -> dict:
        """Serializes the UnityCatalogConnection into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.configuration:
            body["configuration"] = self.configuration
        if self.connection_name is not None:
            body["connection_name"] = self.connection_name
        if self.connector is not None:
            body["connector"] = self.connector
        if self.effective_start_time is not None:
            body["effective_start_time"] = self.effective_start_time.ToJsonString()
        if self.start_time is not None:
            body["start_time"] = self.start_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the UnityCatalogConnection into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.configuration:
            body["configuration"] = self.configuration
        if self.connection_name is not None:
            body["connection_name"] = self.connection_name
        if self.connector is not None:
            body["connector"] = self.connector
        if self.effective_start_time is not None:
            body["effective_start_time"] = self.effective_start_time
        if self.start_time is not None:
            body["start_time"] = self.start_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> UnityCatalogConnection:
        """Deserializes the UnityCatalogConnection from a dictionary."""
        return cls(
            configuration=d.get("configuration", None),
            connection_name=d.get("connection_name", None),
            connector=d.get("connector", None),
            effective_start_time=_timestamp(d, "effective_start_time"),
            start_time=_timestamp(d, "start_time"),
        )


@dataclass
class WebhookExportConfig:
    export_updates: Optional[bool] = None
    """Whether a later change to an already-exported alert is delivered too, as a second
    ``lakewatch.alert.updated`` event to the same webhook URL (a close is such an update, carrying a
    terminal ``alert_state``). Creation export is unaffected either way.
    
    Opt-in, and unset means off: a webhook is an event transport rather than a system whose record
    is edited in place, so an update is an extra event the receiving consumer has to correlate to
    the alert it already handled. A destination configured before this event existed must not start
    receiving more without its owner asking."""

    url: Optional[str] = None
    """Webhook destination the server POSTs payloads to, in plaintext. Userinfo (``user:password@``) is
    sent as HTTP Basic auth."""

    def as_dict(self) -> dict:
        """Serializes the WebhookExportConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.export_updates is not None:
            body["export_updates"] = self.export_updates
        if self.url is not None:
            body["url"] = self.url
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the WebhookExportConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.export_updates is not None:
            body["export_updates"] = self.export_updates
        if self.url is not None:
            body["url"] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> WebhookExportConfig:
        """Deserializes the WebhookExportConfig from a dictionary."""
        return cls(export_updates=d.get("export_updates", None), url=d.get("url", None))


class LakewatchAPI:
    """Manage Lakewatch: security-analytics data sources, detection rules, and per-catalog configuration."""

    def __init__(self, api_client):
        self._api = api_client

    def create_datasource(self, datasource: Datasource) -> Datasource:
        """Creates a new datasource.

        :param datasource: :class:`Datasource`

        :returns: :class:`Datasource`
        """

        body = datasource.as_dict()
        query = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/lakewatch/datasources", body=body, headers=headers)
        return Datasource.from_dict(res)

    def create_rule(self, rule: Rule) -> Rule:
        """Creates a new rule.

        :param rule: :class:`Rule`
          The rule to create. Server-assigned fields (``name``, ``rule_id``, timestamps, ``etag``, …) are
          ignored on the request.

        :returns: :class:`Rule`
        """

        body = rule.as_dict()
        query = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/lakewatch/rules", body=body, headers=headers)
        return Rule.from_dict(res)

    def delete_datasource(self, name: str):
        """Deletes a datasource by its resource name.

        :param name: str


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/lakewatch/{name}", headers=headers)

    def delete_rule(self, name: str):
        """Deletes a rule by its resource name.

        :param name: str
          Resource name of the rule to delete. Format: ``rules/{rule_id}``.


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/lakewatch/{name}", headers=headers)

    def get_alert_config(self, name: str) -> AlertConfig:
        """Returns the alert delivery configuration for a catalog.

        :param name: str

        :returns: :class:`AlertConfig`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/lakewatch/{name}", headers=headers)
        return AlertConfig.from_dict(res)

    def get_common_config(self, name: str) -> CommonConfig:
        """Returns the common Lakewatch configuration for a catalog.

        :param name: str

        :returns: :class:`CommonConfig`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/lakewatch/{name}", headers=headers)
        return CommonConfig.from_dict(res)

    def get_datasource(self, name: str) -> Datasource:
        """Returns a single datasource by its resource name.

        :param name: str

        :returns: :class:`Datasource`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/lakewatch/{name}", headers=headers)
        return Datasource.from_dict(res)

    def get_datasource_config(self, name: str) -> DatasourceConfig:
        """Returns the datasource ingestion configuration for a catalog.

        :param name: str

        :returns: :class:`DatasourceConfig`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/lakewatch/{name}", headers=headers)
        return DatasourceConfig.from_dict(res)

    def get_rule(self, name: str) -> Rule:
        """Returns a single rule by its resource name.

        :param name: str
          Full resource name of the detection rule, in the form ``rules/{rule_id}``.

        :returns: :class:`Rule`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/lakewatch/{name}", headers=headers)
        return Rule.from_dict(res)

    def get_rule_config(self, name: str) -> RuleConfig:
        """Returns the detection-rule configuration for a catalog.

        :param name: str

        :returns: :class:`RuleConfig`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/lakewatch/{name}", headers=headers)
        return RuleConfig.from_dict(res)

    def list_datasources(
        self,
        catalog_name: str,
        *,
        filter: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        schema_name: Optional[str] = None,
        view: Optional[DatasourceView] = None,
    ) -> Iterator[Datasource]:
        """Lists the datasources in a Unity Catalog catalog, optionally narrowed to one schema or filtered by
        name. Results are paginated. Datasources that are still being created or deleted are not listed.

        :param catalog_name: str
          Name of the Unity Catalog catalog to list datasources from. Required; each request lists the
          datasources of a single catalog.
        :param filter: str (optional)
          Filter expression that restricts the results to datasources with a given name, for example
          ``datasource_name = "my_source"``. Only a single exact-match comparison on ``datasource_name`` is
          supported, and it matches the datasource's current Unity Catalog name, which reads report in
          ``effective_datasource_name``. Filtered results are returned in a single page.
        :param page_size: int (optional)
          Maximum number of results to return in one page. This is a best-effort upper bound, not a guarantee:
          the server may return fewer items than requested (even zero) while more results still exist. If
          unset or 0, the server picks a default.
        :param page_token: str (optional)
        :param schema_name: str (optional)
          Name of a Unity Catalog schema in ``catalog_name``. Optional; if set, only the datasources in this
          schema are returned, and if omitted, the datasources in all schemas of the catalog are returned.
        :param view: :class:`DatasourceView` (optional)
          Which fields to return for each datasource. Defaults to ``DATASOURCE_VIEW_FULL``.
          ``DATASOURCE_VIEW_BASIC`` returns only the identity and Unity Catalog location fields.

        :returns: Iterator over :class:`Datasource`
        """

        query = {}
        if catalog_name is not None:
            query["catalog_name"] = catalog_name
        if filter is not None:
            query["filter"] = filter
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        if schema_name is not None:
            query["schema_name"] = schema_name
        if view is not None:
            query["view"] = view.value
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", "/api/2.0/lakewatch/datasources", query=query, headers=headers)
            if "datasources" in json:
                for v in json["datasources"]:
                    yield Datasource.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_rules(
        self,
        catalog_name: str,
        *,
        filter: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        schema_name: Optional[str] = None,
        view: Optional[RuleView] = None,
    ) -> Iterator[Rule]:
        """Lists rules, with optional filtering and pagination.

        :param catalog_name: str
          Name of the Unity Catalog catalog to list rules from. Required.
        :param filter: str (optional)
          Filter expression that restricts the results, such as ``rule_name = "my_rule"`` to return only the
          rule with that name. The name is matched against the current UC name, which reads report in
          ``effective_rule_name``.
        :param page_size: int (optional)
          Maximum number of rules to return. The server may return fewer. If unset or 0, the server picks a
          default page size.
        :param page_token: str (optional)
          Page token from a previous ``ListRules`` response, used to fetch the next page of results.
        :param schema_name: str (optional)
          Name of a Unity Catalog schema in ``catalog_name``. If set, only rules in this schema are returned.
          If unset, rules in all schemas of the catalog are returned.
        :param view: :class:`RuleView` (optional)
          How much of each rule to return. Defaults to ``RULE_VIEW_FULL``. ``RULE_VIEW_BASIC`` returns only
          each rule's identity and Unity Catalog location.

        :returns: Iterator over :class:`Rule`
        """

        query = {}
        if catalog_name is not None:
            query["catalog_name"] = catalog_name
        if filter is not None:
            query["filter"] = filter
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        if schema_name is not None:
            query["schema_name"] = schema_name
        if view is not None:
            query["view"] = view.value
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", "/api/2.0/lakewatch/rules", query=query, headers=headers)
            if "rules" in json:
                for v in json["rules"]:
                    yield Rule.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def update_alert_config(
        self, name: str, alert_config: AlertConfig, update_mask: FieldMask, *, etag: Optional[str] = None
    ) -> AlertConfig:
        """Updates the alert delivery configuration for a catalog.

        :param name: str
        :param alert_config: :class:`AlertConfig`
        :param update_mask: FieldMask
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g.,
          ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of ``*`` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using ``*`` wildcards, as it can lead to unintended results if the
          API changes in the future.
        :param etag: str (optional)
          Optimistic-concurrency precondition: if set and it does not match the resource's current ``etag``,
          the update is rejected as a conflict (HTTP 409).

        :returns: :class:`AlertConfig`
        """

        body = alert_config.as_dict()
        query = {}
        if etag is not None:
            query["etag"] = etag
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/lakewatch/{name}", query=query, body=body, headers=headers)
        return AlertConfig.from_dict(res)

    def update_common_config(
        self, name: str, common_config: CommonConfig, update_mask: FieldMask, *, etag: Optional[str] = None
    ) -> CommonConfig:
        """Updates the common Lakewatch configuration for a catalog.

        :param name: str
        :param common_config: :class:`CommonConfig`
        :param update_mask: FieldMask
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g.,
          ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of ``*`` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using ``*`` wildcards, as it can lead to unintended results if the
          API changes in the future.
        :param etag: str (optional)
          Optimistic-concurrency precondition: if set and it does not match the resource's current ``etag``,
          the update is rejected as a conflict (HTTP 409).

        :returns: :class:`CommonConfig`
        """

        body = common_config.as_dict()
        query = {}
        if etag is not None:
            query["etag"] = etag
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/lakewatch/{name}", query=query, body=body, headers=headers)
        return CommonConfig.from_dict(res)

    def update_datasource(
        self, name: str, datasource: Datasource, update_mask: FieldMask, *, etag: Optional[str] = None
    ) -> Datasource:
        """Updates an existing datasource.

        :param name: str
          Resource name of the datasource, in the format ``datasources/{datasource_id}``. Unlike the
          datasource's Unity Catalog location (``catalog_name``, ``schema_name``, and ``datasource_name``),
          the name does not change when the datasource or its catalog or schema is renamed in Unity Catalog.
        :param datasource: :class:`Datasource`
        :param update_mask: FieldMask
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g.,
          ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of ``*`` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using ``*`` wildcards, as it can lead to unintended results if the
          API changes in the future.
        :param etag: str (optional)
          Optimistic-concurrency precondition: if set to a non-empty value that does not match the resource's
          current ``etag``, the update is rejected as a conflict (HTTP 409). Omit this field or send an empty
          string to update unconditionally.

        :returns: :class:`Datasource`
        """

        body = datasource.as_dict()
        query = {}
        if etag is not None:
            query["etag"] = etag
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/lakewatch/{name}", query=query, body=body, headers=headers)
        return Datasource.from_dict(res)

    def update_datasource_config(
        self, name: str, datasource_config: DatasourceConfig, update_mask: FieldMask, *, etag: Optional[str] = None
    ) -> DatasourceConfig:
        """Updates the datasource ingestion configuration for a catalog.

        :param name: str
        :param datasource_config: :class:`DatasourceConfig`
        :param update_mask: FieldMask
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g.,
          ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of ``*`` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using ``*`` wildcards, as it can lead to unintended results if the
          API changes in the future.
        :param etag: str (optional)
          Optimistic-concurrency precondition: if set and it does not match the resource's current ``etag``,
          the update is rejected as a conflict (HTTP 409).

        :returns: :class:`DatasourceConfig`
        """

        body = datasource_config.as_dict()
        query = {}
        if etag is not None:
            query["etag"] = etag
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/lakewatch/{name}", query=query, body=body, headers=headers)
        return DatasourceConfig.from_dict(res)

    def update_rule(self, name: str, rule: Rule, update_mask: FieldMask, *, etag: Optional[str] = None) -> Rule:
        """Updates an existing rule.

        :param name: str
          Resource name, in the form ``rules/{rule_id}``. Assigned by the server on create; required on
          update.
        :param rule: :class:`Rule`
          The rule with its new field values. ``rule.name`` identifies the rule to update.
        :param update_mask: FieldMask
          The set of fields to update. Only fields named in the mask are modified.
        :param etag: str (optional)
          Optimistic-concurrency token from the latest read. A non-empty token that does not match the current
          ``etag`` rejects the update as a conflict (HTTP 409). Omit this field or provide an empty string to
          update unconditionally.

        :returns: :class:`Rule`
        """

        body = rule.as_dict()
        query = {}
        if etag is not None:
            query["etag"] = etag
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/lakewatch/{name}", query=query, body=body, headers=headers)
        return Rule.from_dict(res)

    def update_rule_config(
        self, name: str, rule_config: RuleConfig, update_mask: FieldMask, *, etag: Optional[str] = None
    ) -> RuleConfig:
        """Updates the detection-rule configuration for a catalog.

        :param name: str
        :param rule_config: :class:`RuleConfig`
        :param update_mask: FieldMask
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g.,
          ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of ``*`` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using ``*`` wildcards, as it can lead to unintended results if the
          API changes in the future.
        :param etag: str (optional)
          Optimistic-concurrency precondition: if set and it does not match the resource's current ``etag``,
          the update is rejected as a conflict (HTTP 409).

        :returns: :class:`RuleConfig`
        """

        body = rule_config.as_dict()
        query = {}
        if etag is not None:
            query["etag"] = etag
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/lakewatch/{name}", query=query, body=body, headers=headers)
        return RuleConfig.from_dict(res)

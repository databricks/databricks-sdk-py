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
from databricks.sdk.common import lro
from databricks.sdk.retries import RetryError, poll


_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class AddProjectFilesResponse:
    """Lists the files from an ``AddProjectFiles`` request, including files that were already in the
    project."""

    files: Optional[List[ProjectFile]] = None
    """The requested files, in request order, without conversion results. Call ``ListProjectFiles`` or
    ``GetProjectFile`` to read their state."""

    def as_dict(self) -> dict:
        """Serializes the AddProjectFilesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.files:
            body["files"] = [v.as_dict() for v in self.files]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AddProjectFilesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.files:
            body["files"] = self.files
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AddProjectFilesResponse:
        """Deserializes the AddProjectFilesResponse from a dictionary."""
        return cls(files=_repeated_dict(d, "files", ProjectFile))


@dataclass
class ConversionRun:
    """A conversion of a migration project's files, with its state and the status of each file."""

    create_time: Optional[Timestamp] = None
    """The time the run was accepted, before its background job started."""

    end_time: Optional[Timestamp] = None
    """The time the run ended. Absent while the run is active."""

    error_code: Optional[ConversionRunErrorCode] = None
    """Why the run failed. Set only when ``state`` is ``CONVERSION_RUN_STATE_FAILED``."""

    files: Optional[List[ConversionRunFile]] = None
    """The files in this run, at most 500, each with its status in this run. Later conversions and
    reviews can change ``ProjectFile.status`` but don't change this list."""

    project: Optional[str] = None
    """The resource name of the project being converted, in the format ``projects/{project_id}``."""

    skill_paths: Optional[List[str]] = None
    """The skill folders that the run was started with. Empty if the run discovers skills
    automatically."""

    state: Optional[ConversionRunState] = None
    """The state of the run."""

    def as_dict(self) -> dict:
        """Serializes the ConversionRun into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.end_time is not None:
            body["end_time"] = self.end_time.ToJsonString()
        if self.error_code is not None:
            body["error_code"] = self.error_code.value
        if self.files:
            body["files"] = [v.as_dict() for v in self.files]
        if self.project is not None:
            body["project"] = self.project
        if self.skill_paths:
            body["skill_paths"] = [v for v in self.skill_paths]
        if self.state is not None:
            body["state"] = self.state.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ConversionRun into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.end_time is not None:
            body["end_time"] = self.end_time
        if self.error_code is not None:
            body["error_code"] = self.error_code
        if self.files:
            body["files"] = self.files
        if self.project is not None:
            body["project"] = self.project
        if self.skill_paths:
            body["skill_paths"] = self.skill_paths
        if self.state is not None:
            body["state"] = self.state
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ConversionRun:
        """Deserializes the ConversionRun from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            end_time=_timestamp(d, "end_time"),
            error_code=_enum(d, "error_code", ConversionRunErrorCode),
            files=_repeated_dict(d, "files", ConversionRunFile),
            project=d.get("project", None),
            skill_paths=d.get("skill_paths", None),
            state=_enum(d, "state", ConversionRunState),
        )


class ConversionRunErrorCode(Enum):
    """Why a conversion run failed."""

    CONVERSION_RUN_ERROR_CODE_EXPIRED = "CONVERSION_RUN_ERROR_CODE_EXPIRED"
    CONVERSION_RUN_ERROR_CODE_JOB_FAILED = "CONVERSION_RUN_ERROR_CODE_JOB_FAILED"
    CONVERSION_RUN_ERROR_CODE_SUBMIT_REJECTED = "CONVERSION_RUN_ERROR_CODE_SUBMIT_REJECTED"


@dataclass
class ConversionRunFile:
    """A file in a conversion run."""

    name: Optional[str] = None
    """The resource name of the file, in the format ``projects/{project_id}/files/{file_id}``."""

    status: Optional[FileStatus] = None
    """The status of the file in this run. ``ProjectFile.status`` has the file's latest status across
    all runs."""

    def as_dict(self) -> dict:
        """Serializes the ConversionRunFile into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.status is not None:
            body["status"] = self.status.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ConversionRunFile into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.status is not None:
            body["status"] = self.status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ConversionRunFile:
        """Deserializes the ConversionRunFile from a dictionary."""
        return cls(name=d.get("name", None), status=_enum(d, "status", FileStatus))


class ConversionRunState(Enum):
    """State of a conversion run."""

    CONVERSION_RUN_STATE_ACTIVE = "CONVERSION_RUN_STATE_ACTIVE"
    CONVERSION_RUN_STATE_CANCELLED = "CONVERSION_RUN_STATE_CANCELLED"
    CONVERSION_RUN_STATE_COMPLETED = "CONVERSION_RUN_STATE_COMPLETED"
    CONVERSION_RUN_STATE_FAILED = "CONVERSION_RUN_STATE_FAILED"


@dataclass
class ConvertProjectFilesResponse:
    """The result of a completed conversion."""

    run: Optional[ConversionRun] = None
    """The completed conversion run. Each file's outcome is in ``run.files``; a completed run can
    include files that failed to convert."""

    def as_dict(self) -> dict:
        """Serializes the ConvertProjectFilesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.run:
            body["run"] = self.run.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ConvertProjectFilesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.run:
            body["run"] = self.run
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ConvertProjectFilesResponse:
        """Deserializes the ConvertProjectFilesResponse from a dictionary."""
        return cls(run=_from_dict(d, "run", ConversionRun))


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


class DestinationKind(Enum):
    """Destination asset kind for a converted file."""

    DESTINATION_KIND_DESIGNER_FILE = "DESTINATION_KIND_DESIGNER_FILE"
    DESTINATION_KIND_FILE = "DESTINATION_KIND_FILE"
    DESTINATION_KIND_NOTEBOOK = "DESTINATION_KIND_NOTEBOOK"
    DESTINATION_KIND_QUERY = "DESTINATION_KIND_QUERY"


@dataclass
class DestinationResource:
    """A Databricks job or pipeline created during conversion."""

    job_id: Optional[int] = None
    """The ID of the job that conversion created, if any."""

    pipeline_id: Optional[str] = None
    """The ID (a UUID) of the pipeline that conversion created, if any."""

    def as_dict(self) -> dict:
        """Serializes the DestinationResource into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.job_id is not None:
            body["job_id"] = self.job_id
        if self.pipeline_id is not None:
            body["pipeline_id"] = self.pipeline_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DestinationResource into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.job_id is not None:
            body["job_id"] = self.job_id
        if self.pipeline_id is not None:
            body["pipeline_id"] = self.pipeline_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DestinationResource:
        """Deserializes the DestinationResource from a dictionary."""
        return cls(job_id=_int64(d, "job_id"), pipeline_id=d.get("pipeline_id", None))


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


class FileStatus(Enum):
    """Conversion status of a file in a migration project."""

    FILE_STATUS_ERROR = "FILE_STATUS_ERROR"
    FILE_STATUS_IN_PROGRESS = "FILE_STATUS_IN_PROGRESS"
    FILE_STATUS_PARTIAL_SUCCESS = "FILE_STATUS_PARTIAL_SUCCESS"
    FILE_STATUS_QUEUED = "FILE_STATUS_QUEUED"
    FILE_STATUS_REVIEWED = "FILE_STATUS_REVIEWED"
    FILE_STATUS_STOPPED = "FILE_STATUS_STOPPED"
    FILE_STATUS_SUCCESS = "FILE_STATUS_SUCCESS"


@dataclass
class ListProjectFilesResponse:
    """The response to ``ListProjectFiles``."""

    next_page_token: Optional[str] = None
    """The token for the next page. Empty when there are no more pages."""

    project_files: Optional[List[ProjectFile]] = None
    """The files in this page."""

    def as_dict(self) -> dict:
        """Serializes the ListProjectFilesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.project_files:
            body["project_files"] = [v.as_dict() for v in self.project_files]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListProjectFilesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.project_files:
            body["project_files"] = self.project_files
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListProjectFilesResponse:
        """Deserializes the ListProjectFilesResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            project_files=_repeated_dict(d, "project_files", ProjectFile),
        )


@dataclass
class ListProjectsResponse:
    """The response to ``ListProjects``."""

    next_page_token: Optional[str] = None
    """The token for the next page. Empty when there are no more pages."""

    projects: Optional[List[Project]] = None
    """The projects in this page, without ``project_config`` or ``changes_locked``. Call ``GetProject``
    for the full project."""

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
class Location:
    """The location of a file or folder. Exactly one location type is set. More location types can be
    added later, so clients should ignore types they don't recognize."""

    workspace: Optional[WorkspaceLocation] = None
    """A file or folder in the workspace."""

    def as_dict(self) -> dict:
        """Serializes the Location into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.workspace:
            body["workspace"] = self.workspace.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Location into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.workspace:
            body["workspace"] = self.workspace
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Location:
        """Deserializes the Location from a dictionary."""
        return cls(workspace=_from_dict(d, "workspace", WorkspaceLocation))


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
    """A migration project: the conversion settings and source files of one migration."""

    project_config: ProjectConfig
    """The conversion settings of the project. Required on create. Returned by ``CreateProject``,
    ``GetProject``, and ``UpdateProject``, but not by ``ListProjects``."""

    display_name: str
    """The display name of the project. Required on create, and can't be blank. Changing it renames the
    project."""

    changes_locked: Optional[bool] = None
    """Whether the source dialect and target framework are locked. They lock after a conversion or
    analysis runs on the project. Other settings stay editable."""

    create_time: Optional[Timestamp] = None
    """The time the project was created, if available. Can be absent from ``CreateProject`` and
    ``UpdateProject`` responses."""

    folder: Optional[str] = None
    """The workspace folder that contains the project, in the format ``folders/{folder_id}``. For
    example, ``folders/456``. If omitted on create, defaults to the caller's home folder.
    ``UpdateProject`` can't change it, but moving the project in the workspace does. Returned when
    available. Converted files are written to ``project_config.destination_location``, which can be
    a different folder."""

    name: Optional[str] = None
    """The resource name of the project, in the format ``projects/{project_id}``. For example,
    ``projects/123``. The server assigns it when the project is created."""

    update_time: Optional[Timestamp] = None
    """The time the project was last modified, if available. Can be absent from ``CreateProject`` and
    ``UpdateProject`` responses."""

    def as_dict(self) -> dict:
        """Serializes the Project into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.changes_locked is not None:
            body["changes_locked"] = self.changes_locked
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.folder is not None:
            body["folder"] = self.folder
        if self.name is not None:
            body["name"] = self.name
        if self.project_config:
            body["project_config"] = self.project_config.as_dict()
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Project into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.changes_locked is not None:
            body["changes_locked"] = self.changes_locked
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.folder is not None:
            body["folder"] = self.folder
        if self.name is not None:
            body["name"] = self.name
        if self.project_config:
            body["project_config"] = self.project_config
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Project:
        """Deserializes the Project from a dictionary."""
        return cls(
            changes_locked=d.get("changes_locked", None),
            create_time=_timestamp(d, "create_time"),
            display_name=d.get("display_name", None),
            folder=d.get("folder", None),
            name=d.get("name", None),
            project_config=_from_dict(d, "project_config", ProjectConfig),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class ProjectConfig:
    """Conversion settings of a migration project."""

    target_framework: TargetFramework
    """The framework that source files are converted to. Required on create, and can't be
    ``TARGET_FRAMEWORK_UNSPECIFIED``. Can't be changed when ``Project.changes_locked`` is ``true``."""

    destination_location: Optional[Location] = None
    """The workspace folder where converted files are written. Required on create; set
    ``workspace.path`` or ``workspace.object_id``. ``UpdateProject`` can't change it."""

    lineage_location: Optional[Location] = None
    """The workspace JSON file that holds the project's lineage report. Optional. To clear it, include
    ``project_config.lineage_location`` in ``update_mask`` and leave this field unset."""

    source_dialect: Optional[SourceDialect] = None
    """The dialect of the project's source files. Can't be changed when ``Project.changes_locked`` is
    ``true``."""

    def as_dict(self) -> dict:
        """Serializes the ProjectConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.destination_location:
            body["destination_location"] = self.destination_location.as_dict()
        if self.lineage_location:
            body["lineage_location"] = self.lineage_location.as_dict()
        if self.source_dialect is not None:
            body["source_dialect"] = self.source_dialect.value
        if self.target_framework is not None:
            body["target_framework"] = self.target_framework.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ProjectConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.destination_location:
            body["destination_location"] = self.destination_location
        if self.lineage_location:
            body["lineage_location"] = self.lineage_location
        if self.source_dialect is not None:
            body["source_dialect"] = self.source_dialect
        if self.target_framework is not None:
            body["target_framework"] = self.target_framework
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ProjectConfig:
        """Deserializes the ProjectConfig from a dictionary."""
        return cls(
            destination_location=_from_dict(d, "destination_location", Location),
            lineage_location=_from_dict(d, "lineage_location", Location),
            source_dialect=_enum(d, "source_dialect", SourceDialect),
            target_framework=_enum(d, "target_framework", TargetFramework),
        )


@dataclass
class ProjectFile:
    """A source file in a migration project, with its latest conversion results. The service sets the
    conversion results. To accept the converted output, call ``ReviewProjectFiles``; to undo that,
    call ``UnreviewProjectFiles``. Neither method changes the conversion results."""

    blockers: Optional[List[str]] = None
    """Issues that block the conversion. Returned only by ``GetProjectFile``, which reads them from the
    converted file."""

    changes: Optional[List[str]] = None
    """The changes made during conversion. Returned only by ``GetProjectFile``, which reads them from
    the converted file."""

    derived_from: Optional[Location] = None
    """The location of the asset that this file was derived from. Absent if the file wasn't derived
    from another asset."""

    destination: Optional[Location] = None
    """The location of the converted file. Absent until a conversion writes it."""

    destination_kind: Optional[DestinationKind] = None
    """The kind of the converted file, when recorded."""

    destination_resource: Optional[DestinationResource] = None
    """The Databricks job or pipeline that conversion created for this file, if any."""

    error_message: Optional[str] = None
    """The error reported for this file, if any. ``GetProjectFile`` returns the error stored with the
    converted file when available, and otherwise the latest error recorded for the project file."""

    has_notes: Optional[bool] = None
    """Whether the file has conversion notes. Returned by ``ListProjectFiles``; call ``GetProjectFile``
    to read the notes."""

    name: Optional[str] = None
    """The resource name of the file, in the format ``projects/{project_id}/files/{file_id}``. For
    example, ``projects/123/files/789``. The server assigns ``file_id``, an opaque value of at most
    63 characters."""

    notes: Optional[List[str]] = None
    """Informational notes about the conversion that need no decision. Returned only by
    ``GetProjectFile``, which reads them from the converted file."""

    source: Optional[Location] = None
    """The location of the source file."""

    status: Optional[FileStatus] = None
    """The file's latest conversion status across all runs. For its status in a specific run, read
    ``ConversionRun.files`` in that run's operation metadata."""

    todos: Optional[List[str]] = None
    """Follow-up work (to-do items) identified during conversion. Returned only by ``GetProjectFile``,
    which reads them from the converted file."""

    def as_dict(self) -> dict:
        """Serializes the ProjectFile into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.blockers:
            body["blockers"] = [v for v in self.blockers]
        if self.changes:
            body["changes"] = [v for v in self.changes]
        if self.derived_from:
            body["derived_from"] = self.derived_from.as_dict()
        if self.destination:
            body["destination"] = self.destination.as_dict()
        if self.destination_kind is not None:
            body["destination_kind"] = self.destination_kind.value
        if self.destination_resource:
            body["destination_resource"] = self.destination_resource.as_dict()
        if self.error_message is not None:
            body["error_message"] = self.error_message
        if self.has_notes is not None:
            body["has_notes"] = self.has_notes
        if self.name is not None:
            body["name"] = self.name
        if self.notes:
            body["notes"] = [v for v in self.notes]
        if self.source:
            body["source"] = self.source.as_dict()
        if self.status is not None:
            body["status"] = self.status.value
        if self.todos:
            body["todos"] = [v for v in self.todos]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ProjectFile into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.blockers:
            body["blockers"] = self.blockers
        if self.changes:
            body["changes"] = self.changes
        if self.derived_from:
            body["derived_from"] = self.derived_from
        if self.destination:
            body["destination"] = self.destination
        if self.destination_kind is not None:
            body["destination_kind"] = self.destination_kind
        if self.destination_resource:
            body["destination_resource"] = self.destination_resource
        if self.error_message is not None:
            body["error_message"] = self.error_message
        if self.has_notes is not None:
            body["has_notes"] = self.has_notes
        if self.name is not None:
            body["name"] = self.name
        if self.notes:
            body["notes"] = self.notes
        if self.source:
            body["source"] = self.source
        if self.status is not None:
            body["status"] = self.status
        if self.todos:
            body["todos"] = self.todos
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ProjectFile:
        """Deserializes the ProjectFile from a dictionary."""
        return cls(
            blockers=d.get("blockers", None),
            changes=d.get("changes", None),
            derived_from=_from_dict(d, "derived_from", Location),
            destination=_from_dict(d, "destination", Location),
            destination_kind=_enum(d, "destination_kind", DestinationKind),
            destination_resource=_from_dict(d, "destination_resource", DestinationResource),
            error_message=d.get("error_message", None),
            has_notes=d.get("has_notes", None),
            name=d.get("name", None),
            notes=d.get("notes", None),
            source=_from_dict(d, "source", Location),
            status=_enum(d, "status", FileStatus),
            todos=d.get("todos", None),
        )


@dataclass
class RemoveProjectFilesResponse:
    """Lists the files from a ``RemoveProjectFiles`` request."""

    files: Optional[List[ProjectFile]] = None
    """The requested files, in request order. Each entry identifies a source file and has no conversion
    results."""

    def as_dict(self) -> dict:
        """Serializes the RemoveProjectFilesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.files:
            body["files"] = [v.as_dict() for v in self.files]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RemoveProjectFilesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.files:
            body["files"] = self.files
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RemoveProjectFilesResponse:
        """Deserializes the RemoveProjectFilesResponse from a dictionary."""
        return cls(files=_repeated_dict(d, "files", ProjectFile))


@dataclass
class ReviewProjectFilesResponse:
    """The files reviewed by ``ReviewProjectFiles``, in request order."""

    project_files: Optional[List[ProjectFile]] = None
    """The reviewed files, in request order. To read a file's changes, to-do items, blockers, and
    notes, call ``GetProjectFile``."""

    def as_dict(self) -> dict:
        """Serializes the ReviewProjectFilesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.project_files:
            body["project_files"] = [v.as_dict() for v in self.project_files]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ReviewProjectFilesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.project_files:
            body["project_files"] = self.project_files
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ReviewProjectFilesResponse:
        """Deserializes the ReviewProjectFilesResponse from a dictionary."""
        return cls(project_files=_repeated_dict(d, "project_files", ProjectFile))


class SourceDialect(Enum):
    """Source dialect of the files in a migration project."""

    SOURCE_DIALECT_ALTERYX = "SOURCE_DIALECT_ALTERYX"
    SOURCE_DIALECT_BIGQUERY = "SOURCE_DIALECT_BIGQUERY"
    SOURCE_DIALECT_INFORMATICA = "SOURCE_DIALECT_INFORMATICA"
    SOURCE_DIALECT_ORACLE = "SOURCE_DIALECT_ORACLE"
    SOURCE_DIALECT_REDSHIFT = "SOURCE_DIALECT_REDSHIFT"
    SOURCE_DIALECT_SNOWFLAKE = "SOURCE_DIALECT_SNOWFLAKE"
    SOURCE_DIALECT_SSIS = "SOURCE_DIALECT_SSIS"
    SOURCE_DIALECT_TERADATA = "SOURCE_DIALECT_TERADATA"
    SOURCE_DIALECT_T_SQL = "SOURCE_DIALECT_T_SQL"


@dataclass
class SourceFileRef:
    """A reference to a source file in the workspace. Set ``workspace.path`` or
    ``workspace.object_id``. For example, ``{"workspace": {"path":
    "/Workspace/Shared/migration/source.sql"}}``."""

    derived_from: Optional[Location] = None
    """The location of the asset that this file was derived from, if any. Used only by
    ``AddProjectFiles``, and can't be changed after the file is added."""

    workspace: Optional[WorkspaceLocation] = None
    """The source file in the workspace. Must identify an existing file the caller can read."""

    def as_dict(self) -> dict:
        """Serializes the SourceFileRef into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.derived_from:
            body["derived_from"] = self.derived_from.as_dict()
        if self.workspace:
            body["workspace"] = self.workspace.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SourceFileRef into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.derived_from:
            body["derived_from"] = self.derived_from
        if self.workspace:
            body["workspace"] = self.workspace
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SourceFileRef:
        """Deserializes the SourceFileRef from a dictionary."""
        return cls(
            derived_from=_from_dict(d, "derived_from", Location),
            workspace=_from_dict(d, "workspace", WorkspaceLocation),
        )


class TargetFramework(Enum):
    """Output framework of the converted files in a migration project."""

    TARGET_FRAMEWORK_DESIGNER = "TARGET_FRAMEWORK_DESIGNER"
    TARGET_FRAMEWORK_PYSPARK = "TARGET_FRAMEWORK_PYSPARK"
    TARGET_FRAMEWORK_SPARK_DECLARATIVE_PIPELINES = "TARGET_FRAMEWORK_SPARK_DECLARATIVE_PIPELINES"
    TARGET_FRAMEWORK_SQL = "TARGET_FRAMEWORK_SQL"


@dataclass
class UnreviewProjectFilesResponse:
    """The files unreviewed by ``UnreviewProjectFiles``, in request order."""

    project_files: Optional[List[ProjectFile]] = None
    """The unreviewed files, in request order. To read a file's changes, to-do items, blockers, and
    notes, call ``GetProjectFile``."""

    def as_dict(self) -> dict:
        """Serializes the UnreviewProjectFilesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.project_files:
            body["project_files"] = [v.as_dict() for v in self.project_files]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the UnreviewProjectFilesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.project_files:
            body["project_files"] = self.project_files
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> UnreviewProjectFilesResponse:
        """Deserializes the UnreviewProjectFilesResponse from a dictionary."""
        return cls(project_files=_repeated_dict(d, "project_files", ProjectFile))


@dataclass
class WorkspaceLocation:
    """A file or folder in the workspace. On input, set ``path`` or ``object_id``; if both are set,
    ``object_id`` is used. Responses set both when known."""

    object_id: Optional[int] = None
    """The workspace object ID, as returned in ``object_id`` by the Workspace API. For example,
    ``12345``."""

    path: Optional[str] = None
    """The absolute workspace path. For example, ``/Workspace/Shared/migration/source.sql``."""

    def as_dict(self) -> dict:
        """Serializes the WorkspaceLocation into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.object_id is not None:
            body["object_id"] = self.object_id
        if self.path is not None:
            body["path"] = self.path
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the WorkspaceLocation into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.object_id is not None:
            body["object_id"] = self.object_id
        if self.path is not None:
            body["path"] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> WorkspaceLocation:
        """Deserializes the WorkspaceLocation from a dictionary."""
        return cls(object_id=_int64(d, "object_id"), path=d.get("path", None))


class GenieMigrateAPI:
    """Use the Genie Migrate API to create and manage migration projects and the source files to convert."""

    def __init__(self, api_client):
        self._api = api_client

    def add_files(self, name: str, sources: List[SourceFileRef]) -> AddProjectFilesResponse:
        """Adds source files to a migration project. Files that are already in the project are skipped and keep
        their conversion results.

        :param name: str
          The resource name of the project, in the format ``projects/{project_id}``. For example,
          ``projects/123``.
        :param sources: List[:class:`SourceFileRef`]
          The files to add, each identified by ``workspace.path`` or ``workspace.object_id``. Send at most 500
          files per request. Duplicate files, and requests that exceed a file-count limit, return
          ``INVALID_PARAMETER_VALUE``. Files already in the project aren't overwritten. An empty list changes
          nothing.

        :returns: :class:`AddProjectFilesResponse`
        """

        body = {}
        if sources is not None:
            body["sources"] = [v.as_dict() for v in sources]
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/migrations/{name}/files:add", body=body, headers=headers)
        return AddProjectFilesResponse.from_dict(res)

    def cancel_operation(self, name: str):
        """Requests cancellation of a long-running operation. Requires ``CAN_EDIT`` permission on the project.
        Cancellation is best effort: the operation can complete before cancellation takes effect. Call
        ``GetOperation`` to see its final state.

        :param name: str
          The name of the operation resource to be cancelled.


        """

        body = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("POST", f"/api/2.0/migrations/{name}/cancel", body=body, headers=headers)

    def convert_project_files(
        self,
        parent: str,
        *,
        names: Optional[List[str]] = None,
        skill_paths: Optional[List[str]] = None,
        start_over: Optional[bool] = None,
    ) -> ConvertProjectFilesOperation:
        """Converts files of a migration project in a background job. Returns an operation; poll it with
        ``GetOperation``. The operation's metadata is the current ``ConversionRun``, with the run's state and
        the status of each file. When the run completes, the operation's response is a
        ``ConvertProjectFilesResponse``. A failed or cancelled run sets the operation's ``error`` instead.
        Files that fail to convert don't fail the run.

        To stop a conversion, call ``CancelOperation``. Cancellation is best effort, and the conversion can
        complete first. ``GetOperation`` reports the final outcome.

        :param parent: str
          The resource name of the project whose files to convert, in the format ``projects/{project_id}``.
          For example, ``projects/123``.
        :param names: List[str] (optional)
          The files to convert, in the format ``projects/{project_id}/files/{file_id}``. For example,
          ``projects/123/files/789``. All files must belong to ``parent``. At most 500 files; a workspace can
          set a lower limit, and requests over it return ``INVALID_PARAMETER_VALUE``.
        :param skill_paths: List[str] (optional)
          Custom skills that the conversion can use, as workspace paths of skill folders. Each folder must
          contain a ``SKILL.md`` file and be directly inside a skills folder: ``<home>/.assistant/skills``,
          ``/Workspace/.assistant/skills``, or another configured skills folder. At most 10 paths, which
          together must fit in 1000 bytes when encoded as a JSON array. Larger values return
          ``INVALID_PARAMETER_VALUE``. If empty, the conversion discovers skills automatically.
        :param start_over: bool (optional)
          Whether to convert each selected file from scratch instead of continuing from its previous results
          (changes, to-do items, blockers, and notes). Supported only for projects whose target framework is
          ``TARGET_FRAMEWORK_SQL``; other projects return ``INVALID_PARAMETER_VALUE``. Defaults to ``false``.

        :returns: :class:`Operation`
        """

        body = {}
        if names is not None:
            body["names"] = [v for v in names]
        if skill_paths is not None:
            body["skill_paths"] = [v for v in skill_paths]
        if start_over is not None:
            body["start_over"] = start_over
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/migrations/{parent}/files:convert", body=body, headers=headers)
        operation = Operation.from_dict(res)
        return ConvertProjectFilesOperation(self, operation)

    def create(self, project: Project) -> Project:
        """Creates a migration project in a workspace folder. The server assigns the project ID. Add source files
        to the project with ``AddProjectFiles``.

        :param project: :class:`Project`
          The project to create. The server sets ``name`` in the response.

        :returns: :class:`Project`
        """

        body = project.as_dict()
        query = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/migrations/projects", body=body, headers=headers)
        return Project.from_dict(res)

    def delete(self, name: str):
        """Moves a migration project to the workspace trash. The project keeps its ID until it's removed from the
        trash.

        :param name: str
          The resource name of the project, in the format ``projects/{project_id}``. For example,
          ``projects/123``.


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/migrations/{name}", headers=headers)

    def get(self, name: str) -> Project:
        """Gets a migration project, including its conversion settings and whether they're locked. To list the
        project's source files, call ``ListProjectFiles``. To track a conversion, call ``GetOperation``.

        :param name: str
          The resource name of the project, in the format ``projects/{project_id}``. For example,
          ``projects/123``.

        :returns: :class:`Project`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/migrations/{name}", headers=headers)
        return Project.from_dict(res)

    def get_file(self, name: str) -> ProjectFile:
        """Gets a file of a migration project, including the conversion details stored with its converted file,
        when available. Requires ``CAN_READ`` permission on the project and, once the file is converted, on
        the converted file.

        :param name: str
          The resource name of the file, in the format ``projects/{project_id}/files/{file_id}``. For example,
          ``projects/123/files/789``.

        :returns: :class:`ProjectFile`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/migrations/{name}", headers=headers)
        return ProjectFile.from_dict(res)

    def get_operation(self, name: str) -> Operation:
        """Gets the latest state of a long-running operation, such as a conversion started by
        ``ConvertProjectFiles``. Operation names have the format
        ``projects/{project_id}/operations/{operation_id}``. Use the full name that the service returned, and
        treat the operation ID as opaque. Requires ``CAN_READ`` permission on the project.

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

        res = self._api.do("GET", f"/api/2.0/migrations/{name}", headers=headers)
        return Operation.from_dict(res)

    def list(
        self, *, filter: Optional[str] = None, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Project]:
        """Lists the migration projects in a workspace folder. Select the folder with ``filter``; without a
        filter, lists the caller's home folder. Listing every project in the workspace isn't supported.

        Returns project summaries without conversion settings; call ``GetProject`` for the full project. A
        page can be empty even when more pages follow, so keep requesting pages until ``next_page_token`` is
        empty.

        :param filter: str (optional)
          The folder to list, as ``folder = "folders/{folder_id}"``. For example, ``folder = "folders/456"``.
          No other filter is supported. Defaults to the caller's home folder.
        :param page_size: int (optional)
          The maximum number of projects to return, at most 500. Defaults to 100 if omitted, zero, or
          negative. A page can have fewer projects than requested, or none, even when more pages follow.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response. Omit it for the first page. Use the same
          ``filter`` for every page.

        :returns: Iterator over :class:`Project`
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
            json = self._api.do("GET", "/api/2.0/migrations/projects", query=query, headers=headers)
            if "projects" in json:
                for v in json["projects"]:
                    yield Project.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_files(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[ProjectFile]:
        """Lists the files of a migration project with their latest conversion statuses. To read a file's
        changes, to-do items, blockers, and notes, call ``GetProjectFile``. A page can have fewer files than
        requested, or none, even when more pages follow; keep requesting pages until ``next_page_token`` is
        empty.

        :param parent: str
          The resource name of the project, in the format ``projects/{project_id}``. For example,
          ``projects/123``.
        :param page_size: int (optional)
          The maximum number of files to return, at most 500. If omitted, zero, or negative, the server
          chooses. The server can return a different number of files than requested, so keep requesting pages
          until ``next_page_token`` is empty.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response. Omit it for the first page. Use it only with the
          same ``parent``.

        :returns: Iterator over :class:`ProjectFile`
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
            json = self._api.do("GET", f"/api/2.0/migrations/{parent}/files", query=query, headers=headers)
            if "project_files" in json:
                for v in json["project_files"]:
                    yield ProjectFile.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def remove_files(self, name: str, *, names: Optional[List[str]] = None) -> RemoveProjectFilesResponse:
        """Removes files from a migration project by their resource names. The source files and their converted
        output stay in the workspace.

        :param name: str
          The resource name of the project, in the format ``projects/{project_id}``. For example,
          ``projects/123``.
        :param names: List[str] (optional)
          The files to remove, by ``ProjectFile.name``. For example, ``projects/123/files/789``. Every file
          must belong to the project in ``name``. An empty list changes nothing. Send at most 10 files per
          request, the default limit. Requests over a project's limit return ``INVALID_PARAMETER_VALUE``.

        :returns: :class:`RemoveProjectFilesResponse`
        """

        body = {}
        if names is not None:
            body["names"] = [v for v in names]
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/migrations/{name}/files:remove", body=body, headers=headers)
        return RemoveProjectFilesResponse.from_dict(res)

    def review_project_files(self, parent: str, names: List[str]) -> ReviewProjectFilesResponse:
        """Marks files of a migration project as reviewed, accepting their converted output. Each file's status
        becomes ``FILE_STATUS_REVIEWED``, and reviewed files aren't converted again. Files that are already
        reviewed don't change. Returns the files in request order.

        :param parent: str
          The resource name of the project, in the format ``projects/{project_id}``. For example,
          ``projects/123``. Every file in ``names`` must belong to this project.
        :param names: List[str]
          The files to review: 1 to 100 distinct file resource names, in the format
          ``projects/{project_id}/files/{file_id}``. For example, ``projects/123/files/789``.

        :returns: :class:`ReviewProjectFilesResponse`
        """

        body = {}
        if names is not None:
            body["names"] = [v for v in names]
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/migrations/{parent}/files:review", body=body, headers=headers)
        return ReviewProjectFilesResponse.from_dict(res)

    def unreview_project_files(self, parent: str, names: List[str]) -> UnreviewProjectFilesResponse:
        """Removes the reviewed status from files of a migration project. Each file returns to the status it had
        before it was reviewed. Files that aren't reviewed don't change. Returns the files in request order.

        :param parent: str
          The resource name of the project, in the format ``projects/{project_id}``. For example,
          ``projects/123``. Every file in ``names`` must belong to this project.
        :param names: List[str]
          The files to unreview: 1 to 100 distinct file resource names, in the format
          ``projects/{project_id}/files/{file_id}``. For example, ``projects/123/files/789``.

        :returns: :class:`UnreviewProjectFilesResponse`
        """

        body = {}
        if names is not None:
            body["names"] = [v for v in names]
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/migrations/{parent}/files:unreview", body=body, headers=headers)
        return UnreviewProjectFilesResponse.from_dict(res)

    def update(self, name: str, project: Project, update_mask: FieldMask) -> Project:
        """Updates a migration project. Only the fields listed in ``update_mask`` change. An empty mask, or a
        mask with an unsupported field, returns ``INVALID_PARAMETER_VALUE``. When ``changes_locked`` is
        ``true``, the source dialect and target framework can't be changed.

        :param name: str
          The resource name of the project, in the format ``projects/{project_id}``. For example,
          ``projects/123``. The server assigns it when the project is created.
        :param project: :class:`Project`
          The project to update, identified by ``name``.
        :param update_mask: FieldMask
          The fields to update. Supported fields are ``display_name``, ``project_config.source_dialect``,
          ``project_config.target_framework``, and ``project_config.lineage_location``. ``project_config`` and
          ``*`` update all three ``project_config`` fields and can't be combined with ``display_name``.

        :returns: :class:`Project`
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

        res = self._api.do("PATCH", f"/api/2.0/migrations/{name}", query=query, body=body, headers=headers)
        return Project.from_dict(res)


class ConvertProjectFilesOperation:
    """Long-running operation for convert_project_files"""

    def __init__(self, impl: GenieMigrateAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> ConvertProjectFilesResponse:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`ConvertProjectFilesResponse`
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

            convert_project_files_response = ConvertProjectFilesResponse.from_dict(operation.response)

            return convert_project_files_response, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def cancel(self):
        """Starts asynchronous cancellation on a long-running operation. The server
        makes a best effort to cancel the operation, but success is not guaranteed.
        """
        self._impl.cancel_operation(name=self._operation.name)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> ConversionRun:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`ConversionRun` or None
        """
        if self._operation.metadata is None:
            return None

        return ConversionRun.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done

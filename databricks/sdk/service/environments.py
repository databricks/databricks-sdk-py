# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
import uuid
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List, Optional

from google.protobuf.timestamp_pb2 import Timestamp

from databricks.sdk.common import lro
from databricks.sdk.common.types.fieldmask import FieldMask
from databricks.sdk.retries import RetryError, poll
from databricks.sdk.service._internal import (_enum, _from_dict,
                                              _repeated_dict, _timestamp)

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


class BaseEnvironmentType(Enum):
    """If changed, also update estore/namespaces/defaultbaseenvironments/latest.proto"""

    CPU = "CPU"
    GPU = "GPU"


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


@dataclass
class DefaultWorkspaceBaseEnvironment:
    """A singleton resource representing the default workspace base environment configuration. This
    resource contains the workspace base environments that are used as defaults for serverless
    notebooks and jobs in the workspace, for both CPU and GPU compute types."""

    cpu_workspace_base_environment: Optional[str] = None
    """The default workspace base environment for CPU compute. Format:
    workspace-base-environments/{workspace_base_environment}"""

    gpu_workspace_base_environment: Optional[str] = None
    """The default workspace base environment for GPU compute. Format:
    workspace-base-environments/{workspace_base_environment}"""

    name: Optional[str] = None
    """The resource name of this singleton resource. Format: default-workspace-base-environment"""

    def as_dict(self) -> dict:
        """Serializes the DefaultWorkspaceBaseEnvironment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.cpu_workspace_base_environment is not None:
            body["cpu_workspace_base_environment"] = self.cpu_workspace_base_environment
        if self.gpu_workspace_base_environment is not None:
            body["gpu_workspace_base_environment"] = self.gpu_workspace_base_environment
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DefaultWorkspaceBaseEnvironment into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.cpu_workspace_base_environment is not None:
            body["cpu_workspace_base_environment"] = self.cpu_workspace_base_environment
        if self.gpu_workspace_base_environment is not None:
            body["gpu_workspace_base_environment"] = self.gpu_workspace_base_environment
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DefaultWorkspaceBaseEnvironment:
        """Deserializes the DefaultWorkspaceBaseEnvironment from a dictionary."""
        return cls(
            cpu_workspace_base_environment=d.get("cpu_workspace_base_environment", None),
            gpu_workspace_base_environment=d.get("gpu_workspace_base_environment", None),
            name=d.get("name", None),
        )


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
class ListWorkspaceBaseEnvironmentsResponse:
    """Response message for ListWorkspaceBaseEnvironments."""

    next_page_token: Optional[str] = None
    """Token to retrieve the next page of results. Empty if there are no more results."""

    workspace_base_environments: Optional[List[WorkspaceBaseEnvironment]] = None
    """The list of workspace base environments."""

    def as_dict(self) -> dict:
        """Serializes the ListWorkspaceBaseEnvironmentsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.workspace_base_environments:
            body["workspace_base_environments"] = [v.as_dict() for v in self.workspace_base_environments]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListWorkspaceBaseEnvironmentsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.workspace_base_environments:
            body["workspace_base_environments"] = self.workspace_base_environments
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListWorkspaceBaseEnvironmentsResponse:
        """Deserializes the ListWorkspaceBaseEnvironmentsResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            workspace_base_environments=_repeated_dict(d, "workspace_base_environments", WorkspaceBaseEnvironment),
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


@dataclass
class WorkspaceBaseEnvironment:
    """A WorkspaceBaseEnvironment defines a workspace-level environment configuration consisting of an
    environment version and a list of dependencies."""

    display_name: str
    """Human-readable display name for the workspace base environment."""

    base_environment_type: Optional[BaseEnvironmentType] = None
    """The type of base environment (CPU or GPU)."""

    create_time: Optional[Timestamp] = None
    """Timestamp when the environment was created."""

    creator_user_id: Optional[str] = None
    """User ID of the creator."""

    filepath: Optional[str] = None
    """The WSFS or UC Volumes path to the environment YAML file."""

    is_default: Optional[bool] = None
    """Whether this is the default environment for the workspace."""

    last_updated_user_id: Optional[str] = None
    """User ID of the last user who updated the environment."""

    message: Optional[str] = None
    """Status message providing additional details about the environment status."""

    name: Optional[str] = None
    """The resource name of the workspace base environment. Format:
    workspace-base-environments/{workspace-base-environment}"""

    status: Optional[WorkspaceBaseEnvironmentCacheStatus] = None
    """The status of the materialized workspace base environment."""

    update_time: Optional[Timestamp] = None
    """Timestamp when the environment was last updated."""

    def as_dict(self) -> dict:
        """Serializes the WorkspaceBaseEnvironment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.base_environment_type is not None:
            body["base_environment_type"] = self.base_environment_type.value
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.creator_user_id is not None:
            body["creator_user_id"] = self.creator_user_id
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.filepath is not None:
            body["filepath"] = self.filepath
        if self.is_default is not None:
            body["is_default"] = self.is_default
        if self.last_updated_user_id is not None:
            body["last_updated_user_id"] = self.last_updated_user_id
        if self.message is not None:
            body["message"] = self.message
        if self.name is not None:
            body["name"] = self.name
        if self.status is not None:
            body["status"] = self.status.value
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the WorkspaceBaseEnvironment into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.base_environment_type is not None:
            body["base_environment_type"] = self.base_environment_type
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.creator_user_id is not None:
            body["creator_user_id"] = self.creator_user_id
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.filepath is not None:
            body["filepath"] = self.filepath
        if self.is_default is not None:
            body["is_default"] = self.is_default
        if self.last_updated_user_id is not None:
            body["last_updated_user_id"] = self.last_updated_user_id
        if self.message is not None:
            body["message"] = self.message
        if self.name is not None:
            body["name"] = self.name
        if self.status is not None:
            body["status"] = self.status
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> WorkspaceBaseEnvironment:
        """Deserializes the WorkspaceBaseEnvironment from a dictionary."""
        return cls(
            base_environment_type=_enum(d, "base_environment_type", BaseEnvironmentType),
            create_time=_timestamp(d, "create_time"),
            creator_user_id=d.get("creator_user_id", None),
            display_name=d.get("display_name", None),
            filepath=d.get("filepath", None),
            is_default=d.get("is_default", None),
            last_updated_user_id=d.get("last_updated_user_id", None),
            message=d.get("message", None),
            name=d.get("name", None),
            status=_enum(d, "status", WorkspaceBaseEnvironmentCacheStatus),
            update_time=_timestamp(d, "update_time"),
        )


class WorkspaceBaseEnvironmentCacheStatus(Enum):
    """Status of the environment materialization."""

    CREATED = "CREATED"
    EXPIRED = "EXPIRED"
    FAILED = "FAILED"
    INVALID = "INVALID"
    PENDING = "PENDING"
    REFRESHING = "REFRESHING"


@dataclass
class WorkspaceBaseEnvironmentOperationMetadata:
    """Metadata for the WorkspaceBaseEnvironment long-running operations. This message tracks the
    progress of the workspace base environment long-running process."""

    def as_dict(self) -> dict:
        """Serializes the WorkspaceBaseEnvironmentOperationMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the WorkspaceBaseEnvironmentOperationMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> WorkspaceBaseEnvironmentOperationMetadata:
        """Deserializes the WorkspaceBaseEnvironmentOperationMetadata from a dictionary."""
        return cls()


class EnvironmentsAPI:
    """APIs to manage environment resources.

    The Environments API provides management capabilities for different types of environments including
    workspace-level base environments that define the environment version and dependencies to be used in
    serverless notebooks and jobs."""

    def __init__(self, api_client):
        self._api = api_client

    def create_workspace_base_environment(
        self,
        workspace_base_environment: WorkspaceBaseEnvironment,
        *,
        request_id: Optional[str] = None,
        workspace_base_environment_id: Optional[str] = None,
    ) -> CreateWorkspaceBaseEnvironmentOperation:
        """Creates a new WorkspaceBaseEnvironment. This is a long-running operation. The operation will
        asynchronously generate a materialized environment to optimize dependency resolution and is only
        marked as done when the materialized environment has been successfully generated or has failed.

        :param workspace_base_environment: :class:`WorkspaceBaseEnvironment`
          Required. The workspace base environment to create.
        :param request_id: str (optional)
          A unique identifier for this request. A random UUID is recommended. This request is only idempotent
          if a request_id is provided.
        :param workspace_base_environment_id: str (optional)
          The ID to use for the workspace base environment, which will become the final component of the
          resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

        :returns: :class:`Operation`
        """

        if request_id is None or request_id == "":
            request_id = str(uuid.uuid4())
        body = workspace_base_environment.as_dict()
        query = {}
        if request_id is not None:
            query["request_id"] = request_id
        if workspace_base_environment_id is not None:
            query["workspace_base_environment_id"] = workspace_base_environment_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do(
            "POST", "/api/environments/v1/workspace-base-environments", query=query, body=body, headers=headers
        )
        operation = Operation.from_dict(res)
        return CreateWorkspaceBaseEnvironmentOperation(self, operation)

    def delete_workspace_base_environment(self, name: str):
        """Deletes a WorkspaceBaseEnvironment. Deleting a base environment may impact linked notebooks and jobs.
        This operation is irreversible and should be performed only when you are certain the environment is no
        longer needed.

        :param name: str
          Required. The resource name of the workspace base environment to delete. Format:
          workspace-base-environments/{workspace_base_environment}


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/environments/v1/{name}", headers=headers)

    def get_default_workspace_base_environment(self, name: str) -> DefaultWorkspaceBaseEnvironment:
        """Gets the default WorkspaceBaseEnvironment configuration for the workspace. Returns the current default
        base environment settings for both CPU and GPU compute.

        :param name: str
          A static resource name of the default workspace base environment. Format:
          default-workspace-base-environment

        :returns: :class:`DefaultWorkspaceBaseEnvironment`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/environments/v1/{name}", headers=headers)
        return DefaultWorkspaceBaseEnvironment.from_dict(res)

    def get_operation(self, name: str) -> Operation:
        """Gets the status of a long-running operation. Clients can use this method to poll the operation result.

        :param name: str
          The name of the operation resource.

        :returns: :class:`Operation`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/environments/v1/{name}", headers=headers)
        return Operation.from_dict(res)

    def get_workspace_base_environment(self, name: str) -> WorkspaceBaseEnvironment:
        """Retrieves a WorkspaceBaseEnvironment by its name.

        :param name: str
          Required. The resource name of the workspace base environment to retrieve. Format:
          workspace-base-environments/{workspace_base_environment}

        :returns: :class:`WorkspaceBaseEnvironment`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/environments/v1/{name}", headers=headers)
        return WorkspaceBaseEnvironment.from_dict(res)

    def list_workspace_base_environments(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[WorkspaceBaseEnvironment]:
        """Lists all WorkspaceBaseEnvironments in the workspace.

        :param page_size: int (optional)
          The maximum number of environments to return per page. Default is 1000.
        :param page_token: str (optional)
          Page token for pagination. Received from a previous ListWorkspaceBaseEnvironments call.

        :returns: Iterator over :class:`WorkspaceBaseEnvironment`
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
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", "/api/environments/v1/workspace-base-environments", query=query, headers=headers)
            if "workspace_base_environments" in json:
                for v in json["workspace_base_environments"]:
                    yield WorkspaceBaseEnvironment.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def refresh_workspace_base_environment(self, name: str) -> RefreshWorkspaceBaseEnvironmentOperation:
        """Refreshes the materialized environment for a WorkspaceBaseEnvironment. This is a long-running
        operation. The operation will asynchronously regenerate the materialized environment and is only
        marked as done when the materialized environment has been successfully generated or has failed. The
        existing materialized environment remains available until it expires.

        :param name: str
          Required. The resource name of the workspace base environment to delete. Format:
          workspace-base-environments/{workspace_base_environment}

        :returns: :class:`Operation`
        """

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/environments/v1/{name}/refresh", headers=headers)
        operation = Operation.from_dict(res)
        return RefreshWorkspaceBaseEnvironmentOperation(self, operation)

    def update_default_workspace_base_environment(
        self, name: str, default_workspace_base_environment: DefaultWorkspaceBaseEnvironment, update_mask: FieldMask
    ) -> DefaultWorkspaceBaseEnvironment:
        """Updates the default WorkspaceBaseEnvironment configuration for the workspace. Sets the specified base
        environments as the workspace defaults for CPU and/or GPU compute.

        :param name: str
          The resource name of this singleton resource. Format: default-workspace-base-environment
        :param default_workspace_base_environment: :class:`DefaultWorkspaceBaseEnvironment`
          Required. The default workspace base environment configuration to update.
        :param update_mask: FieldMask
          Field mask specifying which fields to update. Use comma as the separator for multiple fields (no
          space). The special value '*' indicates that all fields should be updated (full replacement). Valid
          field paths: cpu_workspace_base_environment, gpu_workspace_base_environment

          To unset one or both defaults, include the field path(s) in the mask and omit them from the request
          body. To unset both, you must list both paths explicitly — the wildcard '*' cannot be used to
          unset fields.

        :returns: :class:`DefaultWorkspaceBaseEnvironment`
        """

        body = default_workspace_base_environment.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/environments/v1/{name}", query=query, body=body, headers=headers)
        return DefaultWorkspaceBaseEnvironment.from_dict(res)

    def update_workspace_base_environment(
        self, name: str, workspace_base_environment: WorkspaceBaseEnvironment
    ) -> UpdateWorkspaceBaseEnvironmentOperation:
        """Updates an existing WorkspaceBaseEnvironment. This is a long-running operation. The operation will
        asynchronously regenerate the materialized environment and is only marked as done when the
        materialized environment has been successfully generated or has failed. The existing materialized
        environment remains available until it expires.

        :param name: str
        :param workspace_base_environment: :class:`WorkspaceBaseEnvironment`
          Required. The workspace base environment with updated fields. The name field is used to identify the
          environment to update.

        :returns: :class:`Operation`
        """

        body = workspace_base_environment.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/environments/v1/{name}", body=body, headers=headers)
        operation = Operation.from_dict(res)
        return UpdateWorkspaceBaseEnvironmentOperation(self, operation)


class CreateWorkspaceBaseEnvironmentOperation:
    """Long-running operation for create_workspace_base_environment"""

    def __init__(self, impl: EnvironmentsAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> WorkspaceBaseEnvironment:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`WorkspaceBaseEnvironment`
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

            workspace_base_environment = WorkspaceBaseEnvironment.from_dict(operation.response)

            return workspace_base_environment, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> WorkspaceBaseEnvironmentOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`WorkspaceBaseEnvironmentOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return WorkspaceBaseEnvironmentOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class RefreshWorkspaceBaseEnvironmentOperation:
    """Long-running operation for refresh_workspace_base_environment"""

    def __init__(self, impl: EnvironmentsAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> WorkspaceBaseEnvironment:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`WorkspaceBaseEnvironment`
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

            workspace_base_environment = WorkspaceBaseEnvironment.from_dict(operation.response)

            return workspace_base_environment, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> WorkspaceBaseEnvironmentOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`WorkspaceBaseEnvironmentOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return WorkspaceBaseEnvironmentOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class UpdateWorkspaceBaseEnvironmentOperation:
    """Long-running operation for update_workspace_base_environment"""

    def __init__(self, impl: EnvironmentsAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> WorkspaceBaseEnvironment:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`WorkspaceBaseEnvironment`
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

            workspace_base_environment = WorkspaceBaseEnvironment.from_dict(operation.response)

            return workspace_base_environment, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> WorkspaceBaseEnvironmentOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`WorkspaceBaseEnvironmentOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return WorkspaceBaseEnvironmentOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done

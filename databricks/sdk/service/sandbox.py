# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.
# ruff: noqa: F811, F841
# F401 is intentionally NOT covered: `make fmt` uses `ruff check --fix-only`
# to strip the fat-import header below; ignoring F401 would defeat that.

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any, Iterator, Optional

from google.protobuf.duration_pb2 import Duration
from google.protobuf.timestamp_pb2 import Timestamp

import logging

from databricks.sdk.service._internal import (
    _duration,
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
class Command:
    """A single command execution."""

    args: Optional[List[str]] = None
    """Arguments passed to the program."""

    cmd: Optional[str] = None
    """The program that was executed."""

    command_id: Optional[str] = None
    """Stable identifier for this command."""

    exit_code: Optional[int] = None
    """Process exit code. Only present when finished is true and the process exited normally (not
    killed by signal or failed to start)."""

    finished: Optional[bool] = None
    """Whether the command has finished executing."""

    pid: Optional[int] = None
    """PID of the spawned process. Absent if the process failed to start."""

    def as_dict(self) -> dict:
        """Serializes the Command into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.args:
            body["args"] = [v for v in self.args]
        if self.cmd is not None:
            body["cmd"] = self.cmd
        if self.command_id is not None:
            body["command_id"] = self.command_id
        if self.exit_code is not None:
            body["exit_code"] = self.exit_code
        if self.finished is not None:
            body["finished"] = self.finished
        if self.pid is not None:
            body["pid"] = self.pid
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Command into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.args:
            body["args"] = self.args
        if self.cmd is not None:
            body["cmd"] = self.cmd
        if self.command_id is not None:
            body["command_id"] = self.command_id
        if self.exit_code is not None:
            body["exit_code"] = self.exit_code
        if self.finished is not None:
            body["finished"] = self.finished
        if self.pid is not None:
            body["pid"] = self.pid
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Command:
        """Deserializes the Command from a dictionary."""
        return cls(
            args=d.get("args", None),
            cmd=d.get("cmd", None),
            command_id=d.get("command_id", None),
            exit_code=d.get("exit_code", None),
            finished=d.get("finished", None),
            pid=_int64(d, "pid"),
        )


@dataclass
class ComputeSpec:
    inactivity_timeout: Optional[Duration] = None
    """Idle duration after which the sandbox is automatically terminated."""

    def as_dict(self) -> dict:
        """Serializes the ComputeSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.inactivity_timeout is not None:
            body["inactivity_timeout"] = self.inactivity_timeout.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ComputeSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.inactivity_timeout is not None:
            body["inactivity_timeout"] = self.inactivity_timeout
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ComputeSpec:
        """Deserializes the ComputeSpec from a dictionary."""
        return cls(inactivity_timeout=_duration(d, "inactivity_timeout"))


@dataclass
class CreateDirectoryResponse:
    """Confirms that the requested directory exists."""

    def as_dict(self) -> dict:
        """Serializes the CreateDirectoryResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CreateDirectoryResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CreateDirectoryResponse:
        """Deserializes the CreateDirectoryResponse from a dictionary."""
        return cls()


@dataclass
class DeletePathResponse:
    """Confirms that the requested path is absent."""

    def as_dict(self) -> dict:
        """Serializes the DeletePathResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DeletePathResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DeletePathResponse:
        """Deserializes the DeletePathResponse from a dictionary."""
        return cls()


@dataclass
class EnvironmentSpec:
    image_uri: Optional[str] = None
    """A Unity Catalog container artifact (e.g. ``catalog.schema.folder.image:tag``) to run as the
    sandbox environment. When set, this image is used as the environment instead of resolving a
    managed image from ``environment_version``."""

    def as_dict(self) -> dict:
        """Serializes the EnvironmentSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.image_uri is not None:
            body["image_uri"] = self.image_uri
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EnvironmentSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.image_uri is not None:
            body["image_uri"] = self.image_uri
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> EnvironmentSpec:
        """Deserializes the EnvironmentSpec from a dictionary."""
        return cls(image_uri=d.get("image_uri", None))


class ExecuteCommandStatus(Enum):
    """Terminal status of a unary command execution."""

    EXECUTE_COMMAND_STATUS_COMPLETED = "EXECUTE_COMMAND_STATUS_COMPLETED"
    EXECUTE_COMMAND_STATUS_FAILED = "EXECUTE_COMMAND_STATUS_FAILED"
    EXECUTE_COMMAND_STATUS_TIMED_OUT = "EXECUTE_COMMAND_STATUS_TIMED_OUT"


@dataclass
class ExecuteCommandSyncResponse:
    """Result of a completed unary command execution: captured output, exit code, and terminal status."""

    command_id: Optional[str] = None
    """Daemon-generated identifier for this command execution, for correlation (for example in
    ``ListCommands``)."""

    exit_code: Optional[int] = None
    """Process exit code. Unset when the process was terminated by a signal (e.g. on ``TIMED_OUT``) or
    never started (``FAILED``) rather than exiting normally."""

    status: Optional[ExecuteCommandStatus] = None
    """Terminal status of the command execution. Always set on a successful response; never
    ``EXECUTE_COMMAND_STATUS_UNSPECIFIED``."""

    stderr: Optional[str] = None
    """Captured standard error, with the same UTF-8 semantics as ``stdout``."""

    stdout: Optional[str] = None
    """Captured standard output as UTF-8 text. Invalid UTF-8 bytes are replaced with the Unicode
    replacement character (U+FFFD)."""

    truncated: Optional[bool] = None
    """True when ``stdout`` / ``stderr`` were truncated because the captured output exceeded the
    server's per-response size cap. The dropped output is not included in this response and is not
    recoverable through this unary API."""

    def as_dict(self) -> dict:
        """Serializes the ExecuteCommandSyncResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.command_id is not None:
            body["command_id"] = self.command_id
        if self.exit_code is not None:
            body["exit_code"] = self.exit_code
        if self.status is not None:
            body["status"] = self.status.value
        if self.stderr is not None:
            body["stderr"] = self.stderr
        if self.stdout is not None:
            body["stdout"] = self.stdout
        if self.truncated is not None:
            body["truncated"] = self.truncated
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ExecuteCommandSyncResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.command_id is not None:
            body["command_id"] = self.command_id
        if self.exit_code is not None:
            body["exit_code"] = self.exit_code
        if self.status is not None:
            body["status"] = self.status
        if self.stderr is not None:
            body["stderr"] = self.stderr
        if self.stdout is not None:
            body["stdout"] = self.stdout
        if self.truncated is not None:
            body["truncated"] = self.truncated
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ExecuteCommandSyncResponse:
        """Deserializes the ExecuteCommandSyncResponse from a dictionary."""
        return cls(
            command_id=d.get("command_id", None),
            exit_code=d.get("exit_code", None),
            status=_enum(d, "status", ExecuteCommandStatus),
            stderr=d.get("stderr", None),
            stdout=d.get("stdout", None),
            truncated=d.get("truncated", None),
        )


@dataclass
class GetMetadataResponse:
    """Contains metadata for the requested path without following its final symlink."""

    file: Optional[SandboxFileInfo] = None

    def as_dict(self) -> dict:
        """Serializes the GetMetadataResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.file:
            body["file"] = self.file.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GetMetadataResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.file:
            body["file"] = self.file
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GetMetadataResponse:
        """Deserializes the GetMetadataResponse from a dictionary."""
        return cls(file=_from_dict(d, "file", SandboxFileInfo))


@dataclass
class ListCommandsResponse:
    """Response listing tracked command executions."""

    commands: Optional[List[Command]] = None
    """Commands in this page of results."""

    next_page_token: Optional[str] = None
    """Token to retrieve the next page. Empty when there are no more results."""

    def as_dict(self) -> dict:
        """Serializes the ListCommandsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.commands:
            body["commands"] = [v.as_dict() for v in self.commands]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListCommandsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.commands:
            body["commands"] = self.commands
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListCommandsResponse:
        """Deserializes the ListCommandsResponse from a dictionary."""
        return cls(commands=_repeated_dict(d, "commands", Command), next_page_token=d.get("next_page_token", None))


@dataclass
class ListDirectoryContentsResponse:
    """Contains a page of immediate directory entries and an optional continuation token. An empty
    token marks the final page. Pages reflect concurrent directory changes."""

    contents: Optional[List[SandboxFileInfo]] = None

    next_page_token: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the ListDirectoryContentsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.contents:
            body["contents"] = [v.as_dict() for v in self.contents]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListDirectoryContentsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.contents:
            body["contents"] = self.contents
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListDirectoryContentsResponse:
        """Deserializes the ListDirectoryContentsResponse from a dictionary."""
        return cls(
            contents=_repeated_dict(d, "contents", SandboxFileInfo), next_page_token=d.get("next_page_token", None)
        )


@dataclass
class ListSandboxesResponse:
    """A list of Sandboxes."""

    next_page_token: Optional[str] = None

    sandboxes: Optional[List[Sandbox]] = None

    def as_dict(self) -> dict:
        """Serializes the ListSandboxesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.sandboxes:
            body["sandboxes"] = [v.as_dict() for v in self.sandboxes]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListSandboxesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.sandboxes:
            body["sandboxes"] = self.sandboxes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListSandboxesResponse:
        """Deserializes the ListSandboxesResponse from a dictionary."""
        return cls(next_page_token=d.get("next_page_token", None), sandboxes=_repeated_dict(d, "sandboxes", Sandbox))


@dataclass
class RenamePathResponse:
    """Confirms that the sandbox path was renamed."""

    def as_dict(self) -> dict:
        """Serializes the RenamePathResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RenamePathResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RenamePathResponse:
        """Deserializes the RenamePathResponse from a dictionary."""
        return cls()


@dataclass
class Sandbox:
    """A Sandbox resource representing an execution environment."""

    create_time: Optional[Timestamp] = None
    """Output only. The creation time of the sandbox."""

    display_name: Optional[str] = None
    """Human-readable display label for the sandbox. At most 256 characters."""

    name: Optional[str] = None
    """The sandbox resource name, in the form ``sandboxes/{sandbox_id}``. Derived from ``sandbox_id``;
    any value supplied in a create or update request body is ignored."""

    spec: Optional[SandboxSpec] = None
    """The desired configuration of the sandbox, supplied by the caller at creation time."""

    status: Optional[SandboxStatus] = None
    """The observed runtime state of the sandbox, populated by the server."""

    update_time: Optional[Timestamp] = None
    """Output only. The last update time of the sandbox metadata and spec."""

    def as_dict(self) -> dict:
        """Serializes the Sandbox into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.name is not None:
            body["name"] = self.name
        if self.spec:
            body["spec"] = self.spec.as_dict()
        if self.status:
            body["status"] = self.status.as_dict()
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Sandbox into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.name is not None:
            body["name"] = self.name
        if self.spec:
            body["spec"] = self.spec
        if self.status:
            body["status"] = self.status
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Sandbox:
        """Deserializes the Sandbox from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            display_name=d.get("display_name", None),
            name=d.get("name", None),
            spec=_from_dict(d, "spec", SandboxSpec),
            status=_from_dict(d, "status", SandboxStatus),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class SandboxFileInfo:
    """Metadata for a sandbox filesystem entry, describing a final symlink itself."""

    file_type: Optional[SandboxFileType] = None

    group: Optional[str] = None

    mode: Optional[int] = None

    modify_time: Optional[Timestamp] = None
    """Nanosecond precision is preserved on the wire."""

    name: Optional[str] = None

    owner: Optional[str] = None

    path: Optional[str] = None

    permissions: Optional[str] = None

    size: Optional[int] = None

    symlink_target: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the SandboxFileInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.file_type is not None:
            body["file_type"] = self.file_type.value
        if self.group is not None:
            body["group"] = self.group
        if self.mode is not None:
            body["mode"] = self.mode
        if self.modify_time is not None:
            body["modify_time"] = self.modify_time.ToJsonString()
        if self.name is not None:
            body["name"] = self.name
        if self.owner is not None:
            body["owner"] = self.owner
        if self.path is not None:
            body["path"] = self.path
        if self.permissions is not None:
            body["permissions"] = self.permissions
        if self.size is not None:
            body["size"] = self.size
        if self.symlink_target is not None:
            body["symlink_target"] = self.symlink_target
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SandboxFileInfo into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.file_type is not None:
            body["file_type"] = self.file_type
        if self.group is not None:
            body["group"] = self.group
        if self.mode is not None:
            body["mode"] = self.mode
        if self.modify_time is not None:
            body["modify_time"] = self.modify_time
        if self.name is not None:
            body["name"] = self.name
        if self.owner is not None:
            body["owner"] = self.owner
        if self.path is not None:
            body["path"] = self.path
        if self.permissions is not None:
            body["permissions"] = self.permissions
        if self.size is not None:
            body["size"] = self.size
        if self.symlink_target is not None:
            body["symlink_target"] = self.symlink_target
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SandboxFileInfo:
        """Deserializes the SandboxFileInfo from a dictionary."""
        return cls(
            file_type=_enum(d, "file_type", SandboxFileType),
            group=d.get("group", None),
            mode=d.get("mode", None),
            modify_time=_timestamp(d, "modify_time"),
            name=d.get("name", None),
            owner=d.get("owner", None),
            path=d.get("path", None),
            permissions=d.get("permissions", None),
            size=_int64(d, "size"),
            symlink_target=d.get("symlink_target", None),
        )


class SandboxFileType(Enum):
    """Type of a sandbox filesystem entry without following its final symlink."""

    SANDBOX_FILE_TYPE_DIRECTORY = "SANDBOX_FILE_TYPE_DIRECTORY"
    SANDBOX_FILE_TYPE_FILE = "SANDBOX_FILE_TYPE_FILE"
    SANDBOX_FILE_TYPE_OTHER = "SANDBOX_FILE_TYPE_OTHER"
    SANDBOX_FILE_TYPE_SYMLINK = "SANDBOX_FILE_TYPE_SYMLINK"


@dataclass
class SandboxSpec:
    compute: Optional[ComputeSpec] = None
    """Compute configuration (size, inactivity timeout) requested for the sandbox."""

    environment: Optional[EnvironmentSpec] = None
    """The execution environment to use for the sandbox."""

    def as_dict(self) -> dict:
        """Serializes the SandboxSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.compute:
            body["compute"] = self.compute.as_dict()
        if self.environment:
            body["environment"] = self.environment.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SandboxSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.compute:
            body["compute"] = self.compute
        if self.environment:
            body["environment"] = self.environment
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SandboxSpec:
        """Deserializes the SandboxSpec from a dictionary."""
        return cls(
            compute=_from_dict(d, "compute", ComputeSpec), environment=_from_dict(d, "environment", EnvironmentSpec)
        )


class SandboxState(Enum):
    """Lifecycle state of a Sandbox resource. STOPPING is the transient state while the sandbox is
    being stopped -- by a Stop request or inactivity auto-termination -- and settles to STOPPED once
    the operation completes."""

    SANDBOX_STATE_PENDING = "SANDBOX_STATE_PENDING"
    SANDBOX_STATE_RUNNING = "SANDBOX_STATE_RUNNING"
    SANDBOX_STATE_STOPPED = "SANDBOX_STATE_STOPPED"
    SANDBOX_STATE_STOPPING = "SANDBOX_STATE_STOPPING"


@dataclass
class SandboxStatus:
    state: Optional[SandboxState] = None
    """Lifecycle state of the sandbox."""

    def as_dict(self) -> dict:
        """Serializes the SandboxStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.state is not None:
            body["state"] = self.state.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SandboxStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.state is not None:
            body["state"] = self.state
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SandboxStatus:
        """Deserializes the SandboxStatus from a dictionary."""
        return cls(state=_enum(d, "state", SandboxState))


class SandboxAPI:
    """Create, manage, and control the lifecycle of sandboxes -- isolated, pre-configured, low-latency Serverless
    compute environments for running code."""

    def __init__(self, api_client):
        self._api = api_client

    def create_directory(self, parent: str, path: str, *, parents: Optional[bool] = None) -> CreateDirectoryResponse:
        """Creates a directory in a sandbox, including missing parents by default.

        :param parent: str
        :param path: str
          Absolute UTF-8 path of the directory.
        :param parents: bool (optional)
          Defaults to true, which also succeeds when the directory already exists.

        :returns: :class:`CreateDirectoryResponse`
        """

        body = {}
        if parents is not None:
            body["parents"] = parents
        if path is not None:
            body["path"] = path
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/sandbox-files/{parent}/directories:make", body=body, headers=headers)
        return CreateDirectoryResponse.from_dict(res)

    def create_sandbox(self, sandbox: Sandbox, sandbox_id: str) -> Sandbox:
        """Creates a new Sandbox.

        :param sandbox: :class:`Sandbox`
          The sandbox to create.
        :param sandbox_id: str
          Client-supplied ID that becomes the final path segment of the resource name.

        :returns: :class:`Sandbox`
        """

        body = sandbox.as_dict()
        query = {}
        if sandbox_id is not None:
            query["sandbox_id"] = sandbox_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/sandboxes", query=query, body=body, headers=headers)
        return Sandbox.from_dict(res)

    def delete_path(self, parent: str, path: str, *, recursive: Optional[bool] = None) -> DeletePathResponse:
        """Deletes a file, symlink, or empty directory, with an option for recursive deletion. Succeeds if the
        path is already absent.

        :param parent: str
        :param path: str
          Absolute UTF-8 path of the entry to delete.
        :param recursive: bool (optional)
          Required for a non-empty directory.

        :returns: :class:`DeletePathResponse`
        """

        body = {}
        if path is not None:
            body["path"] = path
        if recursive is not None:
            body["recursive"] = recursive
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/sandbox-files/{parent}/paths:remove", body=body, headers=headers)
        return DeletePathResponse.from_dict(res)

    def delete_sandbox(self, name: str):
        """Deletes a Sandbox.

        :param name: str


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/{name}", headers=headers)

    def execute_command_sync(
        self,
        name: str,
        cmd: str,
        *,
        args: Optional[List[str]] = None,
        envs: Optional[Dict[str, str]] = None,
        execution_timeout: Optional[Duration] = None,
    ) -> ExecuteCommandSyncResponse:
        """Runs a command in the sandbox and blocks until it exits, returning the captured stdout, stderr and
        exit code in a single response.

        :param name: str
          Resource name of the sandbox to run the command in, in the form ``sandboxes/{sandbox_id}``. Bound
          from the URL path.
        :param cmd: str
          Executable or command to run (e.g. ``/bin/echo``, ``python3``).
        :param args: List[str] (optional)
          Arguments passed to ``cmd``.
        :param envs: Dict[str,str] (optional)
          Extra environment variables for the command's process, merged over the sandbox's default
          environment.
        :param execution_timeout: Duration (optional)
          Maximum time to wait for the command to finish. When it elapses the command is terminated and the
          response carries status ``TIMED_OUT``. The server applies a default when unset and clamps to an
          upper bound; negative or otherwise invalid durations are rejected with ``INVALID_ARGUMENT``.

        :returns: :class:`ExecuteCommandSyncResponse`
        """

        body = {}
        if args is not None:
            body["args"] = [v for v in args]
        if cmd is not None:
            body["cmd"] = cmd
        if envs is not None:
            body["envs"] = envs
        if execution_timeout is not None:
            body["execution_timeout"] = execution_timeout.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/sandbox-exec/{name}/exec-sync", body=body, headers=headers)
        return ExecuteCommandSyncResponse.from_dict(res)

    def get_metadata(self, parent: str, path: str) -> GetMetadataResponse:
        """Returns metadata for a path without following its final symlink.

        :param parent: str
        :param path: str
          Absolute UTF-8 path of the entry to inspect.

        :returns: :class:`GetMetadataResponse`
        """

        query = {}
        if path is not None:
            query["path"] = path
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/sandbox-files/{parent}/paths:describe", query=query, headers=headers)
        return GetMetadataResponse.from_dict(res)

    def get_sandbox(self, name: str) -> Sandbox:
        """Retrieves a Sandbox by name.

        :param name: str

        :returns: :class:`Sandbox`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/{name}", headers=headers)
        return Sandbox.from_dict(res)

    def list_commands(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> ListCommandsResponse:
        """Lists the tracked command executions (running and completed) in a sandbox.

        :param parent: str
          The sandbox whose commands to list, in the form ``sandboxes/{sandbox_id}``.
        :param page_size: int (optional)
          Maximum number of commands to return. The server may return fewer. If unspecified, the server
          returns all commands.
        :param page_token: str (optional)
          Page token returned by a previous ListCommands call. Use this to retrieve the next page of results.

        :returns: :class:`ListCommandsResponse`
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

        res = self._api.do("GET", f"/api/2.0/sandbox-exec/{parent}/commands", query=query, headers=headers)
        return ListCommandsResponse.from_dict(res)

    def list_directory_contents(
        self, parent: str, path: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[SandboxFileInfo]:
        """Lists a directory's immediate children in UTF-8 name order. Later pages may reflect concurrent
        changes.

        :param parent: str
        :param path: str
          Absolute UTF-8 path of the directory.
        :param page_size: int (optional)
          Zero uses the default of 1000; values above 1000 are clamped to 1000.
        :param page_token: str (optional)
          The token from a prior response. Keep parent and path unchanged between pages.

        :returns: Iterator over :class:`SandboxFileInfo`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        if path is not None:
            query["path"] = path
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do(
                "GET", f"/api/2.0/sandbox-files/{parent}/directory-entries", query=query, headers=headers
            )
            if "contents" in json:
                for v in json["contents"]:
                    yield SandboxFileInfo.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_sandboxes(self, *, page_size: Optional[int] = None, page_token: Optional[str] = None) -> Iterator[Sandbox]:
        """Lists all Sandboxes.

        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`Sandbox`
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
            json = self._api.do("GET", "/api/2.0/sandboxes", query=query, headers=headers)
            if "sandboxes" in json:
                for v in json["sandboxes"]:
                    yield Sandbox.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def rename_path(self, parent: str, source: str, destination: str) -> RenamePathResponse:
        """Renames a path within a sandbox. The destination must be absent and on the same filesystem.

        :param parent: str
          Sandbox resource name, for example ``sandboxes/my-sandbox``.
        :param source: str
          Absolute UTF-8 path to move.
        :param destination: str
          Exact absolute UTF-8 destination; it must not already exist.

        :returns: :class:`RenamePathResponse`
        """

        body = {}
        if destination is not None:
            body["destination"] = destination
        if source is not None:
            body["source"] = source
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/sandbox-files/{parent}/paths:rename", body=body, headers=headers)
        return RenamePathResponse.from_dict(res)

    def start_sandbox(self, name: str) -> Sandbox:
        """Starts a previously stopped Sandbox under the same sandbox name. Returns NOT_FOUND if there is no
        stopped sandbox to start for the given name.

        :param name: str
          Resource name of the sandbox to start, in the form ``sandboxes/{sandbox_id}``.

        :returns: :class:`Sandbox`
        """

        body = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/{name}/start", body=body, headers=headers)
        return Sandbox.from_dict(res)

    def stop_sandbox(self, name: str) -> Sandbox:
        """Stops a running Sandbox, preserving it so it can later be restarted with a Start request.

        :param name: str
          Resource name of the sandbox to stop, in the form ``sandboxes/{sandbox_id}``.

        :returns: :class:`Sandbox`
        """

        body = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/{name}/stop", body=body, headers=headers)
        return Sandbox.from_dict(res)

    def update_sandbox(self, name: str, sandbox: Sandbox, update_mask: FieldMask) -> Sandbox:
        """Updates mutable fields on an existing Sandbox. Allowlisted update_mask paths today: display_name,
        spec.compute.inactivity_timeout. Returns INVALID_PARAMETER_VALUE for empty masks or unknown paths;
        NOT_FOUND if the sandbox does not exist.

        :param name: str
          Resource name of the sandbox to update, in the form ``sandboxes/{sandbox_id}``.
        :param sandbox: :class:`Sandbox`
          The Sandbox resource carrying new field values. Only fields named in ``update_mask`` are read;
          unmasked fields are ignored.
        :param update_mask: FieldMask
          Field paths to update. Must be a non-empty subset of:

          - display_name
          - spec.compute.inactivity_timeout Any other path returns INVALID_PARAMETER_VALUE.

        :returns: :class:`Sandbox`
        """

        body = sandbox.as_dict()
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

        res = self._api.do("PATCH", f"/api/2.0/{name}", query=query, body=body, headers=headers)
        return Sandbox.from_dict(res)

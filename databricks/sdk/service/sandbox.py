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
    _repeated_dict,
    _timestamp,
)
from databricks.sdk.common.types.fieldmask import FieldMask


_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


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
class Sandbox:
    """A Sandbox resource representing an execution environment."""

    create_time: Optional[Timestamp] = None
    """Output only. The creation time of the sandbox."""

    display_name: Optional[str] = None
    """Customer-supplied display label. Mutable via UpdateSandbox. Bounds enforced at the RPC boundary
    (<=256 bytes, mirrors lakebox MAX_SANDBOX_NAME_LEN)."""

    name: Optional[str] = None
    """The AIP-compliant resource name, such as "sandboxes/my-sandbox"."""

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
class SandboxSpec:
    compute: Optional[ComputeSpec] = None
    """Compute configuration (size, inactivity timeout) requested for the sandbox."""

    def as_dict(self) -> dict:
        """Serializes the SandboxSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.compute:
            body["compute"] = self.compute.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SandboxSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.compute:
            body["compute"] = self.compute
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SandboxSpec:
        """Deserializes the SandboxSpec from a dictionary."""
        return cls(compute=_from_dict(d, "compute", ComputeSpec))


class SandboxState(Enum):
    """Lifecycle state of a Sandbox resource. STOPPING is the transient state surfaced while a teardown
    (Stop, DeleteSandbox, auto-terminate, provisioning failure) is in flight but the sandbox row
    still exists; the row settles to STOPPED once the workflow finishes."""

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

    def start_sandbox(self, name: str) -> Sandbox:
        """Starts a stopped Sandbox by atomically restoring the TerminatedSandbox tombstone to the active table
        in PENDING and re-running the provisioning workflow. The provisioning workflow's claimWarmPoolSandbox
        step re-mints the app_instance_name (deterministic from sandbox_id, so equal to the prior life's
        name). The tombstone's volume_id is preserved so the new AppInstance binds to the same backing device
        file. The restored sandbox gets a fresh uid and create_time. Returns NOT_FOUND if no tombstone exists
        for the given (workspace_id, sandbox_id) — the sandbox may not exist or may currently be active;
        clients can disambiguate via Get.

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
        """Stops a Sandbox, terminating the sandbox while allowing future use of StartSandbox to re-provision the
        same Sandbox without re-creating a brand new one. Transitions the active row to TERMINATING with
        USER_REQUEST_STOP; the termination workflow settles to a TerminatedSandbox tombstone (no row drop) so
        the sandbox can later be restarted via StartSandbox.

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
        """Updates mutable fields on an existing Sandbox. Allowlisted update_mask paths today:
        metadata.display_name, spec.compute.inactivity_timeout. Returns INVALID_PARAMETER_VALUE for empty
        masks or unknown paths; NOT_FOUND if no active row or tombstone exists for the given sandbox.
        Concurrent-update conflicts surface as ABORTED via EStore OccConflict.

        :param name: str
          Resource name of the sandbox to update, in the form ``sandboxes/{sandbox_id}``.
        :param sandbox: :class:`Sandbox`
          The Sandbox resource carrying new field values. Only fields named in ``update_mask`` are read;
          unmasked fields are ignored.
        :param update_mask: FieldMask
          Field paths to update. Must be a non-empty subset of:

          - metadata.display_name
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

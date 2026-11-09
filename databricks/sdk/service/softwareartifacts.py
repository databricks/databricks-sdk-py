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
    _repeated_dict,
    _timestamp,
)
from databricks.sdk.common.types.fieldmask import FieldMask


_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class ImageAccelerationDetail:
    """Image acceleration information for a software artifact version."""

    status: Optional[ImageAccelerationDetailStatus] = None
    """Image acceleration status for the version."""

    def as_dict(self) -> dict:
        """Serializes the ImageAccelerationDetail into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.status is not None:
            body["status"] = self.status.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ImageAccelerationDetail into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.status is not None:
            body["status"] = self.status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ImageAccelerationDetail:
        """Deserializes the ImageAccelerationDetail from a dictionary."""
        return cls(status=_enum(d, "status", ImageAccelerationDetailStatus))


class ImageAccelerationDetailStatus(Enum):
    """Image acceleration status for a software artifact version."""

    SUCCESS = "SUCCESS"
    UNSPECIFIED = "UNSPECIFIED"


@dataclass
class ListSoftwareArtifactVersionsResponse:
    """Response containing a page of software artifact versions."""

    next_page_token: Optional[str] = None
    """Opaque token to pass as the next request's page_token. Empty when there are no more pages."""

    software_artifact_versions: Optional[List[SoftwareArtifactVersion]] = None
    """The versions of the requested software artifact."""

    def as_dict(self) -> dict:
        """Serializes the ListSoftwareArtifactVersionsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.software_artifact_versions:
            body["software_artifact_versions"] = [v.as_dict() for v in self.software_artifact_versions]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListSoftwareArtifactVersionsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.software_artifact_versions:
            body["software_artifact_versions"] = self.software_artifact_versions
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListSoftwareArtifactVersionsResponse:
        """Deserializes the ListSoftwareArtifactVersionsResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            software_artifact_versions=_repeated_dict(d, "software_artifact_versions", SoftwareArtifactVersion),
        )


@dataclass
class ListSoftwareArtifactsResponse:
    """Response containing a page of software artifacts."""

    next_page_token: Optional[str] = None
    """Opaque token to pass as the next request's page_token. Empty when there are no more pages."""

    software_artifacts: Optional[List[SoftwareArtifact]] = None
    """The software artifacts under the requested schema."""

    def as_dict(self) -> dict:
        """Serializes the ListSoftwareArtifactsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.software_artifacts:
            body["software_artifacts"] = [v.as_dict() for v in self.software_artifacts]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListSoftwareArtifactsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.software_artifacts:
            body["software_artifacts"] = self.software_artifacts
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListSoftwareArtifactsResponse:
        """Deserializes the ListSoftwareArtifactsResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            software_artifacts=_repeated_dict(d, "software_artifacts", SoftwareArtifact),
        )


@dataclass
class ResolveSoftwareArtifactVersionResponse:
    """Response containing the resolved software artifact version."""

    software_artifact_version: Optional[SoftwareArtifactVersion] = None
    """The software artifact version selected by the alias."""

    def as_dict(self) -> dict:
        """Serializes the ResolveSoftwareArtifactVersionResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.software_artifact_version:
            body["software_artifact_version"] = self.software_artifact_version.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ResolveSoftwareArtifactVersionResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.software_artifact_version:
            body["software_artifact_version"] = self.software_artifact_version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ResolveSoftwareArtifactVersionResponse:
        """Deserializes the ResolveSoftwareArtifactVersionResponse from a dictionary."""
        return cls(software_artifact_version=_from_dict(d, "software_artifact_version", SoftwareArtifactVersion))


@dataclass
class SoftwareArtifact:
    """A software artifact in a Unity Catalog schema."""

    create_time: Optional[Timestamp] = None
    """Time at which this software artifact was created."""

    created_by: Optional[str] = None
    """Principal name of the software artifact creator."""

    name: Optional[str] = None
    """Resource name of the artifact, of the form ``software-artifacts/{catalog}.{schema}.{artifact}``."""

    owner: Optional[str] = None
    """Principal name (a user, service principal, or group) that owns this artifact."""

    update_time: Optional[Timestamp] = None
    """Time at which this software artifact was last updated."""

    updated_by: Optional[str] = None
    """Principal name that last updated this software artifact."""

    def as_dict(self) -> dict:
        """Serializes the SoftwareArtifact into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.created_by is not None:
            body["created_by"] = self.created_by
        if self.name is not None:
            body["name"] = self.name
        if self.owner is not None:
            body["owner"] = self.owner
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        if self.updated_by is not None:
            body["updated_by"] = self.updated_by
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SoftwareArtifact into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.created_by is not None:
            body["created_by"] = self.created_by
        if self.name is not None:
            body["name"] = self.name
        if self.owner is not None:
            body["owner"] = self.owner
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.updated_by is not None:
            body["updated_by"] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SoftwareArtifact:
        """Deserializes the SoftwareArtifact from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            created_by=d.get("created_by", None),
            name=d.get("name", None),
            owner=d.get("owner", None),
            update_time=_timestamp(d, "update_time"),
            updated_by=d.get("updated_by", None),
        )


@dataclass
class SoftwareArtifactVersion:
    """An immutable version of a software artifact, identified by its content digest."""

    create_time: Optional[Timestamp] = None
    """Time at which this software artifact version was created."""

    created_by: Optional[str] = None
    """Principal name of the software artifact version creator."""

    digest: Optional[str] = None
    """Content digest of the version, for example ``sha256:...``."""

    image_acceleration_details: Optional[ImageAccelerationDetail] = None
    """Image acceleration information for this version."""

    name: Optional[str] = None
    """Resource name of the version, of the form
    ``software-artifacts/{catalog}.{schema}.{artifact}/versions/{version}``."""

    tags: Optional[List[str]] = None
    """Tags (aliases) that currently point at this version, for example ``latest`` or ``v1.2.3``.
    Bounded at 10 per version; a version pointed at by more tags returns an arbitrary 10 of them."""

    update_time: Optional[Timestamp] = None
    """Time at which this software artifact version was last updated."""

    updated_by: Optional[str] = None
    """Principal name that last updated this software artifact version."""

    def as_dict(self) -> dict:
        """Serializes the SoftwareArtifactVersion into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.created_by is not None:
            body["created_by"] = self.created_by
        if self.digest is not None:
            body["digest"] = self.digest
        if self.image_acceleration_details:
            body["image_acceleration_details"] = self.image_acceleration_details.as_dict()
        if self.name is not None:
            body["name"] = self.name
        if self.tags:
            body["tags"] = [v for v in self.tags]
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        if self.updated_by is not None:
            body["updated_by"] = self.updated_by
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SoftwareArtifactVersion into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.created_by is not None:
            body["created_by"] = self.created_by
        if self.digest is not None:
            body["digest"] = self.digest
        if self.image_acceleration_details:
            body["image_acceleration_details"] = self.image_acceleration_details
        if self.name is not None:
            body["name"] = self.name
        if self.tags:
            body["tags"] = self.tags
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.updated_by is not None:
            body["updated_by"] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SoftwareArtifactVersion:
        """Deserializes the SoftwareArtifactVersion from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            created_by=d.get("created_by", None),
            digest=d.get("digest", None),
            image_acceleration_details=_from_dict(d, "image_acceleration_details", ImageAccelerationDetail),
            name=d.get("name", None),
            tags=d.get("tags", None),
            update_time=_timestamp(d, "update_time"),
            updated_by=d.get("updated_by", None),
        )


class SoftwareArtifactsAPI:
    """Manage software artifacts and their versions in Unity Catalog."""

    def __init__(self, api_client):
        self._api = api_client

    def get_software_artifact(self, name: str) -> SoftwareArtifact:
        """Gets a software artifact.

        :param name: str
          Resource name of the artifact, of the form ``software-artifacts/{catalog}.{schema}.{artifact}``.

        :returns: :class:`SoftwareArtifact`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.1/unity-catalog/{name}", headers=headers)
        return SoftwareArtifact.from_dict(res)

    def get_software_artifact_version(self, name: str) -> SoftwareArtifactVersion:
        """Gets a software artifact version.

        :param name: str
          Resource name of the version, of the form
          ``software-artifacts/{catalog}.{schema}.{artifact}/versions/{version}``.

        :returns: :class:`SoftwareArtifactVersion`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.1/unity-catalog/{name}", headers=headers)
        return SoftwareArtifactVersion.from_dict(res)

    def list_software_artifact_versions(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[SoftwareArtifactVersion]:
        """Lists the versions of a software artifact.

        :param parent: str
          Resource name of the parent artifact, of the form
          ``software-artifacts/{catalog}.{schema}.{artifact}``.
        :param page_size: int (optional)
          Maximum number of versions to return. If omitted or set to 0, the page size defaults to 50. The
          maximum value is 50; values above 50 or below 0 are rejected.
        :param page_token: str (optional)
          Opaque continuation token from a previous response's next_page_token. Omit for the first page.

        :returns: Iterator over :class:`SoftwareArtifactVersion`
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
            json = self._api.do("GET", f"/api/2.1/unity-catalog/{parent}/versions", query=query, headers=headers)
            if "software_artifact_versions" in json:
                for v in json["software_artifact_versions"]:
                    yield SoftwareArtifactVersion.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_software_artifacts(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[SoftwareArtifact]:
        """Lists software artifacts in a schema.

        :param parent: str
          Resource name of the parent schema, of the form ``schemas/{catalog}.{schema}``.
        :param page_size: int (optional)
          Maximum number of software artifacts to return. If omitted or set to 0, the page size defaults to
          50. The maximum value is 50; values above 50 or below 0 are rejected.
        :param page_token: str (optional)
          Opaque continuation token from a previous response's next_page_token. Omit for the first page.

        :returns: Iterator over :class:`SoftwareArtifact`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        if parent is not None:
            query["parent"] = parent
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", "/api/2.1/unity-catalog/software-artifacts", query=query, headers=headers)
            if "software_artifacts" in json:
                for v in json["software_artifacts"]:
                    yield SoftwareArtifact.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def resolve_software_artifact_version(self, parent: str, alias: str) -> ResolveSoftwareArtifactVersionResponse:
        """Resolves a software artifact version from its tag alias.

        :param parent: str
          Resource name of the software artifact containing the alias.
        :param alias: str
          Image tag alias selecting the version.

        :returns: :class:`ResolveSoftwareArtifactVersionResponse`
        """

        body = {}
        if alias is not None:
            body["alias"] = alias
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.1/unity-catalog/{parent}/versions:resolve", body=body, headers=headers)
        return ResolveSoftwareArtifactVersionResponse.from_dict(res)

    def update_software_artifact(
        self, name: str, software_artifact: SoftwareArtifact, update_mask: FieldMask
    ) -> SoftwareArtifact:
        """Updates a software artifact. The name is immutable; only the owner may be changed. The destination
        owner must exist in the account. The caller needs MANAGE_ACCESS_CONTROL on the artifact. The response
        contains its name and the requested owner; audit fields are omitted.

        :param name: str
          Resource name of the artifact, of the form ``software-artifacts/{catalog}.{schema}.{artifact}``.
        :param software_artifact: :class:`SoftwareArtifact`
          The software artifact to update. Its name identifies the existing artifact; only owner may be
          changed.
        :param update_mask: FieldMask
          Fields to update, relative to ``software_artifact``. Accepts ``owner`` or ``*``; owner is the only
          mutable field, so both select the same update. Output-only values in the resource are ignored.

        :returns: :class:`SoftwareArtifact`
        """

        body = software_artifact.as_dict()
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

        res = self._api.do("PATCH", f"/api/2.1/unity-catalog/{name}", query=query, body=body, headers=headers)
        return SoftwareArtifact.from_dict(res)

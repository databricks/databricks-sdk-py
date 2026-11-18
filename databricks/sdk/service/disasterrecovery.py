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


class FailoverFailoverGroupRequestFailoverType(Enum):
    """The type of failover to perform."""

    FORCED = "FORCED"


@dataclass
class FailoverGroup:
    """A failover group manages Databricks Managed Disaster Recovery for a pair of workspaces in two
    regions. It continuously replicates the selected Unity Catalog catalogs and workspace assets
    from the primary region to the secondary region and lets you fail over to the secondary region;
    at least one of the two replication types must be enabled. See
    https://docs.databricks.com/aws/en/admin/managed-disaster-recovery for the product
    documentation."""

    regions: List[str]
    """The two cloud regions that participate in this failover group, the primary and the secondary.
    Each workspace set contains one workspace in each region."""

    workspace_sets: List[WorkspaceSet]
    """Workspace sets, each containing workspaces that replicate to each other. A failover group
    currently supports exactly one workspace set."""

    initial_primary_region: str
    """Initial primary region. Used only in Create requests to set the starting primary region, and
    must be one of the regions in ``regions``. Not returned in responses."""

    create_time: Optional[Timestamp] = None
    """Time at which this failover group was created."""

    effective_primary_region: Optional[str] = None
    """Current effective primary region. Replication flows FROM workspaces in this region. Changes
    after a successful failover."""

    etag: Optional[str] = None
    """Opaque version string for optimistic locking. Server-generated and returned in responses."""

    has_replication_point_blocking_errors: Optional[bool] = None
    """True when replication errors are preventing the replication point from advancing. Populated only
    while the failover group is INITIAL_REPLICATION or ACTIVE; the blocking errors are listed in the
    system.replication.states system table."""

    initial_replication_progress: Optional[InitialReplicationProgress] = None
    """Initial replication progress of all in-scope assets. Set only when the FailoverGroup is in
    INITIAL_REPLICATION state."""

    name: Optional[str] = None
    """Fully qualified resource name in the format
    accounts/{account_id}/failover-groups/{failover_group_id}."""

    replication_point: Optional[Timestamp] = None
    """The most recent point in time up to which all in-scope assets have been replicated to the
    secondary region. Data written after this point might not exist in the secondary yet and can be
    lost in an unplanned failover. When both Unity Catalog and workspace assets are replicated, this
    is the older of the two replication points. Not populated until the first replication point
    exists, and not populated in ListFailoverGroups responses."""

    state: Optional[FailoverGroupState] = None
    """Aggregate state of the failover group across Unity Catalog and workspace asset replication. The
    group is INITIAL_REPLICATION until it has a replication point, ACTIVE while replication is in
    steady state and failover is available, and FAILING_OVER while a failover is in progress; the
    ``*_FAILED`` values mean that the last operation did not complete. Not populated in
    ListFailoverGroups responses."""

    unity_catalog_assets: Optional[UcReplicationConfig] = None
    """Unity Catalog replication configuration: the catalogs to replicate and the storage location
    mappings for their data. Omit it to replicate workspace assets only."""

    update_time: Optional[Timestamp] = None
    """Time at which this failover group was last modified."""

    def as_dict(self) -> dict:
        """Serializes the FailoverGroup into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.effective_primary_region is not None:
            body["effective_primary_region"] = self.effective_primary_region
        if self.etag is not None:
            body["etag"] = self.etag
        if self.has_replication_point_blocking_errors is not None:
            body["has_replication_point_blocking_errors"] = self.has_replication_point_blocking_errors
        if self.initial_primary_region is not None:
            body["initial_primary_region"] = self.initial_primary_region
        if self.initial_replication_progress:
            body["initial_replication_progress"] = self.initial_replication_progress.as_dict()
        if self.name is not None:
            body["name"] = self.name
        if self.regions:
            body["regions"] = [v for v in self.regions]
        if self.replication_point is not None:
            body["replication_point"] = self.replication_point.ToJsonString()
        if self.state is not None:
            body["state"] = self.state.value
        if self.unity_catalog_assets:
            body["unity_catalog_assets"] = self.unity_catalog_assets.as_dict()
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        if self.workspace_sets:
            body["workspace_sets"] = [v.as_dict() for v in self.workspace_sets]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the FailoverGroup into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.effective_primary_region is not None:
            body["effective_primary_region"] = self.effective_primary_region
        if self.etag is not None:
            body["etag"] = self.etag
        if self.has_replication_point_blocking_errors is not None:
            body["has_replication_point_blocking_errors"] = self.has_replication_point_blocking_errors
        if self.initial_primary_region is not None:
            body["initial_primary_region"] = self.initial_primary_region
        if self.initial_replication_progress:
            body["initial_replication_progress"] = self.initial_replication_progress
        if self.name is not None:
            body["name"] = self.name
        if self.regions:
            body["regions"] = self.regions
        if self.replication_point is not None:
            body["replication_point"] = self.replication_point
        if self.state is not None:
            body["state"] = self.state
        if self.unity_catalog_assets:
            body["unity_catalog_assets"] = self.unity_catalog_assets
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.workspace_sets:
            body["workspace_sets"] = self.workspace_sets
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> FailoverGroup:
        """Deserializes the FailoverGroup from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            effective_primary_region=d.get("effective_primary_region", None),
            etag=d.get("etag", None),
            has_replication_point_blocking_errors=d.get("has_replication_point_blocking_errors", None),
            initial_primary_region=d.get("initial_primary_region", None),
            initial_replication_progress=_from_dict(d, "initial_replication_progress", InitialReplicationProgress),
            name=d.get("name", None),
            regions=d.get("regions", None),
            replication_point=_timestamp(d, "replication_point"),
            state=_enum(d, "state", FailoverGroupState),
            unity_catalog_assets=_from_dict(d, "unity_catalog_assets", UcReplicationConfig),
            update_time=_timestamp(d, "update_time"),
            workspace_sets=_repeated_dict(d, "workspace_sets", WorkspaceSet),
        )


class FailoverGroupState(Enum):
    """The aggregate state of a FailoverGroup."""

    ACTIVE = "ACTIVE"
    CREATING = "CREATING"
    CREATION_FAILED = "CREATION_FAILED"
    DELETING = "DELETING"
    DELETION_FAILED = "DELETION_FAILED"
    FAILING_OVER = "FAILING_OVER"
    FAILOVER_FAILED = "FAILOVER_FAILED"
    INITIAL_REPLICATION = "INITIAL_REPLICATION"


@dataclass
class InitialReplicationProgress:
    """Progress of the initial replication of all in-scope assets (Unity Catalog and workspace assets)
    of a FailoverGroup. Populated only while the FailoverGroup is in INITIAL_REPLICATION."""

    completed: Optional[int] = None
    """Percentage of in-scope assets replicated so far, from 0 to 100. Stays below 100 while errors
    block the first replication point."""

    def as_dict(self) -> dict:
        """Serializes the InitialReplicationProgress into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.completed is not None:
            body["completed"] = self.completed
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the InitialReplicationProgress into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.completed is not None:
            body["completed"] = self.completed
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> InitialReplicationProgress:
        """Deserializes the InitialReplicationProgress from a dictionary."""
        return cls(completed=d.get("completed", None))


@dataclass
class ListFailoverGroupsResponse:
    """Response for listing failover groups."""

    failover_groups: Optional[List[FailoverGroup]] = None
    """The failover groups for this account."""

    next_page_token: Optional[str] = None
    """A token that can be sent as page_token to retrieve the next page. If omitted, there are no
    subsequent pages."""

    def as_dict(self) -> dict:
        """Serializes the ListFailoverGroupsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.failover_groups:
            body["failover_groups"] = [v.as_dict() for v in self.failover_groups]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListFailoverGroupsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.failover_groups:
            body["failover_groups"] = self.failover_groups
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListFailoverGroupsResponse:
        """Deserializes the ListFailoverGroupsResponse from a dictionary."""
        return cls(
            failover_groups=_repeated_dict(d, "failover_groups", FailoverGroup),
            next_page_token=d.get("next_page_token", None),
        )


@dataclass
class ListStableUrlsResponse:
    """Response for listing stable URLs."""

    next_page_token: Optional[str] = None
    """A token that can be sent as page_token to retrieve the next page. If omitted, there are no
    subsequent pages."""

    stable_urls: Optional[List[StableUrl]] = None
    """The stable URLs for this account."""

    def as_dict(self) -> dict:
        """Serializes the ListStableUrlsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.stable_urls:
            body["stable_urls"] = [v.as_dict() for v in self.stable_urls]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListStableUrlsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.stable_urls:
            body["stable_urls"] = self.stable_urls
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListStableUrlsResponse:
        """Deserializes the ListStableUrlsResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None), stable_urls=_repeated_dict(d, "stable_urls", StableUrl)
        )


@dataclass
class LocationMapping:
    """A location mapping identified by a name, with URIs per region. The system derives replication
    direction from effective_primary_region."""

    name: str
    """Identifier of this location mapping, unique within the failover group."""

    uri_by_region: List[LocationMappingEntry]
    """The storage URI of this location in each region, with exactly one entry per region of the
    failover group."""

    def as_dict(self) -> dict:
        """Serializes the LocationMapping into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.uri_by_region:
            body["uri_by_region"] = [v.as_dict() for v in self.uri_by_region]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the LocationMapping into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.uri_by_region:
            body["uri_by_region"] = self.uri_by_region
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> LocationMapping:
        """Deserializes the LocationMapping from a dictionary."""
        return cls(name=d.get("name", None), uri_by_region=_repeated_dict(d, "uri_by_region", LocationMappingEntry))


@dataclass
class LocationMappingEntry:
    """A single entry in a location mapping, mapping a region to a storage URI. Used instead of
    map<string, string> for proto2 compatibility."""

    region: str
    """Cloud region this URI applies to. Must be one of the failover group's regions."""

    uri: str
    """Cloud storage URI of the location in this region. End the URI with ``/*`` to map every path
    under it as a prefix; within one mapping, either all URIs or none carry the ``/*`` suffix."""

    def as_dict(self) -> dict:
        """Serializes the LocationMappingEntry into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.region is not None:
            body["region"] = self.region
        if self.uri is not None:
            body["uri"] = self.uri
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the LocationMappingEntry into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.region is not None:
            body["region"] = self.region
        if self.uri is not None:
            body["uri"] = self.uri
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> LocationMappingEntry:
        """Deserializes the LocationMappingEntry from a dictionary."""
        return cls(region=d.get("region", None), uri=d.get("uri", None))


@dataclass
class StableUrl:
    """A stable URL provides a failover-aware endpoint for accessing a workspace. Its lifecycle is
    independent of any failover group."""

    initial_workspace_id: str
    """The workspace this stable URL is initially bound to. Used only in Create requests to associate
    the stable URL with a workspace. Not returned in responses."""

    effective_workspace_id: Optional[str] = None
    """The workspace this stable URL currently routes to. Set to ``initial_workspace_id`` at creation,
    advanced to the failover group's primary while attached (including across a failover), and
    preserved when the stable URL is detached from its failover group. Read this to see where an
    unattached stable URL points: after a failover followed by a detach it reflects the
    post-failover primary, not ``initial_workspace_id``."""

    failover_group_name: Optional[str] = None
    """Fully qualified resource name of the FailoverGroup this stable URL is currently linked to, in
    the format ``accounts/{account_id}/failover-groups/{failover_group_id}``. Empty when the stable
    URL is not attached to any failover group."""

    name: Optional[str] = None
    """Fully qualified resource name. Format: accounts/{account_id}/stable-urls/{stable_url_id}."""

    stable_workspace_id: Optional[str] = None
    """The stable workspace ID for this stable URL. Generated on creation and immutable thereafter;
    identifies the URL across failovers and is the same value embedded in the ``url`` (as the ``w=``
    query parameter for SPOG URLs, or in the ``conn-<id>`` hostname for Private-Link URLs)."""

    url: Optional[str] = None
    """The stable URL endpoint. Generated on creation and immutable thereafter. For non-Private-Link
    workspaces this is ``https://<spog_host>/?w=<connection_id>``. For Private-Link workspaces this
    is the per-connection hostname."""

    def as_dict(self) -> dict:
        """Serializes the StableUrl into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.effective_workspace_id is not None:
            body["effective_workspace_id"] = self.effective_workspace_id
        if self.failover_group_name is not None:
            body["failover_group_name"] = self.failover_group_name
        if self.initial_workspace_id is not None:
            body["initial_workspace_id"] = self.initial_workspace_id
        if self.name is not None:
            body["name"] = self.name
        if self.stable_workspace_id is not None:
            body["stable_workspace_id"] = self.stable_workspace_id
        if self.url is not None:
            body["url"] = self.url
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the StableUrl into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.effective_workspace_id is not None:
            body["effective_workspace_id"] = self.effective_workspace_id
        if self.failover_group_name is not None:
            body["failover_group_name"] = self.failover_group_name
        if self.initial_workspace_id is not None:
            body["initial_workspace_id"] = self.initial_workspace_id
        if self.name is not None:
            body["name"] = self.name
        if self.stable_workspace_id is not None:
            body["stable_workspace_id"] = self.stable_workspace_id
        if self.url is not None:
            body["url"] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> StableUrl:
        """Deserializes the StableUrl from a dictionary."""
        return cls(
            effective_workspace_id=d.get("effective_workspace_id", None),
            failover_group_name=d.get("failover_group_name", None),
            initial_workspace_id=d.get("initial_workspace_id", None),
            name=d.get("name", None),
            stable_workspace_id=d.get("stable_workspace_id", None),
            url=d.get("url", None),
        )


@dataclass
class UcCatalog:
    """A Unity Catalog catalog to replicate."""

    name: str
    """Name of the Unity Catalog catalog to replicate."""

    def as_dict(self) -> dict:
        """Serializes the UcCatalog into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the UcCatalog into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> UcCatalog:
        """Deserializes the UcCatalog from a dictionary."""
        return cls(name=d.get("name", None))


@dataclass
class UcReplicationConfig:
    """Unity Catalog replication configuration (top-level, not per-set)."""

    catalogs: List[UcCatalog]
    """Unity Catalog catalogs to replicate, including their metadata and managed table data. Adding a
    catalog to an existing failover group returns the group to INITIAL_REPLICATION until the catalog
    has been replicated."""

    data_replication_workspace_set: str
    """Name of the workspace set whose workspaces run the data replication for the catalogs' underlying
    storage. Must match the name of a workspace set in this failover group."""

    location_mappings: Optional[List[LocationMapping]] = None
    """Storage location mappings. Each mapping pairs a storage path used by the replicated catalogs in
    one region with the corresponding path in the other region, so that replicated data is written
    to the matching storage in the secondary region."""

    def as_dict(self) -> dict:
        """Serializes the UcReplicationConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.catalogs:
            body["catalogs"] = [v.as_dict() for v in self.catalogs]
        if self.data_replication_workspace_set is not None:
            body["data_replication_workspace_set"] = self.data_replication_workspace_set
        if self.location_mappings:
            body["location_mappings"] = [v.as_dict() for v in self.location_mappings]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the UcReplicationConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.catalogs:
            body["catalogs"] = self.catalogs
        if self.data_replication_workspace_set is not None:
            body["data_replication_workspace_set"] = self.data_replication_workspace_set
        if self.location_mappings:
            body["location_mappings"] = self.location_mappings
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> UcReplicationConfig:
        """Deserializes the UcReplicationConfig from a dictionary."""
        return cls(
            catalogs=_repeated_dict(d, "catalogs", UcCatalog),
            data_replication_workspace_set=d.get("data_replication_workspace_set", None),
            location_mappings=_repeated_dict(d, "location_mappings", LocationMapping),
        )


@dataclass
class WorkspaceSet:
    """A set of workspaces that replicate to each other across regions."""

    name: str
    """Identifier of the workspace set, unique within the failover group and referenced by
    unity_catalog_assets.data_replication_workspace_set. Cannot be changed after creation."""

    workspace_ids: List[str]
    """IDs of the two workspaces in this set, one in each of the failover group's regions. The system
    derives and validates each workspace's region. Both workspaces must belong to the account and
    have the Mission Critical add-on enabled, and they cannot be changed after creation."""

    replicate_workspace_assets: Optional[bool] = None
    """Whether to replicate workspace assets (notebooks, jobs, clusters, SQL warehouses and so on) and
    their ACLs for this set. Defaults to false. Can be turned on or off with UpdateFailoverGroup."""

    stable_url_names: Optional[List[str]] = None
    """Resource names of stable URLs associated with this workspace set. Format:
    accounts/{account_id}/stable-urls/{stable_url_id}. The referenced stable URLs must already exist
    (via CreateStableUrl), and the list can only be set when replicate_workspace_assets is true.
    While workspace asset replication stays enabled, an update can attach or detach one stable URL
    at a time."""

    def as_dict(self) -> dict:
        """Serializes the WorkspaceSet into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.replicate_workspace_assets is not None:
            body["replicate_workspace_assets"] = self.replicate_workspace_assets
        if self.stable_url_names:
            body["stable_url_names"] = [v for v in self.stable_url_names]
        if self.workspace_ids:
            body["workspace_ids"] = [v for v in self.workspace_ids]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the WorkspaceSet into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.replicate_workspace_assets is not None:
            body["replicate_workspace_assets"] = self.replicate_workspace_assets
        if self.stable_url_names:
            body["stable_url_names"] = self.stable_url_names
        if self.workspace_ids:
            body["workspace_ids"] = self.workspace_ids
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> WorkspaceSet:
        """Deserializes the WorkspaceSet from a dictionary."""
        return cls(
            name=d.get("name", None),
            replicate_workspace_assets=d.get("replicate_workspace_assets", None),
            stable_url_names=d.get("stable_url_names", None),
            workspace_ids=d.get("workspace_ids", None),
        )


class DisasterRecoveryAPI:
    """Manage disaster recovery configurations and execute failover operations."""

    def __init__(self, api_client):
        self._api = api_client

    def create_failover_group(
        self,
        parent: str,
        failover_group: FailoverGroup,
        failover_group_id: str,
        *,
        validate_only: Optional[bool] = None,
    ) -> FailoverGroup:
        """Create a failover group. The group starts in the CREATING state and moves to INITIAL_REPLICATION while
        the first replication cycle copies all in-scope data to the secondary region; failover becomes
        available once the group is ACTIVE. Set validate_only to check the request without creating anything.

        :param parent: str
          The parent resource. Format: accounts/{account_id}.
        :param failover_group: :class:`FailoverGroup`
          The failover group to create.
        :param failover_group_id: str
          Client-provided identifier for the failover group. Used to construct the resource name as
          {parent}/failover-groups/{failover_group_id}.
        :param validate_only: bool (optional)
          When true, validates the request without creating the failover group.

        :returns: :class:`FailoverGroup`
        """

        body = failover_group.as_dict()
        query = {}
        if failover_group_id is not None:
            query["failover_group_id"] = failover_group_id
        if validate_only is not None:
            query["validate_only"] = validate_only
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST", f"/api/disaster-recovery/v1/{parent}/failover-groups", query=query, body=body, headers=headers
        )
        return FailoverGroup.from_dict(res)

    def create_stable_url(
        self, parent: str, stable_url: StableUrl, stable_url_id: str, *, validate_only: Optional[bool] = None
    ) -> StableUrl:
        """Create a new stable URL.

        :param parent: str
          The parent resource. Format: accounts/{account_id}.
        :param stable_url: :class:`StableUrl`
          The stable URL to create.
        :param stable_url_id: str
          Client-provided identifier for the stable URL. Used to construct the resource name as
          {parent}/stable-urls/{stable_url_id}.
        :param validate_only: bool (optional)
          When true, validates the request without creating the stable URL.

        :returns: :class:`StableUrl`
        """

        body = stable_url.as_dict()
        query = {}
        if stable_url_id is not None:
            query["stable_url_id"] = stable_url_id
        if validate_only is not None:
            query["validate_only"] = validate_only
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST", f"/api/disaster-recovery/v1/{parent}/stable-urls", query=query, body=body, headers=headers
        )
        return StableUrl.from_dict(res)

    def delete_failover_group(self, name: str, *, etag: Optional[str] = None):
        """Delete a failover group. Deleting stops replication for the group; stable URLs linked to it are
        detached but not deleted.

        :param name: str
          The fully qualified resource name of the failover group to delete. Format:
          accounts/{account_id}/failover-groups/{failover_group_id}.
        :param etag: str (optional)
          Opaque version string for optimistic locking. If provided, must match the current etag. If omitted,
          the delete proceeds without an etag check.


        """

        query = {}
        if etag is not None:
            query["etag"] = etag
        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/disaster-recovery/v1/{name}", query=query, headers=headers)

    def delete_stable_url(self, name: str):
        """Delete a stable URL.

        :param name: str
          The fully qualified resource name. Format: accounts/{account_id}/stable-urls/{stable_url_id}.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/disaster-recovery/v1/{name}", headers=headers)

    def failover_failover_group(
        self,
        name: str,
        target_primary_region: str,
        failover_type: FailoverFailoverGroupRequestFailoverType,
        *,
        etag: Optional[str] = None,
    ) -> FailoverGroup:
        """Initiate a failover that makes target_primary_region the primary region. Stable URLs linked to the
        group are pointed at the new primary workspace, replication is reversed so that the former primary
        becomes the secondary, and the group moves through FAILING_OVER to INITIAL_REPLICATION until it has a
        replication point in the new direction. The group must be ACTIVE; repeating the request while it is
        FAILING_OVER is accepted. To fail back, repeat the request with the former primary region as the
        target once the group is ACTIVE again. In an unplanned failover, data written after the replication
        point can be lost.

        :param name: str
          The fully qualified resource name of the failover group to failover. Format:
          accounts/{account_id}/failover-groups/{failover_group_id}.
        :param target_primary_region: str
          The target primary region. Must be one of the participating regions and different from the current
          effective_primary_region. Serves as an idempotency check.
        :param failover_type: :class:`FailoverFailoverGroupRequestFailoverType`
          The type of failover to perform. FORCED is the only supported type.
        :param etag: str (optional)
          Opaque version string for optimistic locking. If provided, must match the current etag. If omitted,
          the failover proceeds regardless of current state.

        :returns: :class:`FailoverGroup`
        """

        body = {}
        if etag is not None:
            body["etag"] = etag
        if failover_type is not None:
            body["failover_type"] = failover_type.value
        if target_primary_region is not None:
            body["target_primary_region"] = target_primary_region
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", f"/api/disaster-recovery/v1/{name}/failover", body=body, headers=headers)
        return FailoverGroup.from_dict(res)

    def get_failover_group(self, name: str) -> FailoverGroup:
        """Get a failover group, including its current state and replication point.

        :param name: str
          The fully qualified resource name of the failover group. Format:
          accounts/{account_id}/failover-groups/{failover_group_id}.

        :returns: :class:`FailoverGroup`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/disaster-recovery/v1/{name}", headers=headers)
        return FailoverGroup.from_dict(res)

    def get_stable_url(self, name: str) -> StableUrl:
        """Get a stable URL.

        :param name: str
          The fully qualified resource name. Format: accounts/{account_id}/stable-urls/{stable_url_id}.

        :returns: :class:`StableUrl`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/disaster-recovery/v1/{name}", headers=headers)
        return StableUrl.from_dict(res)

    def list_failover_groups(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[FailoverGroup]:
        """List the failover groups in an account.

        List entries are abbreviated: ``state``, ``replication_point`` and
        ``unity_catalog_assets.location_mappings`` are not populated. Call GetFailoverGroup to retrieve the
        full resource.

        :param parent: str
          The parent resource. Format: accounts/{account_id}.
        :param page_size: int (optional)
          Maximum number of failover groups to return per page:

          - when set to a value greater than 0, the page length is the minimum of this value and a server
            configured value;
          - when set to 0 or unset, the page length is set to a server configured value (recommended);
          - when set to a value less than 0, an invalid parameter error is returned.
        :param page_token: str (optional)
          Page token received from a previous ListFailoverGroups call. Provide this to retrieve the subsequent
          page.

        :returns: Iterator over :class:`FailoverGroup`
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
            json = self._api.do(
                "GET", f"/api/disaster-recovery/v1/{parent}/failover-groups", query=query, headers=headers
            )
            if "failover_groups" in json:
                for v in json["failover_groups"]:
                    yield FailoverGroup.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_stable_urls(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[StableUrl]:
        """List stable URLs for an account.

        :param parent: str
          The parent resource. Format: accounts/{account_id}.
        :param page_size: int (optional)
          Maximum number of stable URLs to return per page:

          - when set to a value greater than 0, the page length is the minimum of this value and a server
            configured value;
          - when set to 0 or unset, the page length is set to a server configured value (recommended);
          - when set to a value less than 0, an invalid parameter error is returned.
        :param page_token: str (optional)
          Page token received from a previous ListStableUrls call. Provide this to retrieve the subsequent
          page.

        :returns: Iterator over :class:`StableUrl`
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
            json = self._api.do("GET", f"/api/disaster-recovery/v1/{parent}/stable-urls", query=query, headers=headers)
            if "stable_urls" in json:
                for v in json["stable_urls"]:
                    yield StableUrl.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def update_failover_group(
        self, name: str, failover_group: FailoverGroup, update_mask: FieldMask, *, etag: Optional[str] = None
    ) -> FailoverGroup:
        """Update a failover group. Only the fields named in update_mask change. You can turn workspace asset
        replication on or off, attach or detach a stable URL, and change the Unity Catalog catalogs and
        location mappings; the regions, the workspace set name and the workspace IDs cannot be changed.
        Updates are rejected while a create, failover or delete is in progress, and after a create or delete
        has failed.

        :param name: str
          Fully qualified resource name in the format
          accounts/{account_id}/failover-groups/{failover_group_id}.
        :param failover_group: :class:`FailoverGroup`
          The failover group with updated fields. The name field identifies the resource and is populated from
          the URL path.
        :param update_mask: FieldMask
          Comma-separated list of the fields to update. The supported paths are ``workspace_sets``,
          ``unity_catalog_assets``, ``unity_catalog_assets.catalogs`` and
          ``unity_catalog_assets.location_mappings``; any other path is rejected.
        :param etag: str (optional)
          Optional opaque version string for optimistic locking, obtained from a prior read of the failover
          group. If provided, the update is rejected unless it matches the failover group's current etag. If
          omitted, the update proceeds without an optimistic-lock check.

        :returns: :class:`FailoverGroup`
        """

        body = failover_group.as_dict()
        query = {}
        if etag is not None:
            query["etag"] = etag
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/disaster-recovery/v1/{name}", query=query, body=body, headers=headers)
        return FailoverGroup.from_dict(res)

# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List, Optional

from google.protobuf.timestamp_pb2 import Timestamp

from databricks.sdk.common.types.fieldmask import FieldMask
from databricks.sdk.service._internal import (_enum, _from_dict,
                                              _repeated_dict, _timestamp)

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


class FailoverFailoverGroupRequestFailoverType(Enum):
    """The type of failover to perform."""

    FORCED = "FORCED"


@dataclass
class FailoverGroup:
    """A failover group manages disaster recovery across workspace sets, coordinating UCDR and CPDR
    replication."""

    regions: List[str]
    """List of all regions participating in this failover group."""

    workspace_sets: List[WorkspaceSet]
    """Workspace sets, each containing workspaces that replicate to each other."""

    initial_primary_region: str
    """Initial primary region. Used only in Create requests to set the starting primary region. Not
    returned in responses."""

    create_time: Optional[Timestamp] = None
    """Time at which this failover group was created."""

    effective_primary_region: Optional[str] = None
    """Current effective primary region. Replication flows FROM workspaces in this region. Changes
    after a successful failover."""

    etag: Optional[str] = None
    """Opaque version string for optimistic locking. Server-generated, returned in responses. Must be
    provided on Update requests to prevent concurrent modifications."""

    name: Optional[str] = None
    """Fully qualified resource name in the format
    accounts/{account_id}/failover-groups/{failover_group_id}."""

    replication_point: Optional[Timestamp] = None
    """The latest point in time to which data has been replicated."""

    state: Optional[FailoverGroupState] = None
    """Aggregate state of the failover group."""

    unity_catalog_assets: Optional[UcReplicationConfig] = None
    """Unity Catalog replication configuration."""

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
        if self.initial_primary_region is not None:
            body["initial_primary_region"] = self.initial_primary_region
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
        if self.initial_primary_region is not None:
            body["initial_primary_region"] = self.initial_primary_region
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
            initial_primary_region=d.get("initial_primary_region", None),
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
    """Resource name for this location."""

    uri_by_region: List[LocationMappingEntry]
    """URI for each region. Each entry maps a region name to a storage URI."""

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
    """The region name."""

    uri: str
    """The storage URI for this region."""

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
    the stable URL with a workspace. Not returned in responses. Mirrors
    FailoverGroup.initial_primary_region semantics."""

    failover_group_name: Optional[str] = None
    """Fully qualified resource name of the FailoverGroup this stable URL is currently linked to, in
    the format `accounts/{account_id}/failover-groups/{failover_group_id}`. Empty when the stable
    URL is not attached to any failover group. Server-controlled: written by CreateFailoverGroup /
    UpdateFailoverGroup on link, cleared by DeleteFailoverGroup / UpdateFailoverGroup on unlink."""

    name: Optional[str] = None
    """Fully qualified resource name. Format: accounts/{account_id}/stable-urls/{stable_url_id}."""

    url: Optional[str] = None
    """The stable URL endpoint. Generated by the backend on creation and immutable thereafter. For
    non-Private-Link workspaces this is `https://<spog_host>/?c=<connection_id>`. For Private-Link
    workspaces this is the per-connection hostname."""

    def as_dict(self) -> dict:
        """Serializes the StableUrl into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.failover_group_name is not None:
            body["failover_group_name"] = self.failover_group_name
        if self.initial_workspace_id is not None:
            body["initial_workspace_id"] = self.initial_workspace_id
        if self.name is not None:
            body["name"] = self.name
        if self.url is not None:
            body["url"] = self.url
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the StableUrl into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.failover_group_name is not None:
            body["failover_group_name"] = self.failover_group_name
        if self.initial_workspace_id is not None:
            body["initial_workspace_id"] = self.initial_workspace_id
        if self.name is not None:
            body["name"] = self.name
        if self.url is not None:
            body["url"] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> StableUrl:
        """Deserializes the StableUrl from a dictionary."""
        return cls(
            failover_group_name=d.get("failover_group_name", None),
            initial_workspace_id=d.get("initial_workspace_id", None),
            name=d.get("name", None),
            url=d.get("url", None),
        )


@dataclass
class UcCatalog:
    """A Unity Catalog catalog to replicate."""

    name: str
    """The name of the UC catalog to replicate."""

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
    """UC catalogs to replicate."""

    data_replication_workspace_set: str
    """The workspace set whose workspaces will be used for data replication of all UC catalogs'
    underlying storage."""

    location_mappings: Optional[List[LocationMapping]] = None
    """Location mappings - storage URI per region for each location."""

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
    """Resource name for this workspace set."""

    workspace_ids: List[str]
    """Workspace IDs in this set. The system derives and validates regions. EA: exactly 2 workspaces
    (one per region)."""

    replicate_workspace_assets: bool
    """Whether to enable control plane DR (notebooks, jobs, clusters, etc.) for this set. Requires all
    workspaces in the set to be Mission Critical tier."""

    stable_url_names: Optional[List[str]] = None
    """Resource names of stable URLs associated with this workspace set. Format:
    accounts/{account_id}/stable-urls/{stable_url_id}. The referenced stable URLs must already exist
    (via CreateStableUrl)."""

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
        """Create a new failover group.

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
        """Delete a failover group.

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
        """Initiate a failover to a new primary region.

        :param name: str
          The fully qualified resource name of the failover group to failover. Format:
          accounts/{account_id}/failover-groups/{failover_group_id}.
        :param target_primary_region: str
          The target primary region. Must be one of the derived regions and different from the current
          effective_primary_region. Serves as an idempotency check.
        :param failover_type: :class:`FailoverFailoverGroupRequestFailoverType`
          The type of failover to perform.
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
        """Get a failover group.

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
        """List failover groups.

        :param parent: str
          The parent resource. Format: accounts/{account_id}.
        :param page_size: int (optional)
          Maximum number of failover groups to return per page. Default: 50, maximum: 100.
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
          Maximum number of stable URLs to return per page. Default: 50, maximum: 100.
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

    def update_failover_group(self, name: str, failover_group: FailoverGroup, update_mask: FieldMask) -> FailoverGroup:
        """Update a failover group.

        :param name: str
          Fully qualified resource name in the format
          accounts/{account_id}/failover-groups/{failover_group_id}.
        :param failover_group: :class:`FailoverGroup`
          The failover group with updated fields. The name field identifies the resource and is populated from
          the URL path.
        :param update_mask: FieldMask
          Comma-separated list of fields to update.

        :returns: :class:`FailoverGroup`
        """

        body = failover_group.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/disaster-recovery/v1/{name}", query=query, body=body, headers=headers)
        return FailoverGroup.from_dict(res)

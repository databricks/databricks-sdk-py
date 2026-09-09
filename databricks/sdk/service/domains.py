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
    _repeated_int64,
    _timestamp,
)
from databricks.sdk.common.types.fieldmask import FieldMask


_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class Domain:
    tag_key: str
    """Governed tag key associated with this domain."""

    business_owner_ids: Optional[List[int]] = None
    """Principal IDs of the business owners (users, groups, or service principals)."""

    create_time: Optional[Timestamp] = None
    """Timestamp when the domain was created."""

    description: Optional[str] = None
    """Full description (max 4096 chars)"""

    domain_id: Optional[str] = None
    """Unique identifier for the domain. If omitted at Create, the server generates one."""

    draft: Optional[bool] = None
    """Whether to mark the domain as a draft. If omitted on Create, the server applies a default; the
    resolved value is returned in ``effective_draft``."""

    effective_draft: Optional[bool] = None
    """Resolved draft state of the domain."""

    icon: Optional[DomainIcon] = None
    """Icon to display for the domain."""

    name: Optional[str] = None
    """Full resource name of the domain. The primary identifier for this resource. Format:
    ``domains/{domain_id}`` Identifies the domain on get, update, and delete. Not an input on create
    — to choose the id, set ``CreateDomainRequest.domain_id``."""

    parent_domain_id: Optional[str] = None
    """Domain ID of the parent. If absent, this is a top-level domain. If present, this domain is a
    subdomain of the specified parent."""

    subtitle: Optional[str] = None
    """Short description (max 280 chars)"""

    technical_owner_ids: Optional[List[int]] = None
    """Principal IDs of the technical owners (users, groups, or service principals)."""

    update_time: Optional[Timestamp] = None
    """Timestamp when the domain was last updated."""

    def as_dict(self) -> dict:
        """Serializes the Domain into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.business_owner_ids:
            body["business_owner_ids"] = [v for v in self.business_owner_ids]
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.description is not None:
            body["description"] = self.description
        if self.domain_id is not None:
            body["domain_id"] = self.domain_id
        if self.draft is not None:
            body["draft"] = self.draft
        if self.effective_draft is not None:
            body["effective_draft"] = self.effective_draft
        if self.icon:
            body["icon"] = self.icon.as_dict()
        if self.name is not None:
            body["name"] = self.name
        if self.parent_domain_id is not None:
            body["parent_domain_id"] = self.parent_domain_id
        if self.subtitle is not None:
            body["subtitle"] = self.subtitle
        if self.tag_key is not None:
            body["tag_key"] = self.tag_key
        if self.technical_owner_ids:
            body["technical_owner_ids"] = [v for v in self.technical_owner_ids]
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Domain into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.business_owner_ids:
            body["business_owner_ids"] = self.business_owner_ids
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.description is not None:
            body["description"] = self.description
        if self.domain_id is not None:
            body["domain_id"] = self.domain_id
        if self.draft is not None:
            body["draft"] = self.draft
        if self.effective_draft is not None:
            body["effective_draft"] = self.effective_draft
        if self.icon:
            body["icon"] = self.icon
        if self.name is not None:
            body["name"] = self.name
        if self.parent_domain_id is not None:
            body["parent_domain_id"] = self.parent_domain_id
        if self.subtitle is not None:
            body["subtitle"] = self.subtitle
        if self.tag_key is not None:
            body["tag_key"] = self.tag_key
        if self.technical_owner_ids:
            body["technical_owner_ids"] = self.technical_owner_ids
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Domain:
        """Deserializes the Domain from a dictionary."""
        return cls(
            business_owner_ids=_repeated_int64(d, "business_owner_ids"),
            create_time=_timestamp(d, "create_time"),
            description=d.get("description", None),
            domain_id=d.get("domain_id", None),
            draft=d.get("draft", None),
            effective_draft=d.get("effective_draft", None),
            icon=_from_dict(d, "icon", DomainIcon),
            name=d.get("name", None),
            parent_domain_id=d.get("parent_domain_id", None),
            subtitle=d.get("subtitle", None),
            tag_key=d.get("tag_key", None),
            technical_owner_ids=_repeated_int64(d, "technical_owner_ids"),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class DomainIcon:
    """Icon configuration for a domain."""

    color: Optional[str] = None
    """Hex color code with # prefix (e.g., "#FF5733")."""

    name: Optional[DomainIconName] = None

    def as_dict(self) -> dict:
        """Serializes the DomainIcon into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.color is not None:
            body["color"] = self.color
        if self.name is not None:
            body["name"] = self.name.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DomainIcon into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.color is not None:
            body["color"] = self.color
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DomainIcon:
        """Deserializes the DomainIcon from a dictionary."""
        return cls(color=d.get("color", None), name=_enum(d, "name", DomainIconName))


class DomainIconName(Enum):
    """Available icon names for a domain."""

    ADDRESS_BOOK = "ADDRESS_BOOK"
    ALARM = "ALARM"
    ARROWS_IN = "ARROWS_IN"
    ATOM = "ATOM"
    BALLOON = "BALLOON"
    BANK = "BANK"
    BARRICADE = "BARRICADE"
    BASKET = "BASKET"
    BRIDGE = "BRIDGE"
    CACTUS = "CACTUS"
    CALL_BELL = "CALL_BELL"
    CARROT = "CARROT"
    CHART_PIE_SLICE = "CHART_PIE_SLICE"
    CITY = "CITY"
    CLOUD = "CLOUD"
    COINS = "COINS"
    COMPASS_ROSE = "COMPASS_ROSE"
    CRANE_TOWER = "CRANE_TOWER"
    CROWN = "CROWN"
    CUBE_TRANSPARENT = "CUBE_TRANSPARENT"
    FADERS = "FADERS"
    FLAG_BANNER_FOLD = "FLAG_BANNER_FOLD"
    FLAG_CHECKERED = "FLAG_CHECKERED"
    GAVEL = "GAVEL"
    HAMBURGER = "HAMBURGER"
    HEAD_CIRCUIT = "HEAD_CIRCUIT"
    HOURGLASS_HIGH = "HOURGLASS_HIGH"
    INTERSECT_THREE = "INTERSECT_THREE"
    MICROSCOPE = "MICROSCOPE"
    MOON_STARS = "MOON_STARS"
    PACKAGE = "PACKAGE"
    PARACHUTE = "PARACHUTE"
    PEPPER = "PEPPER"
    PIGGY_BANK = "PIGGY_BANK"
    PILL = "PILL"
    PLANET = "PLANET"
    PLANT = "PLANT"
    PLUGS_CONNECTED = "PLUGS_CONNECTED"
    POPCORN = "POPCORN"
    PRESENTATION_CHART = "PRESENTATION_CHART"
    PUZZLE_PIECE = "PUZZLE_PIECE"
    RAINBOW = "RAINBOW"
    RANKING = "RANKING"
    RECEIPT = "RECEIPT"
    ROCKET = "ROCKET"
    RULER = "RULER"
    SAILBOAT = "SAILBOAT"
    SCALES = "SCALES"
    SCAN_SMILEY = "SCAN_SMILEY"
    SCROLL = "SCROLL"
    SHIELD_CHECKERED = "SHIELD_CHECKERED"
    SNEAKER = "SNEAKER"
    SNOWFLAKE = "SNOWFLAKE"
    SOLAR_ROOF = "SOLAR_ROOF"
    SPEEDOMETER = "SPEEDOMETER"
    STAMP = "STAMP"
    STEPS = "STEPS"
    STRATEGY = "STRATEGY"
    SWORD = "SWORD"
    TELEVISION_SIMPLE = "TELEVISION_SIMPLE"
    TENT = "TENT"
    TICKET = "TICKET"
    TRACTOR = "TRACTOR"
    TRAFFIC_CONE = "TRAFFIC_CONE"
    TRAIN = "TRAIN"
    TREE_EVERGREEN = "TREE_EVERGREEN"
    TREE_STRUCTURE = "TREE_STRUCTURE"
    TROLLEY_SUITCASE = "TROLLEY_SUITCASE"
    TROPHY = "TROPHY"
    TRUCK_TRAILER = "TRUCK_TRAILER"
    USERS_THREE = "USERS_THREE"
    VECTOR_THREE = "VECTOR_THREE"


@dataclass
class ListDomainsResponse:
    domains: Optional[List[Domain]] = None

    next_page_token: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the ListDomainsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.domains:
            body["domains"] = [v.as_dict() for v in self.domains]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListDomainsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.domains:
            body["domains"] = self.domains
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListDomainsResponse:
        """Deserializes the ListDomainsResponse from a dictionary."""
        return cls(domains=_repeated_dict(d, "domains", Domain), next_page_token=d.get("next_page_token", None))


class DomainsAPI:
    """Manage domains for organizing and discovering data assets."""

    def __init__(self, api_client):
        self._api = api_client

    def create_domain(self, domain: Domain, *, domain_id: Optional[str] = None) -> Domain:
        """Create a domain. If ``domain_id`` is omitted, the server generates one.

        :param domain: :class:`Domain`
        :param domain_id: str (optional)
          Client-supplied resource ID for the new domain. If omitted, the server generates one.

        :returns: :class:`Domain`
        """

        body = domain.as_dict()
        query = {}
        if domain_id is not None:
            query["domain_id"] = domain_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/domains", query=query, body=body, headers=headers)
        return Domain.from_dict(res)

    def delete_domain(self, name: str, *, force: Optional[bool] = None):
        """Delete a domain. By default the request fails if the domain still has Glossary pages; set ``force`` to
        delete those pages along with the domain.

        :param name: str
          Full resource name of the domain to delete. Format: ``domains/{domain_id}``
        :param force: bool (optional)
          When false (default), DeleteDomain is rejected with FAILED_PRECONDITION if the domain still has
          Glossary pages. When true, those pages are deleted first and then the domain is removed.


        """

        query = {}
        if force is not None:
            query["force"] = force
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/{name}", query=query, headers=headers)

    def get_domain(self, name: str) -> Domain:
        """Get a domain by resource name.

        Authorization: external callers must have the ``MANAGE DISCOVERY`` permission.

        :param name: str
          Full resource name of the domain to retrieve. Format: ``domains/{domain_id}``

        :returns: :class:`Domain`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/{name}", headers=headers)
        return Domain.from_dict(res)

    def list_domains(
        self,
        *,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        parent_domain_id: Optional[str] = None,
    ) -> Iterator[Domain]:
        """List domains in the account. Set ``parent_domain_id`` to return only the direct subdomains of a given
        domain.

        Authorization: external callers must have the ``MANAGE DISCOVERY`` permission; only domains the caller
        is authorized to read are returned.

        :param page_size: int (optional)
        :param page_token: str (optional)
        :param parent_domain_id: str (optional)
          Filter by parent domain.

          - Absent: return all domains regardless of hierarchy.
          - Present: return only direct children of the specified domain.

        :returns: Iterator over :class:`Domain`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        if parent_domain_id is not None:
            query["parent_domain_id"] = parent_domain_id
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", "/api/2.0/domains", query=query, headers=headers)
            if "domains" in json:
                for v in json["domains"]:
                    yield Domain.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def update_domain(self, name: str, domain: Domain, update_mask: FieldMask) -> Domain:
        """Update a domain. ``update_mask`` selects which fields to modify; the domain is identified by its
        resource ``name``.

        :param name: str
          Full resource name of the domain. The primary identifier for this resource. Format:
          ``domains/{domain_id}`` Identifies the domain on get, update, and delete. Not an input on create —
          to choose the id, set ``CreateDomainRequest.domain_id``.
        :param domain: :class:`Domain`
        :param update_mask: FieldMask
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g.,
          ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of ``*`` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using ``*`` wildcards, as it can lead to unintended results if the
          API changes in the future.

        :returns: :class:`Domain`
        """

        body = domain.as_dict()
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
        return Domain.from_dict(res)

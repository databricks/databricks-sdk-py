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
class AppendSessionItemsResponse:
    """Response containing appended items."""

    session_items: Optional[List[SessionItem]] = None
    """Persisted session items with service-assigned fields."""

    def as_dict(self) -> dict:
        """Serializes the AppendSessionItemsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.session_items:
            body["session_items"] = [v.as_dict() for v in self.session_items]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AppendSessionItemsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.session_items:
            body["session_items"] = self.session_items
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AppendSessionItemsResponse:
        """Deserializes the AppendSessionItemsResponse from a dictionary."""
        return cls(session_items=_repeated_dict(d, "session_items", SessionItem))


@dataclass
class ClearSessionItemsResponse:
    """Response from clearing items from a session."""

    def as_dict(self) -> dict:
        """Serializes the ClearSessionItemsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ClearSessionItemsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ClearSessionItemsResponse:
        """Deserializes the ClearSessionItemsResponse from a dictionary."""
        return cls()


@dataclass
class ExtractMemoriesResponse:
    """Result of a single-session memory extraction."""

    entries: Optional[List[ManagedMemoryEntry]] = None
    """The memory entries written by this extraction."""

    name: Optional[str] = None
    """Correlation identifier for this extraction, for logging and tracing. Not a fetchable resource."""

    def as_dict(self) -> dict:
        """Serializes the ExtractMemoriesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.entries:
            body["entries"] = [v.as_dict() for v in self.entries]
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ExtractMemoriesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.entries:
            body["entries"] = self.entries
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ExtractMemoriesResponse:
        """Deserializes the ExtractMemoriesResponse from a dictionary."""
        return cls(entries=_repeated_dict(d, "entries", ManagedMemoryEntry), name=d.get("name", None))


@dataclass
class ForkSessionResponse:
    """Response from forking a session."""

    session: Optional[Session] = None
    """The newly-created independent top-level session."""

    def as_dict(self) -> dict:
        """Serializes the ForkSessionResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.session:
            body["session"] = self.session.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ForkSessionResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.session:
            body["session"] = self.session
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ForkSessionResponse:
        """Deserializes the ForkSessionResponse from a dictionary."""
        return cls(session=_from_dict(d, "session", Session))


@dataclass
class ListManagedMemoryEntriesResponse:
    """Response containing managed memory entries."""

    managed_memory_entries: Optional[List[ManagedMemoryEntry]] = None
    """Managed memory entries matching the request and its read mask."""

    next_page_token: Optional[str] = None
    """Opaque pagination token. This field is omitted when there are no more results."""

    def as_dict(self) -> dict:
        """Serializes the ListManagedMemoryEntriesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.managed_memory_entries:
            body["managed_memory_entries"] = [v.as_dict() for v in self.managed_memory_entries]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListManagedMemoryEntriesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.managed_memory_entries:
            body["managed_memory_entries"] = self.managed_memory_entries
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListManagedMemoryEntriesResponse:
        """Deserializes the ListManagedMemoryEntriesResponse from a dictionary."""
        return cls(
            managed_memory_entries=_repeated_dict(d, "managed_memory_entries", ManagedMemoryEntry),
            next_page_token=d.get("next_page_token", None),
        )


@dataclass
class ListManagedMemoryStoresResponse:
    """Response containing managed memory stores in the caller's workspace."""

    managed_memory_stores: Optional[List[ManagedMemoryStore]] = None
    """Managed memory stores in the caller's workspace."""

    next_page_token: Optional[str] = None
    """Opaque pagination token. This field is omitted when there are no more results."""

    def as_dict(self) -> dict:
        """Serializes the ListManagedMemoryStoresResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.managed_memory_stores:
            body["managed_memory_stores"] = [v.as_dict() for v in self.managed_memory_stores]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListManagedMemoryStoresResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.managed_memory_stores:
            body["managed_memory_stores"] = self.managed_memory_stores
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListManagedMemoryStoresResponse:
        """Deserializes the ListManagedMemoryStoresResponse from a dictionary."""
        return cls(
            managed_memory_stores=_repeated_dict(d, "managed_memory_stores", ManagedMemoryStore),
            next_page_token=d.get("next_page_token", None),
        )


@dataclass
class ListSessionItemsResponse:
    """Response containing a page of session items."""

    next_page_token: Optional[str] = None
    """Token to retrieve the next page."""

    session_items: Optional[List[SessionItem]] = None
    """Session items in the requested page."""

    def as_dict(self) -> dict:
        """Serializes the ListSessionItemsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.session_items:
            body["session_items"] = [v.as_dict() for v in self.session_items]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListSessionItemsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.session_items:
            body["session_items"] = self.session_items
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListSessionItemsResponse:
        """Deserializes the ListSessionItemsResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            session_items=_repeated_dict(d, "session_items", SessionItem),
        )


@dataclass
class ListSessionStoresResponse:
    """Response containing a page of session stores."""

    next_page_token: Optional[str] = None
    """Token to retrieve the next page."""

    session_stores: Optional[List[SessionStore]] = None
    """Session stores in the requested page."""

    def as_dict(self) -> dict:
        """Serializes the ListSessionStoresResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.session_stores:
            body["session_stores"] = [v.as_dict() for v in self.session_stores]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListSessionStoresResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.session_stores:
            body["session_stores"] = self.session_stores
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListSessionStoresResponse:
        """Deserializes the ListSessionStoresResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            session_stores=_repeated_dict(d, "session_stores", SessionStore),
        )


@dataclass
class ListSessionsResponse:
    """Response containing a page of sessions."""

    next_page_token: Optional[str] = None
    """Token to retrieve the next page."""

    sessions: Optional[List[Session]] = None
    """Sessions in the requested page."""

    def as_dict(self) -> dict:
        """Serializes the ListSessionsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.sessions:
            body["sessions"] = [v.as_dict() for v in self.sessions]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListSessionsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.sessions:
            body["sessions"] = self.sessions
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListSessionsResponse:
        """Deserializes the ListSessionsResponse from a dictionary."""
        return cls(next_page_token=d.get("next_page_token", None), sessions=_repeated_dict(d, "sessions", Session))


@dataclass
class ManagedMemoryEntry:
    """A workspace-scoped entry in a managed memory store."""

    actor_id: str
    """Customer-provided identifier for the actor whose memory this entry represents."""

    path: str
    """Absolute, case-sensitive path identifying the entry within its actor and optional session. Paths
    must begin with ``/`` and must not contain empty, ``.`` or ``..`` segments."""

    content: Optional[str] = None
    """Optional free-form memory content."""

    create_time: Optional[Timestamp] = None
    """Time when the entry was created."""

    description: Optional[str] = None
    """Human-readable description of the memory entry."""

    name: Optional[str] = None
    """Resource name in the form
    ``memory-stores/{managed_memory_store_id}/entries/{managed_memory_entry_id}``."""

    session_id: Optional[str] = None
    """Optional identifier for the session associated with this memory entry. When omitted, the entry
    applies across the actor's sessions."""

    source_type: Optional[ManagedMemoryEntrySourceType] = None
    """Which writer created this entry. Caller sets this on Create; immutable after creation."""

    update_time: Optional[Timestamp] = None
    """Time when the entry was last updated."""

    def as_dict(self) -> dict:
        """Serializes the ManagedMemoryEntry into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.actor_id is not None:
            body["actor_id"] = self.actor_id
        if self.content is not None:
            body["content"] = self.content
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.description is not None:
            body["description"] = self.description
        if self.name is not None:
            body["name"] = self.name
        if self.path is not None:
            body["path"] = self.path
        if self.session_id is not None:
            body["session_id"] = self.session_id
        if self.source_type is not None:
            body["source_type"] = self.source_type.value
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ManagedMemoryEntry into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.actor_id is not None:
            body["actor_id"] = self.actor_id
        if self.content is not None:
            body["content"] = self.content
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.description is not None:
            body["description"] = self.description
        if self.name is not None:
            body["name"] = self.name
        if self.path is not None:
            body["path"] = self.path
        if self.session_id is not None:
            body["session_id"] = self.session_id
        if self.source_type is not None:
            body["source_type"] = self.source_type
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ManagedMemoryEntry:
        """Deserializes the ManagedMemoryEntry from a dictionary."""
        return cls(
            actor_id=d.get("actor_id", None),
            content=d.get("content", None),
            create_time=_timestamp(d, "create_time"),
            description=d.get("description", None),
            name=d.get("name", None),
            path=d.get("path", None),
            session_id=d.get("session_id", None),
            source_type=_enum(d, "source_type", ManagedMemoryEntrySourceType),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class ManagedMemoryEntrySearchResult:
    """One relevance-ranked managed memory search result."""

    managed_memory_entry: Optional[ManagedMemoryEntry] = None
    """Managed memory entry matching the query."""

    score: Optional[float] = None
    """Relevance score for the result. Higher scores are more relevant."""

    def as_dict(self) -> dict:
        """Serializes the ManagedMemoryEntrySearchResult into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.managed_memory_entry:
            body["managed_memory_entry"] = self.managed_memory_entry.as_dict()
        if self.score is not None:
            body["score"] = self.score
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ManagedMemoryEntrySearchResult into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.managed_memory_entry:
            body["managed_memory_entry"] = self.managed_memory_entry
        if self.score is not None:
            body["score"] = self.score
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ManagedMemoryEntrySearchResult:
        """Deserializes the ManagedMemoryEntrySearchResult from a dictionary."""
        return cls(
            managed_memory_entry=_from_dict(d, "managed_memory_entry", ManagedMemoryEntry), score=d.get("score", None)
        )


class ManagedMemoryEntrySourceType(Enum):
    """Identifies the source that created a managed memory entry."""

    MANAGED_MEMORY_ENTRY_SOURCE_TYPE_AGENT = "MANAGED_MEMORY_ENTRY_SOURCE_TYPE_AGENT"
    MANAGED_MEMORY_ENTRY_SOURCE_TYPE_DREAMER = "MANAGED_MEMORY_ENTRY_SOURCE_TYPE_DREAMER"


@dataclass
class ManagedMemoryStore:
    """A workspace-scoped managed memory store backed by service-managed storage."""

    create_time: Optional[Timestamp] = None
    """Time when the store was created."""

    creator_user_id: Optional[str] = None
    """Workspace-local user ID of the authenticated principal that created the store. This is immutable
    server-set attribution and does not grant access; authorization is evaluated from the
    authenticated request context."""

    description: Optional[str] = None
    """Human-readable description of the memory store."""

    display_name: Optional[str] = None
    """Deprecated compatibility alias for the caller-provided managed memory store ID. Canonical
    clients provide the ID through ``CreateMemoryStoreRequest.managed_memory_store_id`` and use
    ``name`` as the resource identifier."""

    name: Optional[str] = None
    """Resource name in the form ``memory-stores/{managed_memory_store_id}``."""

    owner_user_id: Optional[str] = None
    """Deprecated alias for ``creator_user_id``. This identifies the original creator, not a
    transferable owner. Use ``creator_user_id`` instead."""

    storage_backend: Optional[StorageBackend] = None
    """Service-managed storage backing this memory store."""

    update_time: Optional[Timestamp] = None
    """Time when the store was last updated."""

    workspace_id: Optional[int] = None
    """Workspace that owns the memory store."""

    def as_dict(self) -> dict:
        """Serializes the ManagedMemoryStore into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.creator_user_id is not None:
            body["creator_user_id"] = self.creator_user_id
        if self.description is not None:
            body["description"] = self.description
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.name is not None:
            body["name"] = self.name
        if self.owner_user_id is not None:
            body["owner_user_id"] = self.owner_user_id
        if self.storage_backend:
            body["storage_backend"] = self.storage_backend.as_dict()
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        if self.workspace_id is not None:
            body["workspace_id"] = self.workspace_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ManagedMemoryStore into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.creator_user_id is not None:
            body["creator_user_id"] = self.creator_user_id
        if self.description is not None:
            body["description"] = self.description
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.name is not None:
            body["name"] = self.name
        if self.owner_user_id is not None:
            body["owner_user_id"] = self.owner_user_id
        if self.storage_backend:
            body["storage_backend"] = self.storage_backend
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.workspace_id is not None:
            body["workspace_id"] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ManagedMemoryStore:
        """Deserializes the ManagedMemoryStore from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            creator_user_id=d.get("creator_user_id", None),
            description=d.get("description", None),
            display_name=d.get("display_name", None),
            name=d.get("name", None),
            owner_user_id=d.get("owner_user_id", None),
            storage_backend=_from_dict(d, "storage_backend", StorageBackend),
            update_time=_timestamp(d, "update_time"),
            workspace_id=_int64(d, "workspace_id"),
        )


@dataclass
class PopSessionItemResponse:
    """Response containing the popped item."""

    item: Optional[SessionItem] = None
    """Removed item, if any."""

    def as_dict(self) -> dict:
        """Serializes the PopSessionItemResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.item:
            body["item"] = self.item.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PopSessionItemResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.item:
            body["item"] = self.item
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PopSessionItemResponse:
        """Deserializes the PopSessionItemResponse from a dictionary."""
        return cls(item=_from_dict(d, "item", SessionItem))


@dataclass
class SearchManagedMemoryEntriesResponse:
    """Response containing managed memory entries ranked by relevance."""

    managed_memory_entries: Optional[List[ManagedMemoryEntry]] = None
    """Deprecated compatibility alias for clients migrating to ``results``. This contains the same
    entries in the same order, but omits their relevance scores."""

    next_page_token: Optional[str] = None
    """Opaque pagination token. Search currently returns an unpaginated ranked top-N result set, so the
    server does not populate this field."""

    results: Optional[List[ManagedMemoryEntrySearchResult]] = None
    """Canonical matching entries and relevance scores, ordered most relevant first."""

    def as_dict(self) -> dict:
        """Serializes the SearchManagedMemoryEntriesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.managed_memory_entries:
            body["managed_memory_entries"] = [v.as_dict() for v in self.managed_memory_entries]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.results:
            body["results"] = [v.as_dict() for v in self.results]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SearchManagedMemoryEntriesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.managed_memory_entries:
            body["managed_memory_entries"] = self.managed_memory_entries
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.results:
            body["results"] = self.results
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SearchManagedMemoryEntriesResponse:
        """Deserializes the SearchManagedMemoryEntriesResponse from a dictionary."""
        return cls(
            managed_memory_entries=_repeated_dict(d, "managed_memory_entries", ManagedMemoryEntry),
            next_page_token=d.get("next_page_token", None),
            results=_repeated_dict(d, "results", ManagedMemoryEntrySearchResult),
        )


@dataclass
class Session:
    """A durable logical interaction stored within a Session Store."""

    actor_id: str
    """Opaque caller-provided identifier for the application actor associated with the session.
    
    This is application data and has no Databricks authentication or authorization semantics. Use
    the same value as the Managed Memory Entry ``actor_id`` when storing memories associated with
    this actor. Every session must set it. A child session must use the same value as its parent."""

    create_time: Optional[Timestamp] = None
    """Time when the session was created."""

    last_activity_time: Optional[Timestamp] = None
    """Time when the session's item history was last mutated."""

    metadata: Optional[Dict[str, str]] = None
    """Mutable caller-defined string labels."""

    name: Optional[str] = None
    """Resource name in the form ``session-stores/{session_store_id}/sessions/{session_id}``."""

    parent_session_id: Optional[str] = None
    """Immediate parent session ID. Set only at creation for child sessions, immutable thereafter, and
    restricted to the same store."""

    root_session_id: Optional[str] = None
    """Top-level session ID in the spawn tree. This equals ``session_id`` for a root or fork and is
    inherited transitively by child sessions."""

    session_id: Optional[str] = None
    """Unique session ID. The service generates a UUID unless the caller supplies
    ``CreateSessionRequest.session_id``."""

    update_time: Optional[Timestamp] = None
    """Time when session resource fields last changed."""

    def as_dict(self) -> dict:
        """Serializes the Session into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.actor_id is not None:
            body["actor_id"] = self.actor_id
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.last_activity_time is not None:
            body["last_activity_time"] = self.last_activity_time.ToJsonString()
        if self.metadata:
            body["metadata"] = self.metadata
        if self.name is not None:
            body["name"] = self.name
        if self.parent_session_id is not None:
            body["parent_session_id"] = self.parent_session_id
        if self.root_session_id is not None:
            body["root_session_id"] = self.root_session_id
        if self.session_id is not None:
            body["session_id"] = self.session_id
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Session into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.actor_id is not None:
            body["actor_id"] = self.actor_id
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.last_activity_time is not None:
            body["last_activity_time"] = self.last_activity_time
        if self.metadata:
            body["metadata"] = self.metadata
        if self.name is not None:
            body["name"] = self.name
        if self.parent_session_id is not None:
            body["parent_session_id"] = self.parent_session_id
        if self.root_session_id is not None:
            body["root_session_id"] = self.root_session_id
        if self.session_id is not None:
            body["session_id"] = self.session_id
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Session:
        """Deserializes the Session from a dictionary."""
        return cls(
            actor_id=d.get("actor_id", None),
            create_time=_timestamp(d, "create_time"),
            last_activity_time=_timestamp(d, "last_activity_time"),
            metadata=d.get("metadata", None),
            name=d.get("name", None),
            parent_session_id=d.get("parent_session_id", None),
            root_session_id=d.get("root_session_id", None),
            session_id=d.get("session_id", None),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class SessionItem:
    """A transcript entry in a session's history."""

    data: any
    """Complete SDK-native, JSON-compatible item. The service stores and returns this value without
    interpreting provider-specific fields such as ``type``, ``role``, or ``content``."""

    create_time: Optional[Timestamp] = None
    """Server-assigned time when the append commits. Values are nondecreasing within a session. Item
    listing orders by this timestamp; equal timestamps are resolved by committed append order."""

    item_id: Optional[str] = None
    """Stable service-generated item ID."""

    def as_dict(self) -> dict:
        """Serializes the SessionItem into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.data:
            body["data"] = self.data
        if self.item_id is not None:
            body["item_id"] = self.item_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SessionItem into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.data:
            body["data"] = self.data
        if self.item_id is not None:
            body["item_id"] = self.item_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SessionItem:
        """Deserializes the SessionItem from a dictionary."""
        return cls(create_time=_timestamp(d, "create_time"), data=d.get("data", None), item_id=d.get("item_id", None))


@dataclass
class SessionStore:
    """A workspace-scoped session store."""

    create_time: Optional[Timestamp] = None
    """Time when the store was created."""

    creator_user_id: Optional[str] = None
    """Workspace-local user ID of the authenticated principal that created the store. This is immutable
    server-set attribution and does not grant access; authorization is evaluated from the
    authenticated request context."""

    description: Optional[str] = None
    """Human-readable description of the session store."""

    metadata: Optional[Dict[str, str]] = None
    """Mutable caller-defined string labels."""

    name: Optional[str] = None
    """Resource name in the form ``session-stores/{session_store_id}``."""

    update_time: Optional[Timestamp] = None
    """Time when the store was last updated."""

    def as_dict(self) -> dict:
        """Serializes the SessionStore into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.creator_user_id is not None:
            body["creator_user_id"] = self.creator_user_id
        if self.description is not None:
            body["description"] = self.description
        if self.metadata:
            body["metadata"] = self.metadata
        if self.name is not None:
            body["name"] = self.name
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SessionStore into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.creator_user_id is not None:
            body["creator_user_id"] = self.creator_user_id
        if self.description is not None:
            body["description"] = self.description
        if self.metadata:
            body["metadata"] = self.metadata
        if self.name is not None:
            body["name"] = self.name
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SessionStore:
        """Deserializes the SessionStore from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            creator_user_id=d.get("creator_user_id", None),
            description=d.get("description", None),
            metadata=d.get("metadata", None),
            name=d.get("name", None),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class StorageBackend:
    """Service-managed storage backing a managed memory store."""

    backend_id: Optional[str] = None
    """Backend-specific identifier. For Lakebase, this is the project ID."""

    backend_type: Optional[StorageBackendType] = None
    """Type of the storage backend."""

    def as_dict(self) -> dict:
        """Serializes the StorageBackend into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.backend_id is not None:
            body["backend_id"] = self.backend_id
        if self.backend_type is not None:
            body["backend_type"] = self.backend_type.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the StorageBackend into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.backend_id is not None:
            body["backend_id"] = self.backend_id
        if self.backend_type is not None:
            body["backend_type"] = self.backend_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> StorageBackend:
        """Deserializes the StorageBackend from a dictionary."""
        return cls(backend_id=d.get("backend_id", None), backend_type=_enum(d, "backend_type", StorageBackendType))


class StorageBackendType(Enum):
    """Type of service-managed storage backing a managed memory store."""

    STORAGE_BACKEND_TYPE_LAKEBASE = "STORAGE_BACKEND_TYPE_LAKEBASE"


class MasonAPI:
    """APIs for managing agent memory and durable session state. This interface is under active development and
    may change."""

    def __init__(self, api_client):
        self._api = api_client

    def append_session_items(self, parent: str, items: List[SessionItem]) -> AppendSessionItemsResponse:
        """Appends items to a session.

        :param parent: str
          Resource name of the containing session, in the form
          ``session-stores/{session_store_id}/sessions/{session_id}``.
        :param items: List[:class:`SessionItem`]
          Items to append atomically in request order. Concurrent append requests are serialized into one
          committed order without exposing a numeric sequence in the public contract.

        :returns: :class:`AppendSessionItemsResponse`
        """

        body = {}
        if items is not None:
            body["items"] = [v.as_dict() for v in items]
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/agents/{parent}/items:append", body=body, headers=headers)
        return AppendSessionItemsResponse.from_dict(res)

    def clear_session_items(self, parent: str) -> ClearSessionItemsResponse:
        """Clears all items from a session.

        :param parent: str
          Resource name of the containing session, in the form
          ``session-stores/{session_store_id}/sessions/{session_id}``.

        :returns: :class:`ClearSessionItemsResponse`
        """

        body = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/agents/{parent}/items:clear", body=body, headers=headers)
        return ClearSessionItemsResponse.from_dict(res)

    def create_memory(
        self, parent: str, managed_memory_entry: ManagedMemoryEntry, *, managed_memory_entry_id: Optional[str] = None
    ) -> ManagedMemoryEntry:
        """Creates a managed memory entry using exclusive-create semantics. Callers may choose the entry ID; the
        service generates one when it is omitted. Returns ``ALREADY_EXISTS`` when an entry with the same
        actor, session, and path already exists. Omitted ``session_id`` is its own uniqueness key: two
        omitted-session entries with the same actor and path conflict, but an omitted-session entry does not
        conflict with a session-scoped entry at the same actor and path.

        :param parent: str
          Managed memory store that will contain the entry, in the form
          ``memory-stores/{managed_memory_store_id}``.
        :param managed_memory_entry: :class:`ManagedMemoryEntry`
          The managed memory entry to create.
        :param managed_memory_entry_id: str (optional)
          Optional caller-selected managed memory entry ID. The service generates an ID when omitted.

        :returns: :class:`ManagedMemoryEntry`
        """

        body = managed_memory_entry.as_dict()
        query = {}
        if managed_memory_entry_id is not None:
            query["managed_memory_entry_id"] = managed_memory_entry_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/agents/{parent}/entries", query=query, body=body, headers=headers)
        return ManagedMemoryEntry.from_dict(res)

    def create_memory_store(
        self, managed_memory_store: ManagedMemoryStore, managed_memory_store_id: str
    ) -> ManagedMemoryStore:
        """Creates a managed memory store in the caller's workspace.

        :param managed_memory_store: :class:`ManagedMemoryStore`
          The managed memory store to create.
        :param managed_memory_store_id: str
          Caller-provided, workspace-unique managed memory store ID. It must be 3-56 characters, begin with a
          lowercase letter, contain only lowercase letters, digits, and hyphens, and end with a letter or
          digit.

        :returns: :class:`ManagedMemoryStore`
        """

        body = managed_memory_store.as_dict()
        query = {}
        if managed_memory_store_id is not None:
            query["managed_memory_store_id"] = managed_memory_store_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/agents/memory-stores", query=query, body=body, headers=headers)
        return ManagedMemoryStore.from_dict(res)

    def create_session(self, parent: str, session: Session, *, session_id: Optional[str] = None) -> Session:
        """Creates a session within a session store.

        :param parent: str
          Resource name of the containing session store, in the form ``session-stores/{session_store_id}``.
        :param session: :class:`Session`
          The session to create. ``actor_id`` is required. A session with ``parent_session_id`` is a child and
          must use its parent's ``actor_id``. Independent forks are created only through ``ForkSession``.
        :param session_id: str (optional)
          Optional caller-selected session ID. The service generates a UUID when this field is omitted. The ID
          must be unique; a collision returns ``ALREADY_EXISTS``.

        :returns: :class:`Session`
        """

        body = session.as_dict()
        query = {}
        if session_id is not None:
            query["session_id"] = session_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/agents/{parent}/sessions", query=query, body=body, headers=headers)
        return Session.from_dict(res)

    def create_session_store(self, session_store: SessionStore, session_store_id: str) -> SessionStore:
        """Creates a session store.

        :param session_store: :class:`SessionStore`
          The session store to create.
        :param session_store_id: str
          Caller-provided, workspace-unique session store ID. It must be 3-55 characters, begin with a
          lowercase letter, and contain only lowercase letters, digits, and hyphens.

        :returns: :class:`SessionStore`
        """

        body = session_store.as_dict()
        query = {}
        if session_store_id is not None:
            query["session_store_id"] = session_store_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/agents/session-stores", query=query, body=body, headers=headers)
        return SessionStore.from_dict(res)

    def delete_memory(self, name: str):
        """Deletes a managed memory entry by resource name. Returns ``NOT_FOUND`` when the entry does not exist
        in the caller's workspace.

        :param name: str
          Resource name in the form
          ``memory-stores/{managed_memory_store_id}/entries/{managed_memory_entry_id}``.


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/agents/{name}", headers=headers)

    def delete_memory_store(self, name: str):
        """Deletes a managed memory store by resource name. Returns ``NOT_FOUND`` when the store does not exist
        in the caller's workspace.

        :param name: str
          Resource name in the form ``memory-stores/{managed_memory_store_id}``.


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/agents/{name}", headers=headers)

    def delete_session(self, name: str):
        """Deletes a session, its items, and any descendant sessions recursively. Independently retained memory
        is not deleted.

        :param name: str
          Resource name in the form ``session-stores/{session_store_id}/sessions/{session_id}``.


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/agents/{name}", headers=headers)

    def delete_session_store(self, name: str):
        """Deletes a session store, its sessions and items, and its service-managed storage. Memory entries
        retained by a separate Memory Store are not deleted.

        :param name: str
          Resource name in the form ``session-stores/{session_store_id}``.


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/agents/{name}", headers=headers)

    def extract_memories(
        self,
        session_store: str,
        session_id: str,
        memory_store: str,
        *,
        dry_run: Optional[bool] = None,
        instructions: Optional[str] = None,
    ) -> ExtractMemoriesResponse:
        """Synchronously extracts memories from a single session into the given memory store, returning the
        entries that were written.

        :param session_store: str
          Session store containing the session, in the form ``session-stores/{session_store_id}``.
        :param session_id: str
          Identifier of the session whose transcript is distilled into memories.
        :param memory_store: str
          Managed memory store the extracted entries are written to, in the form
          ``memory-stores/{managed_memory_store_id}``.
        :param dry_run: bool (optional)
          When true, extract and return the entries without writing them to the memory store. Defaults to
          false, which persists the extracted entries and returns them.
        :param instructions: str (optional)
          Instructions steering what is extracted from the session.

        :returns: :class:`ExtractMemoriesResponse`
        """

        body = {}
        if dry_run is not None:
            body["dry_run"] = dry_run
        if instructions is not None:
            body["instructions"] = instructions
        if memory_store is not None:
            body["memory_store"] = memory_store
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "POST", f"/api/2.0/agents/{session_store}/sessions/{session_id}/extractions", body=body, headers=headers
        )
        return ExtractMemoriesResponse.from_dict(res)

    def fork_session(
        self,
        parent: str,
        source_session_id: str,
        actor_id: str,
        *,
        metadata: Optional[Dict[str, str]] = None,
        session_id: Optional[str] = None,
        up_to_item_id: Optional[str] = None,
    ) -> ForkSessionResponse:
        """Forks a session into an independent top-level copy.

        :param parent: str
          Resource name of the containing session store, in the form ``session-stores/{session_store_id}``.
        :param source_session_id: str
          ID of the session to copy.
        :param actor_id: str
          Opaque caller-provided identifier for the application actor associated with the forked session.
        :param metadata: Dict[str,str] (optional)
          Optional metadata for the fork.
        :param session_id: str (optional)
          Optional unique ID for the forked session. A collision returns ``ALREADY_EXISTS``.
        :param up_to_item_id: str (optional)
          Optional last item ID to copy through, inclusively. When omitted, the fork atomically copies all
          items committed before the fork operation begins.

        :returns: :class:`ForkSessionResponse`
        """

        body = {}
        if actor_id is not None:
            body["actor_id"] = actor_id
        if metadata is not None:
            body["metadata"] = metadata
        if session_id is not None:
            body["session_id"] = session_id
        if source_session_id is not None:
            body["source_session_id"] = source_session_id
        if up_to_item_id is not None:
            body["up_to_item_id"] = up_to_item_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/agents/{parent}/sessions:fork", body=body, headers=headers)
        return ForkSessionResponse.from_dict(res)

    def get_memory(self, name: str, *, read_mask: Optional[FieldMask] = None) -> ManagedMemoryEntry:
        """Retrieves a managed memory entry, including its content, by resource name. Returns ``NOT_FOUND`` when
        the entry does not exist in the caller's workspace.

        :param name: str
          Resource name in the form
          ``memory-stores/{managed_memory_store_id}/entries/{managed_memory_entry_id}``.
        :param read_mask: FieldMask (optional)
          Fields to return, using proto field names such as ``content`` (not ``contents``). An omitted or
          empty mask returns the full entry, including ``content``; a non-empty mask returns only the
          requested fields.

        :returns: :class:`ManagedMemoryEntry`
        """

        query = {}
        if read_mask is not None:
            query["read_mask"] = read_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/agents/{name}", query=query, headers=headers)
        return ManagedMemoryEntry.from_dict(res)

    def get_memory_store(self, name: str) -> ManagedMemoryStore:
        """Retrieves a managed memory store by resource name. Returns ``NOT_FOUND`` when the store does not exist
        in the caller's workspace.

        :param name: str
          Resource name in the form ``memory-stores/{managed_memory_store_id}``.

        :returns: :class:`ManagedMemoryStore`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/agents/{name}", headers=headers)
        return ManagedMemoryStore.from_dict(res)

    def get_session(self, name: str) -> Session:
        """Gets a session by resource name.

        :param name: str
          Resource name in the form ``session-stores/{session_store_id}/sessions/{session_id}``.

        :returns: :class:`Session`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/agents/{name}", headers=headers)
        return Session.from_dict(res)

    def get_session_store(self, name: str) -> SessionStore:
        """Gets a session store by resource name.

        :param name: str
          Resource name in the form ``session-stores/{session_store_id}``.

        :returns: :class:`SessionStore`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/agents/{name}", headers=headers)
        return SessionStore.from_dict(res)

    def list_memories(
        self,
        parent: str,
        actor_id: str,
        *,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        path_prefix: Optional[str] = None,
        read_mask: Optional[FieldMask] = None,
        session_id: Optional[str] = None,
    ) -> Iterator[ManagedMemoryEntry]:
        """Lists managed memory entries for one actor. An exact ``path`` filters entries across sessions,
        ignoring session metadata. Otherwise, ``session_id`` and ``path_prefix`` restrict the actor partition.
        ``read_mask`` selects fields in each returned entry.

        :param parent: str
          Managed memory store whose entries are listed, in the form
          ``memory-stores/{managed_memory_store_id}``.
        :param actor_id: str
          Customer-provided identifier for the actor whose entries are listed.
        :param page_size: int (optional)
          Maximum number of entries to return. The service may return fewer entries than requested. Defaults
          to 10; must be between 1 and 100.
        :param page_token: str (optional)
          Opaque pagination token from a previous ListManagedMemoryEntries response.
        :param path_prefix: str (optional)
          Optional path prefix used to restrict entries within the actor partition.
        :param read_mask: FieldMask (optional)
          Fields to return in each entry, using proto field names such as ``content`` (not ``contents``). An
          omitted or empty mask returns each full entry, including ``content``; a non-empty mask returns only
          the requested fields.
        :param session_id: str (optional)
          Optional session identifier. When set, only entries with this exact ``session_id`` are returned.
          Omitted-session (cross-session) entries are not included. Ignored when path is set.

        :returns: Iterator over :class:`ManagedMemoryEntry`
        """

        query = {}
        if actor_id is not None:
            query["actor_id"] = actor_id
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        if path_prefix is not None:
            query["path_prefix"] = path_prefix
        if read_mask is not None:
            query["read_mask"] = read_mask.ToJsonString()
        if session_id is not None:
            query["session_id"] = session_id
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", f"/api/2.0/agents/{parent}/entries", query=query, headers=headers)
            if "managed_memory_entries" in json:
                for v in json["managed_memory_entries"]:
                    yield ManagedMemoryEntry.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_memory_stores(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[ManagedMemoryStore]:
        """Lists managed memory stores in the caller's workspace.

        :param page_size: int (optional)
          Maximum number of stores to return. The service may return fewer stores than requested. Defaults to
          10; must be between 1 and 100.
        :param page_token: str (optional)
          Opaque pagination token from a previous ListManagedMemoryStores response.

        :returns: Iterator over :class:`ManagedMemoryStore`
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
            json = self._api.do("GET", "/api/2.0/agents/memory-stores", query=query, headers=headers)
            if "managed_memory_stores" in json:
                for v in json["managed_memory_stores"]:
                    yield ManagedMemoryStore.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_session_items(
        self,
        parent: str,
        *,
        order_by: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
    ) -> Iterator[SessionItem]:
        """Lists items in a session.

        :param parent: str
          Resource name of the containing session, in the form
          ``session-stores/{session_store_id}/sessions/{session_id}``.
        :param order_by: str (optional)
          Sort order. Supported values are ``create_time asc`` and ``create_time desc``. The default is
          ``create_time desc``, which returns the most recently appended items first. Equal timestamps are
          resolved by committed append order in the requested direction.
        :param page_size: int (optional)
          Maximum number of items to return. Defaults to 10; must be between 1 and 100.
        :param page_token: str (optional)
          Token returned by a previous list request.

        :returns: Iterator over :class:`SessionItem`
        """

        query = {}
        if order_by is not None:
            query["order_by"] = order_by
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
            json = self._api.do("GET", f"/api/2.0/agents/{parent}/items", query=query, headers=headers)
            if "session_items" in json:
                for v in json["session_items"]:
                    yield SessionItem.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_session_stores(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[SessionStore]:
        """Lists session stores.

        :param page_size: int (optional)
          Maximum number of session stores to return. Defaults to 10; must be between 1 and 100.
        :param page_token: str (optional)
          Token returned by a previous list request.

        :returns: Iterator over :class:`SessionStore`
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
            json = self._api.do("GET", "/api/2.0/agents/session-stores", query=query, headers=headers)
            if "session_stores" in json:
                for v in json["session_stores"]:
                    yield SessionStore.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_sessions(
        self,
        parent: str,
        *,
        filter: Optional[str] = None,
        order_by: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
    ) -> Iterator[Session]:
        """Lists sessions within a session store.

        :param parent: str
          Resource name of the containing session store, in the form ``session-stores/{session_store_id}``.
        :param filter: str (optional)
          Filter expression. Supported fields include ``actor_id`` and ``metadata``; for example, ``actor_id =
          "support-customer-123"``.
        :param order_by: str (optional)
          Sort order. Defaults to ``last_activity_time desc``. Page-token continuation is exactly-once when
          ordering by ``create_time`` (immutable); ordering by ``last_activity_time`` is best-effort, because
          that value changes as a session gains activity, so a session updated between page requests may be
          repeated or skipped. To enumerate every session exactly once, order by ``create_time``.
        :param page_size: int (optional)
          Maximum number of sessions to return. Defaults to 10; must be between 1 and 100.
        :param page_token: str (optional)
          Token returned by a previous list request.

        :returns: Iterator over :class:`Session`
        """

        query = {}
        if filter is not None:
            query["filter"] = filter
        if order_by is not None:
            query["order_by"] = order_by
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
            json = self._api.do("GET", f"/api/2.0/agents/{parent}/sessions", query=query, headers=headers)
            if "sessions" in json:
                for v in json["sessions"]:
                    yield Session.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def pop_session_item(self, parent: str) -> PopSessionItemResponse:
        """Pops the newest item from a session.

        :param parent: str
          Resource name of the containing session, in the form
          ``session-stores/{session_store_id}/sessions/{session_id}``.

        :returns: :class:`PopSessionItemResponse`
        """

        body = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/agents/{parent}/items:pop", body=body, headers=headers)
        return PopSessionItemResponse.from_dict(res)

    def search_memories(
        self,
        parent: str,
        actor_id: str,
        query: str,
        *,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        path_prefix: Optional[str] = None,
        read_mask: Optional[FieldMask] = None,
        session_id: Optional[str] = None,
    ) -> Iterator[ManagedMemoryEntrySearchResult]:
        """Searches managed memory entries by text query for one actor. Returns matching entries and scores
        ranked by relevance; ``read_mask`` selects fields in each returned entry.

        :param parent: str
          Managed memory store whose entries are searched, in the form
          ``memory-stores/{managed_memory_store_id}``.
        :param actor_id: str
          Customer-provided identifier for the actor whose entries are searched.
        :param query: str
          Free-form search query.
        :param limit: int (optional)
          Deprecated alias for ``page_size``. When both fields are set, their values must match.
        :param page_size: int (optional)
          Maximum number of relevance-ranked entries to return. Defaults to 10 and must be between 1 and 100.
        :param page_token: str (optional)
          Reserved for pagination compatibility. The server currently ignores this field because Search
          returns a ranked top-N result set.
        :param path_prefix: str (optional)
          Optional absolute, case-sensitive path prefix used to restrict searched entries within the actor
          partition. The prefix must begin with ``/`` and must not contain empty, ``.`` or ``..`` segments.
        :param read_mask: FieldMask (optional)
          Fields to return in each matching entry, using proto field names such as ``content`` (not
          ``contents``). An omitted or empty mask returns each full entry, including ``content``; a non-empty
          mask returns only the requested fields. Search scores are always returned.

          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g.,
          ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.
        :param session_id: str (optional)
          Optional session identifier. When set, only entries with this exact ``session_id`` are searched.
          Omitted-session (cross-session) entries are not included.

        :returns: Iterator over :class:`ManagedMemoryEntrySearchResult`
        """

        body = {}
        if actor_id is not None:
            body["actor_id"] = actor_id
        if limit is not None:
            body["limit"] = limit
        if page_size is not None:
            body["page_size"] = page_size
        if page_token is not None:
            body["page_token"] = page_token
        if path_prefix is not None:
            body["path_prefix"] = path_prefix
        if query is not None:
            body["query"] = query
        if read_mask is not None:
            body["read_mask"] = read_mask.ToJsonString()
        if session_id is not None:
            body["session_id"] = session_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("POST", f"/api/2.0/agents/{parent}/entries:search", body=body, headers=headers)
            if "results" in json:
                for v in json["results"]:
                    yield ManagedMemoryEntrySearchResult.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            body["page_token"] = json["next_page_token"]

    def update_memory(
        self, name: str, managed_memory_entry: ManagedMemoryEntry, update_mask: FieldMask
    ) -> ManagedMemoryEntry:
        """Updates selected mutable fields on a managed memory entry. Identity fields are immutable.

        :param name: str
          Resource name in the form
          ``memory-stores/{managed_memory_store_id}/entries/{managed_memory_entry_id}``.
        :param managed_memory_entry: :class:`ManagedMemoryEntry`
          The managed memory entry to update.
        :param update_mask: FieldMask
          Fields to update. Only ``content`` and ``description`` may be updated.

        :returns: :class:`ManagedMemoryEntry`
        """

        body = managed_memory_entry.as_dict()
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

        res = self._api.do("PATCH", f"/api/2.0/agents/{name}", query=query, body=body, headers=headers)
        return ManagedMemoryEntry.from_dict(res)

    def update_memory_store(
        self, name: str, managed_memory_store: ManagedMemoryStore, update_mask: FieldMask
    ) -> ManagedMemoryStore:
        """Updates a managed memory store's description.

        :param name: str
          Resource name in the form ``memory-stores/{managed_memory_store_id}``.
        :param managed_memory_store: :class:`ManagedMemoryStore`
          The managed memory store to update. ``name`` is taken from the URL.
        :param update_mask: FieldMask
          Only ``description`` may be updated.

        :returns: :class:`ManagedMemoryStore`
        """

        body = managed_memory_store.as_dict()
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

        res = self._api.do("PATCH", f"/api/2.0/agents/{name}", query=query, body=body, headers=headers)
        return ManagedMemoryStore.from_dict(res)

    def update_session(self, name: str, session: Session, update_mask: FieldMask) -> Session:
        """Updates a session's mutable fields.

        :param name: str
          Resource name in the form ``session-stores/{session_store_id}/sessions/{session_id}``.
        :param session: :class:`Session`
          Session to update.
        :param update_mask: FieldMask
          Fields to update. Only ``metadata`` is mutable; any other path returns ``INVALID_PARAMETER_VALUE``.

        :returns: :class:`Session`
        """

        body = session.as_dict()
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

        res = self._api.do("PATCH", f"/api/2.0/agents/{name}", query=query, body=body, headers=headers)
        return Session.from_dict(res)

    def update_session_store(self, name: str, session_store: SessionStore, update_mask: FieldMask) -> SessionStore:
        """Updates a session store's description and metadata.

        :param name: str
          Resource name in the form ``session-stores/{session_store_id}``.
        :param session_store: :class:`SessionStore`
          Session store to update.
        :param update_mask: FieldMask
          Fields to update. Only ``description`` and ``metadata`` are mutable; any other path returns
          ``INVALID_PARAMETER_VALUE``.

        :returns: :class:`SessionStore`
        """

        body = session_store.as_dict()
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

        res = self._api.do("PATCH", f"/api/2.0/agents/{name}", query=query, body=body, headers=headers)
        return SessionStore.from_dict(res)

``w.mason``: Mason.v1
=====================
.. currentmodule:: databricks.sdk.service.mason

.. py:class:: MasonAPI

    APIs for managing agent memory and durable session state. This interface is under active development and
    may change.

    .. py:method:: append_session_items(parent: str, items: List[SessionItem]) -> AppendSessionItemsResponse

        Appends items to a session.

        :param parent: str
          Resource name of the containing session, in the form
          ``session-stores/{session_store_id}/sessions/{session_id}``.
        :param items: List[:class:`SessionItem`]
          Items to append atomically in request order. Concurrent append requests are serialized into one
          committed order without exposing a numeric sequence in the public contract.

        :returns: :class:`AppendSessionItemsResponse`
        

    .. py:method:: clear_session_items(parent: str) -> ClearSessionItemsResponse

        Clears all items from a session.

        :param parent: str
          Resource name of the containing session, in the form
          ``session-stores/{session_store_id}/sessions/{session_id}``.

        :returns: :class:`ClearSessionItemsResponse`
        

    .. py:method:: create_memory(parent: str, managed_memory_entry: ManagedMemoryEntry [, managed_memory_entry_id: Optional[str]]) -> ManagedMemoryEntry

        Creates a managed memory entry using exclusive-create semantics. Callers may choose the entry ID; the
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
        

    .. py:method:: create_memory_store(managed_memory_store: ManagedMemoryStore, managed_memory_store_id: str) -> ManagedMemoryStore

        Creates a managed memory store in the caller's workspace.

        :param managed_memory_store: :class:`ManagedMemoryStore`
          The managed memory store to create.
        :param managed_memory_store_id: str
          Caller-provided, workspace-unique managed memory store ID. It must be 3-56 characters, begin with a
          lowercase letter, contain only lowercase letters, digits, and hyphens, and end with a letter or
          digit.

        :returns: :class:`ManagedMemoryStore`
        

    .. py:method:: create_session(parent: str, session: Session [, session_id: Optional[str]]) -> Session

        Creates a session within a session store.

        :param parent: str
          Resource name of the containing session store, in the form ``session-stores/{session_store_id}``.
        :param session: :class:`Session`
          The session to create. ``actor_id`` is required. A session with ``parent_session_id`` is a child and
          must use its parent's ``actor_id``. Independent forks are created only through ``ForkSession``.
        :param session_id: str (optional)
          Optional caller-selected session ID. The service generates a UUID when this field is omitted. The ID
          must be unique; a collision returns ``ALREADY_EXISTS``.

        :returns: :class:`Session`
        

    .. py:method:: create_session_store(session_store: SessionStore, session_store_id: str) -> SessionStore

        Creates a session store.

        :param session_store: :class:`SessionStore`
          The session store to create.
        :param session_store_id: str
          Caller-provided, workspace-unique session store ID. It must be 3-55 characters, begin with a
          lowercase letter, and contain only lowercase letters, digits, and hyphens.

        :returns: :class:`SessionStore`
        

    .. py:method:: delete_memory(name: str)

        Deletes a managed memory entry by resource name. Returns ``NOT_FOUND`` when the entry does not exist
        in the caller's workspace.

        :param name: str
          Resource name in the form
          ``memory-stores/{managed_memory_store_id}/entries/{managed_memory_entry_id}``.


        

    .. py:method:: delete_memory_store(name: str)

        Deletes a managed memory store by resource name. Returns ``NOT_FOUND`` when the store does not exist
        in the caller's workspace.

        :param name: str
          Resource name in the form ``memory-stores/{managed_memory_store_id}``.


        

    .. py:method:: delete_session(name: str)

        Deletes a session, its items, and any descendant sessions recursively. Independently retained memory
        is not deleted.

        :param name: str
          Resource name in the form ``session-stores/{session_store_id}/sessions/{session_id}``.


        

    .. py:method:: delete_session_store(name: str)

        Deletes a session store, its sessions and items, and its service-managed storage. Memory entries
        retained by a separate Memory Store are not deleted.

        :param name: str
          Resource name in the form ``session-stores/{session_store_id}``.


        

    .. py:method:: extract_memories(session_store: str, session_id: str, memory_store: str [, dry_run: Optional[bool], instructions: Optional[str]]) -> ExtractMemoriesResponse

        Synchronously extracts memories from a single session into the given memory store, returning the
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
        

    .. py:method:: fork_session(parent: str, source_session_id: str, actor_id: str [, metadata: Optional[Dict[str, str]], session_id: Optional[str], up_to_item_id: Optional[str]]) -> ForkSessionResponse

        Forks a session into an independent top-level copy.

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
        

    .. py:method:: get_memory(name: str [, read_mask: Optional[FieldMask]]) -> ManagedMemoryEntry

        Retrieves a managed memory entry, including its content, by resource name. Returns ``NOT_FOUND`` when
        the entry does not exist in the caller's workspace.

        :param name: str
          Resource name in the form
          ``memory-stores/{managed_memory_store_id}/entries/{managed_memory_entry_id}``.
        :param read_mask: FieldMask (optional)
          Fields to return, using proto field names such as ``content`` (not ``contents``). An omitted or
          empty mask returns the full entry, including ``content``; a non-empty mask returns only the
          requested fields.

        :returns: :class:`ManagedMemoryEntry`
        

    .. py:method:: get_memory_store(name: str) -> ManagedMemoryStore

        Retrieves a managed memory store by resource name. Returns ``NOT_FOUND`` when the store does not exist
        in the caller's workspace.

        :param name: str
          Resource name in the form ``memory-stores/{managed_memory_store_id}``.

        :returns: :class:`ManagedMemoryStore`
        

    .. py:method:: get_session(name: str) -> Session

        Gets a session by resource name.

        :param name: str
          Resource name in the form ``session-stores/{session_store_id}/sessions/{session_id}``.

        :returns: :class:`Session`
        

    .. py:method:: get_session_store(name: str) -> SessionStore

        Gets a session store by resource name.

        :param name: str
          Resource name in the form ``session-stores/{session_store_id}``.

        :returns: :class:`SessionStore`
        

    .. py:method:: list_memories(parent: str, actor_id: str [, page_size: Optional[int], page_token: Optional[str], path_prefix: Optional[str], read_mask: Optional[FieldMask], session_id: Optional[str]]) -> Iterator[ManagedMemoryEntry]

        Lists managed memory entries for one actor. Optional ``session_id`` and ``path_prefix`` further
        restrict the actor partition; ``read_mask`` selects fields in each returned entry.

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
          Omitted-session (cross-session) entries are not included.

        :returns: Iterator over :class:`ManagedMemoryEntry`
        

    .. py:method:: list_memory_stores( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ManagedMemoryStore]

        Lists managed memory stores in the caller's workspace.

        :param page_size: int (optional)
          Maximum number of stores to return. The service may return fewer stores than requested. Defaults to
          10; must be between 1 and 100.
        :param page_token: str (optional)
          Opaque pagination token from a previous ListManagedMemoryStores response.

        :returns: Iterator over :class:`ManagedMemoryStore`
        

    .. py:method:: list_session_items(parent: str [, order_by: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> Iterator[SessionItem]

        Lists items in a session.

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
        

    .. py:method:: list_session_stores( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[SessionStore]

        Lists session stores.

        :param page_size: int (optional)
          Maximum number of session stores to return. Defaults to 10; must be between 1 and 100.
        :param page_token: str (optional)
          Token returned by a previous list request.

        :returns: Iterator over :class:`SessionStore`
        

    .. py:method:: list_sessions(parent: str [, filter: Optional[str], order_by: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Session]

        Lists sessions within a session store.

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
        

    .. py:method:: pop_session_item(parent: str) -> PopSessionItemResponse

        Pops the newest item from a session.

        :param parent: str
          Resource name of the containing session, in the form
          ``session-stores/{session_store_id}/sessions/{session_id}``.

        :returns: :class:`PopSessionItemResponse`
        

    .. py:method:: search_memories(parent: str, actor_id: str, query: str [, limit: Optional[int], page_size: Optional[int], page_token: Optional[str], path_prefix: Optional[str], read_mask: Optional[FieldMask], session_id: Optional[str]]) -> Iterator[ManagedMemoryEntrySearchResult]

        Searches managed memory entries by text query for one actor. Returns matching entries and scores
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
        

    .. py:method:: update_memory(name: str, managed_memory_entry: ManagedMemoryEntry, update_mask: FieldMask) -> ManagedMemoryEntry

        Updates selected mutable fields on a managed memory entry. Identity fields are immutable.

        :param name: str
          Resource name in the form
          ``memory-stores/{managed_memory_store_id}/entries/{managed_memory_entry_id}``.
        :param managed_memory_entry: :class:`ManagedMemoryEntry`
          The managed memory entry to update.
        :param update_mask: FieldMask
          Fields to update. Only ``content`` and ``description`` may be updated.

        :returns: :class:`ManagedMemoryEntry`
        

    .. py:method:: update_memory_store(name: str, managed_memory_store: ManagedMemoryStore, update_mask: FieldMask) -> ManagedMemoryStore

        Updates a managed memory store's description.

        :param name: str
          Resource name in the form ``memory-stores/{managed_memory_store_id}``.
        :param managed_memory_store: :class:`ManagedMemoryStore`
          The managed memory store to update. ``name`` is taken from the URL.
        :param update_mask: FieldMask
          Only ``description`` may be updated.

        :returns: :class:`ManagedMemoryStore`
        

    .. py:method:: update_session(name: str, session: Session, update_mask: FieldMask) -> Session

        Updates a session's mutable fields.

        :param name: str
          Resource name in the form ``session-stores/{session_store_id}/sessions/{session_id}``.
        :param session: :class:`Session`
          Session to update.
        :param update_mask: FieldMask
          Fields to update. Only ``metadata`` is mutable; any other path returns ``INVALID_PARAMETER_VALUE``.

        :returns: :class:`Session`
        

    .. py:method:: update_session_store(name: str, session_store: SessionStore, update_mask: FieldMask) -> SessionStore

        Updates a session store's description and metadata.

        :param name: str
          Resource name in the form ``session-stores/{session_store_id}``.
        :param session_store: :class:`SessionStore`
          Session store to update.
        :param update_mask: FieldMask
          Fields to update. Only ``description`` and ``metadata`` are mutable; any other path returns
          ``INVALID_PARAMETER_VALUE``.

        :returns: :class:`SessionStore`
        
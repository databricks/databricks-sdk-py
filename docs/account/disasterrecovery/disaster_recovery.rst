``a.disaster_recovery``: DisasterRecovery.v1
============================================
.. currentmodule:: databricks.sdk.service.disasterrecovery

.. py:class:: DisasterRecoveryAPI

    Manage disaster recovery configurations and execute failover operations.

    .. py:method:: create_failover_group(parent: str, failover_group: FailoverGroup, failover_group_id: str [, validate_only: Optional[bool]]) -> FailoverGroup

        Create a failover group. The group starts in the CREATING state and moves to INITIAL_REPLICATION while
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
        

    .. py:method:: create_stable_url(parent: str, stable_url: StableUrl, stable_url_id: str [, validate_only: Optional[bool]]) -> StableUrl

        Create a new stable URL.

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
        

    .. py:method:: delete_failover_group(name: str [, etag: Optional[str]])

        Delete a failover group. Deleting stops replication for the group; stable URLs linked to it are
        detached but not deleted.

        :param name: str
          The fully qualified resource name of the failover group to delete. Format:
          accounts/{account_id}/failover-groups/{failover_group_id}.
        :param etag: str (optional)
          Opaque version string for optimistic locking. If provided, must match the current etag. If omitted,
          the delete proceeds without an etag check.


        

    .. py:method:: delete_stable_url(name: str)

        Delete a stable URL.

        :param name: str
          The fully qualified resource name. Format: accounts/{account_id}/stable-urls/{stable_url_id}.


        

    .. py:method:: failover_failover_group(name: str, target_primary_region: str, failover_type: FailoverFailoverGroupRequestFailoverType [, etag: Optional[str]]) -> FailoverGroup

        Initiate a failover that makes target_primary_region the primary region. Stable URLs linked to the
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
        

    .. py:method:: get_failover_group(name: str) -> FailoverGroup

        Get a failover group, including its current state and replication point.

        :param name: str
          The fully qualified resource name of the failover group. Format:
          accounts/{account_id}/failover-groups/{failover_group_id}.

        :returns: :class:`FailoverGroup`
        

    .. py:method:: get_stable_url(name: str) -> StableUrl

        Get a stable URL.

        :param name: str
          The fully qualified resource name. Format: accounts/{account_id}/stable-urls/{stable_url_id}.

        :returns: :class:`StableUrl`
        

    .. py:method:: list_failover_groups(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[FailoverGroup]

        List the failover groups in an account.

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
        

    .. py:method:: list_stable_urls(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[StableUrl]

        List stable URLs for an account.

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
        

    .. py:method:: update_failover_group(name: str, failover_group: FailoverGroup, update_mask: FieldMask [, etag: Optional[str]]) -> FailoverGroup

        Update a failover group. Only the fields named in update_mask change. You can turn workspace asset
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
        
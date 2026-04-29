``a.disaster_recovery``: DisasterRecovery.v1
============================================
.. currentmodule:: databricks.sdk.service.disasterrecovery

.. py:class:: DisasterRecoveryAPI

    Manage disaster recovery configurations and execute failover operations.

    .. py:method:: create_failover_group(parent: str, failover_group: FailoverGroup, failover_group_id: str [, validate_only: Optional[bool]]) -> FailoverGroup

        Create a new failover group.

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

        Delete a failover group.

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

        Initiate a failover to a new primary region.

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
        

    .. py:method:: get_failover_group(name: str) -> FailoverGroup

        Get a failover group.

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

        List failover groups.

        :param parent: str
          The parent resource. Format: accounts/{account_id}.
        :param page_size: int (optional)
          Maximum number of failover groups to return per page. Default: 50, maximum: 100.
        :param page_token: str (optional)
          Page token received from a previous ListFailoverGroups call. Provide this to retrieve the subsequent
          page.

        :returns: Iterator over :class:`FailoverGroup`
        

    .. py:method:: list_stable_urls(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[StableUrl]

        List stable URLs for an account.

        :param parent: str
          The parent resource. Format: accounts/{account_id}.
        :param page_size: int (optional)
          Maximum number of stable URLs to return per page. Default: 50, maximum: 100.
        :param page_token: str (optional)
          Page token received from a previous ListStableUrls call. Provide this to retrieve the subsequent
          page.

        :returns: Iterator over :class:`StableUrl`
        

    .. py:method:: update_failover_group(name: str, failover_group: FailoverGroup, update_mask: FieldMask) -> FailoverGroup

        Update a failover group.

        :param name: str
          Fully qualified resource name in the format
          accounts/{account_id}/failover-groups/{failover_group_id}.
        :param failover_group: :class:`FailoverGroup`
          The failover group with updated fields. The name field identifies the resource and is populated from
          the URL path.
        :param update_mask: FieldMask
          Comma-separated list of fields to update.

        :returns: :class:`FailoverGroup`
        
``w.assume_group``: AssumeGroup
===============================
.. currentmodule:: databricks.sdk.service.iam

.. py:class:: AssumeGroupAPI

    Manage the workspace's restricted sharing groups.

    .. py:method:: create_restricted_sharing_group(restricted_sharing_group: RestrictedSharingGroup, restricted_sharing_group_id: str) -> RestrictedSharingGroup

        Adds a group to the workspace's restricted list. The workspace allows at most 100 restricted sharing
        groups. Requires workspace admin.

        :param restricted_sharing_group: :class:`RestrictedSharingGroup`
          The restricted sharing group to create. It has no client-set fields; the group is identified by
          restricted_sharing_group_id.
        :param restricted_sharing_group_id: str
          The id of the workspace group to restrict: the numeric id of an existing and non-system workspace
          group.

        :returns: :class:`RestrictedSharingGroup`
        

    .. py:method:: delete_restricted_sharing_group(name: str)

        Removes a group from the workspace's restricted list. Requires workspace admin.

        :param name: str
          The name of the restricted sharing group to delete. Format:
          ``restricted-sharing-groups/{restricted_sharing_group_id}``


        

    .. py:method:: get_restricted_sharing_group(name: str) -> RestrictedSharingGroup

        Gets a restricted sharing group in the workspace. Use it to check whether a group is on the
        workspace's restricted list. Requires workspace admin.

        :param name: str
          The name of the restricted sharing group to get. Format:
          ``restricted-sharing-groups/{restricted_sharing_group_id}``

        :returns: :class:`RestrictedSharingGroup`
        

    .. py:method:: list_restricted_sharing_groups( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[RestrictedSharingGroup]

        Lists the restricted sharing groups in the workspace. Requires workspace admin.

        :param page_size: int (optional)
          The maximum number of groups to return. The service may return fewer. If unspecified or 0, at most
          100 groups are returned. Values above 100 are coerced to 100. Negative values are rejected.
        :param page_token: str (optional)
          A page token from a previous ListRestrictedSharingGroups call. Provide this to retrieve the
          subsequent page.

        :returns: Iterator over :class:`RestrictedSharingGroup`
        
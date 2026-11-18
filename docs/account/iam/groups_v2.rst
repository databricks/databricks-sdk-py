``a.groups_v2``: Account Groups
===============================
.. currentmodule:: databricks.sdk.service.iam

.. py:class:: AccountGroupsV2API

    Groups simplify identity management, making it easier to assign access to Databricks account, data, and
    other securable objects.

    It is best practice to assign access to workspaces and access-control policies in Unity Catalog to groups,
    instead of to users individually. All Databricks account identities can be assigned as members of groups,
    and members inherit permissions that are assigned to their group.

    .. py:method:: create( [, display_name: Optional[str], external_id: Optional[str], id: Optional[str], members: Optional[List[ComplexValue]], meta: Optional[ResourceMeta], roles: Optional[List[ComplexValue]]]) -> AccountGroup

        Creates a group in the Databricks account with a unique name, using the supplied group details.

        :param display_name: str (optional)
          Sets the human-readable name of the group. The name must be unique within the account and must not
          exceed 255 characters.
        :param external_id: str (optional)
          Sets the identifier of the group in an external identity provider.
        :param id: str (optional)
          Identifies the group within Databricks.
        :param members: List[:class:`ComplexValue`] (optional)
          Lists the members of the group. Each entry identifies a user, service principal or group in the
          account by its ID in the value sub-attribute.
        :param meta: :class:`ResourceMeta` (optional)
          Container for the group identifier. Workspace local versus account.
        :param roles: List[:class:`ComplexValue`] (optional)
          Lists the account roles that are assigned to the group. The only supported role value is
          ``account_admin``.

        :returns: :class:`AccountGroup`
        

    .. py:method:: delete(id: str)

        Deletes a group from the Databricks account.

        :param id: str
          Unique ID for a group in the Databricks account.


        

    .. py:method:: get(id: str) -> AccountGroup

        Gets the information for a specific group in the Databricks account.

        :param id: str
          Unique ID for a group in the Databricks account.

        :returns: :class:`AccountGroup`
        

    .. py:method:: list( [, attributes: Optional[str], count: Optional[int], excluded_attributes: Optional[str], filter: Optional[str], sort_by: Optional[str], sort_order: Optional[ListSortOrder], start_index: Optional[int]]) -> Iterator[AccountGroup]

        Gets all details of the groups associated with the Databricks account. As of 08/22/2025, this endpoint
        will no longer return members. Instead, members should be retrieved by iterating through ``Get group
        details``. Existing accounts that rely on this attribute will not be impacted and will continue
        receiving member data as before.

        :param attributes: str (optional)
          Comma-separated list of attributes to return in response.
        :param count: int (optional)
          Specifies the number of results per page. When omitted, the server uses its default page size.
        :param excluded_attributes: str (optional)
          Comma-separated list of attributes to exclude in response.
        :param filter: str (optional)
          Query by which the results have to be filtered. Supported operators are equals(``eq``),
          contains(``co``), starts with(``sw``) and not equals(``ne``). Additionally, simple expressions can
          be formed using logical operators - ``and`` and ``or``. The `SCIM RFC
          <https://tools.ietf.org/html/rfc7644#section-3.4.2.2>`__ has more details but we currently only
          support simple expressions.
        :param sort_by: str (optional)
          Attribute to sort the results.
        :param sort_order: :class:`ListSortOrder` (optional)
          The order to sort the results.
        :param start_index: int (optional)
          Specifies the index of the first result. First item is number 1.

        :returns: Iterator over :class:`AccountGroup`
        

    .. py:method:: patch(id: str [, operations: Optional[List[Patch]], schemas: Optional[List[PatchSchema]]])

        Partially updates the details of a group.

        :param id: str
          Unique ID for a group in the Databricks account.
        :param operations: List[:class:`Patch`] (optional)
          Lists the patch operations to apply to the group.
        :param schemas: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].


        

    .. py:method:: update(id: str [, display_name: Optional[str], external_id: Optional[str], members: Optional[List[ComplexValue]], meta: Optional[ResourceMeta], roles: Optional[List[ComplexValue]]])

        Updates the details of a group by replacing the entire group entity.

        :param id: str
          Identifies the group within Databricks.
        :param display_name: str (optional)
          Sets the human-readable name of the group. The name must be unique within the account and must not
          exceed 255 characters.
        :param external_id: str (optional)
          Sets the identifier of the group in an external identity provider.
        :param members: List[:class:`ComplexValue`] (optional)
          Lists the members of the group. Each entry identifies a user, service principal or group in the
          account by its ID in the value sub-attribute.
        :param meta: :class:`ResourceMeta` (optional)
          Container for the group identifier. Workspace local versus account.
        :param roles: List[:class:`ComplexValue`] (optional)
          Lists the account roles that are assigned to the group. The only supported role value is
          ``account_admin``.


        
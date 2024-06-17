``a.groups``: Account Groups
============================
.. currentmodule:: databricks.sdk.service.iam

.. py:class:: AccountGroupsAPI

    Groups simplify identity management, making it easier to assign access to Databricks account, data, and
    other securable objects.
    
    It is best practice to assign access to workspaces and access-control policies in Unity Catalog to groups,
    instead of to users individually. All Databricks account identities can be assigned as members of groups,
    and members inherit permissions that are assigned to their group.

    .. py:method:: create( [, display_name: Optional[str], entitlements: Optional[List[ComplexValue]], external_id: Optional[str], groups: Optional[List[ComplexValue]], id: Optional[str], members: Optional[List[ComplexValue]], meta: Optional[ResourceMeta], roles: Optional[List[ComplexValue]], schemas: Optional[List[GroupSchema]]]) -> Group

        Create a new group.
        
        Creates a group in the Databricks account with a unique name, using the supplied group details.
        
        :param display_name: str (optional)
          String that represents a human-readable group name
        :param entitlements: List[:class:`ComplexValue`] (optional)
          Entitlements assigned to the group. See [assigning entitlements] for a full list of supported
          values.
          
          [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param id: str (optional)
          Databricks group ID
        :param members: List[:class:`ComplexValue`] (optional)
        :param meta: :class:`ResourceMeta` (optional)
          Container for the group identifier. Workspace local versus account.
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`GroupSchema`] (optional)
          The schema of the group.
        
        :returns: :class:`Group`
        

    .. py:method:: delete(id: str)

        Delete a group.
        
        Deletes a group from the Databricks account.
        
        :param id: str
          Unique ID for a group in the Databricks account.
        
        
        

    .. py:method:: get(id: str) -> Group

        Get group details.
        
        Gets the information for a specific group in the Databricks account.
        
        :param id: str
          Unique ID for a group in the Databricks account.
        
        :returns: :class:`Group`
        

    .. py:method:: list( [, attributes: Optional[str], count: Optional[int], excluded_attributes: Optional[str], filter: Optional[str], sort_by: Optional[str], sort_order: Optional[ListSortOrder], start_index: Optional[int]]) -> Iterator[Group]

        List group details.
        
        Gets all details of the groups associated with the Databricks account.
        
        :param attributes: str (optional)
          Comma-separated list of attributes to return in response.
        :param count: int (optional)
          Desired number of results per page. Default is 10000.
        :param excluded_attributes: str (optional)
          Comma-separated list of attributes to exclude in response.
        :param filter: str (optional)
          Query by which the results have to be filtered. Supported operators are equals(`eq`),
          contains(`co`), starts with(`sw`) and not equals(`ne`). Additionally, simple expressions can be
          formed using logical operators - `and` and `or`. The [SCIM RFC] has more details but we currently
          only support simple expressions.
          
          [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2
        :param sort_by: str (optional)
          Attribute to sort the results.
        :param sort_order: :class:`ListSortOrder` (optional)
          The order to sort the results.
        :param start_index: int (optional)
          Specifies the index of the first result. First item is number 1.
        
        :returns: Iterator over :class:`Group`
        

    .. py:method:: patch(id: str [, operations: Optional[List[Patch]], schemas: Optional[List[PatchSchema]]])

        Update group details.
        
        Partially updates the details of a group.
        
        :param id: str
          Unique ID for a group in the Databricks account.
        :param operations: List[:class:`Patch`] (optional)
        :param schemas: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].
        
        
        

    .. py:method:: update(id: str [, display_name: Optional[str], entitlements: Optional[List[ComplexValue]], external_id: Optional[str], groups: Optional[List[ComplexValue]], members: Optional[List[ComplexValue]], meta: Optional[ResourceMeta], roles: Optional[List[ComplexValue]], schemas: Optional[List[GroupSchema]]])

        Replace a group.
        
        Updates the details of a group by replacing the entire group entity.
        
        :param id: str
          Databricks group ID
        :param display_name: str (optional)
          String that represents a human-readable group name
        :param entitlements: List[:class:`ComplexValue`] (optional)
          Entitlements assigned to the group. See [assigning entitlements] for a full list of supported
          values.
          
          [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param members: List[:class:`ComplexValue`] (optional)
        :param meta: :class:`ResourceMeta` (optional)
          Container for the group identifier. Workspace local versus account.
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`GroupSchema`] (optional)
          The schema of the group.
        
        
        
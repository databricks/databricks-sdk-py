Groups
======
.. py:class:: GroupsAPI

    Groups simplify identity management, making it easier to assign access to Databricks workspace, data, and
    other securable objects.
    
    It is best practice to assign access to workspaces and access-control policies in Unity Catalog to groups,
    instead of to users individually. All Databricks workspace identities can be assigned as members of
    groups, and members inherit permissions that are assigned to their group.

    .. py:method:: create( [, display_name, entitlements, external_id, groups, id, members, roles])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            group = w.groups.create(display_name=f'sdk-{time.time_ns()}')
            
            # cleanup
            w.groups.delete(delete=group.id)

        Create a new group.
        
        Creates a group in the Databricks workspace with a unique name, using the supplied group details.
        
        :param display_name: str (optional)
          String that represents a human-readable group name
        :param entitlements: List[:class:`ComplexValue`] (optional)
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param id: str (optional)
          Databricks group ID
        :param members: List[:class:`ComplexValue`] (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
        
        :returns: :class:`Group`
        

    .. py:method:: delete(id)

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            group = w.groups.create(display_name=f'sdk-{time.time_ns()}')
            
            w.groups.delete(delete=group.id)

        Delete a group.
        
        Deletes a group from the Databricks workspace.
        
        :param id: str
          Unique ID for a group in the Databricks workspace.
        
        
        

    .. py:method:: get(id)

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            group = w.groups.create(display_name=f'sdk-{time.time_ns()}')
            
            fetch = w.groups.get(get=group.id)
            
            # cleanup
            w.groups.delete(delete=group.id)

        Get group details.
        
        Gets the information for a specific group in the Databricks workspace.
        
        :param id: str
          Unique ID for a group in the Databricks workspace.
        
        :returns: :class:`Group`
        

    .. py:method:: list( [, attributes, count, excluded_attributes, filter, sort_by, sort_order, start_index])

        List group details.
        
        Gets all details of the groups associated with the Databricks workspace.
        
        :param attributes: str (optional)
          Comma-separated list of attributes to return in response.
        :param count: int (optional)
          Desired number of results per page.
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
        

    .. py:method:: patch(id [, operations])

        Update group details.
        
        Partially updates the details of a group.
        
        :param id: str
          Unique ID for a group in the Databricks workspace.
        :param operations: List[:class:`Patch`] (optional)
        
        
        

    .. py:method:: update(id [, display_name, entitlements, external_id, groups, members, roles])

        Replace a group.
        
        Updates the details of a group by replacing the entire group entity.
        
        :param id: str
          Databricks group ID
        :param display_name: str (optional)
          String that represents a human-readable group name
        :param entitlements: List[:class:`ComplexValue`] (optional)
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param members: List[:class:`ComplexValue`] (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
        
        
        
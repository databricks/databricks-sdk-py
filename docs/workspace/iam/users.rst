``w.users``: Users
==================
.. currentmodule:: databricks.sdk.service.iam

.. py:class:: UsersAPI

    User identities recognized by Databricks and represented by email addresses.
    
    Databricks recommends using SCIM provisioning to sync users and groups automatically from your identity
    provider to your Databricks workspace. SCIM streamlines onboarding a new employee or team by using your
    identity provider to create users and groups in Databricks workspace and give them the proper level of
    access. When a user leaves your organization or no longer needs access to Databricks workspace, admins can
    terminate the user in your identity provider and that user’s account will also be removed from
    Databricks workspace. This ensures a consistent offboarding process and prevents unauthorized users from
    accessing sensitive data.

    .. py:method:: create( [, active: Optional[bool], display_name: Optional[str], emails: Optional[List[ComplexValue]], entitlements: Optional[List[ComplexValue]], external_id: Optional[str], groups: Optional[List[ComplexValue]], id: Optional[str], name: Optional[Name], roles: Optional[List[ComplexValue]], schemas: Optional[List[UserSchema]], user_name: Optional[str]]) -> User


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            user = w.users.create(display_name=f'sdk-{time.time_ns()}', user_name=f'sdk-{time.time_ns()}@example.com')

        Create a new user.
        
        Creates a new user in the Databricks workspace. This new user will also be added to the Databricks
        account.
        
        :param active: bool (optional)
          If this user is active
        :param display_name: str (optional)
          String that represents a concatenation of given and family names. For example `John Smith`. This
          field cannot be updated through the Workspace SCIM APIs when [identity federation is enabled]. Use
          Account SCIM APIs to update `displayName`.
          
          [identity federation is enabled]: https://docs.databricks.com/administration-guide/users-groups/best-practices.html#enable-identity-federation
        :param emails: List[:class:`ComplexValue`] (optional)
          All the emails associated with the Databricks user.
        :param entitlements: List[:class:`ComplexValue`] (optional)
          Entitlements assigned to the user. See [assigning entitlements] for a full list of supported values.
          
          [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
        :param external_id: str (optional)
          External ID is not currently supported. It is reserved for future use.
        :param groups: List[:class:`ComplexValue`] (optional)
        :param id: str (optional)
          Databricks user ID. This is automatically set by Databricks. Any value provided by the client will
          be ignored.
        :param name: :class:`Name` (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`UserSchema`] (optional)
          The schema of the user.
        :param user_name: str (optional)
          Email address of the Databricks user.
        
        :returns: :class:`User`
        

    .. py:method:: delete(id: str)


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            other_owner = w.users.create(user_name=f'sdk-{time.time_ns()}@example.com')
            
            w.users.delete(id=other_owner.id)

        Delete a user.
        
        Deletes a user. Deleting a user from a Databricks workspace also removes objects associated with the
        user.
        
        :param id: str
          Unique ID for a user in the Databricks workspace.
        
        
        

    .. py:method:: get(id: str [, attributes: Optional[str], count: Optional[int], excluded_attributes: Optional[str], filter: Optional[str], sort_by: Optional[str], sort_order: Optional[GetSortOrder], start_index: Optional[int]]) -> User


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            user = w.users.create(display_name=f'sdk-{time.time_ns()}', user_name=f'sdk-{time.time_ns()}@example.com')
            
            fetch = w.users.get(id=user.id)

        Get user details.
        
        Gets information for a specific user in Databricks workspace.
        
        :param id: str
          Unique ID for a user in the Databricks workspace.
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
          Attribute to sort the results. Multi-part paths are supported. For example, `userName`,
          `name.givenName`, and `emails`.
        :param sort_order: :class:`GetSortOrder` (optional)
          The order to sort the results.
        :param start_index: int (optional)
          Specifies the index of the first result. First item is number 1.
        
        :returns: :class:`User`
        

    .. py:method:: get_permission_levels() -> GetPasswordPermissionLevelsResponse

        Get password permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :returns: :class:`GetPasswordPermissionLevelsResponse`
        

    .. py:method:: get_permissions() -> PasswordPermissions

        Get password permissions.
        
        Gets the permissions of all passwords. Passwords can inherit permissions from their root object.
        
        :returns: :class:`PasswordPermissions`
        

    .. py:method:: list( [, attributes: Optional[str], count: Optional[int], excluded_attributes: Optional[str], filter: Optional[str], sort_by: Optional[str], sort_order: Optional[ListSortOrder], start_index: Optional[int]]) -> Iterator[User]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import iam
            
            w = WorkspaceClient()
            
            all_users = w.users.list(attributes="id,userName",
                                     sort_by="userName",
                                     sort_order=iam.ListSortOrder.DESCENDING)

        List users.
        
        Gets details for all the users associated with a Databricks workspace.
        
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
          Attribute to sort the results. Multi-part paths are supported. For example, `userName`,
          `name.givenName`, and `emails`.
        :param sort_order: :class:`ListSortOrder` (optional)
          The order to sort the results.
        :param start_index: int (optional)
          Specifies the index of the first result. First item is number 1.
        
        :returns: Iterator over :class:`User`
        

    .. py:method:: patch(id: str [, operations: Optional[List[Patch]], schemas: Optional[List[PatchSchema]]])


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import iam
            
            w = WorkspaceClient()
            
            user = w.users.create(display_name=f'sdk-{time.time_ns()}', user_name=f'sdk-{time.time_ns()}@example.com')
            
            w.users.patch(id=user.id,
                          operations=[iam.Patch(op=iam.PatchOp.REPLACE, path="active", value="false")],
                          schemas=[iam.PatchSchema.URN_IETF_PARAMS_SCIM_API_MESSAGES_2_0_PATCH_OP])

        Update user details.
        
        Partially updates a user resource by applying the supplied operations on specific user attributes.
        
        :param id: str
          Unique ID for a user in the Databricks workspace.
        :param operations: List[:class:`Patch`] (optional)
        :param schemas: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].
        
        
        

    .. py:method:: set_permissions( [, access_control_list: Optional[List[PasswordAccessControlRequest]]]) -> PasswordPermissions

        Set password permissions.
        
        Sets permissions on all passwords. Passwords can inherit permissions from their root object.
        
        :param access_control_list: List[:class:`PasswordAccessControlRequest`] (optional)
        
        :returns: :class:`PasswordPermissions`
        

    .. py:method:: update(id: str [, active: Optional[bool], display_name: Optional[str], emails: Optional[List[ComplexValue]], entitlements: Optional[List[ComplexValue]], external_id: Optional[str], groups: Optional[List[ComplexValue]], name: Optional[Name], roles: Optional[List[ComplexValue]], schemas: Optional[List[UserSchema]], user_name: Optional[str]])


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            user = w.users.create(display_name=f'sdk-{time.time_ns()}', user_name=f'sdk-{time.time_ns()}@example.com')
            
            w.users.update(id=user.id, user_name=user.user_name, active=True)

        Replace a user.
        
        Replaces a user's information with the data supplied in request.
        
        :param id: str
          Databricks user ID. This is automatically set by Databricks. Any value provided by the client will
          be ignored.
        :param active: bool (optional)
          If this user is active
        :param display_name: str (optional)
          String that represents a concatenation of given and family names. For example `John Smith`. This
          field cannot be updated through the Workspace SCIM APIs when [identity federation is enabled]. Use
          Account SCIM APIs to update `displayName`.
          
          [identity federation is enabled]: https://docs.databricks.com/administration-guide/users-groups/best-practices.html#enable-identity-federation
        :param emails: List[:class:`ComplexValue`] (optional)
          All the emails associated with the Databricks user.
        :param entitlements: List[:class:`ComplexValue`] (optional)
          Entitlements assigned to the user. See [assigning entitlements] for a full list of supported values.
          
          [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
        :param external_id: str (optional)
          External ID is not currently supported. It is reserved for future use.
        :param groups: List[:class:`ComplexValue`] (optional)
        :param name: :class:`Name` (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`UserSchema`] (optional)
          The schema of the user.
        :param user_name: str (optional)
          Email address of the Databricks user.
        
        
        

    .. py:method:: update_permissions( [, access_control_list: Optional[List[PasswordAccessControlRequest]]]) -> PasswordPermissions

        Update password permissions.
        
        Updates the permissions on all passwords. Passwords can inherit permissions from their root object.
        
        :param access_control_list: List[:class:`PasswordAccessControlRequest`] (optional)
        
        :returns: :class:`PasswordPermissions`
        
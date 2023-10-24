Account Users
=============
.. py:class:: AccountUsersAPI

    User identities recognized by Databricks and represented by email addresses.
    
    Databricks recommends using SCIM provisioning to sync users and groups automatically from your identity
    provider to your Databricks account. SCIM streamlines onboarding a new employee or team by using your
    identity provider to create users and groups in Databricks account and give them the proper level of
    access. When a user leaves your organization or no longer needs access to Databricks account, admins can
    terminate the user in your identity provider and that user’s account will also be removed from
    Databricks account. This ensures a consistent offboarding process and prevents unauthorized users from
    accessing sensitive data.

    .. py:method:: create( [, active, display_name, emails, entitlements, external_id, groups, id, name, roles, schemas, user_name])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            user = a.users.create(display_name=f'sdk-{time.time_ns()}', user_name=f'sdk-{time.time_ns()}@example.com')
            
            # cleanup
            a.users.delete(id=user.id)

        Create a new user.
        
        Creates a new user in the Databricks account. This new user will also be added to the Databricks
        account.
        
        :param active: bool (optional)
          If this user is active
        :param display_name: str (optional)
          String that represents a concatenation of given and family names. For example `John Smith`.
        :param emails: List[:class:`ComplexValue`] (optional)
          All the emails associated with the Databricks user.
        :param entitlements: List[:class:`ComplexValue`] (optional)
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param id: str (optional)
          Databricks user ID.
        :param name: :class:`Name` (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`UserSchema`] (optional)
          The schema of the user.
        :param user_name: str (optional)
          Email address of the Databricks user.
        
        :returns: :class:`User`
        

    .. py:method:: delete(id)

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            other_owner = w.users.create(user_name=f'sdk-{time.time_ns()}@example.com')
            
            w.users.delete(id=other_owner.id)

        Delete a user.
        
        Deletes a user. Deleting a user from a Databricks account also removes objects associated with the
        user.
        
        :param id: str
          Unique ID for a user in the Databricks account.
        
        
        

    .. py:method:: get(id [, attributes, count, excluded_attributes, filter, sort_by, sort_order, start_index])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            user = a.users.create(display_name=f'sdk-{time.time_ns()}', user_name=f'sdk-{time.time_ns()}@example.com')
            
            by_id = a.users.get(id=user.id)
            
            # cleanup
            a.users.delete(id=user.id)

        Get user details.
        
        Gets information for a specific user in Databricks account.
        
        :param id: str
          Unique ID for a user in the Databricks account.
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
          Attribute to sort the results. Multi-part paths are supported. For example, `userName`,
          `name.givenName`, and `emails`.
        :param sort_order: :class:`GetSortOrder` (optional)
          The order to sort the results.
        :param start_index: int (optional)
          Specifies the index of the first result. First item is number 1.
        
        :returns: :class:`User`
        

    .. py:method:: list( [, attributes, count, excluded_attributes, filter, sort_by, sort_order, start_index])

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import iam
            
            w = WorkspaceClient()
            
            all_users = w.users.list(attributes="id,userName",
                                     sort_by="userName",
                                     sort_order=iam.ListSortOrder.DESCENDING)

        List users.
        
        Gets details for all the users associated with a Databricks account.
        
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
          Attribute to sort the results. Multi-part paths are supported. For example, `userName`,
          `name.givenName`, and `emails`.
        :param sort_order: :class:`ListSortOrder` (optional)
          The order to sort the results.
        :param start_index: int (optional)
          Specifies the index of the first result. First item is number 1.
        
        :returns: Iterator over :class:`User`
        

    .. py:method:: patch(id [, operations, schemas])

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
          Unique ID for a user in the Databricks account.
        :param operations: List[:class:`Patch`] (optional)
        :param schemas: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].
        
        
        

    .. py:method:: update(id [, active, display_name, emails, entitlements, external_id, groups, name, roles, schemas, user_name])

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
          Databricks user ID.
        :param active: bool (optional)
          If this user is active
        :param display_name: str (optional)
          String that represents a concatenation of given and family names. For example `John Smith`.
        :param emails: List[:class:`ComplexValue`] (optional)
          All the emails associated with the Databricks user.
        :param entitlements: List[:class:`ComplexValue`] (optional)
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param name: :class:`Name` (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`UserSchema`] (optional)
          The schema of the user.
        :param user_name: str (optional)
          Email address of the Databricks user.
        
        
        
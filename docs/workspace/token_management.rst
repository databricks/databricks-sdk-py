``w.token_management``: Token management
========================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: TokenManagementAPI

    Enables administrators to get all tokens and delete tokens for other users. Admins can either get every
    token, get a specific token by ID, or get all tokens for a particular user.

    .. py:method:: create_obo_token(application_id: str, lifetime_seconds: int [, comment: Optional[str]]) -> CreateOboTokenResponse


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import iam
            
            w = WorkspaceClient()
            
            groups = w.groups.group_display_name_to_id_map(iam.ListGroupsRequest())
            
            spn = w.service_principals.create(display_name=f'sdk-{time.time_ns()}',
                                              groups=[iam.ComplexValue(value=groups["admins"])])
            
            obo = w.token_management.create_obo_token(application_id=spn.application_id, lifetime_seconds=60)
            
            # cleanup
            w.service_principals.delete(id=spn.id)
            w.token_management.delete(token_id=obo.token_info.token_id)

        Create on-behalf token.
        
        Creates a token on behalf of a service principal.
        
        :param application_id: str
          Application ID of the service principal.
        :param lifetime_seconds: int
          The number of seconds before the token expires.
        :param comment: str (optional)
          Comment that describes the purpose of the token.
        
        :returns: :class:`CreateOboTokenResponse`
        

    .. py:method:: delete(token_id: str)

        Delete a token.
        
        Deletes a token, specified by its ID.
        
        :param token_id: str
          The ID of the token to get.
        
        
        

    .. py:method:: get(token_id: str) -> TokenInfo


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import iam
            
            w = WorkspaceClient()
            
            groups = w.groups.group_display_name_to_id_map(iam.ListGroupsRequest())
            
            spn = w.service_principals.create(display_name=f'sdk-{time.time_ns()}',
                                              groups=[iam.ComplexValue(value=groups["admins"])])
            
            obo = w.token_management.create_obo_token(application_id=spn.application_id, lifetime_seconds=60)
            
            by_id = w.token_management.get(token_id=obo.token_info.token_id)
            
            # cleanup
            w.service_principals.delete(id=spn.id)
            w.token_management.delete(token_id=obo.token_info.token_id)

        Get token info.
        
        Gets information about a token, specified by its ID.
        
        :param token_id: str
          The ID of the token to get.
        
        :returns: :class:`TokenInfo`
        

    .. py:method:: get_permission_levels() -> GetTokenPermissionLevelsResponse

        Get token permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :returns: :class:`GetTokenPermissionLevelsResponse`
        

    .. py:method:: get_permissions() -> TokenPermissions

        Get token permissions.
        
        Gets the permissions of all tokens. Tokens can inherit permissions from their root object.
        
        :returns: :class:`TokenPermissions`
        

    .. py:method:: list( [, created_by_id: Optional[str], created_by_username: Optional[str]]) -> Iterator[TokenInfo]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import settings
            
            w = WorkspaceClient()
            
            all = w.token_management.list(settings.ListTokenManagementRequest())

        List all tokens.
        
        Lists all tokens associated with the specified workspace or user.
        
        :param created_by_id: str (optional)
          User ID of the user that created the token.
        :param created_by_username: str (optional)
          Username of the user that created the token.
        
        :returns: Iterator over :class:`TokenInfo`
        

    .. py:method:: set_permissions( [, access_control_list: Optional[List[TokenAccessControlRequest]]]) -> TokenPermissions

        Set token permissions.
        
        Sets permissions on all tokens. Tokens can inherit permissions from their root object.
        
        :param access_control_list: List[:class:`TokenAccessControlRequest`] (optional)
        
        :returns: :class:`TokenPermissions`
        

    .. py:method:: update_permissions( [, access_control_list: Optional[List[TokenAccessControlRequest]]]) -> TokenPermissions

        Update token permissions.
        
        Updates the permissions on all tokens. Tokens can inherit permissions from their root object.
        
        :param access_control_list: List[:class:`TokenAccessControlRequest`] (optional)
        
        :returns: :class:`TokenPermissions`
        
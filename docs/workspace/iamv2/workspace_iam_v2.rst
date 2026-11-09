``w.workspace_iam_v2``: workspace_iam.v2
========================================
.. currentmodule:: databricks.sdk.service.iamv2

.. py:class:: WorkspaceIamV2API

    These APIs are used to manage identities and the workspace access of these identities in Databricks.

    .. py:method:: create_direct_group_member_proxy(parent: str, direct_group_member: DirectGroupMember) -> DirectGroupMember

        Adds a user, service principal, or group as a direct member of a group in the account that contains
        this workspace.

        If automatic identity management is on and the group has an ``external_id``, its members come from
        your identity provider and can't be changed in Databricks.

        :param parent: str
          The resource name of the group to add the member to, in the format ``groups/{group_id}``.
        :param direct_group_member: :class:`DirectGroupMember`
          The member to add. Set its ``principal_id``.

        :returns: :class:`DirectGroupMember`
        

    .. py:method:: create_group_proxy(group: Group [, parent: Optional[str]]) -> Group

        Creates a local group in the account that contains this workspace. A local group is a group that isn't
        synced from your identity provider (IdP). You become a manager of the new group.

        If automatic identity management is on, you can't set ``external_id``. To add a group from your IdP,
        get it as an external group instead.

        :param group: :class:`Group`
          The group to create.
        :param parent: str (optional)
          The resource name of the account to create the group in, in the format ``accounts/{account_id}``.
          Defaults to the account that contains this workspace. Any other account is rejected.

        :returns: :class:`Group`
        

    .. py:method:: create_service_principal_proxy(service_principal: ServicePrincipal [, parent: Optional[str]]) -> ServicePrincipal

        Creates a local service principal in the account that contains this workspace. A local service
        principal is one that isn't synced from your identity provider (IdP).

        If automatic identity management is on, you can't set ``external_id``. To add a service principal from
        your IdP, get it as an external service principal instead.

        :param service_principal: :class:`ServicePrincipal`
          The service principal to create.
        :param parent: str (optional)
          The resource name of the account to create the service principal in, in the format
          ``accounts/{account_id}``. Defaults to the account that contains this workspace. Any other account
          is rejected.

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: create_user_proxy(user: User [, parent: Optional[str]]) -> User

        Creates a local user in the account that contains this workspace. A local user is a user that isn't
        synced from your identity provider (IdP).

        If automatic identity management is on, you can't set ``external_id``. To add a user from your IdP,
        get them as an external user instead.

        :param user: :class:`User`
          The user to create.
        :param parent: str (optional)
          The resource name of the account to create the user in, in the format ``accounts/{account_id}``.
          Defaults to the account that contains this workspace. Any other account is rejected.

        :returns: :class:`User`
        

    .. py:method:: create_workspace_assignment_detail_proxy(workspace_assignment_detail: WorkspaceAssignmentDetail) -> WorkspaceAssignmentDetail

        Creates a workspace assignment detail for a principal in the calling workspace.

        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be created in Databricks.

        :returns: :class:`WorkspaceAssignmentDetail`
        

    .. py:method:: create_workspace_assignment_proxy(workspace_assignment: WorkspaceAssignment [, parent: Optional[str]]) -> WorkspaceAssignment

        Assigns a user, service principal, or group directly to this workspace with the given entitlements.
        Returns an error if the principal is already assigned directly.

        Entitlements are granted one at a time. If the request fails partway through, the principal stays
        assigned with only some of the entitlements. Get the assignment afterwards to check which were
        granted.

        :param workspace_assignment: :class:`WorkspaceAssignment`
          The assignment to create. Set its ``principal_id`` and ``entitlements``.
        :param parent: str (optional)
          The resource name of the workspace, in the format
          ``accounts/{account_id}/workspaces/{workspace_id}``. Defaults to this workspace. Any other workspace
          is rejected.

        :returns: :class:`WorkspaceAssignment`
        

    .. py:method:: delete_direct_group_member_proxy(name: str)

        Removes a direct member from a group in the account that contains this workspace.

        If automatic identity management is on and the group has an ``external_id``, its members come from
        your identity provider and can't be changed in Databricks.

        :param name: str
          The resource name of the membership, in the format
          ``groups/{group_id}/direct-members/{principal_id}``.


        

    .. py:method:: delete_group_proxy(name: str)

        Deletes a group from the account that contains this workspace and removes it from the workspaces it's
        assigned to.

        :param name: str
          The resource name of the group, in the format ``groups/{group_id}``.


        

    .. py:method:: delete_service_principal_proxy(name: str)

        Deletes a service principal from the account that contains this workspace and removes it from the
        workspaces it's assigned to. You can't delete service principals that Databricks manages.

        :param name: str
          The resource name of the service principal, in the format
          ``service-principals/{service_principal_id}``.


        

    .. py:method:: delete_user_proxy(name: str)

        Deletes a user from the account that contains this workspace and removes them from the workspaces
        they're assigned to.

        :param name: str
          The resource name of the user, in the format ``users/{user_id}``.


        

    .. py:method:: delete_workspace_assignment_detail_proxy(principal_id: int)

        Deletes a workspace assignment detail for a principal in the calling workspace, revoking all of its
        entitlements. Entitlements are revoked one at a time rather than atomically. If the request fails
        partway through, the principal stays assigned with some of its original entitlements. Retrying is
        safe.

        :param principal_id: int
          Required. ID of the principal in Databricks to delete workspace assignment for.


        

    .. py:method:: delete_workspace_assignment_proxy(name: str)

        Removes a principal's direct assignment to this workspace and revokes the entitlements it granted. The
        principal keeps any access it gets through groups.

        Entitlements are revoked one at a time. If the request fails partway through, the principal stays
        assigned with some of its entitlements. You can retry the request.

        :param name: str
          The resource name of the assignment, in the format ``workspace-assignments/{principal_id}``.


        

    .. py:method:: get_direct_group_member_proxy(name: str) -> DirectGroupMember

        Gets a direct member of a group in the account that contains this workspace, including where the
        membership comes from. Returns an error if the principal isn't a direct member.

        :param name: str
          The resource name of the membership, in the format
          ``groups/{group_id}/direct-members/{principal_id}``.

        :returns: :class:`DirectGroupMember`
        

    .. py:method:: get_external_group_proxy(name: str) -> ExternalGroup

        Gets a group by its ID in your identity provider (IdP) and syncs its name and parent groups from your
        IdP. If the group isn't in the account that contains this workspace yet, it's added. Requires
        automatic identity management. If your account has group visibility filters, the group must match
        them.

        :param name: str
          The resource name of the external group, in the format ``external-groups/{external_group_id}``.

        :returns: :class:`ExternalGroup`
        

    .. py:method:: get_external_service_principal_proxy(name: str) -> ExternalServicePrincipal

        Gets a service principal by its ID in your identity provider (IdP) and syncs its details and group
        memberships from your IdP. If the service principal isn't in the account that contains this workspace
        yet, it's added. Requires automatic identity management with Microsoft Entra ID as your IdP.

        :param name: str
          The resource name of the external service principal, in the format
          ``external-service-principals/{external_service_principal_id}``.

        :returns: :class:`ExternalServicePrincipal`
        

    .. py:method:: get_external_user_proxy(name: str) -> ExternalUser

        Gets a user by their ID in your identity provider (IdP) and syncs their details and group memberships
        from your IdP. If the user isn't in the account that contains this workspace yet, they're added.
        Requires automatic identity management.

        :param name: str
          The resource name of the external user, in the format ``external-users/{external_user_id}``.

        :returns: :class:`ExternalUser`
        

    .. py:method:: get_group_proxy(name: str) -> Group

        Gets a group in the account that contains this workspace by its Databricks ID.

        :param name: str
          The resource name of the group, in the format ``groups/{group_id}``.

        :returns: :class:`Group`
        

    .. py:method:: get_service_principal_proxy(name: str) -> ServicePrincipal

        Gets a service principal in the account that contains this workspace by its Databricks ID.

        :param name: str
          The resource name of the service principal, in the format
          ``service-principals/{service_principal_id}``.

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: get_user_proxy(name: str) -> User

        Gets a user in the account that contains this workspace by their Databricks ID.

        :param name: str
          The resource name of the user, in the format ``users/{user_id}``.

        :returns: :class:`User`
        

    .. py:method:: get_workspace_access_detail_local(name: str [, view: Optional[WorkspaceAccessDetailView]]) -> WorkspaceAccessDetail

        Returns the access details for a principal in the current workspace. Allows for checking access
        details for any provisioned principal (user, service principal, or group) in the current workspace.

        - Provisioned principal here refers to one that has been synced into Databricks from the customer's
          IdP or added explicitly to Databricks via SCIM/UI. Allows for passing in a "view" parameter to
          control what fields are returned (BASIC by default or FULL).

        :param name: str
          The resource name of the workspace access detail. Format: workspace-access-details/{principal_id}
        :param view: :class:`WorkspaceAccessDetailView` (optional)
          Controls what fields are returned.

        :returns: :class:`WorkspaceAccessDetail`
        

    .. py:method:: get_workspace_assignment_detail_proxy(principal_id: int) -> WorkspaceAssignmentDetail

        Returns the assignment details for a principal in the calling workspace.

        :param principal_id: int
          Required. The internal ID of the principal (user/sp/group) for which the assignment details are
          being requested.

        :returns: :class:`WorkspaceAssignmentDetail`
        

    .. py:method:: get_workspace_assignment_proxy(name: str) -> WorkspaceAssignment

        Gets a principal's direct assignment to this workspace, including its effective entitlements. Returns
        an error if the principal isn't assigned directly.

        :param name: str
          The resource name of the assignment, in the format ``workspace-assignments/{principal_id}``.

        :returns: :class:`WorkspaceAssignment`
        

    .. py:method:: get_workspace_identity_detail(name: str) -> WorkspaceIdentityDetail

        Gets a principal's status in this workspace and whether it has access directly or through a group.
        Returns an error if the principal doesn't have access to the workspace.

        :param name: str
          The resource name of the workspace identity detail, in the format
          ``principals/{principal_id}/workspace-identity-detail``.

        :returns: :class:`WorkspaceIdentityDetail`
        

    .. py:method:: list_direct_group_members_proxy(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[DirectGroupMember]

        Lists the direct members of a group in the account that contains this workspace, sorted by display
        name, with where each membership comes from. Members in your identity provider who haven't been added
        to Databricks aren't included.

        :param parent: str
          The resource name of the group, in the format ``groups/{group_id}``.
        :param page_size: int (optional)
          The maximum number of members to return, up to 1000. The default is 1000. A page can contain fewer
          members.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.

        :returns: Iterator over :class:`DirectGroupMember`
        

    .. py:method:: list_groups_proxy( [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str], parent: Optional[str]]) -> Iterator[Group]

        Lists the groups in the account that contains this workspace, sorted by Databricks ID. Groups in your
        identity provider that haven't been added to Databricks aren't included.

        :param filter: str (optional)
          Filters groups by ``group_name`` or ``external_id``, for example ``group_name eq "Data engineers"``.
          Put the value in quotes.
        :param page_size: int (optional)
          The maximum number of groups to return, up to 1000. The default is 1000. A page can contain fewer
          groups.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.
        :param parent: str (optional)
          The resource name of the account to list groups in, in the format ``accounts/{account_id}``.
          Defaults to the account that contains this workspace. Any other account is rejected.

        :returns: Iterator over :class:`Group`
        

    .. py:method:: list_service_principals_proxy( [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str], parent: Optional[str]]) -> Iterator[ServicePrincipal]

        Lists the service principals in the account that contains this workspace, sorted by Databricks ID.
        Service principals in your identity provider that haven't been added to Databricks aren't included.

        :param filter: str (optional)
          Filters service principals by ``application_id`` or ``external_id``, for example ``application_id eq
          "<application-id>"``. Put the value in quotes.
        :param page_size: int (optional)
          The maximum number of service principals to return, up to 1000. The default is 1000. A page can
          contain fewer service principals.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.
        :param parent: str (optional)
          The resource name of the account to list service principals in, in the format
          ``accounts/{account_id}``. Defaults to the account that contains this workspace. Any other account
          is rejected.

        :returns: Iterator over :class:`ServicePrincipal`
        

    .. py:method:: list_transitive_parent_groups_proxy(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> ListTransitiveParentGroupsResponse

        Lists every group that a user, service principal, or group belongs to, directly or through other
        groups, in the account that contains this workspace. Results are sorted by Databricks ID. If automatic
        identity management is on, the principal's group memberships are synced from your identity provider
        first.

        :param parent: str
          The user, service principal, or group whose parent groups to list, in the format
          ``principals/{principal_id}``.
        :param page_size: int (optional)
          The maximum number of groups to return, up to 1000. The default is 1000. A page can contain fewer
          groups.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.

        :returns: :class:`ListTransitiveParentGroupsResponse`
        

    .. py:method:: list_users_proxy( [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str], parent: Optional[str]]) -> Iterator[User]

        Lists the users in the account that contains this workspace, sorted by Databricks ID. Users in your
        identity provider who haven't been added to Databricks aren't included.

        :param filter: str (optional)
          Filters users by ``username`` or ``external_id``, for example ``username eq "someone@example.com"``.
          Put the value in quotes.
        :param page_size: int (optional)
          The maximum number of users to return, up to 1000. The default is 1000. A page can contain fewer
          users.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.
        :param parent: str (optional)
          The resource name of the account to list users in, in the format ``accounts/{account_id}``. Defaults
          to the account that contains this workspace. Any other account is rejected.

        :returns: Iterator over :class:`User`
        

    .. py:method:: list_workspace_assignment_details_proxy( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[WorkspaceAssignmentDetail]

        Lists workspace assignment details for the calling workspace. The response omits the per-principal
        entitlement fields (``entitlements`` and ``effective_entitlements``). To read the entitlements for a
        single principal, get that principal's assignment detail.

        :param page_size: int (optional)
          The maximum number of workspace assignment details to return. The service may return fewer than this
          value. If not provided, defaults to 1000, which is also the maximum allowed. Requests for more than
          the maximum are clamped to 1000.
        :param page_token: str (optional)
          A page token from a previous list call. Provide this to retrieve the subsequent page.

        :returns: Iterator over :class:`WorkspaceAssignmentDetail`
        

    .. py:method:: list_workspace_assignments_proxy( [, page_size: Optional[int], page_token: Optional[str], parent: Optional[str]]) -> Iterator[WorkspaceAssignment]

        Lists the principals assigned directly to this workspace. The response leaves ``entitlements`` and
        ``effective_entitlements`` empty. To read a principal's entitlements, get its assignment.

        :param page_size: int (optional)
          The maximum number of assignments to return, up to 1000. The default is 1000. A page can contain
          fewer assignments.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.
        :param parent: str (optional)
          The resource name of the workspace, in the format
          ``accounts/{account_id}/workspaces/{workspace_id}``. Defaults to this workspace. Any other workspace
          is rejected.

        :returns: Iterator over :class:`WorkspaceAssignment`
        

    .. py:method:: resolve_group_proxy(external_id: str) -> ResolveGroupResponse

        Gets a group by its ID in your identity provider (IdP) and syncs its name and parent groups from your
        IdP. If the group isn't in the account that contains this workspace yet, it's added. Requires
        automatic identity management. If your account has group visibility filters, the group must match
        them.

        :param external_id: str
          The ID of the group in your IdP.

        :returns: :class:`ResolveGroupResponse`
        

    .. py:method:: resolve_service_principal_proxy(external_id: str) -> ResolveServicePrincipalResponse

        Gets a service principal by its ID in your identity provider (IdP) and syncs its details and group
        memberships from your IdP. If the service principal isn't in the account that contains this workspace
        yet, it's added. Requires automatic identity management with Microsoft Entra ID as your IdP.

        :param external_id: str
          The ID of the service principal in your IdP.

        :returns: :class:`ResolveServicePrincipalResponse`
        

    .. py:method:: resolve_user_proxy(external_id: str) -> ResolveUserResponse

        Gets a user by their ID in your identity provider (IdP) and syncs their details and group memberships
        from your IdP. If the user isn't in the account that contains this workspace yet, they're added.
        Requires automatic identity management.

        :param external_id: str
          The ID of the user in your IdP.

        :returns: :class:`ResolveUserResponse`
        

    .. py:method:: update_group_proxy(name: str, group: Group, update_mask: str) -> Group

        Updates a group in the account that contains this workspace. Only the fields in ``update_mask``
        change.

        If automatic identity management is on and the group has an ``external_id``, you can only update
        ``external_id``. The group's other fields come from your identity provider. If your account also has
        group visibility filters, a new ``external_id`` must match them. You can always clear ``external_id``.

        :param name: str
          The resource name of the group, in one of these formats:

          - Account APIs: ``accounts/{account_id}/groups/{group_id}``
          - Workspace APIs: ``groups/{group_id}``
        :param group: :class:`Group`
          The group to update. Its ``name`` identifies the group.
        :param update_mask: str
          The fields to update, separated by commas. You can update ``group_name`` and ``external_id``.

        :returns: :class:`Group`
        

    .. py:method:: update_service_principal_proxy(name: str, service_principal: ServicePrincipal, update_mask: str) -> ServicePrincipal

        Updates a service principal in the account that contains this workspace. Only the fields in
        ``update_mask`` change.

        If automatic identity management is on and the service principal has an ``external_id``, you can only
        update ``external_id``. Its other fields come from your identity provider. A service principal can't
        deactivate itself, and you can't update service principals that Databricks manages.

        :param name: str
          The resource name of the service principal, in one of these formats:

          - Account APIs: ``accounts/{account_id}/service-principals/{service_principal_id}``
          - Workspace APIs: ``service-principals/{service_principal_id}``
        :param service_principal: :class:`ServicePrincipal`
          The service principal to update. Its ``name`` identifies the service principal.
        :param update_mask: str
          The fields to update, separated by commas. You can update ``display_name``, ``account_sp_status``,
          and ``external_id``.

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: update_user_proxy(name: str, user: User, update_mask: str) -> User

        Updates a user in the account that contains this workspace. Only the fields in ``update_mask`` change.

        If automatic identity management is on and the user has an ``external_id``, you can only update
        ``external_id``. The user's other fields come from your identity provider. You can't deactivate
        yourself or change the status of the account owner.

        :param name: str
          The resource name of the user, in one of these formats:

          - Account APIs: ``accounts/{account_id}/users/{user_id}``
          - Workspace APIs: ``users/{user_id}``
        :param user: :class:`User`
          The user to update. Its ``name`` identifies the user.
        :param update_mask: str
          The fields to update, separated by commas. You can update ``full_name.given_name``,
          ``full_name.family_name``, ``account_user_status``, and ``external_id``.

        :returns: :class:`User`
        

    .. py:method:: update_workspace_assignment_detail_proxy(principal_id: int, workspace_assignment_detail: WorkspaceAssignmentDetail, update_mask: FieldMask) -> WorkspaceAssignmentDetail

        Updates the entitlements of a directly assigned principal in the calling workspace. Changes are
        applied one at a time rather than atomically. If the request fails partway through, only some of the
        requested changes take effect. Get the assignment detail afterwards to confirm the final state.

        :param principal_id: int
          Required. ID of the principal in Databricks.
        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be updated in Databricks.
        :param update_mask: FieldMask
          Required. The list of fields to update.

        :returns: :class:`WorkspaceAssignmentDetail`
        

    .. py:method:: update_workspace_assignment_proxy(name: str, workspace_assignment: WorkspaceAssignment, update_mask: FieldMask) -> WorkspaceAssignment

        Replaces the entitlements of a principal's direct assignment to this workspace. The new list can't be
        empty.

        Entitlements are changed one at a time. If the request fails partway through, only some of the changes
        take effect. Get the assignment afterwards to check the result.

        :param name: str
          The resource name of the assignment, in one of these formats:

          - Account APIs:
            ``accounts/{account_id}/workspaces/{workspace_id}/workspace-assignments/{principal_id}``
          - Workspace APIs: ``workspace-assignments/{principal_id}``
        :param workspace_assignment: :class:`WorkspaceAssignment`
          The assignment to update. Its ``name`` identifies the assignment.
        :param update_mask: FieldMask
          The fields to update. The only supported field is ``entitlements``.

        :returns: :class:`WorkspaceAssignment`
        

    .. py:method:: update_workspace_identity_detail(name: str, workspace_identity_detail: WorkspaceIdentityDetail, update_mask: FieldMask) -> WorkspaceIdentityDetail

        Activates or deactivates a user or service principal in this workspace. You can only update
        ``workspace_identity_status``. You can't change your own status or the status of a group.

        :param name: str
          The resource name of the workspace identity detail, in the format
          ``principals/{principal_id}/workspace-identity-detail``.
        :param workspace_identity_detail: :class:`WorkspaceIdentityDetail`
          The workspace identity detail to update. Its ``name`` identifies the principal.
        :param update_mask: FieldMask
          The fields to update. The only supported field is ``workspace_identity_status``.

        :returns: :class:`WorkspaceIdentityDetail`
        
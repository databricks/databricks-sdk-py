``a.iam_v2``: account_iam.v2
============================
.. currentmodule:: databricks.sdk.service.iamv2

.. py:class:: AccountIamV2API

    These APIs are used to manage identities and the workspace access of these identities in Databricks.

    .. py:method:: create_direct_group_member(parent: str, direct_group_member: DirectGroupMember) -> DirectGroupMember

        Creates a group membership (assigns a principal to a group).

        Authorization: the caller must be an account admin or a manager of the group (holds the
        ``roles/group.manager`` role on it).

        :param parent: str
          The parent resource name of the group to add the member to. Format:
          accounts/{account_id}/groups/{group_id}
        :param direct_group_member: :class:`DirectGroupMember`
          Required. The direct group member to be added to the group.

        :returns: :class:`DirectGroupMember`
        

    .. py:method:: create_group(parent: str, group: Group) -> Group

        Creates a local group in the Databricks account and returns the created group. A local group is one
        that is not synced from the customer's identity provider, and can be created whether or not Account
        Identity Management (AIM) is enabled.

        When AIM is enabled, supplying an external ID returns an error. To provision the identity from your
        identity provider, resolve it by its external ID with ResolveGroup; to read an existing external
        identity, use the ExternalGroup resource.

        :param parent: str
          The parent resource name of the account in which to create the group. Format: accounts/{account_id}
        :param group: :class:`Group`
          Required. Group to be created in Databricks

        :returns: :class:`Group`
        

    .. py:method:: create_identity_visibility_filter(parent: str, identity_visibility_filter: IdentityVisibilityFilter [, identity_visibility_filter_id: Optional[str]]) -> IdentityVisibilityFilter

        Creates a group visibility filter in the account. Requires account admin privileges. Set
        ``principal_type`` to ``GROUP`` and specify exactly one of ``exact`` (external ID), ``prefix``
        (display-name starts with), or ``regex`` (full RE2 display-name match). The filter applies across all
        workspaces in the account. A duplicate filter ID or an existing rule with the same type and match
        value returns ``ALREADY_EXISTS``. Filters are immutable; to change a rule, delete it and create a new
        one.

        :param parent: str
          Required. The parent account. Format: accounts/{account_id}
        :param identity_visibility_filter: :class:`IdentityVisibilityFilter`
          Required. The filter to create. Set ``principal_type`` to ``GROUP`` and specify exactly one of
          ``exact``, ``prefix``, or ``regex``. The server assigns the resource name; any supplied ``name`` is
          ignored.
        :param identity_visibility_filter_id: str (optional)
          Optional. The ID to use for the filter, which becomes the final component of its resource name. If
          not specified or empty, the server generates one. Must not contain ``/``.

        :returns: :class:`IdentityVisibilityFilter`
        

    .. py:method:: create_service_principal(parent: str, service_principal: ServicePrincipal) -> ServicePrincipal

        Creates a local service principal in the Databricks account and returns the created service principal.
        A local service principal is one that is not synced from the customer's identity provider, and can be
        created whether or not Account Identity Management (AIM) is enabled.

        When AIM is enabled, supplying an external ID returns an error. To provision the identity from your
        identity provider, resolve it by its external ID with ResolveServicePrincipal; to read an existing
        external identity, use the ExternalServicePrincipal resource.

        :param parent: str
          The parent resource name of the account in which to create the service principal. Format:
          accounts/{account_id}
        :param service_principal: :class:`ServicePrincipal`
          Required. Service principal to be created in Databricks

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: create_user(parent: str, user: User) -> User

        Creates a local user in the Databricks account and returns the created user. A local user is one that
        is not synced from the customer's identity provider, and can be created whether or not Account
        Identity Management (AIM) is enabled.

        When AIM is enabled, supplying an external ID returns an error. To provision the identity from your
        identity provider, resolve it by its external ID with ResolveUser; to read an existing external
        identity, use the ExternalUser resource.

        :param parent: str
          The parent resource name of the account in which to create the user. Format: accounts/{account_id}
        :param user: :class:`User`
          Required. User to be created in Databricks

        :returns: :class:`User`
        

    .. py:method:: create_workspace_assignment(parent: str, workspace_assignment: WorkspaceAssignment) -> WorkspaceAssignment

        Creates a workspace assignment for a principal. Entitlements are granted one at a time rather than
        atomically. If the request fails partway through, the principal stays assigned to the workspace with
        only some of the requested entitlements. Get the assignment afterwards to confirm which entitlements
        were granted.

        :param parent: str
          The parent resource name of the workspace to assign the principal to. Format:
          accounts/{account_id}/workspaces/{workspace_id}
        :param workspace_assignment: :class:`WorkspaceAssignment`
          Required. Workspace assignment to be created in Databricks.

        :returns: :class:`WorkspaceAssignment`
        

    .. py:method:: create_workspace_assignment_detail(workspace_id: int, workspace_assignment_detail: WorkspaceAssignmentDetail) -> WorkspaceAssignmentDetail

        Creates a workspace assignment detail for a principal.

        :param workspace_id: int
          Required. The workspace ID for which the workspace assignment detail is being created.
        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be created in Databricks.

        :returns: :class:`WorkspaceAssignmentDetail`
        

    .. py:method:: delete_direct_group_member(name: str)

        Deletes a group membership (unassigns a principal from a group).

        Authorization: the caller must be an account admin or a manager of the group (holds the
        ``roles/group.manager`` role on it).

        :param name: str
          The resource name of the group membership. Format:
          accounts/{account_id}/groups/{group_id}/direct-members/{principal_id}


        

    .. py:method:: delete_group(name: str)

        Deletes a group from the Databricks account by its internal ID.

        Authorization: the caller must be an account admin or a manager of the group (holds the
        ``roles/group.manager`` role on it).

        :param name: str
          The resource name of the group. Format: accounts/{account_id}/groups/{group_id}


        

    .. py:method:: delete_identity_visibility_filter(name: str)

        Deletes a group visibility filter by its resource name. Requires account admin privileges. Deleting a
        filter does not delete groups or revoke access. Groups covered only by this rule stop being
        discoverable unless they or a transitive parent are already provisioned in the account. If no group
        filters remain, all groups become visible again. Deleting a filter that does not exist succeeds
        without making any changes.

        :param name: str
          Required. The resource name of the filter. Format:
          accounts/{account_id}/identity-visibility-filters/{identity_visibility_filter_id}


        

    .. py:method:: delete_service_principal(name: str)

        Deletes a service principal from the Databricks account by its internal ID.

        :param name: str
          The resource name of the service principal. Format:
          accounts/{account_id}/service-principals/{service_principal_id}


        

    .. py:method:: delete_user(name: str)

        Deletes a user from the Databricks account by its internal ID.

        :param name: str
          The resource name of the user. Format: accounts/{account_id}/users/{user_id}


        

    .. py:method:: delete_workspace_assignment(name: str)

        Deletes a workspace assignment for a principal, revoking all of its entitlements. Entitlements are
        revoked one at a time rather than atomically. If the request fails partway through, the principal
        stays assigned with some of its original entitlements. Retrying is safe.

        :param name: str
          The resource name of the workspace assignment. Format:
          accounts/{account_id}/workspaces/{workspace_id}/workspace-assignments/{principal_id}


        

    .. py:method:: delete_workspace_assignment_detail(workspace_id: int, principal_id: int)

        Deletes a workspace assignment detail for a principal, revoking all of its entitlements. Entitlements
        are revoked one at a time rather than atomically. If the request fails partway through, the principal
        stays assigned with some of its original entitlements. Retrying is safe.

        :param workspace_id: int
          The workspace ID where the principal has access.
        :param principal_id: int
          Required. ID of the principal in Databricks to delete workspace assignment for.


        

    .. py:method:: get_direct_group_member(name: str) -> DirectGroupMember

        Gets a provisioned direct member of a group.

        :param name: str
          The resource name of the group membership. Format:
          accounts/{account_id}/groups/{group_id}/direct-members/{principal_id}

        :returns: :class:`DirectGroupMember`
        

    .. py:method:: get_external_group(name: str) -> ExternalGroup

        Retrieves an external group with the given external ID from the customer's IdP. If the group does not
        exist, it will be created in the account. If the customer is not onboarded onto Automatic Identity
        Management (AIM), this will return an error.

        :param name: str
          Required. The resource name of the external group. Format:
          accounts/{account_id}/external-groups/{external_group_id}

        :returns: :class:`ExternalGroup`
        

    .. py:method:: get_external_service_principal(name: str) -> ExternalServicePrincipal

        Retrieves an external service principal with the given external ID from the customer's IdP. If the
        service principal does not exist, it will be created. If the customer is not onboarded onto Automatic
        Identity Management (AIM), this will return an error.

        :param name: str
          Required. The resource name of the external service principal. Format:
          accounts/{account_id}/external-service-principals/{external_service_principal_id}

        :returns: :class:`ExternalServicePrincipal`
        

    .. py:method:: get_external_user(name: str) -> ExternalUser

        Retrieves an external user with the given external ID from the customer's IdP. If the user does not
        exist, it will be created. If the customer is not onboarded onto Automatic Identity Management (AIM),
        this will return an error.

        :param name: str
          Required. The resource name of the external user. Format:
          accounts/{account_id}/external-users/{external_user_id}

        :returns: :class:`ExternalUser`
        

    .. py:method:: get_group(name: str) -> Group

        Fetches a group from the Databricks account by its internal ID.

        :param name: str
          The resource name of the group. Format: accounts/{account_id}/groups/{group_id}

        :returns: :class:`Group`
        

    .. py:method:: get_identity_visibility_filter(name: str) -> IdentityVisibilityFilter

        Gets a group visibility filter by its resource name. Requires account admin privileges. Returns the
        filter rule, not the groups matched by the rule.

        :param name: str
          Required. The resource name of the filter. Format:
          accounts/{account_id}/identity-visibility-filters/{identity_visibility_filter_id}

        :returns: :class:`IdentityVisibilityFilter`
        

    .. py:method:: get_service_principal(name: str) -> ServicePrincipal

        Fetches a service principal from the Databricks account by its internal ID.

        :param name: str
          The resource name of the service principal. Format:
          accounts/{account_id}/service-principals/{service_principal_id}

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: get_user(name: str) -> User

        Fetches a user from the Databricks account by its internal ID.

        :param name: str
          The resource name of the user. Format: accounts/{account_id}/users/{user_id}

        :returns: :class:`User`
        

    .. py:method:: get_workspace_access_detail(name: str [, view: Optional[WorkspaceAccessDetailView]]) -> WorkspaceAccessDetail

        Returns the access details for a principal in a workspace. Allows for checking access details for any
        provisioned principal (user, service principal, or group) in a workspace.

        - Provisioned principal here refers to one that has been synced into Databricks from the customer's
          IdP or added explicitly to Databricks via SCIM/UI. Allows for passing in a "view" parameter to
          control what fields are returned (BASIC by default or FULL).

        :param name: str
          The resource name of the workspace access detail. Format:
          accounts/{account_id}/workspaces/{workspace_id}/workspace-access-details/{principal_id}
        :param view: :class:`WorkspaceAccessDetailView` (optional)
          Controls what fields are returned.

        :returns: :class:`WorkspaceAccessDetail`
        

    .. py:method:: get_workspace_assignment(name: str) -> WorkspaceAssignment

        Returns the assignment for a principal in a workspace.

        :param name: str
          The resource name of the workspace assignment. Format:
          accounts/{account_id}/workspaces/{workspace_id}/workspace-assignments/{principal_id}

        :returns: :class:`WorkspaceAssignment`
        

    .. py:method:: get_workspace_assignment_detail(workspace_id: int, principal_id: int) -> WorkspaceAssignmentDetail

        Returns the assignment details for a principal in a workspace.

        :param workspace_id: int
          Required. The workspace ID for which the assignment details are being requested.
        :param principal_id: int
          Required. The internal ID of the principal (user/sp/group) for which the assignment details are
          being requested.

        :returns: :class:`WorkspaceAssignmentDetail`
        

    .. py:method:: list_direct_group_members(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[DirectGroupMember]

        Lists provisioned direct members of a group with their membership source (internal or from identity
        provider).

        :param parent: str
          The parent resource name of the group whose direct members to list. Format:
          accounts/{account_id}/groups/{group_id}
        :param page_size: int (optional)
          The maximum number of members to return. The service may return fewer than this value. If not
          provided, defaults to 1000, which is also the maximum allowed. Requests for more than the maximum
          are clamped to 1000.
        :param page_token: str (optional)
          A page token, received from a previous ListDirectGroupMembers call. Provide this to retrieve the
          subsequent page.

        :returns: Iterator over :class:`DirectGroupMember`
        

    .. py:method:: list_groups(parent: str [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Group]

        Lists the groups in the Databricks account, returning one page per call. Supports filtering by group
        name or external ID.

        :param parent: str
          The parent resource name of the account whose groups to list. Format: accounts/{account_id}
        :param filter: str (optional)
          Optional. Allows filtering groups by group name or external id.
        :param page_size: int (optional)
          The maximum number of groups to return. The service may return fewer than this value. If not
          provided, defaults to 1000, which is also the maximum allowed. Requests for more than the maximum
          are clamped to 1000.
        :param page_token: str (optional)
          A page token, received from a previous ListGroups call. Provide this to retrieve the subsequent
          page.

        :returns: Iterator over :class:`Group`
        

    .. py:method:: list_identity_visibility_filters(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[IdentityVisibilityFilter]

        Lists group visibility filters in the account, returning one page per call. Requires account admin
        privileges. Returns filter rules, not the groups matched by those rules. To retrieve the next page,
        pass the response's ``next_page_token`` as ``page_token`` in the next request. If ``next_page_token``
        is omitted, there are no more pages.

        :param parent: str
          Required. The parent account. Format: accounts/{account_id}
        :param page_size: int (optional)
          The maximum number of filters to return. The service may return fewer than this value. If omitted or
          non-positive, defaults to 100. Values above 1000 are reduced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous ListIdentityVisibilityFilters call. Provide this to retrieve
          the subsequent page.

        :returns: Iterator over :class:`IdentityVisibilityFilter`
        

    .. py:method:: list_service_principals(parent: str [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ServicePrincipal]

        Lists the service principals in the Databricks account, returning one page per call. Supports
        filtering by application ID or external ID.

        :param parent: str
          The parent resource name of the account whose service principals to list. Format:
          accounts/{account_id}
        :param filter: str (optional)
          Optional. Allows filtering service principals by application id or external id.
        :param page_size: int (optional)
          The maximum number of service principals to return. The service may return fewer than this value. If
          not provided, defaults to 1000, which is also the maximum allowed. Requests for more than the
          maximum are clamped to 1000.
        :param page_token: str (optional)
          A page token, received from a previous ListServicePrincipals call. Provide this to retrieve the
          subsequent page.

        :returns: Iterator over :class:`ServicePrincipal`
        

    .. py:method:: list_transitive_parent_groups(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> ListTransitiveParentGroupsResponse

        Lists all transitive parent groups of a principal.

        :param parent: str
          The parent resource name of the principal whose transitive parent groups to list. Format:
          accounts/{account_id}/principals/{principal_id}
        :param page_size: int (optional)
          The maximum number of parent groups to return. The service may return fewer than this value. If not
          provided, defaults to 1000, which is also the maximum allowed. Requests for more than the maximum
          are clamped to 1000.
        :param page_token: str (optional)
          A page token, received from a previous ListTransitiveParentGroups call. Provide this to retrieve the
          subsequent page.

        :returns: :class:`ListTransitiveParentGroupsResponse`
        

    .. py:method:: list_users(parent: str [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> Iterator[User]

        Lists the users in the Databricks account, returning one page per call. Supports filtering by username
        or external ID.

        :param parent: str
          The parent resource name of the account whose users to list. Format: accounts/{account_id}
        :param filter: str (optional)
          Optional. Allows filtering users by username or external id.
        :param page_size: int (optional)
          The maximum number of users to return. The service may return fewer than this value. If not
          provided, defaults to 1000, which is also the maximum allowed. Requests for more than the maximum
          are clamped to 1000.
        :param page_token: str (optional)
          A page token, received from a previous ListUsers call. Provide this to retrieve the subsequent page.

        :returns: Iterator over :class:`User`
        

    .. py:method:: list_workspace_assignment_details(workspace_id: int [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[WorkspaceAssignmentDetail]

        Lists workspace assignment details for a workspace. The response omits the per-principal entitlement
        fields (``entitlements`` and ``effective_entitlements``). To read the entitlements for a single
        principal, get that principal's assignment detail.

        :param workspace_id: int
          Required. The workspace ID for which the workspace assignment details are being fetched.
        :param page_size: int (optional)
          The maximum number of workspace assignment details to return. The service may return fewer than this
          value. If not provided, defaults to 1000, which is also the maximum allowed. Requests for more than
          the maximum are clamped to 1000.
        :param page_token: str (optional)
          A page token, received from a previous ListWorkspaceAssignmentDetails call. Provide this to retrieve
          the subsequent page.

        :returns: Iterator over :class:`WorkspaceAssignmentDetail`
        

    .. py:method:: list_workspace_assignments(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[WorkspaceAssignment]

        Lists workspace assignments for a workspace. The response omits the per-principal entitlement fields
        (``entitlements`` and ``effective_entitlements``). To read the entitlements for a single principal,
        get that principal's assignment.

        :param parent: str
          The parent resource name of the workspace whose assignments to list. Format:
          accounts/{account_id}/workspaces/{workspace_id}
        :param page_size: int (optional)
          The maximum number of workspace assignments to return. The service may return fewer than this value.
          If not provided, defaults to 1000, which is also the maximum allowed. Requests for more than the
          maximum are clamped to 1000.
        :param page_token: str (optional)
          A page token, received from a previous ListWorkspaceAssignments call. Provide this to retrieve the
          subsequent page.

        :returns: Iterator over :class:`WorkspaceAssignment`
        

    .. py:method:: resolve_group(external_id: str) -> ResolveGroupResponse

        Resolves a group with the given external ID from the customer's IdP. If the group does not exist, it
        will be created in the account. If the customer is not onboarded onto Automatic Identity Management
        (AIM), this will return an error.

        :param external_id: str
          Required. The external ID of the group in the customer's IdP.

        :returns: :class:`ResolveGroupResponse`
        

    .. py:method:: resolve_service_principal(external_id: str) -> ResolveServicePrincipalResponse

        Resolves a service principal with the given external ID from the customer's IdP. If the service
        principal does not exist, it will be created. If the customer is not onboarded onto Automatic Identity
        Management (AIM), this will return an error.

        :param external_id: str
          Required. The external ID of the service principal in the customer's IdP.

        :returns: :class:`ResolveServicePrincipalResponse`
        

    .. py:method:: resolve_user(external_id: str) -> ResolveUserResponse

        Resolves a user with the given external ID from the customer's IdP. If the user does not exist, it
        will be created. If the customer is not onboarded onto Automatic Identity Management (AIM), this will
        return an error.

        :param external_id: str
          Required. The external ID of the user in the customer's IdP.

        :returns: :class:`ResolveUserResponse`
        

    .. py:method:: update_group(name: str, group: Group, update_mask: str) -> Group

        Updates an existing group in the Databricks account. Only the fields named in the update mask are
        modified. Returns the updated Group resource.

        When AIM is enabled and the group is an external identity (its external_id is set), only external_id
        can be updated; its other fields are sourced from your identity provider. With AIM and group
        visibility filters, a new nonempty external_id must identify a visible group. Clearing external_id is
        allowed.

        Authorization: the caller must be an account admin or a manager of the group (holds the
        ``roles/group.manager`` role on it).

        :param name: str
          The resource name of the group. The format depends on the API that returned it:

          - Account-scoped: accounts/{account_id}/groups/{group_id}
          - Workspace-scoped: groups/{group_id}
        :param group: :class:`Group`
          Required. Group to be updated in Databricks
        :param update_mask: str
          Required. The list of fields to update.

        :returns: :class:`Group`
        

    .. py:method:: update_service_principal(name: str, service_principal: ServicePrincipal, update_mask: str) -> ServicePrincipal

        Updates an existing service principal in the Databricks account. Only the fields named in the update
        mask are modified. Returns the updated ServicePrincipal resource.

        To change is_agent on a locally managed service principal, set it to true or false. Naming is_agent in
        the update mask without a value leaves it unchanged.

        When AIM is enabled and the service principal is an external identity (its external_id is set), only
        external_id can be updated; its other fields are sourced from your identity provider.

        :param name: str
          The resource name of the service principal. The format depends on the API that returned it:

          - Account-scoped: accounts/{account_id}/service-principals/{service_principal_id}
          - Workspace-scoped: service-principals/{service_principal_id}
        :param service_principal: :class:`ServicePrincipal`
          Required. Service Principal to be updated in Databricks
        :param update_mask: str
          Required. The list of fields to update.

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: update_user(name: str, user: User, update_mask: str) -> User

        Updates an existing user in the Databricks account and returns the updated user. Only the fields named
        in the update mask are modified. The updatable fields are fullName.givenName, fullName.familyName,
        status, and externalId.

        When AIM is enabled and the user is an external identity (its external_id is set), only external_id
        can be updated; its other fields are sourced from your identity provider.

        :param name: str
          The resource name of the user. The format depends on the API that returned it:

          - Account-scoped: accounts/{account_id}/users/{user_id}
          - Workspace-scoped: users/{user_id}
        :param user: :class:`User`
          Required. User to be updated in Databricks
        :param update_mask: str
          Required. The list of fields to update.

        :returns: :class:`User`
        

    .. py:method:: update_workspace_assignment(name: str, workspace_assignment: WorkspaceAssignment, update_mask: FieldMask) -> WorkspaceAssignment

        Updates the entitlements of a directly assigned principal in a workspace. Changes are applied one at a
        time rather than atomically. If the request fails partway through, only some of the requested changes
        take effect. Get the assignment afterwards to confirm the final state.

        :param name: str
          The resource name of the workspace assignment. The format depends on the API that returned it:

          - Account-scoped:
            accounts/{account_id}/workspaces/{workspace_id}/workspace-assignments/{principal_id}
          - Workspace-scoped: workspace-assignments/{principal_id}
        :param workspace_assignment: :class:`WorkspaceAssignment`
          Required. Workspace assignment to be updated in Databricks.
        :param update_mask: FieldMask
          Required. The list of fields to update.

        :returns: :class:`WorkspaceAssignment`
        

    .. py:method:: update_workspace_assignment_detail(workspace_id: int, principal_id: int, workspace_assignment_detail: WorkspaceAssignmentDetail, update_mask: FieldMask) -> WorkspaceAssignmentDetail

        Updates the entitlements of a directly assigned principal in a workspace. Changes are applied one at a
        time rather than atomically. If the request fails partway through, only some of the requested changes
        take effect. Get the assignment detail afterwards to confirm the final state.

        :param workspace_id: int
          Required. The workspace ID for which the workspace assignment detail is being updated.
        :param principal_id: int
          Required. ID of the principal in Databricks.
        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be updated in Databricks.
        :param update_mask: FieldMask
          Required. The list of fields to update.

        :returns: :class:`WorkspaceAssignmentDetail`
        
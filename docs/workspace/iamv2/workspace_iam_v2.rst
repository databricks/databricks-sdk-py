``w.workspace_iam_v2``: workspace_iam.v2
========================================
.. currentmodule:: databricks.sdk.service.iamv2

.. py:class:: WorkspaceIamV2API

    These APIs are used to manage identities and the workspace access of these identities in Databricks.

    .. py:method:: create_direct_group_member_proxy(parent: str, direct_group_member: DirectGroupMember) -> DirectGroupMember

        Creates a group membership (assigns a principal to a group).

        :param parent: str
          The parent resource name of the group to add the member to. Format: groups/{group_id}
        :param direct_group_member: :class:`DirectGroupMember`
          Required. The group membership to create.

        :returns: :class:`DirectGroupMember`
        

    .. py:method:: create_group_proxy(group: Group [, parent: Optional[str]]) -> Group

        Creates a local group in the Databricks account that parents the calling workspace and returns the
        created group. A local group is one that is not synced from the customer's identity provider, and can
        be created whether or not Account Identity Management (AIM) is enabled.

        When AIM is enabled, supplying an external ID returns an error. To provision the identity from your
        identity provider, resolve it by its external ID with ResolveGroup; to read an existing external
        identity, use the ExternalGroup resource.

        :param group: :class:`Group`
          Required. Group to be created in Databricks
        :param parent: str (optional)
          The resource name of the account to create the group in, ``accounts/{account_id}``. Optional:
          defaults to the account of the calling workspace, and any other account is rejected.

        :returns: :class:`Group`
        

    .. py:method:: create_service_principal_proxy(service_principal: ServicePrincipal [, parent: Optional[str]]) -> ServicePrincipal

        Creates a local service principal in the Databricks account that parents the calling workspace and
        returns the created service principal. A local service principal is one that is not synced from the
        customer's identity provider, and can be created whether or not Account Identity Management (AIM) is
        enabled.

        When AIM is enabled, supplying an external ID returns an error. To provision the identity from your
        identity provider, resolve it by its external ID with ResolveServicePrincipal; to read an existing
        external identity, use the ExternalServicePrincipal resource.

        :param service_principal: :class:`ServicePrincipal`
          Required. Service principal to be created in Databricks
        :param parent: str (optional)
          The resource name of the account to create the service principal in, ``accounts/{account_id}``.
          Optional: defaults to the account of the calling workspace, and any other account is rejected.

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: create_user_proxy(user: User [, parent: Optional[str]]) -> User

        Creates a local user in the Databricks account that parents the calling workspace and returns the
        created user. A local user is one that is not synced from the customer's identity provider, and can be
        created whether or not Account Identity Management (AIM) is enabled.

        When AIM is enabled, supplying an external ID returns an error. To provision the identity from your
        identity provider, resolve it by its external ID with ResolveUser; to read an existing external
        identity, use the ExternalUser resource.

        :param user: :class:`User`
          Required. User to be created in Databricks
        :param parent: str (optional)
          The resource name of the account to create the user in, ``accounts/{account_id}``. Optional:
          defaults to the account of the calling workspace, and any other account is rejected.

        :returns: :class:`User`
        

    .. py:method:: create_workspace_assignment_detail_proxy(workspace_assignment_detail: WorkspaceAssignmentDetail) -> WorkspaceAssignmentDetail

        Creates a workspace assignment detail for a principal in the calling workspace.

        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be created in Databricks.

        :returns: :class:`WorkspaceAssignmentDetail`
        

    .. py:method:: create_workspace_assignment_proxy(workspace_assignment: WorkspaceAssignment [, parent: Optional[str]]) -> WorkspaceAssignment

        Creates a workspace assignment for a principal in the calling workspace. Entitlements are granted one
        at a time rather than atomically. If the request fails partway through, the principal stays assigned
        to the workspace with only some of the requested entitlements. Get the assignment afterwards to
        confirm which entitlements were granted.

        :param workspace_assignment: :class:`WorkspaceAssignment`
          Required. Workspace assignment to be created in Databricks.
        :param parent: str (optional)
          The resource name of the workspace to assign the principal to,
          ``accounts/{account_id}/workspaces/{workspace_id}``. Optional: defaults to the calling workspace,
          and any other workspace is rejected.

        :returns: :class:`WorkspaceAssignment`
        

    .. py:method:: delete_direct_group_member_proxy(name: str)

        Deletes a group membership (unassigns a principal from a group).

        :param name: str
          The resource name of the group membership. Format: groups/{group_id}/direct-members/{principal_id}


        

    .. py:method:: delete_group_proxy(name: str)

        Deletes a group by its internal ID from the Databricks account that parents the calling workspace.

        :param name: str
          The resource name of the group. Format: groups/{group_id}


        

    .. py:method:: delete_service_principal_proxy(name: str)

        Deletes a service principal by its internal ID from the Databricks account that parents the calling
        workspace.

        :param name: str
          The resource name of the service principal. Format: service-principals/{service_principal_id}


        

    .. py:method:: delete_user_proxy(name: str)

        Deletes a user by its internal ID from the Databricks account that parents the calling workspace.

        :param name: str
          The resource name of the user. Format: users/{user_id}


        

    .. py:method:: delete_workspace_assignment_detail_proxy(principal_id: int)

        Deletes a workspace assignment detail for a principal in the calling workspace, revoking all of its
        entitlements. Entitlements are revoked one at a time rather than atomically. If the request fails
        partway through, the principal stays assigned with some of its original entitlements. Retrying is
        safe.

        :param principal_id: int
          Required. ID of the principal in Databricks to delete workspace assignment for.


        

    .. py:method:: delete_workspace_assignment_proxy(name: str)

        Deletes a workspace assignment for a principal in the calling workspace, revoking all of its
        entitlements. Entitlements are revoked one at a time rather than atomically. If the request fails
        partway through, the principal stays assigned with some of its original entitlements. Retrying is
        safe.

        :param name: str
          The resource name of the workspace assignment. Format: workspace-assignments/{principal_id}


        

    .. py:method:: get_direct_group_member_proxy(name: str) -> DirectGroupMember

        Gets a provisioned direct member of a group.

        :param name: str
          The resource name of the group membership. Format: groups/{group_id}/direct-members/{principal_id}

        :returns: :class:`DirectGroupMember`
        

    .. py:method:: get_external_group_proxy(name: str) -> ExternalGroup

        Retrieves an external group with the given external ID from the customer's IdP. If the group does not
        exist, it will be created in the account. If the customer is not onboarded onto Automatic Identity
        Management (AIM), this will return an error. Workspace-scoped variant for workspace-authenticated
        callers.

        :param name: str
          Required. The resource name of the external group. Format: external-groups/{external_group_id}

        :returns: :class:`ExternalGroup`
        

    .. py:method:: get_external_service_principal_proxy(name: str) -> ExternalServicePrincipal

        Retrieves an external service principal with the given external ID from the customer's IdP. If the
        service principal does not exist, it will be created. If the customer is not onboarded onto Automatic
        Identity Management (AIM), this will return an error. Workspace-scoped variant for
        workspace-authenticated callers.

        :param name: str
          Required. The resource name of the external service principal. Format:
          external-service-principals/{external_service_principal_id}

        :returns: :class:`ExternalServicePrincipal`
        

    .. py:method:: get_external_user_proxy(name: str) -> ExternalUser

        Retrieves an external user with the given external ID from the customer's IdP. If the user does not
        exist, it will be created. If the customer is not onboarded onto Automatic Identity Management (AIM),
        this will return an error. Workspace-scoped variant for workspace-authenticated callers.

        :param name: str
          Required. The resource name of the external user. Format: external-users/{external_user_id}

        :returns: :class:`ExternalUser`
        

    .. py:method:: get_group_proxy(name: str) -> Group

        Fetches a group by its internal ID from the Databricks account that parents the calling workspace.

        :param name: str
          The resource name of the group. Format: groups/{group_id}

        :returns: :class:`Group`
        

    .. py:method:: get_service_principal_proxy(name: str) -> ServicePrincipal

        Fetches a service principal by its internal ID from the Databricks account that parents the calling
        workspace.

        :param name: str
          The resource name of the service principal. Format: service-principals/{service_principal_id}

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: get_user_proxy(name: str) -> User

        Fetches a user by its internal ID from the Databricks account that parents the calling workspace.

        :param name: str
          The resource name of the user. Format: users/{user_id}

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

        Returns the assignment for a principal in the calling workspace.

        :param name: str
          The resource name of the workspace assignment. Format: workspace-assignments/{principal_id}

        :returns: :class:`WorkspaceAssignment`
        

    .. py:method:: get_workspace_identity_detail(name: str) -> WorkspaceIdentityDetail

        Returns the identity details for a principal in a workspace.

        :param name: str
          The resource name of the workspace identity detail. Format:
          principals/{principal_id}/workspace-identity-detail

        :returns: :class:`WorkspaceIdentityDetail`
        

    .. py:method:: list_direct_group_members_proxy(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[DirectGroupMember]

        Lists provisioned direct members of a group with their membership source (internal or from identity
        provider).

        :param parent: str
          The parent resource name of the group whose direct members to list. Format: groups/{group_id}
        :param page_size: int (optional)
          The maximum number of members to return. The service may return fewer than this value. If not
          provided, defaults to 1000, which is also the maximum allowed. Requests for more than the maximum
          are clamped to 1000.
        :param page_token: str (optional)
          A page token from a previous list call. Provide this to retrieve the subsequent page.

        :returns: Iterator over :class:`DirectGroupMember`
        

    .. py:method:: list_groups_proxy( [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str], parent: Optional[str]]) -> Iterator[Group]

        Lists the groups in the Databricks account that parents the calling workspace, returning one page per
        call. Supports filtering by group name or external ID.

        :param filter: str (optional)
          Optional. Allows filtering groups by group name or external id.
        :param page_size: int (optional)
          The maximum number of groups to return. The service may return fewer than this value. If not
          provided, defaults to 1000, which is also the maximum allowed. Requests for more than the maximum
          are clamped to 1000.
        :param page_token: str (optional)
          A page token, received from a previous ListGroups call. Provide this to retrieve the subsequent
          page.
        :param parent: str (optional)
          The resource name of the account to list groups in, ``accounts/{account_id}``. Optional: defaults to
          the account of the calling workspace, and any other account is rejected.

        :returns: Iterator over :class:`Group`
        

    .. py:method:: list_service_principals_proxy( [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str], parent: Optional[str]]) -> Iterator[ServicePrincipal]

        Lists the service principals in the Databricks account that parents the calling workspace, returning
        one page per call. Supports filtering by application ID or external ID.

        :param filter: str (optional)
          Optional. Allows filtering service principals by application id or external id.
        :param page_size: int (optional)
          The maximum number of SPs to return. The service may return fewer than this value. If not provided,
          defaults to 1000, which is also the maximum allowed. Requests for more than the maximum are clamped
          to 1000.
        :param page_token: str (optional)
          A page token, received from a previous ListServicePrincipals call. Provide this to retrieve the
          subsequent page.
        :param parent: str (optional)
          The resource name of the account to list service principals in, ``accounts/{account_id}``. Optional:
          defaults to the account of the calling workspace, and any other account is rejected.

        :returns: Iterator over :class:`ServicePrincipal`
        

    .. py:method:: list_transitive_parent_groups_proxy(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> ListTransitiveParentGroupsResponse

        Lists all transitive parent groups of a principal.

        :param parent: str
          The parent resource name of the principal whose transitive parent groups to list. Format:
          principals/{principal_id}
        :param page_size: int (optional)
          The maximum number of parent groups to return. The service may return fewer than this value. If not
          provided, defaults to 1000, which is also the maximum allowed. Requests for more than the maximum
          are clamped to 1000.
        :param page_token: str (optional)
          A page token, received from a previous ListTransitiveParentGroups call. Provide this to retrieve the
          subsequent page.

        :returns: :class:`ListTransitiveParentGroupsResponse`
        

    .. py:method:: list_users_proxy( [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str], parent: Optional[str]]) -> Iterator[User]

        Lists the users in the Databricks account that parents the calling workspace, returning one page per
        call. Supports filtering by username or external ID.

        :param filter: str (optional)
          Optional. Allows filtering users by username or external id.
        :param page_size: int (optional)
          The maximum number of users to return. The service may return fewer than this value. If not
          provided, defaults to 1000, which is also the maximum allowed. Requests for more than the maximum
          are clamped to 1000.
        :param page_token: str (optional)
          A page token, received from a previous ListUsers call. Provide this to retrieve the subsequent page.
        :param parent: str (optional)
          The resource name of the account to list users in, ``accounts/{account_id}``. Optional: defaults to
          the account of the calling workspace, and any other account is rejected.

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

        Lists workspace assignments for the calling workspace. The response omits the per-principal
        entitlement fields (``entitlements`` and ``effective_entitlements``). To read the entitlements for a
        single principal, get that principal's assignment.

        :param page_size: int (optional)
          The maximum number of workspace assignments to return. The service may return fewer than this value.
          If not provided, defaults to 1000, which is also the maximum allowed. Requests for more than the
          maximum are clamped to 1000.
        :param page_token: str (optional)
          A page token from a previous list call. Provide this to retrieve the subsequent page.
        :param parent: str (optional)
          The resource name of the workspace to list assignments of,
          ``accounts/{account_id}/workspaces/{workspace_id}``. Optional: defaults to the calling workspace,
          and any other workspace is rejected.

        :returns: Iterator over :class:`WorkspaceAssignment`
        

    .. py:method:: resolve_group_proxy(external_id: str) -> ResolveGroupResponse

        Resolves a group with the given external ID from the customer's IdP. If the group does not exist, it
        will be created in the account. If the customer is not onboarded onto Automatic Identity Management
        (AIM), this will return an error.

        :param external_id: str
          Required. The external ID of the group in the customer's IdP.

        :returns: :class:`ResolveGroupResponse`
        

    .. py:method:: resolve_service_principal_proxy(external_id: str) -> ResolveServicePrincipalResponse

        Resolves a service principal with the given external ID from the customer's IdP. If the service
        principal does not exist, it will be created. If the customer is not onboarded onto Automatic Identity
        Management (AIM), this will return an error.

        :param external_id: str
          Required. The external ID of the service principal in the customer's IdP.

        :returns: :class:`ResolveServicePrincipalResponse`
        

    .. py:method:: resolve_user_proxy(external_id: str) -> ResolveUserResponse

        Resolves a user with the given external ID from the customer's IdP. If the user does not exist, it
        will be created. If the customer is not onboarded onto Automatic Identity Management (AIM), this will
        return an error.

        :param external_id: str
          Required. The external ID of the user in the customer's IdP.

        :returns: :class:`ResolveUserResponse`
        

    .. py:method:: update_group_proxy(name: str, group: Group, update_mask: str) -> Group

        Updates an existing group in the Databricks account that parents the calling workspace. Only the
        fields named in the update mask are modified. Returns the updated Group resource.

        When AIM is enabled and the group is an external identity (its external_id is set), only external_id
        can be updated; its other fields are sourced from your identity provider. With AIM and group
        visibility filters, a new nonempty external_id must identify a visible group. Clearing external_id is
        allowed.

        :param name: str
          The resource name of the group. The format depends on the API that returned it:

          - Account-scoped: accounts/{account_id}/groups/{group_id}
          - Workspace-scoped: groups/{group_id}
        :param group: :class:`Group`
          Required. Group to be updated in Databricks
        :param update_mask: str
          Required. The list of fields to update.

        :returns: :class:`Group`
        

    .. py:method:: update_service_principal_proxy(name: str, service_principal: ServicePrincipal, update_mask: str) -> ServicePrincipal

        Updates an existing service principal in the Databricks account that parents the calling workspace.
        Only the fields named in the update mask are modified. Returns the updated ServicePrincipal resource.

        To change is_agent on a locally managed service principal, set it to true or false. Naming is_agent in
        the update mask without a value leaves it unchanged.

        When AIM is enabled and the service principal is an external identity (its external_id is set), only
        external_id can be updated; its other fields are sourced from your identity provider.

        :param name: str
          The resource name of the service principal. The format depends on the API that returned it:

          - Account-scoped: accounts/{account_id}/service-principals/{service_principal_id}
          - Workspace-scoped: service-principals/{service_principal_id}
        :param service_principal: :class:`ServicePrincipal`
          Required. Service principal to be updated in Databricks
        :param update_mask: str
          Required. The list of fields to update.

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: update_user_proxy(name: str, user: User, update_mask: str) -> User

        Updates an existing user in the Databricks account that parents the calling workspace and returns the
        updated user. Only the fields named in the update mask are modified. The updatable fields are
        fullName.givenName, fullName.familyName, status, and externalId.

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

        Updates the entitlements of a directly assigned principal in the calling workspace. Changes are
        applied one at a time rather than atomically. If the request fails partway through, only some of the
        requested changes take effect. Get the assignment afterwards to confirm the final state.

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
        

    .. py:method:: update_workspace_identity_detail(name: str, workspace_identity_detail: WorkspaceIdentityDetail, update_mask: FieldMask) -> WorkspaceIdentityDetail

        Updates a workspace identity detail for a principal.

        :param name: str
          The resource name of the workspace identity detail. Format:
          principals/{principal_id}/workspace-identity-detail
        :param workspace_identity_detail: :class:`WorkspaceIdentityDetail`
          Required. Workspace identity detail to be updated in Databricks.
        :param update_mask: FieldMask
          Required. The list of fields to update.

        :returns: :class:`WorkspaceIdentityDetail`
        
``w.workspace_iam_v2``: workspace_iam.v2
========================================
.. currentmodule:: databricks.sdk.service.iamv2

.. py:class:: WorkspaceIamV2API

    These APIs are used to manage identities and the workspace access of these identities in <Databricks>.

    .. py:method:: create_direct_group_member_proxy(group_id: int, direct_group_member: DirectGroupMember) -> DirectGroupMember

        Creates a group membership (assigns a principal to a group).

        :param group_id: int
          Required. Internal ID of the group in Databricks.
        :param direct_group_member: :class:`DirectGroupMember`
          Required. The group membership to create.

        :returns: :class:`DirectGroupMember`
        

    .. py:method:: create_group_proxy(group: Group) -> Group

        Creates a group in the Databricks account that parents the calling workspace and returns the resulting
        Group resource.

        :param group: :class:`Group`
          Required. Group to be created in <Databricks>

        :returns: :class:`Group`
        

    .. py:method:: create_service_principal_proxy(service_principal: ServicePrincipal) -> ServicePrincipal

        Creates a service principal in the Databricks account that parents the calling workspace and returns
        the resulting ServicePrincipal resource.

        :param service_principal: :class:`ServicePrincipal`
          Required. Service principal to be created in <Databricks>

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: create_user_proxy(user: User) -> User

        Creates a user in the Databricks account that parents the calling workspace and returns the resulting
        User resource. The same AIM-dependent provisioning behavior described on CreateUser applies.

        :param user: :class:`User`
          Required. User to be created in <Databricks>

        :returns: :class:`User`
        

    .. py:method:: create_workspace_assignment_detail_proxy(workspace_assignment_detail: WorkspaceAssignmentDetail) -> WorkspaceAssignmentDetail

        Creates a workspace assignment detail for a principal (workspace-level proxy). Entitlement grants are
        applied individually and non-atomically — if a failure occurs partway through, the principal will be
        assigned to the workspace but with only a subset of the requested entitlements. Use
        GetWorkspaceAssignmentDetail to confirm which entitlements were successfully granted.

        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be created in <Databricks>.

        :returns: :class:`WorkspaceAssignmentDetail`
        

    .. py:method:: delete_direct_group_member_proxy(group_id: int, principal_id: int)

        Deletes a group membership (unassigns a principal from a group).

        :param group_id: int
          Required. Internal ID of the group in Databricks.
        :param principal_id: int
          Required. Internal ID of the principal to be unassigned from the group.


        

    .. py:method:: delete_group_proxy(group_id: str)

        Deletes a group by its internal ID from the Databricks account that parents the calling workspace.

        :param group_id: str
          Required. Internal ID of the group in Databricks.


        

    .. py:method:: delete_service_principal_proxy(service_principal_id: str)

        Deletes a service principal by its internal ID from the Databricks account that parents the calling
        workspace.

        :param service_principal_id: str
          Required. Internal ID of the service principal in Databricks.


        

    .. py:method:: delete_user_proxy(user_id: str)

        Deletes a user by its internal ID from the Databricks account that parents the calling workspace.

        :param user_id: str
          Required. Internal ID of the user in Databricks.


        

    .. py:method:: delete_workspace_assignment_detail_proxy(principal_id: int)

        Deletes a workspace assignment detail for a principal (workspace-level proxy), revoking all associated
        entitlements. Entitlement revocations are applied individually and non-atomically — if a failure
        occurs partway through, the principal remains assigned with a subset of its original entitlements, and
        the operation is safe to retry.

        :param principal_id: int
          Required. ID of the principal in Databricks to delete workspace assignment for.


        

    .. py:method:: get_direct_group_member_proxy(group_id: int, principal_id: int) -> DirectGroupMember

        Gets a provisioned direct member of a group.

        :param group_id: int
          Required. Internal ID of the group in Databricks.
        :param principal_id: int
          Required. Internal ID of the principal belonging to the group in Databricks.

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
        

    .. py:method:: get_group_proxy(group_id: str) -> Group

        Fetches a group by its internal ID from the Databricks account that parents the calling workspace.

        :param group_id: str
          Required. Internal ID of the group in Databricks.

        :returns: :class:`Group`
        

    .. py:method:: get_service_principal_proxy(service_principal_id: str) -> ServicePrincipal

        Fetches a service principal by its internal ID from the Databricks account that parents the calling
        workspace.

        :param service_principal_id: str
          Required. Internal ID of the service principal in Databricks.

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: get_user_proxy(user_id: str) -> User

        Fetches a user by its internal ID from the Databricks account that parents the calling workspace.

        :param user_id: str
          Required. Internal ID of the user in Databricks.

        :returns: :class:`User`
        

    .. py:method:: get_workspace_access_detail_local(principal_id: int [, view: Optional[WorkspaceAccessDetailView]]) -> WorkspaceAccessDetail

        Returns the access details for a principal in the current workspace. Allows for checking access
        details for any provisioned principal (user, service principal, or group) in the current workspace.

        - Provisioned principal here refers to one that has been synced into Databricks from the customer's
          IdP or added explicitly to Databricks via SCIM/UI. Allows for passing in a "view" parameter to
          control what fields are returned (BASIC by default or FULL).

        :param principal_id: int
          Required. The internal ID of the principal (user/sp/group) for which the access details are being
          requested.
        :param view: :class:`WorkspaceAccessDetailView` (optional)
          Controls what fields are returned.

        :returns: :class:`WorkspaceAccessDetail`
        

    .. py:method:: get_workspace_assignment_detail_proxy(principal_id: int) -> WorkspaceAssignmentDetail

        Returns the assignment details for a principal in a workspace (workspace-level proxy).

        :param principal_id: int
          Required. The internal ID of the principal (user/sp/group) for which the assignment details are
          being requested.

        :returns: :class:`WorkspaceAssignmentDetail`
        

    .. py:method:: get_workspace_identity_detail(principal_id: int) -> WorkspaceIdentityDetail

        Returns the identity details for a principal in a workspace.

        :param principal_id: int
          Required. The internal ID of the principal (user/sp/group) for which the identity details are being
          requested.

        :returns: :class:`WorkspaceIdentityDetail`
        

    .. py:method:: list_direct_group_members_proxy(group_id: int [, page_size: Optional[int], page_token: Optional[str]]) -> ListDirectGroupMembersResponse

        Lists provisioned direct members of a group with their membership source (internal or from identity
        provider).

        :param group_id: int
          Required. Internal ID of the group in Databricks whose direct members are being listed.
        :param page_size: int (optional)
          The maximum number of members to return. The service may return fewer than this value. If not
          provided, defaults to 1000 (also the maximum allowed).
        :param page_token: str (optional)
          A page token, received from a previous ListDirectGroupMembersProxy call. Provide this to retrieve
          the subsequent page.

        :returns: :class:`ListDirectGroupMembersResponse`
        

    .. py:method:: list_groups_proxy( [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Group]

        Lists the groups in the Databricks account that parents the calling workspace, returning one page per
        call. Supports filtering by group name or external ID.

        :param filter: str (optional)
          Optional. Allows filtering groups by group name or external id.
        :param page_size: int (optional)
          The maximum number of groups to return. The service may return fewer than this value.
        :param page_token: str (optional)
          A page token, received from a previous ListGroups call. Provide this to retrieve the subsequent
          page.

        :returns: Iterator over :class:`Group`
        

    .. py:method:: list_service_principals_proxy( [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ServicePrincipal]

        Lists the service principals in the Databricks account that parents the calling workspace, returning
        one page per call. Supports filtering by application ID or external ID.

        :param filter: str (optional)
          Optional. Allows filtering service principals by application id or external id.
        :param page_size: int (optional)
          The maximum number of SPs to return. The service may return fewer than this value.
        :param page_token: str (optional)
          A page token, received from a previous ListServicePrincipals call. Provide this to retrieve the
          subsequent page.

        :returns: Iterator over :class:`ServicePrincipal`
        

    .. py:method:: list_transitive_parent_groups_proxy(principal_id: int [, page_size: Optional[int], page_token: Optional[str]]) -> ListTransitiveParentGroupsResponse

        Lists all transitive parent groups of a principal.

        :param principal_id: int
          Required. Internal ID of the principal in Databricks whose transitive parent groups are being
          listed.
        :param page_size: int (optional)
          The maximum number of parent groups to return. The service may return fewer than this value. If not
          provided, defaults to 1000 (also the maximum allowed).
        :param page_token: str (optional)
          A page token, received from a previous ListTransitiveParentGroups call. Provide this to retrieve the
          subsequent page.

        :returns: :class:`ListTransitiveParentGroupsResponse`
        

    .. py:method:: list_users_proxy( [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> Iterator[User]

        Lists the users in the Databricks account that parents the calling workspace, returning one page per
        call. Supports filtering by username or external ID.

        :param filter: str (optional)
          Optional. Allows filtering users by username or external id.
        :param page_size: int (optional)
          The maximum number of users to return. The service may return fewer than this value.
        :param page_token: str (optional)
          A page token, received from a previous ListUsers call. Provide this to retrieve the subsequent page.

        :returns: Iterator over :class:`User`
        

    .. py:method:: list_workspace_access_details_local( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[WorkspaceAccessDetail]

        Lists the access details of every provisioned principal (user, service principal, or group) with
        access to the current workspace, returning one page per call.

        - Provisioned principal here refers to one that has been synced into Databricks from the customer's
          IdP or added explicitly to Databricks via SCIM/UI.

        :param page_size: int (optional)
          The maximum number of workspace access details to return. The service may return fewer than this
          value.
        :param page_token: str (optional)
          A page token, received from a previous ListWorkspaceAccessDetails call. Provide this to retrieve the
          subsequent page.

        :returns: Iterator over :class:`WorkspaceAccessDetail`
        

    .. py:method:: list_workspace_assignment_details_proxy( [, page_size: Optional[int], page_token: Optional[str]]) -> ListWorkspaceAssignmentDetailsResponse

        Lists workspace assignment details for a workspace (workspace-level proxy). For scalability, the
        response omits the per-principal entitlement fields (``entitlements`` and ``effective_entitlements``);
        call GetWorkspaceAssignmentDetailProxy to read entitlements for a single principal.

        :param page_size: int (optional)
          The maximum number of workspace assignment details to return. The service may return fewer than this
          value.
        :param page_token: str (optional)
          A page token, received from a previous ListWorkspaceAssignmentDetailsProxy call. Provide this to
          retrieve the subsequent page.

        :returns: :class:`ListWorkspaceAssignmentDetailsResponse`
        

    .. py:method:: resolve_group_proxy(external_id: str) -> ResolveGroupResponse

        Resolves a group with the given external ID from the customer's IdP. If the group does not exist, it
        will be created in the account. If the customer is not onboarded onto Automatic Identity Management
        (AIM), this will return an error.

        :param external_id: str
          Required. The external ID of the group in the customer's IdP.

        :returns: :class:`ResolveGroupResponse`
        

    .. py:method:: resolve_service_principal_proxy(external_id: str) -> ResolveServicePrincipalResponse

        Resolves an SP with the given external ID from the customer's IdP. If the SP does not exist, it will
        be created. If the customer is not onboarded onto Automatic Identity Management (AIM), this will
        return an error.

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
        

    .. py:method:: update_group_proxy(group_id: str, group: Group, update_mask: str) -> Group

        Updates an existing group in the Databricks account that parents the calling workspace. Only the
        fields named in the update mask are modified. Returns the updated Group resource.

        :param group_id: str
          Required. Internal ID of the group in Databricks.
        :param group: :class:`Group`
          Required. Group to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`Group`
        

    .. py:method:: update_service_principal_proxy(service_principal_id: str, service_principal: ServicePrincipal, update_mask: str) -> ServicePrincipal

        Updates an existing service principal in the Databricks account that parents the calling workspace.
        Only the fields named in the update mask are modified. Returns the updated ServicePrincipal resource.

        :param service_principal_id: str
          Required. Internal ID of the service principal in Databricks.
        :param service_principal: :class:`ServicePrincipal`
          Required. Service principal to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: update_user_proxy(user_id: str, user: User, update_mask: str) -> User

        Updates an existing user in the Databricks account that parents the calling workspace. Only the fields
        named in the update mask are modified; the updatable fields are fullName.givenName,
        fullName.familyName, status, and externalId. Returns the updated User resource.

        :param user_id: str
          Required. Internal ID of the user in Databricks.
        :param user: :class:`User`
          Required. User to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`User`
        

    .. py:method:: update_workspace_assignment_detail_proxy(principal_id: int, workspace_assignment_detail: WorkspaceAssignmentDetail, update_mask: FieldMask) -> WorkspaceAssignmentDetail

        Updates the entitlements of a directly assigned principal in a workspace (workspace-level proxy).
        Entitlement changes are applied individually and non-atomically — if a failure occurs partway
        through, only a subset of the requested changes may have been applied. Use
        GetWorkspaceAssignmentDetail to confirm the final state.

        :param principal_id: int
          Required. ID of the principal in Databricks.
        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be updated in <Databricks>.
        :param update_mask: FieldMask
          Required. The list of fields to update.

        :returns: :class:`WorkspaceAssignmentDetail`
        

    .. py:method:: update_workspace_identity_detail(principal_id: int, workspace_identity_detail: WorkspaceIdentityDetail, update_mask: FieldMask) -> WorkspaceIdentityDetail

        Updates a workspace identity detail for a principal.

        :param principal_id: int
          Required. ID of the principal in Databricks.
        :param workspace_identity_detail: :class:`WorkspaceIdentityDetail`
          Required. Workspace identity detail to be updated in <Databricks>.
        :param update_mask: FieldMask
          Required. The list of fields to update.

        :returns: :class:`WorkspaceIdentityDetail`
        
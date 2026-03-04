``a.iam_v2``: account_iam.v2
============================
.. currentmodule:: databricks.sdk.service.iamv2

.. py:class:: AccountIamV2API

    These APIs are used to manage identities and the workspace access of these identities in <Databricks>.

    .. py:method:: create_account_access_identity_rule(account_access_identity_rule: AccountAccessIdentityRule) -> AccountAccessIdentityRule

        Creates a new account access identity rule for a given account. This allows administrators to
        explicitly allow or deny specific principals from accessing the account.

        :param account_access_identity_rule: :class:`AccountAccessIdentityRule`
          Required. The rule to create.

        :returns: :class:`AccountAccessIdentityRule`
        

    .. py:method:: create_group(group: Group) -> Group

        TODO: Write description later when this method is implemented

        :param group: :class:`Group`
          Required. Group to be created in <Databricks>

        :returns: :class:`Group`
        

    .. py:method:: create_group_membership(group_id: int, group_membership: GroupMembership) -> GroupMembership

        Creates a group membership (assigns a principal to a group).

        :param group_id: int
          Required. Internal ID of the group in Databricks.
        :param group_membership: :class:`GroupMembership`
          Required. The group membership to create.

        :returns: :class:`GroupMembership`
        

    .. py:method:: create_service_principal(service_principal: ServicePrincipal) -> ServicePrincipal

        TODO: Write description later when this method is implemented

        :param service_principal: :class:`ServicePrincipal`
          Required. Service principal to be created in <Databricks>

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: create_user(user: User) -> User

        TODO: Write description later when this method is implemented

        :param user: :class:`User`
          Required. User to be created in <Databricks>

        :returns: :class:`User`
        

    .. py:method:: create_workspace_assignment_detail(workspace_id: int, workspace_assignment_detail: WorkspaceAssignmentDetail) -> WorkspaceAssignmentDetail

        Creates a workspace assignment detail for a principal.

        :param workspace_id: int
          Required. The workspace ID for which the workspace assignment detail is being created.
        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be created in <Databricks>.

        :returns: :class:`WorkspaceAssignmentDetail`
        

    .. py:method:: delete_account_access_identity_rule(external_id: str)

        Deletes an account access identity rule for a given principal.

        :param external_id: str
          Required. The external ID of the principal whose rule should be deleted.


        

    .. py:method:: delete_group(internal_id: int)

        TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the group in Databricks.


        

    .. py:method:: delete_group_membership(group_id: int, principal_id: int)

        Deletes a group membership (unassigns a principal from a group).

        :param group_id: int
          Required. Internal ID of the group in Databricks.
        :param principal_id: int
          Required. Internal ID of the principal to be unassigned from the group.


        

    .. py:method:: delete_service_principal(internal_id: int)

        TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the service principal in Databricks.


        

    .. py:method:: delete_user(internal_id: int)

        TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the user in Databricks.


        

    .. py:method:: delete_workspace_assignment_detail(workspace_id: int, principal_id: int)

        Deletes a workspace assignment detail for a principal.

        :param workspace_id: int
          The workspace ID where the principal has access.
        :param principal_id: int
          Required. ID of the principal in Databricks to delete workspace assignment for.


        

    .. py:method:: get_account_access_identity_rule(external_id: str) -> AccountAccessIdentityRule

        Gets an account access identity rule for a given principal.

        :param external_id: str
          Required. The external ID of the principal whose rule should be retrieved.

        :returns: :class:`AccountAccessIdentityRule`
        

    .. py:method:: get_group(internal_id: int) -> Group

        TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the group in Databricks.

        :returns: :class:`Group`
        

    .. py:method:: get_service_principal(internal_id: int) -> ServicePrincipal

        TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the service principal in Databricks.

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: get_user(internal_id: int) -> User

        TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the user in Databricks.

        :returns: :class:`User`
        

    .. py:method:: get_workspace_access_detail(workspace_id: int, principal_id: int [, view: Optional[WorkspaceAccessDetailView]]) -> WorkspaceAccessDetail

        Returns the access details for a principal in a workspace. Allows for checking access details for any
        provisioned principal (user, service principal, or group) in a workspace. * Provisioned principal here
        refers to one that has been synced into Databricks from the customer's IdP or added explicitly to
        Databricks via SCIM/UI. Allows for passing in a "view" parameter to control what fields are returned
        (BASIC by default or FULL).

        :param workspace_id: int
          Required. The workspace ID for which the access details are being requested.
        :param principal_id: int
          Required. The internal ID of the principal (user/sp/group) for which the access details are being
          requested.
        :param view: :class:`WorkspaceAccessDetailView` (optional)
          Controls what fields are returned.

        :returns: :class:`WorkspaceAccessDetail`
        

    .. py:method:: get_workspace_assignment_detail(workspace_id: int, principal_id: int) -> WorkspaceAssignmentDetail

        Returns the assignment details for a principal in a workspace.

        :param workspace_id: int
          Required. The workspace ID for which the assignment details are being requested.
        :param principal_id: int
          Required. The internal ID of the principal (user/sp/group) for which the assignment details are
          being requested.

        :returns: :class:`WorkspaceAssignmentDetail`
        

    .. py:method:: list_account_access_identity_rules( [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> ListAccountAccessIdentityRulesResponse

        Lists all account access identity rules for a given account. These rules control which principals
        (users, service principals, groups) from the customer's IdP are allowed or denied access to the
        Databricks account.

        :param filter: str (optional)
          Optional. Filter to apply to the list. Supports filtering by displayName.
        :param page_size: int (optional)
          Optional. The maximum number of rules to return. The service may return fewer than this value.
        :param page_token: str (optional)
          Optional. A page token, received from a previous call. Provide this to retrieve the subsequent page.

        :returns: :class:`ListAccountAccessIdentityRulesResponse`
        

    .. py:method:: list_direct_group_members(group_id: int [, page_size: Optional[int], page_token: Optional[str]]) -> ListDirectGroupMembersResponse

        Lists provisioned direct members of a group with their membership source (internal or from identity
        provider).

        :param group_id: int
          Required. Internal ID of the group in Databricks whose direct members are being listed.
        :param page_size: int (optional)
          The maximum number of members to return. The service may return fewer than this value. If not
          provided, defaults to 1000 (also the maximum allowed).
        :param page_token: str (optional)
          A page token, received from a previous ListDirectGroupMembers call. Provide this to retrieve the
          subsequent page.

        :returns: :class:`ListDirectGroupMembersResponse`
        

    .. py:method:: list_groups( [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> ListGroupsResponse

        TODO: Write description later when this method is implemented

        :param filter: str (optional)
          Optional. Allows filtering groups by group name or external id.
        :param page_size: int (optional)
          The maximum number of groups to return. The service may return fewer than this value.
        :param page_token: str (optional)
          A page token, received from a previous ListGroups call. Provide this to retrieve the subsequent
          page.

        :returns: :class:`ListGroupsResponse`
        

    .. py:method:: list_service_principals( [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> ListServicePrincipalsResponse

        TODO: Write description later when this method is implemented

        :param filter: str (optional)
          Optional. Allows filtering service principals by application id or external id.
        :param page_size: int (optional)
          The maximum number of service principals to return. The service may return fewer than this value.
        :param page_token: str (optional)
          A page token, received from a previous ListServicePrincipals call. Provide this to retrieve the
          subsequent page.

        :returns: :class:`ListServicePrincipalsResponse`
        

    .. py:method:: list_transitive_parent_groups(principal_id: int [, page_size: Optional[int], page_token: Optional[str]]) -> ListTransitiveParentGroupsResponse

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
        

    .. py:method:: list_users( [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> ListUsersResponse

        TODO: Write description later when this method is implemented

        :param filter: str (optional)
          Optional. Allows filtering users by username or external id.
        :param page_size: int (optional)
          The maximum number of users to return. The service may return fewer than this value.
        :param page_token: str (optional)
          A page token, received from a previous ListUsers call. Provide this to retrieve the subsequent page.

        :returns: :class:`ListUsersResponse`
        

    .. py:method:: list_workspace_access_details(workspace_id: int [, page_size: Optional[int], page_token: Optional[str]]) -> ListWorkspaceAccessDetailsResponse

        TODO: Write description later when this method is implemented

        :param workspace_id: int
          The workspace ID for which the workspace access details are being fetched.
        :param page_size: int (optional)
          The maximum number of workspace access details to return. The service may return fewer than this
          value.
        :param page_token: str (optional)
          A page token, received from a previous ListWorkspaceAccessDetails call. Provide this to retrieve the
          subsequent page.

        :returns: :class:`ListWorkspaceAccessDetailsResponse`
        

    .. py:method:: list_workspace_assignment_details(workspace_id: int [, page_size: Optional[int], page_token: Optional[str]]) -> ListWorkspaceAssignmentDetailsResponse

        Lists workspace assignment details for a workspace.

        :param workspace_id: int
          Required. The workspace ID for which the workspace assignment details are being fetched.
        :param page_size: int (optional)
          The maximum number of workspace assignment details to return. The service may return fewer than this
          value.
        :param page_token: str (optional)
          A page token, received from a previous ListWorkspaceAssignmentDetails call. Provide this to retrieve
          the subsequent page.

        :returns: :class:`ListWorkspaceAssignmentDetailsResponse`
        

    .. py:method:: resolve_group(external_id: str) -> ResolveGroupResponse

        Resolves a group with the given external ID from the customer's IdP. If the group does not exist, it
        will be created in the account. If the customer is not onboarded onto Automatic Identity Management
        (AIM), this will return an error.

        :param external_id: str
          Required. The external ID of the group in the customer's IdP.

        :returns: :class:`ResolveGroupResponse`
        

    .. py:method:: resolve_service_principal(external_id: str) -> ResolveServicePrincipalResponse

        Resolves an SP with the given external ID from the customer's IdP. If the SP does not exist, it will
        be created. If the customer is not onboarded onto Automatic Identity Management (AIM), this will
        return an error.

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
        

    .. py:method:: update_group(internal_id: int, group: Group, update_mask: str) -> Group

        TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the group in Databricks.
        :param group: :class:`Group`
          Required. Group to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`Group`
        

    .. py:method:: update_service_principal(internal_id: int, service_principal: ServicePrincipal, update_mask: str) -> ServicePrincipal

        TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the service principal in Databricks.
        :param service_principal: :class:`ServicePrincipal`
          Required. Service Principal to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: update_user(internal_id: int, user: User, update_mask: str) -> User

        TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the user in Databricks.
        :param user: :class:`User`
          Required. User to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`User`
        

    .. py:method:: update_workspace_assignment_detail(workspace_id: int, principal_id: int, workspace_assignment_detail: WorkspaceAssignmentDetail, update_mask: FieldMask) -> WorkspaceAssignmentDetail

        Updates a workspace assignment detail for a principal.

        :param workspace_id: int
          Required. The workspace ID for which the workspace assignment detail is being updated.
        :param principal_id: int
          Required. ID of the principal in Databricks.
        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be updated in <Databricks>.
        :param update_mask: FieldMask
          Required. The list of fields to update.

        :returns: :class:`WorkspaceAssignmentDetail`
        
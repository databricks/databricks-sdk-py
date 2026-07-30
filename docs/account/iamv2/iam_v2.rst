``a.iam_v2``: account_iam.v2
============================
.. currentmodule:: databricks.sdk.service.iamv2

.. py:class:: AccountIamV2API

    These APIs are used to manage identities and the workspace access of these identities in <Databricks>.

    .. py:method:: create_account_access_identity_rule(parent: str, account_access_identity_rule: AccountAccessIdentityRule, external_principal_id: str) -> AccountAccessIdentityRule

        Creates a new account access identity rule for a given account. This allows administrators to
        explicitly allow or deny specific principals from accessing the account.

        :param parent: str
          Required. The account under which to create the rule. Format: accounts/{account_id}
        :param account_access_identity_rule: :class:`AccountAccessIdentityRule`
          Required. The rule to create.
        :param external_principal_id: str
          Required. The external ID of the principal in the customer's IdP.

        :returns: :class:`AccountAccessIdentityRule`
        

    .. py:method:: create_attribute_control_entry(parent: str, attribute_control_entry: AttributeControlEntry [, attribute_control_entry_id: Optional[str]]) -> AttributeControlEntry

        Creates (allows) an identity attribute control-list entry for an account.

        :param parent: str
          Required. The account under which to create the entry. Format: accounts/{account_id}
        :param attribute_control_entry: :class:`AttributeControlEntry`
          Required. The entry to create.
        :param attribute_control_entry_id: str (optional)
          Optional. The ID to use for the entry, which becomes the last segment of its resource name: the IdP
          attribute being governed (e.g. "department").

        :returns: :class:`AttributeControlEntry`
        

    .. py:method:: create_direct_group_member(group_id: int, direct_group_member: DirectGroupMember) -> DirectGroupMember

        Creates a group membership (assigns a principal to a group).

        :param group_id: int
          Required. Internal ID of the group in Databricks.
        :param direct_group_member: :class:`DirectGroupMember`
          Required. The direct group member to be added to the group.

        :returns: :class:`DirectGroupMember`
        

    .. py:method:: create_group(group: Group) -> Group

        Creates a group in the Databricks account and returns the resulting Group resource.

        :param group: :class:`Group`
          Required. Group to be created in <Databricks>

        :returns: :class:`Group`
        

    .. py:method:: create_service_principal(service_principal: ServicePrincipal) -> ServicePrincipal

        Creates a service principal in the Databricks account and returns the resulting ServicePrincipal
        resource.

        :param service_principal: :class:`ServicePrincipal`
          Required. Service principal to be created in <Databricks>

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: create_user(user: User) -> User

        Creates a user in the Databricks account and returns the resulting User resource. Behavior depends on
        whether Account Identity Management (AIM) is enabled:

        - When AIM is enabled: the user is provisioned with an internalId. If an externalId is provided, the
          identity provider is treated as the source of truth for user metadata, and customer-supplied field
          values may be overridden.
        - When AIM is disabled: the user is provisioned with an internalId only, and customer-supplied
          metadata is used as-is.

        :param user: :class:`User`
          Required. User to be created in <Databricks>

        :returns: :class:`User`
        

    .. py:method:: create_workspace_assignment_detail(workspace_id: int, workspace_assignment_detail: WorkspaceAssignmentDetail) -> WorkspaceAssignmentDetail

        Creates a workspace assignment detail for a principal. Entitlement grants are applied individually and
        non-atomically — if a failure occurs partway through, the principal will be assigned to the
        workspace but with only a subset of the requested entitlements. Use GetWorkspaceAssignmentDetail to
        confirm which entitlements were successfully granted.

        :param workspace_id: int
          Required. The workspace ID for which the workspace assignment detail is being created.
        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be created in <Databricks>.

        :returns: :class:`WorkspaceAssignmentDetail`
        

    .. py:method:: delete_account_access_identity_rule(parent: str, external_principal_id: str)

        Deletes an account access identity rule for a given principal.

        :param parent: str
          Required. The account for which to delete the rule. Format: accounts/{account_id}
        :param external_principal_id: str
          Required. The external ID of the principal whose rule should be deleted.


        

    .. py:method:: delete_attribute_control_entry(name: str)

        Deletes an identity attribute control-list entry.

        :param name: str
          Required. The resource name of the entry to delete. Format:
          accounts/{account_id}/attribute-control-entries/{attribute_name}


        

    .. py:method:: delete_direct_group_member(group_id: int, principal_id: int)

        Deletes a group membership (unassigns a principal from a group).

        :param group_id: int
          Required. Internal ID of the group in Databricks.
        :param principal_id: int
          Required. Internal ID of the principal to be unassigned from the group.


        

    .. py:method:: delete_group(internal_id: str)

        Deletes a group from the Databricks account by its internal ID.

        :param internal_id: str
          Required. Internal ID of the group in Databricks.


        

    .. py:method:: delete_service_principal(internal_id: str)

        Deletes a service principal from the Databricks account by its internal ID.

        :param internal_id: str
          Required. Internal ID of the service principal in Databricks.


        

    .. py:method:: delete_user(internal_id: str)

        Deletes a user from the Databricks account by its internal ID.

        :param internal_id: str
          Required. Internal ID of the user in Databricks.


        

    .. py:method:: delete_workspace_assignment_detail(workspace_id: int, principal_id: int)

        Deletes a workspace assignment detail for a principal, revoking all associated entitlements.
        Entitlement revocations are applied individually and non-atomically — if a failure occurs partway
        through, the principal remains assigned with a subset of its original entitlements, and the operation
        is safe to retry.

        :param workspace_id: int
          The workspace ID where the principal has access.
        :param principal_id: int
          Required. ID of the principal in Databricks to delete workspace assignment for.


        

    .. py:method:: get_account_access_identity_rule(parent: str, external_principal_id: str) -> AccountAccessIdentityRule

        Gets an account access identity rule for a given principal.

        :param parent: str
          Required. The account for which to get the rule. Format: accounts/{account_id}
        :param external_principal_id: str
          Required. The external ID of the principal whose rule should be retrieved.

        :returns: :class:`AccountAccessIdentityRule`
        

    .. py:method:: get_attribute_control_entry(name: str) -> AttributeControlEntry

        Gets an identity attribute control-list entry.

        :param name: str
          Required. The resource name of the entry to get. Format:
          accounts/{account_id}/attribute-control-entries/{attribute_name}

        :returns: :class:`AttributeControlEntry`
        

    .. py:method:: get_direct_group_member(group_id: int, principal_id: int) -> DirectGroupMember

        Gets a provisioned direct member of a group.

        :param group_id: int
          Required. Internal ID of the group in Databricks.
        :param principal_id: int
          Required. Internal ID of the principal belonging to the group in Databricks.

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
        

    .. py:method:: get_group(internal_id: str) -> Group

        Fetches a group from the Databricks account by its internal ID.

        :param internal_id: str
          Required. Internal ID of the group in Databricks.

        :returns: :class:`Group`
        

    .. py:method:: get_service_principal(internal_id: str) -> ServicePrincipal

        Fetches a service principal from the Databricks account by its internal ID.

        :param internal_id: str
          Required. Internal ID of the service principal in Databricks.

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: get_user(internal_id: str) -> User

        Fetches a user from the Databricks account by its internal ID.

        :param internal_id: str
          Required. Internal ID of the user in Databricks.

        :returns: :class:`User`
        

    .. py:method:: get_workspace_access_detail(workspace_id: int, principal_id: int [, view: Optional[WorkspaceAccessDetailView]]) -> WorkspaceAccessDetail

        Returns the access details for a principal in a workspace. Allows for checking access details for any
        provisioned principal (user, service principal, or group) in a workspace.

        - Provisioned principal here refers to one that has been synced into Databricks from the customer's
          IdP or added explicitly to Databricks via SCIM/UI. Allows for passing in a "view" parameter to
          control what fields are returned (BASIC by default or FULL).

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
        

    .. py:method:: list_account_access_identity_rules(parent: str [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> ListAccountAccessIdentityRulesResponse

        Lists all account access identity rules for a given account. These rules control which principals
        (users, service principals, groups) from the customer's IdP are allowed or denied access to the
        Databricks account.

        :param parent: str
          Required. The account for which to list the rules. Format: accounts/{account_id}
        :param filter: str (optional)
          Optional. Filter to apply to the list. Supports filtering by displayName.
        :param page_size: int (optional)
          Optional. The maximum number of rules to return. The service may return fewer than this value.
        :param page_token: str (optional)
          Optional. A page token, received from a previous call. Provide this to retrieve the subsequent page.

        :returns: :class:`ListAccountAccessIdentityRulesResponse`
        

    .. py:method:: list_attribute_control_entries(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> ListAttributeControlEntriesResponse

        Lists the identity attribute control-list entries for an account.

        :param parent: str
          Required. The account for which to list entries. Format: accounts/{account_id}
        :param page_size: int (optional)
          Optional. The maximum number of entries to return.
        :param page_token: str (optional)
          Optional. A page token from a previous call, to retrieve the next page.

        :returns: :class:`ListAttributeControlEntriesResponse`
        

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

        Lists the groups in the Databricks account, returning one page per call. Supports filtering by group
        name or external ID.

        :param filter: str (optional)
          Optional. Allows filtering groups by group name or external id.
        :param page_size: int (optional)
          The maximum number of groups to return. The service may return fewer than this value.
        :param page_token: str (optional)
          A page token, received from a previous ListGroups call. Provide this to retrieve the subsequent
          page.

        :returns: :class:`ListGroupsResponse`
        

    .. py:method:: list_service_principals( [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> ListServicePrincipalsResponse

        Lists the service principals in the Databricks account, returning one page per call. Supports
        filtering by application ID or external ID.

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

        Lists the users in the Databricks account, returning one page per call. Supports filtering by username
        or external ID.

        :param filter: str (optional)
          Optional. Allows filtering users by username or external id.
        :param page_size: int (optional)
          The maximum number of users to return. The service may return fewer than this value.
        :param page_token: str (optional)
          A page token, received from a previous ListUsers call. Provide this to retrieve the subsequent page.

        :returns: :class:`ListUsersResponse`
        

    .. py:method:: list_workspace_access_details(workspace_id: int [, page_size: Optional[int], page_token: Optional[str]]) -> ListWorkspaceAccessDetailsResponse

        Lists the access details of every provisioned principal (user, service principal, or group) with
        access to the given workspace, returning one page per call.

        - Provisioned principal here refers to one that has been synced into Databricks from the customer's
          IdP or added explicitly to Databricks via SCIM/UI.

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

        Lists workspace assignment details for a workspace. For scalability, the response omits the
        per-principal entitlement fields (``entitlements`` and ``effective_entitlements``); call
        GetWorkspaceAssignmentDetail to read entitlements for a single principal.

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
        

    .. py:method:: update_attribute_control_entry(name: str, attribute_control_entry: AttributeControlEntry, update_mask: FieldMask) -> AttributeControlEntry

        Updates an identity attribute control-list entry for an account.

        :param name: str
          The resource name of the entry. Format:
          accounts/{account_id}/attribute-control-entries/{attribute_name} where {attribute_name} is the IdP
          attribute being governed (e.g. "department").
        :param attribute_control_entry: :class:`AttributeControlEntry`
          Required. The entry to update; its ``name`` identifies the existing entry.
        :param update_mask: FieldMask
          Required. The fields to update. For the PrPr only is_allowed is mutable, so the backend currently
          applies the full entry regardless of the mask.

        :returns: :class:`AttributeControlEntry`
        

    .. py:method:: update_group(internal_id: str, group: Group, update_mask: str) -> Group

        Updates an existing group in the Databricks account. Only the fields named in the update mask are
        modified. Returns the updated Group resource.

        :param internal_id: str
          Required. Internal ID of the group in Databricks.
        :param group: :class:`Group`
          Required. Group to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`Group`
        

    .. py:method:: update_service_principal(internal_id: str, service_principal: ServicePrincipal, update_mask: str) -> ServicePrincipal

        Updates an existing service principal in the Databricks account. Only the fields named in the update
        mask are modified. Returns the updated ServicePrincipal resource.

        :param internal_id: str
          Required. Internal ID of the service principal in Databricks.
        :param service_principal: :class:`ServicePrincipal`
          Required. Service Principal to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: update_user(internal_id: str, user: User, update_mask: str) -> User

        Updates an existing user in the Databricks account, returning the updated User resource. The behavior
        is the same whether or not Account Identity Management (AIM) is enabled. Only the fields named in the
        update mask are modified; the updatable fields are fullName.givenName, fullName.familyName, status,
        and externalId.

        :param internal_id: str
          Required. Internal ID of the user in Databricks.
        :param user: :class:`User`
          Required. User to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`User`
        

    .. py:method:: update_workspace_assignment_detail(workspace_id: int, principal_id: int, workspace_assignment_detail: WorkspaceAssignmentDetail, update_mask: FieldMask) -> WorkspaceAssignmentDetail

        Updates the entitlements of a directly assigned principal in a workspace. Entitlement changes are
        applied individually and non-atomically — if a failure occurs partway through, only a subset of the
        requested changes may have been applied. Use GetWorkspaceAssignmentDetail to confirm the final state.

        :param workspace_id: int
          Required. The workspace ID for which the workspace assignment detail is being updated.
        :param principal_id: int
          Required. ID of the principal in Databricks.
        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be updated in <Databricks>.
        :param update_mask: FieldMask
          Required. The list of fields to update.

        :returns: :class:`WorkspaceAssignmentDetail`
        
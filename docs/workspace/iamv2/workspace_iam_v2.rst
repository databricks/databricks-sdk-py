``w.workspace_iam_v2``: workspace_iam.v2
========================================
.. currentmodule:: databricks.sdk.service.iamv2

.. py:class:: WorkspaceIamV2API

    These APIs are used to manage identities and the workspace access of these identities in <Databricks>.

    .. py:method:: create_group_proxy(group: Group) -> Group

        TODO: Write description later when this method is implemented

        :param group: :class:`Group`
          Required. Group to be created in <Databricks>

        :returns: :class:`Group`
        

    .. py:method:: create_service_principal_proxy(service_principal: ServicePrincipal) -> ServicePrincipal

        TODO: Write description later when this method is implemented

        :param service_principal: :class:`ServicePrincipal`
          Required. Service principal to be created in <Databricks>

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: create_user_proxy(user: User) -> User

        TODO: Write description later when this method is implemented

        :param user: :class:`User`
          Required. User to be created in <Databricks>

        :returns: :class:`User`
        

    .. py:method:: create_workspace_access_detail_local(workspace_access_detail: WorkspaceAccessDetail) -> WorkspaceAccessDetail

        TODO: Write description later when this method is implemented

        :param workspace_access_detail: :class:`WorkspaceAccessDetail`
          Required. Workspace access detail to be created in <Databricks>.

        :returns: :class:`WorkspaceAccessDetail`
        

    .. py:method:: delete_group_proxy(internal_id: int)

        TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the group in Databricks.


        

    .. py:method:: delete_service_principal_proxy(internal_id: int)

        TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the service principal in Databricks.


        

    .. py:method:: delete_user_proxy(internal_id: int)

        TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the user in Databricks.


        

    .. py:method:: delete_workspace_access_detail_local(principal_id: int)

        TODO: Write description later when this method is implemented

        :param principal_id: int
          Required. ID of the principal in Databricks.


        

    .. py:method:: get_group_proxy(internal_id: int) -> Group

        TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the group in Databricks.

        :returns: :class:`Group`
        

    .. py:method:: get_service_principal_proxy(internal_id: int) -> ServicePrincipal

        TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the service principal in Databricks.

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: get_user_proxy(internal_id: int) -> User

        TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the user in Databricks.

        :returns: :class:`User`
        

    .. py:method:: get_workspace_access_detail_local(principal_id: int [, view: Optional[WorkspaceAccessDetailView]]) -> WorkspaceAccessDetail

        Returns the access details for a principal in the current workspace. Allows for checking access
        details for any provisioned principal (user, service principal, or group) in the current workspace. *
        Provisioned principal here refers to one that has been synced into Databricks from the customer's IdP
        or added explicitly to Databricks via SCIM/UI. Allows for passing in a "view" parameter to control
        what fields are returned (BASIC by default or FULL).

        :param principal_id: int
          Required. The internal ID of the principal (user/sp/group) for which the access details are being
          requested.
        :param view: :class:`WorkspaceAccessDetailView` (optional)
          Controls what fields are returned.

        :returns: :class:`WorkspaceAccessDetail`
        

    .. py:method:: list_groups_proxy( [, page_size: Optional[int], page_token: Optional[str]]) -> ListGroupsResponse

        TODO: Write description later when this method is implemented

        :param page_size: int (optional)
          The maximum number of groups to return. The service may return fewer than this value.
        :param page_token: str (optional)
          A page token, received from a previous ListGroups call. Provide this to retrieve the subsequent
          page.

        :returns: :class:`ListGroupsResponse`
        

    .. py:method:: list_service_principals_proxy( [, page_size: Optional[int], page_token: Optional[str]]) -> ListServicePrincipalsResponse

        TODO: Write description later when this method is implemented

        :param page_size: int (optional)
          The maximum number of SPs to return. The service may return fewer than this value.
        :param page_token: str (optional)
          A page token, received from a previous ListServicePrincipals call. Provide this to retrieve the
          subsequent page.

        :returns: :class:`ListServicePrincipalsResponse`
        

    .. py:method:: list_users_proxy( [, page_size: Optional[int], page_token: Optional[str]]) -> ListUsersResponse

        TODO: Write description later when this method is implemented

        :param page_size: int (optional)
          The maximum number of users to return. The service may return fewer than this value.
        :param page_token: str (optional)
          A page token, received from a previous ListUsers call. Provide this to retrieve the subsequent page.

        :returns: :class:`ListUsersResponse`
        

    .. py:method:: list_workspace_access_details_local( [, page_size: Optional[int], page_token: Optional[str]]) -> ListWorkspaceAccessDetailsResponse

        TODO: Write description later when this method is implemented

        :param page_size: int (optional)
          The maximum number of workspace access details to return. The service may return fewer than this
          value.
        :param page_token: str (optional)
          A page token, received from a previous ListWorkspaceAccessDetails call. Provide this to retrieve the
          subsequent page.

        :returns: :class:`ListWorkspaceAccessDetailsResponse`
        

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
        

    .. py:method:: update_group_proxy(internal_id: int, group: Group, update_mask: str) -> Group

        TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the group in Databricks.
        :param group: :class:`Group`
          Required. Group to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`Group`
        

    .. py:method:: update_service_principal_proxy(internal_id: int, service_principal: ServicePrincipal, update_mask: str) -> ServicePrincipal

        TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the service principal in Databricks.
        :param service_principal: :class:`ServicePrincipal`
          Required. Service principal to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`ServicePrincipal`
        

    .. py:method:: update_user_proxy(internal_id: int, user: User, update_mask: str) -> User

        TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the user in Databricks.
        :param user: :class:`User`
          Required. User to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`User`
        

    .. py:method:: update_workspace_access_detail_local(principal_id: int, workspace_access_detail: WorkspaceAccessDetail, update_mask: str) -> WorkspaceAccessDetail

        TODO: Write description later when this method is implemented

        :param principal_id: int
          Required. ID of the principal in Databricks.
        :param workspace_access_detail: :class:`WorkspaceAccessDetail`
          Required. WorkspaceAccessDetail to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`WorkspaceAccessDetail`
        
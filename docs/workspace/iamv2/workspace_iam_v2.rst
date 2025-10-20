``w.workspace_iam_v2``: workspace_iam.v2
========================================
.. currentmodule:: databricks.sdk.service.iamv2

.. py:class:: WorkspaceIamV2API

    These APIs are used to manage identities and the workspace access of these identities in <Databricks>.

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
        
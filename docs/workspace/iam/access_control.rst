``w.access_control``: RbacService
=================================
.. currentmodule:: databricks.sdk.service.iam

.. py:class:: AccessControlAPI

    Rule based Access Control for Databricks Resources.

    .. py:method:: check_policy(actor: Actor, permission: str, resource: str, consistency_token: ConsistencyToken, authz_identity: RequestAuthzIdentity [, resource_info: Optional[ResourceInfo]]) -> CheckPolicyResponse

        Check access policy to a resource.

:param actor: :class:`Actor`
:param permission: str
:param resource: str
  Ex: (servicePrincipal/use, accounts/<account-id>/servicePrincipals/<sp-id>) Ex:
  (servicePrincipal.ruleSet/update, accounts/<account-id>/servicePrincipals/<sp-id>/ruleSets/default)
:param consistency_token: :class:`ConsistencyToken`
:param authz_identity: :class:`RequestAuthzIdentity`
:param resource_info: :class:`ResourceInfo` (optional)

:returns: :class:`CheckPolicyResponse`

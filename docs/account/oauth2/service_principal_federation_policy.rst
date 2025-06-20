``a.service_principal_federation_policy``: Service Principal Federation Policies
================================================================================
.. currentmodule:: databricks.sdk.service.oauth2

.. py:class:: ServicePrincipalFederationPolicyAPI

    These APIs manage service principal federation policies.

    Service principal federation, also known as Workload Identity Federation, allows your automated workloads
    running outside of Databricks to securely access Databricks APIs without the need for Databricks secrets.
    With Workload Identity Federation, your application (or workload) authenticates to Databricks as a
    Databricks service principal, using tokens provided by the workload runtime.

    Databricks strongly recommends using Workload Identity Federation to authenticate to Databricks from
    automated workloads, over alternatives such as OAuth client secrets or Personal Access Tokens, whenever
    possible. Workload Identity Federation is supported by many popular services, including Github Actions,
    Azure DevOps, GitLab, Terraform Cloud, and Kubernetes clusters, among others.

    Workload identity federation is configured in your Databricks account using a service principal federation
    policy. A service principal federation policy specifies: * which IdP, or issuer, the service principal is
    allowed to authenticate from * which workload identity, or subject, is allowed to authenticate as the
    Databricks service principal

    To configure a federation policy, you provide the following: * The required token __issuer__, as specified
    in the “iss” claim of workload identity tokens. The issuer is an https URL that identifies the
    workload identity provider. * The required token __subject__, as specified in the “sub” claim of
    workload identity tokens. The subject uniquely identifies the workload in the workload runtime
    environment. * The allowed token __audiences__, as specified in the “aud” claim of workload identity
    tokens. The audience is intended to represent the recipient of the token. As long as the audience in the
    token matches at least one audience in the policy, the token is considered a match. If unspecified, the
    default value is your Databricks account id. * Optionally, the public keys used to validate the signature
    of the workload identity tokens, in JWKS format. If unspecified (recommended), Databricks automatically
    fetches the public keys from the issuer’s well known endpoint. Databricks strongly recommends relying on
    the issuer’s well known endpoint for discovering public keys.

    An example service principal federation policy, for a Github Actions workload, is: ``` issuer:
    "https://token.actions.githubusercontent.com" audiences: ["https://github.com/my-github-org"] subject:
    "repo:my-github-org/my-repo:environment:prod" ```

    An example JWT token body that matches this policy and could be used to authenticate to Databricks is: ```
    { "iss": "https://token.actions.githubusercontent.com", "aud": "https://github.com/my-github-org", "sub":
    "repo:my-github-org/my-repo:environment:prod" } ```

    You may also need to configure the workload runtime to generate tokens for your workloads.

    You do not need to configure an OAuth application in Databricks to use token federation.

    .. py:method:: create(service_principal_id: int, policy: FederationPolicy [, policy_id: Optional[str]]) -> FederationPolicy

        Create account federation policy.

        :param service_principal_id: int
          The service principal id for the federation policy.
        :param policy: :class:`FederationPolicy`
        :param policy_id: str (optional)
          The identifier for the federation policy. The identifier must contain only lowercase alphanumeric
          characters, numbers, hyphens, and slashes. If unspecified, the id will be assigned by Databricks.

        :returns: :class:`FederationPolicy`
        

    .. py:method:: delete(service_principal_id: int, policy_id: str)

        Delete account federation policy.

        :param service_principal_id: int
          The service principal id for the federation policy.
        :param policy_id: str
          The identifier for the federation policy.


        

    .. py:method:: get(service_principal_id: int, policy_id: str) -> FederationPolicy

        Get account federation policy.

        :param service_principal_id: int
          The service principal id for the federation policy.
        :param policy_id: str
          The identifier for the federation policy.

        :returns: :class:`FederationPolicy`
        

    .. py:method:: list(service_principal_id: int [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[FederationPolicy]

        List account federation policies.

        :param service_principal_id: int
          The service principal id for the federation policy.
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`FederationPolicy`
        

    .. py:method:: update(service_principal_id: int, policy_id: str, policy: FederationPolicy [, update_mask: Optional[str]]) -> FederationPolicy

        Update account federation policy.

        :param service_principal_id: int
          The service principal id for the federation policy.
        :param policy_id: str
          The identifier for the federation policy.
        :param policy: :class:`FederationPolicy`
        :param update_mask: str (optional)
          The field mask specifies which fields of the policy to update. To specify multiple fields in the
          field mask, use comma as the separator (no space). The special value '*' indicates that all fields
          should be updated (full replacement). If unspecified, all fields that are set in the policy provided
          in the update request will overwrite the corresponding fields in the existing policy. Example value:
          'description,oidc_policy.audiences'.

        :returns: :class:`FederationPolicy`
        
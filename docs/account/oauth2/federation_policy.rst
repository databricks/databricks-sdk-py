``a.federation_policy``: Account Federation Policies
====================================================
.. currentmodule:: databricks.sdk.service.oauth2

.. py:class:: AccountFederationPolicyAPI

    These APIs manage account federation policies.

    Account federation policies allow users and service principals in your Databricks account to securely
    access Databricks APIs using tokens from your trusted identity providers (IdPs).

    With token federation, your users and service principals can exchange tokens from your IdP for Databricks
    OAuth tokens, which can be used to access Databricks APIs. Token federation eliminates the need to manage
    Databricks secrets, and allows you to centralize management of token issuance policies in your IdP.
    Databricks token federation is typically used in combination with [SCIM], so users in your IdP are
    synchronized into your Databricks account.

    Token federation is configured in your Databricks account using an account federation policy. An account
    federation policy specifies: * which IdP, or issuer, your Databricks account should accept tokens from *
    how to determine which Databricks user, or subject, a token is issued for

    To configure a federation policy, you provide the following: * The required token __issuer__, as specified
    in the “iss” claim of your tokens. The issuer is an https URL that identifies your IdP. * The allowed
    token __audiences__, as specified in the “aud” claim of your tokens. This identifier is intended to
    represent the recipient of the token. As long as the audience in the token matches at least one audience
    in the policy, the token is considered a match. If unspecified, the default value is your Databricks
    account id. * The __subject claim__, which indicates which token claim contains the Databricks username of
    the user the token was issued for. If unspecified, the default value is “sub”. * Optionally, the
    public keys used to validate the signature of your tokens, in JWKS format. If unspecified (recommended),
    Databricks automatically fetches the public keys from your issuer’s well known endpoint. Databricks
    strongly recommends relying on your issuer’s well known endpoint for discovering public keys.

    An example federation policy is: ``` issuer: "https://idp.mycompany.com/oidc" audiences: ["databricks"]
    subject_claim: "sub" ```

    An example JWT token body that matches this policy and could be used to authenticate to Databricks as user
    `username@mycompany.com` is: ``` { "iss": "https://idp.mycompany.com/oidc", "aud": "databricks", "sub":
    "username@mycompany.com" } ```

    You may also need to configure your IdP to generate tokens for your users to exchange with Databricks, if
    your users do not already have the ability to generate tokens that are compatible with your federation
    policy.

    You do not need to configure an OAuth application in Databricks to use token federation.

    [SCIM]: https://docs.databricks.com/admin/users-groups/scim/index.html

    .. py:method:: create( [, policy: Optional[FederationPolicy], policy_id: Optional[str]]) -> FederationPolicy

        Create account federation policy.

        :param policy: :class:`FederationPolicy` (optional)
        :param policy_id: str (optional)
          The identifier for the federation policy. The identifier must contain only lowercase alphanumeric
          characters, numbers, hyphens, and slashes. If unspecified, the id will be assigned by Databricks.

        :returns: :class:`FederationPolicy`
        

    .. py:method:: delete(policy_id: str)

        Delete account federation policy.

        :param policy_id: str
          The identifier for the federation policy.


        

    .. py:method:: get(policy_id: str) -> FederationPolicy

        Get account federation policy.

        :param policy_id: str
          The identifier for the federation policy.

        :returns: :class:`FederationPolicy`
        

    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[FederationPolicy]

        List account federation policies.

        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`FederationPolicy`
        

    .. py:method:: update(policy_id: str [, policy: Optional[FederationPolicy], update_mask: Optional[str]]) -> FederationPolicy

        Update account federation policy.

        :param policy_id: str
          The identifier for the federation policy.
        :param policy: :class:`FederationPolicy` (optional)
        :param update_mask: str (optional)
          The field mask specifies which fields of the policy to update. To specify multiple fields in the
          field mask, use comma as the separator (no space). The special value '*' indicates that all fields
          should be updated (full replacement). If unspecified, all fields that are set in the policy provided
          in the update request will overwrite the corresponding fields in the existing policy. Example value:
          'description,oidc_policy.audiences'.

        :returns: :class:`FederationPolicy`
        
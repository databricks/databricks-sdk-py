``w.recipient_federation_policies``: Recipient Federation Policies
==================================================================
.. currentmodule:: databricks.sdk.service.sharing

.. py:class:: RecipientFederationPoliciesAPI

    The Recipient Federation Policies APIs are only applicable in the open sharing model where the recipient
    object has the authentication type of `OIDC_RECIPIENT`, enabling data sharing from Databricks to
    non-Databricks recipients. OIDC Token Federation enables secure, secret-less authentication for accessing
    Delta Sharing servers. Users and applications authenticate using short-lived OIDC tokens issued by their
    own Identity Provider (IdP), such as Azure Entra ID or Okta, without the need for managing static
    credentials or client secrets. A federation policy defines how non-Databricks recipients authenticate
    using OIDC tokens. It validates the OIDC claims in federated tokens and is set at the recipient level. The
    caller must be the owner of the recipient to create or manage a federation policy. Federation policies
    support the following scenarios: - User-to-Machine (U2M) flow: A user accesses Delta Shares using their
    own identity, such as connecting through PowerBI Delta Sharing Client. - Machine-to-Machine (M2M) flow: An
    application accesses Delta Shares using its own identity, typically for automation tasks like nightly jobs
    through Python Delta Sharing Client. OIDC Token Federation enables fine-grained access control, supports
    Multi-Factor Authentication (MFA), and enhances security by minimizing the risk of credential leakage
    through the use of short-lived, expiring tokens. It is designed for strong identity governance, secure
    cross-platform data sharing, and reduced operational overhead for credential management.

    For more information, see
    https://www.databricks.com/blog/announcing-oidc-token-federation-enhanced-delta-sharing-security and
    https://docs.databricks.com/en/delta-sharing/create-recipient-oidc-fed

    .. py:method:: create(recipient_name: str, policy: FederationPolicy) -> FederationPolicy

        Create a federation policy for an OIDC_FEDERATION recipient for sharing data from Databricks to
        non-Databricks recipients. The caller must be the owner of the recipient. When sharing data from
        Databricks to non-Databricks clients, you can define a federation policy to authenticate
        non-Databricks recipients. The federation policy validates OIDC claims in federated tokens and is
        defined at the recipient level. This enables secretless sharing clients to authenticate using OIDC
        tokens.

        Supported scenarios for federation policies: 1. **User-to-Machine (U2M) flow** (e.g., PowerBI): A user
        accesses a resource using their own identity. 2. **Machine-to-Machine (M2M) flow** (e.g., OAuth App):
        An OAuth App accesses a resource using its own identity, typically for tasks like running nightly
        jobs.

        For an overview, refer to: - Blog post: Overview of feature:
        https://www.databricks.com/blog/announcing-oidc-token-federation-enhanced-delta-sharing-security

        For detailed configuration guides based on your use case: - Creating a Federation Policy as a
        provider: https://docs.databricks.com/en/delta-sharing/create-recipient-oidc-fed - Configuration and
        usage for Machine-to-Machine (M2M) applications (e.g., Python Delta Sharing Client):
        https://docs.databricks.com/aws/en/delta-sharing/sharing-over-oidc-m2m - Configuration and usage for
        User-to-Machine (U2M) applications (e.g., PowerBI):
        https://docs.databricks.com/aws/en/delta-sharing/sharing-over-oidc-u2m

        :param recipient_name: str
          Name of the recipient. This is the name of the recipient for which the policy is being created.
        :param policy: :class:`FederationPolicy`
          Name of the policy. This is the name of the policy to be created.

        :returns: :class:`FederationPolicy`
        

    .. py:method:: delete(recipient_name: str, name: str)

        Deletes an existing federation policy for an OIDC_FEDERATION recipient. The caller must be the owner
        of the recipient.

        :param recipient_name: str
          Name of the recipient. This is the name of the recipient for which the policy is being deleted.
        :param name: str
          Name of the policy. This is the name of the policy to be deleted.


        

    .. py:method:: get_federation_policy(recipient_name: str, name: str) -> FederationPolicy

        Reads an existing federation policy for an OIDC_FEDERATION recipient for sharing data from Databricks
        to non-Databricks recipients. The caller must have read access to the recipient.

        :param recipient_name: str
          Name of the recipient. This is the name of the recipient for which the policy is being retrieved.
        :param name: str
          Name of the policy. This is the name of the policy to be retrieved.

        :returns: :class:`FederationPolicy`
        

    .. py:method:: list(recipient_name: str [, max_results: Optional[int], page_token: Optional[str]]) -> Iterator[FederationPolicy]

        Lists federation policies for an OIDC_FEDERATION recipient for sharing data from Databricks to
        non-Databricks recipients. The caller must have read access to the recipient.

        :param recipient_name: str
          Name of the recipient. This is the name of the recipient for which the policies are being listed.
        :param max_results: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`FederationPolicy`
        

    .. py:method:: update(recipient_name: str, name: str, policy: FederationPolicy [, update_mask: Optional[str]]) -> FederationPolicy

        Updates an existing federation policy for an OIDC_RECIPIENT. The caller must be the owner of the
        recipient.

        :param recipient_name: str
          Name of the recipient. This is the name of the recipient for which the policy is being updated.
        :param name: str
          Name of the policy. This is the name of the current name of the policy.
        :param policy: :class:`FederationPolicy`
        :param update_mask: str (optional)
          The field mask specifies which fields of the policy to update. To specify multiple fields in the
          field mask, use comma as the separator (no space). The special value '*' indicates that all fields
          should be updated (full replacement). If unspecified, all fields that are set in the policy provided
          in the update request will overwrite the corresponding fields in the existing policy. Example value:
          'comment,oidc_policy.audiences'.

        :returns: :class:`FederationPolicy`
        
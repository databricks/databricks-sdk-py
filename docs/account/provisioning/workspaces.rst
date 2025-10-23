``a.workspaces``: Workspaces
============================
.. currentmodule:: databricks.sdk.service.provisioning

.. py:class:: WorkspacesAPI

    These APIs manage workspaces for this account. A Databricks workspace is an environment for accessing all
    of your Databricks assets. The workspace organizes objects (notebooks, libraries, and experiments) into
    folders, and provides access to data and computational resources such as clusters and jobs.

    These endpoints are available if your account is on the E2 version of the platform or on a select custom
    plan that allows multiple workspaces per account.

    .. py:method:: create( [, aws_region: Optional[str], cloud: Optional[str], cloud_resource_container: Optional[CloudResourceContainer], compute_mode: Optional[CustomerFacingComputeMode], credentials_id: Optional[str], custom_tags: Optional[Dict[str, str]], deployment_name: Optional[str], gcp_managed_network_config: Optional[GcpManagedNetworkConfig], gke_config: Optional[GkeConfig], location: Optional[str], managed_services_customer_managed_key_id: Optional[str], network_connectivity_config_id: Optional[str], network_id: Optional[str], pricing_tier: Optional[PricingTier], private_access_settings_id: Optional[str], storage_configuration_id: Optional[str], storage_customer_managed_key_id: Optional[str], workspace_name: Optional[str]]) -> Wait[Workspace]


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import provisioning
            
            a = AccountClient()
            
            storage = a.storage.create(
                storage_configuration_name=f"sdk-{time.time_ns()}",
                root_bucket_info=provisioning.RootBucketInfo(bucket_name=os.environ["TEST_ROOT_BUCKET"]),
            )
            
            role = a.credentials.create(
                credentials_name=f"sdk-{time.time_ns()}",
                aws_credentials=provisioning.CreateCredentialAwsCredentials(
                    sts_role=provisioning.CreateCredentialStsRole(role_arn=os.environ["TEST_CROSSACCOUNT_ARN"])
                ),
            )
            
            waiter = a.workspaces.create(
                workspace_name=f"sdk-{time.time_ns()}",
                aws_region=os.environ["AWS_REGION"],
                credentials_id=role.credentials_id,
                storage_configuration_id=storage.storage_configuration_id,
            )
            
            # cleanup
            a.storage.delete(storage_configuration_id=storage.storage_configuration_id)
            a.credentials.delete(credentials_id=role.credentials_id)
            a.workspaces.delete(workspace_id=waiter.workspace_id)

        Creates a new workspace using a credential configuration and a storage configuration, an optional
        network configuration (if using a customer-managed VPC), an optional managed services key
        configuration (if using customer-managed keys for managed services), and an optional storage key
        configuration (if using customer-managed keys for storage). The key configurations used for managed
        services and storage encryption can be the same or different.

        Important: This operation is asynchronous. A response with HTTP status code 200 means the request has
        been accepted and is in progress, but does not mean that the workspace deployed successfully and is
        running. The initial workspace status is typically PROVISIONING. Use the workspace ID (workspace_id)
        field in the response to identify the new workspace and make repeated GET requests with the workspace
        ID and check its status. The workspace becomes available when the status changes to RUNNING.

        You can share one customer-managed VPC with multiple workspaces in a single account. It is not
        required to create a new VPC for each workspace. However, you cannot reuse subnets or Security Groups
        between workspaces. If you plan to share one VPC with multiple workspaces, make sure you size your VPC
        and subnets accordingly. Because a Databricks Account API network configuration encapsulates this
        information, you cannot reuse a Databricks Account API network configuration across workspaces.

        For information about how to create a new workspace with this API including error handling, see
        [Create a new workspace using the Account API].

        Important: Customer-managed VPCs, PrivateLink, and customer-managed keys are supported on a limited
        set of deployment and subscription types. If you have questions about availability, contact your
        Databricks representative.

        This operation is available only if your account is on the E2 version of the platform or on a select
        custom plan that allows multiple workspaces per account.

        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html

        :param aws_region: str (optional)
        :param cloud: str (optional)
          The cloud name. This field always has the value `gcp`.
        :param cloud_resource_container: :class:`CloudResourceContainer` (optional)
        :param compute_mode: :class:`CustomerFacingComputeMode` (optional)
          If the compute mode is `SERVERLESS`, a serverless workspace is created that comes pre-configured
          with serverless compute and default storage, providing a fully-managed, enterprise-ready SaaS
          experience. This means you don't need to provide any resources managed by you, such as credentials,
          storage, or network. If the compute mode is `HYBRID` (which is the default option), a classic
          workspace is created that uses customer-managed resources.
        :param credentials_id: str (optional)
          ID of the workspace's credential configuration object.
        :param custom_tags: Dict[str,str] (optional)
          The custom tags key-value pairing that is attached to this workspace. The key-value pair is a string
          of utf-8 characters. The value can be an empty string, with maximum length of 255 characters. The
          key can be of maximum length of 127 characters, and cannot be empty.
        :param deployment_name: str (optional)
          The deployment name defines part of the subdomain for the workspace. The workspace URL for the web
          application and REST APIs is <workspace-deployment-name>.cloud.databricks.com. For example, if the
          deployment name is abcsales, your workspace URL will be https://abcsales.cloud.databricks.com.
          Hyphens are allowed. This property supports only the set of characters that are allowed in a
          subdomain. To set this value, you must have a deployment name prefix. Contact your Databricks
          account team to add an account deployment name prefix to your account. Workspace deployment names
          follow the account prefix and a hyphen. For example, if your account's deployment prefix is acme and
          the workspace deployment name is workspace-1, the JSON response for the deployment_name field
          becomes acme-workspace-1. The workspace URL would be acme-workspace-1.cloud.databricks.com. You can
          also set the deployment_name to the reserved keyword EMPTY if you want the deployment name to only
          include the deployment prefix. For example, if your account's deployment prefix is acme and the
          workspace deployment name is EMPTY, the deployment_name becomes acme only and the workspace URL is
          acme.cloud.databricks.com. This value must be unique across all non-deleted deployments across all
          AWS regions. If a new workspace omits this property, the server generates a unique deployment name
          for you with the pattern dbc-xxxxxxxx-xxxx.
        :param gcp_managed_network_config: :class:`GcpManagedNetworkConfig` (optional)
        :param gke_config: :class:`GkeConfig` (optional)
        :param location: str (optional)
          The Google Cloud region of the workspace data plane in your Google account (for example,
          `us-east4`).
        :param managed_services_customer_managed_key_id: str (optional)
          The ID of the workspace's managed services encryption key configuration object. This is used to help
          protect and control access to the workspace's notebooks, secrets, Databricks SQL queries, and query
          history. The provided key configuration object property use_cases must contain MANAGED_SERVICES.
        :param network_connectivity_config_id: str (optional)
          The object ID of network connectivity config. Once assigned, the workspace serverless compute
          resources use the same set of stable IP CIDR blocks and optional private link to access your
          resources.
        :param network_id: str (optional)
          The ID of the workspace's network configuration object. To use AWS PrivateLink, this field is
          required.
        :param pricing_tier: :class:`PricingTier` (optional)
        :param private_access_settings_id: str (optional)
          ID of the workspace's private access settings object. Only used for PrivateLink. You must specify
          this ID if you are using [AWS PrivateLink] for either front-end (user-to-workspace connection),
          back-end (data plane to control plane connection), or both connection types. Before configuring
          PrivateLink, read the [Databricks article about PrivateLink].",

          [AWS PrivateLink]: https://aws.amazon.com/privatelink/
          [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
        :param storage_configuration_id: str (optional)
          ID of the workspace's storage configuration object.
        :param storage_customer_managed_key_id: str (optional)
          The ID of the workspace's storage encryption key configuration object. This is used to encrypt the
          workspace's root S3 bucket (root DBFS and system data) and, optionally, cluster EBS volumes. The
          provided key configuration object property use_cases must contain STORAGE.
        :param workspace_name: str (optional)
          The human-readable name of the workspace.

        :returns:
          Long-running operation waiter for :class:`Workspace`.
          See :method:wait_get_workspace_running for more details.
        

    .. py:method:: create_and_wait( [, aws_region: Optional[str], cloud: Optional[str], cloud_resource_container: Optional[CloudResourceContainer], compute_mode: Optional[CustomerFacingComputeMode], credentials_id: Optional[str], custom_tags: Optional[Dict[str, str]], deployment_name: Optional[str], gcp_managed_network_config: Optional[GcpManagedNetworkConfig], gke_config: Optional[GkeConfig], location: Optional[str], managed_services_customer_managed_key_id: Optional[str], network_connectivity_config_id: Optional[str], network_id: Optional[str], pricing_tier: Optional[PricingTier], private_access_settings_id: Optional[str], storage_configuration_id: Optional[str], storage_customer_managed_key_id: Optional[str], workspace_name: Optional[str], timeout: datetime.timedelta = 0:20:00]) -> Workspace


    .. py:method:: delete(workspace_id: int) -> Workspace

        Deletes a Databricks workspace, both specified by ID.

        :param workspace_id: int

        :returns: :class:`Workspace`
        

    .. py:method:: get(workspace_id: int) -> Workspace


        Usage:

        .. code-block::

            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            created = a.waiter.get()
            
            by_id = a.workspaces.get(workspace_id=created.workspace_id)

        Gets information including status for a Databricks workspace, specified by ID. In the response, the
        `workspace_status` field indicates the current status. After initial workspace creation (which is
        asynchronous), make repeated `GET` requests with the workspace ID and check its status. The workspace
        becomes available when the status changes to `RUNNING`. For information about how to create a new
        workspace with this API **including error handling**, see [Create a new workspace using the Account
        API].

        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html

        :param workspace_id: int

        :returns: :class:`Workspace`
        

    .. py:method:: list() -> Iterator[Workspace]


        Usage:

        .. code-block::

            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            all = a.workspaces.list()

        Lists Databricks workspaces for an account.


        :returns: Iterator over :class:`Workspace`
        

    .. py:method:: update(workspace_id: int, customer_facing_workspace: Workspace [, update_mask: Optional[str]]) -> Wait[Workspace]


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import provisioning
            
            a = AccountClient()
            
            update_role = a.credentials.create(
                credentials_name=f"sdk-{time.time_ns()}",
                aws_credentials=provisioning.CreateCredentialAwsCredentials(
                    sts_role=provisioning.CreateCredentialStsRole(role_arn=os.environ["TEST_CROSSACCOUNT_ARN"])
                ),
            )
            
            created = a.waiter.get()
            
            _ = a.workspaces.update(
                workspace_id=created.workspace_id,
                credentials_id=update_role.credentials_id,
            ).result()
            
            # cleanup
            a.credentials.delete(credentials_id=update_role.credentials_id)

        Updates a workspace.

        :param workspace_id: int
          A unique integer ID for the workspace
        :param customer_facing_workspace: :class:`Workspace`
        :param update_mask: str (optional)
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.

        :returns:
          Long-running operation waiter for :class:`Workspace`.
          See :method:wait_get_workspace_running for more details.
        

    .. py:method:: update_and_wait(workspace_id: int, customer_facing_workspace: Workspace [, update_mask: Optional[str], timeout: datetime.timedelta = 0:20:00]) -> Workspace


    .. py:method:: wait_get_workspace_running(workspace_id: int, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[Workspace], None]]) -> Workspace

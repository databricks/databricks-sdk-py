``a.workspaces``: Workspaces
============================
.. currentmodule:: databricks.sdk.service.provisioning

.. py:class:: WorkspacesAPI

    These APIs manage workspaces for this account. A Databricks workspace is an environment for accessing all
    of your Databricks assets. The workspace organizes objects (notebooks, libraries, and experiments) into
    folders, and provides access to data and computational resources such as clusters and jobs.
    
    These endpoints are available if your account is on the E2 version of the platform or on a select custom
    plan that allows multiple workspaces per account.

    .. py:method:: create(workspace_name: str [, aws_region: Optional[str], cloud: Optional[str], cloud_resource_container: Optional[CloudResourceContainer], credentials_id: Optional[str], custom_tags: Optional[Dict[str, str]], deployment_name: Optional[str], gcp_managed_network_config: Optional[GcpManagedNetworkConfig], gke_config: Optional[GkeConfig], location: Optional[str], managed_services_customer_managed_key_id: Optional[str], network_id: Optional[str], pricing_tier: Optional[PricingTier], private_access_settings_id: Optional[str], storage_configuration_id: Optional[str], storage_customer_managed_key_id: Optional[str]]) -> Wait[Workspace]


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import provisioning
            
            a = AccountClient()
            
            storage = a.storage.create(
                storage_configuration_name=f'sdk-{time.time_ns()}',
                root_bucket_info=provisioning.RootBucketInfo(bucket_name=os.environ["TEST_ROOT_BUCKET"]))
            
            role = a.credentials.create(
                credentials_name=f'sdk-{time.time_ns()}',
                aws_credentials=provisioning.CreateCredentialAwsCredentials(sts_role=provisioning.CreateCredentialStsRole(
                    role_arn=os.environ["TEST_CROSSACCOUNT_ARN"])))
            
            waiter = a.workspaces.create(workspace_name=f'sdk-{time.time_ns()}',
                                         aws_region=os.environ["AWS_REGION"],
                                         credentials_id=role.credentials_id,
                                         storage_configuration_id=storage.storage_configuration_id)
            
            # cleanup
            a.storage.delete(storage_configuration_id=storage.storage_configuration_id)
            a.credentials.delete(credentials_id=role.credentials_id)
            a.workspaces.delete(workspace_id=waiter.workspace_id)

        Create a new workspace.
        
        Creates a new workspace.
        
        **Important**: This operation is asynchronous. A response with HTTP status code 200 means the request
        has been accepted and is in progress, but does not mean that the workspace deployed successfully and
        is running. The initial workspace status is typically `PROVISIONING`. Use the workspace ID
        (`workspace_id`) field in the response to identify the new workspace and make repeated `GET` requests
        with the workspace ID and check its status. The workspace becomes available when the status changes to
        `RUNNING`.
        
        :param workspace_name: str
          The workspace's human-readable name.
        :param aws_region: str (optional)
          The AWS region of the workspace's data plane.
        :param cloud: str (optional)
          The cloud provider which the workspace uses. For Google Cloud workspaces, always set this field to
          `gcp`.
        :param cloud_resource_container: :class:`CloudResourceContainer` (optional)
          The general workspace configurations that are specific to cloud providers.
        :param credentials_id: str (optional)
          ID of the workspace's credential configuration object.
        :param custom_tags: Dict[str,str] (optional)
          The custom tags key-value pairing that is attached to this workspace. The key-value pair is a string
          of utf-8 characters. The value can be an empty string, with maximum length of 255 characters. The
          key can be of maximum length of 127 characters, and cannot be empty.
        :param deployment_name: str (optional)
          The deployment name defines part of the subdomain for the workspace. The workspace URL for the web
          application and REST APIs is `<workspace-deployment-name>.cloud.databricks.com`. For example, if the
          deployment name is `abcsales`, your workspace URL will be `https://abcsales.cloud.databricks.com`.
          Hyphens are allowed. This property supports only the set of characters that are allowed in a
          subdomain.
          
          To set this value, you must have a deployment name prefix. Contact your Databricks account team to
          add an account deployment name prefix to your account.
          
          Workspace deployment names follow the account prefix and a hyphen. For example, if your account's
          deployment prefix is `acme` and the workspace deployment name is `workspace-1`, the JSON response
          for the `deployment_name` field becomes `acme-workspace-1`. The workspace URL would be
          `acme-workspace-1.cloud.databricks.com`.
          
          You can also set the `deployment_name` to the reserved keyword `EMPTY` if you want the deployment
          name to only include the deployment prefix. For example, if your account's deployment prefix is
          `acme` and the workspace deployment name is `EMPTY`, the `deployment_name` becomes `acme` only and
          the workspace URL is `acme.cloud.databricks.com`.
          
          This value must be unique across all non-deleted deployments across all AWS regions.
          
          If a new workspace omits this property, the server generates a unique deployment name for you with
          the pattern `dbc-xxxxxxxx-xxxx`.
        :param gcp_managed_network_config: :class:`GcpManagedNetworkConfig` (optional)
          The network settings for the workspace. The configurations are only for Databricks-managed VPCs. It
          is ignored if you specify a customer-managed VPC in the `network_id` field.", All the IP range
          configurations must be mutually exclusive. An attempt to create a workspace fails if Databricks
          detects an IP range overlap.
          
          Specify custom IP ranges in CIDR format. The IP ranges for these fields must not overlap, and all IP
          addresses must be entirely within the following ranges: `10.0.0.0/8`, `100.64.0.0/10`,
          `172.16.0.0/12`, `192.168.0.0/16`, and `240.0.0.0/4`.
          
          The sizes of these IP ranges affect the maximum number of nodes for the workspace.
          
          **Important**: Confirm the IP ranges used by your Databricks workspace before creating the
          workspace. You cannot change them after your workspace is deployed. If the IP address ranges for
          your Databricks are too small, IP exhaustion can occur, causing your Databricks jobs to fail. To
          determine the address range sizes that you need, Databricks provides a calculator as a Microsoft
          Excel spreadsheet. See [calculate subnet sizes for a new workspace].
          
          [calculate subnet sizes for a new workspace]: https://docs.gcp.databricks.com/administration-guide/cloud-configurations/gcp/network-sizing.html
        :param gke_config: :class:`GkeConfig` (optional)
          The configurations for the GKE cluster of a Databricks workspace.
        :param location: str (optional)
          The Google Cloud region of the workspace data plane in your Google account. For example, `us-east4`.
        :param managed_services_customer_managed_key_id: str (optional)
          The ID of the workspace's managed services encryption key configuration object. This is used to help
          protect and control access to the workspace's notebooks, secrets, Databricks SQL queries, and query
          history. The provided key configuration object property `use_cases` must contain `MANAGED_SERVICES`.
        :param network_id: str (optional)
        :param pricing_tier: :class:`PricingTier` (optional)
          The pricing tier of the workspace. For pricing tier information, see [AWS Pricing].
          
          [AWS Pricing]: https://databricks.com/product/aws-pricing
        :param private_access_settings_id: str (optional)
          ID of the workspace's private access settings object. Only used for PrivateLink. This ID must be
          specified for customers using [AWS PrivateLink] for either front-end (user-to-workspace connection),
          back-end (data plane to control plane connection), or both connection types.
          
          Before configuring PrivateLink, read the [Databricks article about PrivateLink].",
          
          [AWS PrivateLink]: https://aws.amazon.com/privatelink/
          [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
        :param storage_configuration_id: str (optional)
          The ID of the workspace's storage configuration object.
        :param storage_customer_managed_key_id: str (optional)
          The ID of the workspace's storage encryption key configuration object. This is used to encrypt the
          workspace's root S3 bucket (root DBFS and system data) and, optionally, cluster EBS volumes. The
          provided key configuration object property `use_cases` must contain `STORAGE`.
        
        :returns:
          Long-running operation waiter for :class:`Workspace`.
          See :method:wait_get_workspace_running for more details.
        

    .. py:method:: create_and_wait(workspace_name: str [, aws_region: Optional[str], cloud: Optional[str], cloud_resource_container: Optional[CloudResourceContainer], credentials_id: Optional[str], custom_tags: Optional[Dict[str, str]], deployment_name: Optional[str], gcp_managed_network_config: Optional[GcpManagedNetworkConfig], gke_config: Optional[GkeConfig], location: Optional[str], managed_services_customer_managed_key_id: Optional[str], network_id: Optional[str], pricing_tier: Optional[PricingTier], private_access_settings_id: Optional[str], storage_configuration_id: Optional[str], storage_customer_managed_key_id: Optional[str], timeout: datetime.timedelta = 0:20:00]) -> Workspace


    .. py:method:: delete(workspace_id: int)

        Delete a workspace.
        
        Terminates and deletes a Databricks workspace. From an API perspective, deletion is immediate.
        However, it might take a few minutes for all workspaces resources to be deleted, depending on the size
        and number of workspace resources.
        
        This operation is available only if your account is on the E2 version of the platform or on a select
        custom plan that allows multiple workspaces per account.
        
        :param workspace_id: int
          Workspace ID.
        
        
        

    .. py:method:: get(workspace_id: int) -> Workspace


        Usage:

        .. code-block::

            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            created = a.waiter.get()
            
            by_id = a.workspaces.get(workspace_id=created.workspace_id)

        Get a workspace.
        
        Gets information including status for a Databricks workspace, specified by ID. In the response, the
        `workspace_status` field indicates the current status. After initial workspace creation (which is
        asynchronous), make repeated `GET` requests with the workspace ID and check its status. The workspace
        becomes available when the status changes to `RUNNING`.
        
        For information about how to create a new workspace with this API **including error handling**, see
        [Create a new workspace using the Account API].
        
        This operation is available only if your account is on the E2 version of the platform or on a select
        custom plan that allows multiple workspaces per account.
        
        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html
        
        :param workspace_id: int
          Workspace ID.
        
        :returns: :class:`Workspace`
        

    .. py:method:: list() -> Iterator[Workspace]


        Usage:

        .. code-block::

            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            all = a.workspaces.list()

        Get all workspaces.
        
        Gets a list of all workspaces associated with an account, specified by ID.
        
        This operation is available only if your account is on the E2 version of the platform or on a select
        custom plan that allows multiple workspaces per account.
        
        :returns: Iterator over :class:`Workspace`
        

    .. py:method:: update(workspace_id: int [, aws_region: Optional[str], credentials_id: Optional[str], custom_tags: Optional[Dict[str, str]], managed_services_customer_managed_key_id: Optional[str], network_connectivity_config_id: Optional[str], network_id: Optional[str], storage_configuration_id: Optional[str], storage_customer_managed_key_id: Optional[str]]) -> Wait[Workspace]


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import provisioning
            
            a = AccountClient()
            
            update_role = a.credentials.create(
                credentials_name=f'sdk-{time.time_ns()}',
                aws_credentials=provisioning.CreateCredentialAwsCredentials(sts_role=provisioning.CreateCredentialStsRole(
                    role_arn=os.environ["TEST_CROSSACCOUNT_ARN"])))
            
            created = a.waiter.get()
            
            _ = a.workspaces.update(workspace_id=created.workspace_id, credentials_id=update_role.credentials_id).result()
            
            # cleanup
            a.credentials.delete(credentials_id=update_role.credentials_id)

        Update workspace configuration.
        
        Updates a workspace configuration for either a running workspace or a failed workspace. The elements
        that can be updated varies between these two use cases.
        
        ### Update a failed workspace You can update a Databricks workspace configuration for failed workspace
        deployment for some fields, but not all fields. For a failed workspace, this request supports updates
        to the following fields only: - Credential configuration ID - Storage configuration ID - Network
        configuration ID. Used only to add or change a network configuration for a customer-managed VPC. For a
        failed workspace only, you can convert a workspace with Databricks-managed VPC to use a
        customer-managed VPC by adding this ID. You cannot downgrade a workspace with a customer-managed VPC
        to be a Databricks-managed VPC. You can update the network configuration for a failed or running
        workspace to add PrivateLink support, though you must also add a private access settings object. - Key
        configuration ID for managed services (control plane storage, such as notebook source and Databricks
        SQL queries). Used only if you use customer-managed keys for managed services. - Key configuration ID
        for workspace storage (root S3 bucket and, optionally, EBS volumes). Used only if you use
        customer-managed keys for workspace storage. **Important**: If the workspace was ever in the running
        state, even if briefly before becoming a failed workspace, you cannot add a new key configuration ID
        for workspace storage. - Private access settings ID to add PrivateLink support. You can add or update
        the private access settings ID to upgrade a workspace to add support for front-end, back-end, or both
        types of connectivity. You cannot remove (downgrade) any existing front-end or back-end PrivateLink
        support on a workspace. - Custom tags. Given you provide an empty custom tags, the update would not be
        applied. - Network connectivity configuration ID to add serverless stable IP support. You can add or
        update the network connectivity configuration ID to ensure the workspace uses the same set of stable
        IP CIDR blocks to access your resources. You cannot remove a network connectivity configuration from
        the workspace once attached, you can only switch to another one.
        
        After calling the `PATCH` operation to update the workspace configuration, make repeated `GET`
        requests with the workspace ID and check the workspace status. The workspace is successful if the
        status changes to `RUNNING`.
        
        For information about how to create a new workspace with this API **including error handling**, see
        [Create a new workspace using the Account API].
        
        ### Update a running workspace You can update a Databricks workspace configuration for running
        workspaces for some fields, but not all fields. For a running workspace, this request supports
        updating the following fields only: - Credential configuration ID - Network configuration ID. Used
        only if you already use a customer-managed VPC. You cannot convert a running workspace from a
        Databricks-managed VPC to a customer-managed VPC. You can use a network configuration update in this
        API for a failed or running workspace to add support for PrivateLink, although you also need to add a
        private access settings object. - Key configuration ID for managed services (control plane storage,
        such as notebook source and Databricks SQL queries). Databricks does not directly encrypt the data
        with the customer-managed key (CMK). Databricks uses both the CMK and the Databricks managed key (DMK)
        that is unique to your workspace to encrypt the Data Encryption Key (DEK). Databricks uses the DEK to
        encrypt your workspace's managed services persisted data. If the workspace does not already have a CMK
        for managed services, adding this ID enables managed services encryption for new or updated data.
        Existing managed services data that existed before adding the key remains not encrypted with the DEK
        until it is modified. If the workspace already has customer-managed keys for managed services, this
        request rotates (changes) the CMK keys and the DEK is re-encrypted with the DMK and the new CMK. - Key
        configuration ID for workspace storage (root S3 bucket and, optionally, EBS volumes). You can set this
        only if the workspace does not already have a customer-managed key configuration for workspace
        storage. - Private access settings ID to add PrivateLink support. You can add or update the private
        access settings ID to upgrade a workspace to add support for front-end, back-end, or both types of
        connectivity. You cannot remove (downgrade) any existing front-end or back-end PrivateLink support on
        a workspace. - Custom tags. Given you provide an empty custom tags, the update would not be applied. -
        Network connectivity configuration ID to add serverless stable IP support. You can add or update the
        network connectivity configuration ID to ensure the workspace uses the same set of stable IP CIDR
        blocks to access your resources. You cannot remove a network connectivity configuration from the
        workspace once attached, you can only switch to another one.
        
        **Important**: To update a running workspace, your workspace must have no running compute resources
        that run in your workspace's VPC in the Classic data plane. For example, stop all all-purpose
        clusters, job clusters, pools with running clusters, and Classic SQL warehouses. If you do not
        terminate all cluster instances in the workspace before calling this API, the request will fail.
        
        ### Wait until changes take effect. After calling the `PATCH` operation to update the workspace
        configuration, make repeated `GET` requests with the workspace ID and check the workspace status and
        the status of the fields. * For workspaces with a Databricks-managed VPC, the workspace status becomes
        `PROVISIONING` temporarily (typically under 20 minutes). If the workspace update is successful, the
        workspace status changes to `RUNNING`. Note that you can also check the workspace status in the
        [Account Console]. However, you cannot use or create clusters for another 20 minutes after that status
        change. This results in a total of up to 40 minutes in which you cannot create clusters. If you create
        or use clusters before this time interval elapses, clusters do not launch successfully, fail, or could
        cause other unexpected behavior. * For workspaces with a customer-managed VPC, the workspace status
        stays at status `RUNNING` and the VPC change happens immediately. A change to the storage
        customer-managed key configuration ID might take a few minutes to update, so continue to check the
        workspace until you observe that it has been updated. If the update fails, the workspace might revert
        silently to its original configuration. After the workspace has been updated, you cannot use or create
        clusters for another 20 minutes. If you create or use clusters before this time interval elapses,
        clusters do not launch successfully, fail, or could cause other unexpected behavior.
        
        If you update the _storage_ customer-managed key configurations, it takes 20 minutes for the changes
        to fully take effect. During the 20 minute wait, it is important that you stop all REST API calls to
        the DBFS API. If you are modifying _only the managed services key configuration_, you can omit the 20
        minute wait.
        
        **Important**: Customer-managed keys and customer-managed VPCs are supported by only some deployment
        types and subscription types. If you have questions about availability, contact your Databricks
        representative.
        
        This operation is available only if your account is on the E2 version of the platform or on a select
        custom plan that allows multiple workspaces per account.
        
        [Account Console]: https://docs.databricks.com/administration-guide/account-settings-e2/account-console-e2.html
        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html
        
        :param workspace_id: int
          Workspace ID.
        :param aws_region: str (optional)
          The AWS region of the workspace's data plane (for example, `us-west-2`). This parameter is available
          only for updating failed workspaces.
        :param credentials_id: str (optional)
          ID of the workspace's credential configuration object. This parameter is available for updating both
          failed and running workspaces.
        :param custom_tags: Dict[str,str] (optional)
          The custom tags key-value pairing that is attached to this workspace. The key-value pair is a string
          of utf-8 characters. The value can be an empty string, with maximum length of 255 characters. The
          key can be of maximum length of 127 characters, and cannot be empty.
        :param managed_services_customer_managed_key_id: str (optional)
          The ID of the workspace's managed services encryption key configuration object. This parameter is
          available only for updating failed workspaces.
        :param network_connectivity_config_id: str (optional)
        :param network_id: str (optional)
          The ID of the workspace's network configuration object. Used only if you already use a
          customer-managed VPC. For failed workspaces only, you can switch from a Databricks-managed VPC to a
          customer-managed VPC by updating the workspace to add a network configuration ID.
        :param storage_configuration_id: str (optional)
          The ID of the workspace's storage configuration object. This parameter is available only for
          updating failed workspaces.
        :param storage_customer_managed_key_id: str (optional)
          The ID of the key configuration object for workspace storage. This parameter is available for
          updating both failed and running workspaces.
        
        :returns:
          Long-running operation waiter for :class:`Workspace`.
          See :method:wait_get_workspace_running for more details.
        

    .. py:method:: update_and_wait(workspace_id: int [, aws_region: Optional[str], credentials_id: Optional[str], custom_tags: Optional[Dict[str, str]], managed_services_customer_managed_key_id: Optional[str], network_connectivity_config_id: Optional[str], network_id: Optional[str], storage_configuration_id: Optional[str], storage_customer_managed_key_id: Optional[str], timeout: datetime.timedelta = 0:20:00]) -> Workspace


    .. py:method:: wait_get_workspace_running(workspace_id: int, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[Workspace], None]]) -> Workspace

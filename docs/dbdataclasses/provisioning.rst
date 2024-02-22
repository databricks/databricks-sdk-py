Provisioning
============

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.provisioning`` module.

.. py:currentmodule:: databricks.sdk.service.provisioning
.. autoclass:: AwsCredentials
   :members:
   :undoc-members:

.. autoclass:: AwsKeyInfo
   :members:
   :undoc-members:

.. autoclass:: AzureWorkspaceInfo
   :members:
   :undoc-members:

.. autoclass:: CloudResourceContainer
   :members:
   :undoc-members:

.. autoclass:: CreateAwsKeyInfo
   :members:
   :undoc-members:

.. autoclass:: CreateCredentialAwsCredentials
   :members:
   :undoc-members:

.. autoclass:: CreateCredentialRequest
   :members:
   :undoc-members:

.. autoclass:: CreateCredentialStsRole
   :members:
   :undoc-members:

.. autoclass:: CreateCustomerManagedKeyRequest
   :members:
   :undoc-members:

.. autoclass:: CreateGcpKeyInfo
   :members:
   :undoc-members:

.. autoclass:: CreateNetworkRequest
   :members:
   :undoc-members:

.. autoclass:: CreateStorageConfigurationRequest
   :members:
   :undoc-members:

.. autoclass:: CreateVpcEndpointRequest
   :members:
   :undoc-members:

.. autoclass:: CreateWorkspaceRequest
   :members:
   :undoc-members:

.. autoclass:: Credential
   :members:
   :undoc-members:

.. autoclass:: CustomerFacingGcpCloudResourceContainer
   :members:
   :undoc-members:

.. autoclass:: CustomerManagedKey
   :members:
   :undoc-members:

.. py:class:: EndpointUseCase

   This enumeration represents the type of Databricks VPC [endpoint service] that was used when
    creating this VPC endpoint.
    
    [endpoint service]: https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-service.html

   .. py:attribute:: DATAPLANE_RELAY_ACCESS
      :value: "DATAPLANE_RELAY_ACCESS"

   .. py:attribute:: WORKSPACE_ACCESS
      :value: "WORKSPACE_ACCESS"

.. py:class:: ErrorType

   The AWS resource associated with this error: credentials, VPC, subnet, security group, or
    network ACL.

   .. py:attribute:: CREDENTIALS
      :value: "CREDENTIALS"

   .. py:attribute:: NETWORK_ACL
      :value: "NETWORK_ACL"

   .. py:attribute:: SECURITY_GROUP
      :value: "SECURITY_GROUP"

   .. py:attribute:: SUBNET
      :value: "SUBNET"

   .. py:attribute:: VPC
      :value: "VPC"

.. autoclass:: GcpKeyInfo
   :members:
   :undoc-members:

.. autoclass:: GcpManagedNetworkConfig
   :members:
   :undoc-members:

.. autoclass:: GcpNetworkInfo
   :members:
   :undoc-members:

.. autoclass:: GcpVpcEndpointInfo
   :members:
   :undoc-members:

.. autoclass:: GkeConfig
   :members:
   :undoc-members:

.. py:class:: GkeConfigConnectivityType

   Specifies the network connectivity types for the GKE nodes and the GKE master network.
    
    Set to `PRIVATE_NODE_PUBLIC_MASTER` for a private GKE cluster for the workspace. The GKE nodes
    will not have public IPs.
    
    Set to `PUBLIC_NODE_PUBLIC_MASTER` for a public GKE cluster. The nodes of a public GKE cluster
    have public IP addresses.

   .. py:attribute:: PRIVATE_NODE_PUBLIC_MASTER
      :value: "PRIVATE_NODE_PUBLIC_MASTER"

   .. py:attribute:: PUBLIC_NODE_PUBLIC_MASTER
      :value: "PUBLIC_NODE_PUBLIC_MASTER"

.. py:class:: KeyUseCase

   Possible values are: * `MANAGED_SERVICES`: Encrypts notebook and secret data in the control
    plane * `STORAGE`: Encrypts the workspace's root S3 bucket (root DBFS and system data) and,
    optionally, cluster EBS volumes.

   .. py:attribute:: MANAGED_SERVICES
      :value: "MANAGED_SERVICES"

   .. py:attribute:: STORAGE
      :value: "STORAGE"

.. autoclass:: Network
   :members:
   :undoc-members:

.. autoclass:: NetworkHealth
   :members:
   :undoc-members:

.. autoclass:: NetworkVpcEndpoints
   :members:
   :undoc-members:

.. autoclass:: NetworkWarning
   :members:
   :undoc-members:

.. py:class:: PricingTier

   The pricing tier of the workspace. For pricing tier information, see [AWS Pricing].
    
    [AWS Pricing]: https://databricks.com/product/aws-pricing

   .. py:attribute:: COMMUNITY_EDITION
      :value: "COMMUNITY_EDITION"

   .. py:attribute:: DEDICATED
      :value: "DEDICATED"

   .. py:attribute:: ENTERPRISE
      :value: "ENTERPRISE"

   .. py:attribute:: PREMIUM
      :value: "PREMIUM"

   .. py:attribute:: STANDARD
      :value: "STANDARD"

   .. py:attribute:: UNKNOWN
      :value: "UNKNOWN"

.. py:class:: PrivateAccessLevel

   The private access level controls which VPC endpoints can connect to the UI or API of any
    workspace that attaches this private access settings object. * `ACCOUNT` level access (the
    default) allows only VPC endpoints that are registered in your Databricks account connect to
    your workspace. * `ENDPOINT` level access allows only specified VPC endpoints connect to your
    workspace. For details, see `allowed_vpc_endpoint_ids`.

   .. py:attribute:: ACCOUNT
      :value: "ACCOUNT"

   .. py:attribute:: ENDPOINT
      :value: "ENDPOINT"

.. autoclass:: PrivateAccessSettings
   :members:
   :undoc-members:

.. autoclass:: RootBucketInfo
   :members:
   :undoc-members:

.. autoclass:: StorageConfiguration
   :members:
   :undoc-members:

.. autoclass:: StsRole
   :members:
   :undoc-members:

.. autoclass:: UpdateWorkspaceRequest
   :members:
   :undoc-members:

.. autoclass:: UpsertPrivateAccessSettingsRequest
   :members:
   :undoc-members:

.. autoclass:: VpcEndpoint
   :members:
   :undoc-members:

.. py:class:: VpcStatus

   The status of this network configuration object in terms of its use in a workspace: *
    `UNATTACHED`: Unattached. * `VALID`: Valid. * `BROKEN`: Broken. * `WARNED`: Warned.

   .. py:attribute:: BROKEN
      :value: "BROKEN"

   .. py:attribute:: UNATTACHED
      :value: "UNATTACHED"

   .. py:attribute:: VALID
      :value: "VALID"

   .. py:attribute:: WARNED
      :value: "WARNED"

.. py:class:: WarningType

   The AWS resource associated with this warning: a subnet or a security group.

   .. py:attribute:: SECURITY_GROUP
      :value: "SECURITY_GROUP"

   .. py:attribute:: SUBNET
      :value: "SUBNET"

.. autoclass:: Workspace
   :members:
   :undoc-members:

.. py:class:: WorkspaceStatus

   The status of the workspace. For workspace creation, usually it is set to `PROVISIONING`
    initially. Continue to check the status until the status is `RUNNING`.

   .. py:attribute:: BANNED
      :value: "BANNED"

   .. py:attribute:: CANCELLING
      :value: "CANCELLING"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: NOT_PROVISIONED
      :value: "NOT_PROVISIONED"

   .. py:attribute:: PROVISIONING
      :value: "PROVISIONING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

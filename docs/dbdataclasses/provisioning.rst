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

.. autoclass:: AzureKeyInfo
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

.. autoclass:: CreateCredentialStsRole
   :members:
   :undoc-members:

.. autoclass:: CreateGcpKeyInfo
   :members:
   :undoc-members:

.. autoclass:: Credential
   :members:
   :undoc-members:

.. py:class:: CustomerFacingComputeMode

   Corresponds to compute mode defined here: https://src.dev.databricks.com/databricks/universe@9076536b18479afd639d1c1f9dd5a59f72215e69/-/blob/central/api/common.proto?L872

   .. py:attribute:: HYBRID
      :value: "HYBRID"

   .. py:attribute:: SERVERLESS
      :value: "SERVERLESS"

.. autoclass:: CustomerFacingGcpCloudResourceContainer
   :members:
   :undoc-members:

.. py:class:: CustomerFacingStorageMode

   .. py:attribute:: CUSTOMER_HOSTED
      :value: "CUSTOMER_HOSTED"

   .. py:attribute:: DEFAULT_STORAGE
      :value: "DEFAULT_STORAGE"

.. autoclass:: CustomerManagedKey
   :members:
   :undoc-members:

.. py:class:: EndpointUseCase

   .. py:attribute:: DATAPLANE_RELAY_ACCESS
      :value: "DATAPLANE_RELAY_ACCESS"

   .. py:attribute:: WORKSPACE_ACCESS
      :value: "WORKSPACE_ACCESS"

.. py:class:: ErrorType

   ErrorType and WarningType are used to represent the type of error or warning by NetworkHealth and NetworkWarning defined in central/api/accounts/accounts.proto

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

.. autoclass:: GcpCommonNetworkConfig
   :members:
   :undoc-members:

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
   Set to `PRIVATE_NODE_PUBLIC_MASTER` for a private GKE cluster for the workspace. The GKE nodes will not have public IPs.
   Set to `PUBLIC_NODE_PUBLIC_MASTER` for a public GKE cluster. The nodes of a public GKE cluster have public IP addresses.

   .. py:attribute:: PRIVATE_NODE_PUBLIC_MASTER
      :value: "PRIVATE_NODE_PUBLIC_MASTER"

   .. py:attribute:: PUBLIC_NODE_PUBLIC_MASTER
      :value: "PUBLIC_NODE_PUBLIC_MASTER"

.. autoclass:: KeyAccessConfiguration
   :members:
   :undoc-members:

.. py:class:: KeyUseCase

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

.. autoclass:: VpcEndpoint
   :members:
   :undoc-members:

.. py:class:: VpcStatus

   .. py:attribute:: BROKEN
      :value: "BROKEN"

   .. py:attribute:: UNATTACHED
      :value: "UNATTACHED"

   .. py:attribute:: VALID
      :value: "VALID"

   .. py:attribute:: WARNED
      :value: "WARNED"

.. py:class:: WarningType

   .. py:attribute:: SECURITY_GROUP
      :value: "SECURITY_GROUP"

   .. py:attribute:: SUBNET
      :value: "SUBNET"

.. autoclass:: Workspace
   :members:
   :undoc-members:

.. autoclass:: WorkspaceNetwork
   :members:
   :undoc-members:

.. py:class:: WorkspaceStatus

   The different statuses of a workspace. The following represents the current set of valid transitions from status to status: NOT_PROVISIONED -> PROVISIONING -> CANCELLED PROVISIONING -> RUNNING -> FAILED -> CANCELLED (note that this transition is disallowed in the MultiWorkspace Project) RUNNING -> PROVISIONING -> BANNED -> CANCELLED FAILED -> PROVISIONING -> CANCELLED BANNED -> RUNNING -> CANCELLED Note that a transition from any state to itself is also valid. TODO(PLAT-5867): add a transition from CANCELLED to some other value (e.g. RECOVERING)

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

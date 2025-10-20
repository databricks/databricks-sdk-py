Apps
====

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.apps`` module.

.. py:currentmodule:: databricks.sdk.service.apps
.. autoclass:: App
   :members:
   :undoc-members:

.. autoclass:: AppAccessControlRequest
   :members:
   :undoc-members:

.. autoclass:: AppAccessControlResponse
   :members:
   :undoc-members:

.. autoclass:: AppDeployment
   :members:
   :undoc-members:

.. autoclass:: AppDeploymentArtifacts
   :members:
   :undoc-members:

.. py:class:: AppDeploymentMode

   .. py:attribute:: AUTO_SYNC
      :value: "AUTO_SYNC"

   .. py:attribute:: SNAPSHOT
      :value: "SNAPSHOT"

.. py:class:: AppDeploymentState

   .. py:attribute:: CANCELLED
      :value: "CANCELLED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: IN_PROGRESS
      :value: "IN_PROGRESS"

   .. py:attribute:: SUCCEEDED
      :value: "SUCCEEDED"

.. autoclass:: AppDeploymentStatus
   :members:
   :undoc-members:

.. autoclass:: AppManifest
   :members:
   :undoc-members:

.. autoclass:: AppManifestAppResourceJobSpec
   :members:
   :undoc-members:

.. py:class:: AppManifestAppResourceJobSpecJobPermission

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_MANAGE_RUN
      :value: "CAN_MANAGE_RUN"

   .. py:attribute:: CAN_VIEW
      :value: "CAN_VIEW"

   .. py:attribute:: IS_OWNER
      :value: "IS_OWNER"

.. autoclass:: AppManifestAppResourceSecretSpec
   :members:
   :undoc-members:

.. py:class:: AppManifestAppResourceSecretSpecSecretPermission

   Permission to grant on the secret scope. Supported permissions are: "READ", "WRITE", "MANAGE".

   .. py:attribute:: MANAGE
      :value: "MANAGE"

   .. py:attribute:: READ
      :value: "READ"

   .. py:attribute:: WRITE
      :value: "WRITE"

.. autoclass:: AppManifestAppResourceServingEndpointSpec
   :members:
   :undoc-members:

.. py:class:: AppManifestAppResourceServingEndpointSpecServingEndpointPermission

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_QUERY
      :value: "CAN_QUERY"

   .. py:attribute:: CAN_VIEW
      :value: "CAN_VIEW"

.. autoclass:: AppManifestAppResourceSpec
   :members:
   :undoc-members:

.. autoclass:: AppManifestAppResourceSqlWarehouseSpec
   :members:
   :undoc-members:

.. py:class:: AppManifestAppResourceSqlWarehouseSpecSqlWarehousePermission

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_USE
      :value: "CAN_USE"

   .. py:attribute:: IS_OWNER
      :value: "IS_OWNER"

.. autoclass:: AppManifestAppResourceUcSecurableSpec
   :members:
   :undoc-members:

.. py:class:: AppManifestAppResourceUcSecurableSpecUcSecurablePermission

   .. py:attribute:: MANAGE
      :value: "MANAGE"

   .. py:attribute:: READ_VOLUME
      :value: "READ_VOLUME"

   .. py:attribute:: WRITE_VOLUME
      :value: "WRITE_VOLUME"

.. py:class:: AppManifestAppResourceUcSecurableSpecUcSecurableType

   .. py:attribute:: VOLUME
      :value: "VOLUME"

.. autoclass:: AppPermission
   :members:
   :undoc-members:

.. py:class:: AppPermissionLevel

   Permission level

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_USE
      :value: "CAN_USE"

.. autoclass:: AppPermissions
   :members:
   :undoc-members:

.. autoclass:: AppPermissionsDescription
   :members:
   :undoc-members:

.. autoclass:: AppResource
   :members:
   :undoc-members:

.. autoclass:: AppResourceDatabase
   :members:
   :undoc-members:

.. py:class:: AppResourceDatabaseDatabasePermission

   .. py:attribute:: CAN_CONNECT_AND_CREATE
      :value: "CAN_CONNECT_AND_CREATE"

.. autoclass:: AppResourceGenieSpace
   :members:
   :undoc-members:

.. py:class:: AppResourceGenieSpaceGenieSpacePermission

   .. py:attribute:: CAN_EDIT
      :value: "CAN_EDIT"

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_RUN
      :value: "CAN_RUN"

   .. py:attribute:: CAN_VIEW
      :value: "CAN_VIEW"

.. autoclass:: AppResourceJob
   :members:
   :undoc-members:

.. py:class:: AppResourceJobJobPermission

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_MANAGE_RUN
      :value: "CAN_MANAGE_RUN"

   .. py:attribute:: CAN_VIEW
      :value: "CAN_VIEW"

   .. py:attribute:: IS_OWNER
      :value: "IS_OWNER"

.. autoclass:: AppResourceSecret
   :members:
   :undoc-members:

.. py:class:: AppResourceSecretSecretPermission

   Permission to grant on the secret scope. Supported permissions are: "READ", "WRITE", "MANAGE".

   .. py:attribute:: MANAGE
      :value: "MANAGE"

   .. py:attribute:: READ
      :value: "READ"

   .. py:attribute:: WRITE
      :value: "WRITE"

.. autoclass:: AppResourceServingEndpoint
   :members:
   :undoc-members:

.. py:class:: AppResourceServingEndpointServingEndpointPermission

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_QUERY
      :value: "CAN_QUERY"

   .. py:attribute:: CAN_VIEW
      :value: "CAN_VIEW"

.. autoclass:: AppResourceSqlWarehouse
   :members:
   :undoc-members:

.. py:class:: AppResourceSqlWarehouseSqlWarehousePermission

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_USE
      :value: "CAN_USE"

   .. py:attribute:: IS_OWNER
      :value: "IS_OWNER"

.. autoclass:: AppResourceUcSecurable
   :members:
   :undoc-members:

.. py:class:: AppResourceUcSecurableUcSecurablePermission

   .. py:attribute:: READ_VOLUME
      :value: "READ_VOLUME"

   .. py:attribute:: WRITE_VOLUME
      :value: "WRITE_VOLUME"

.. py:class:: AppResourceUcSecurableUcSecurableType

   .. py:attribute:: VOLUME
      :value: "VOLUME"

.. autoclass:: AppUpdate
   :members:
   :undoc-members:

.. autoclass:: AppUpdateUpdateStatus
   :members:
   :undoc-members:

.. py:class:: AppUpdateUpdateStatusUpdateState

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: IN_PROGRESS
      :value: "IN_PROGRESS"

   .. py:attribute:: NOT_UPDATED
      :value: "NOT_UPDATED"

   .. py:attribute:: SUCCEEDED
      :value: "SUCCEEDED"

.. py:class:: ApplicationState

   .. py:attribute:: CRASHED
      :value: "CRASHED"

   .. py:attribute:: DEPLOYING
      :value: "DEPLOYING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: UNAVAILABLE
      :value: "UNAVAILABLE"

.. autoclass:: ApplicationStatus
   :members:
   :undoc-members:

.. py:class:: ComputeSize

   .. py:attribute:: LARGE
      :value: "LARGE"

   .. py:attribute:: LIQUID
      :value: "LIQUID"

   .. py:attribute:: MEDIUM
      :value: "MEDIUM"

.. py:class:: ComputeState

   .. py:attribute:: ACTIVE
      :value: "ACTIVE"

   .. py:attribute:: DELETING
      :value: "DELETING"

   .. py:attribute:: ERROR
      :value: "ERROR"

   .. py:attribute:: STARTING
      :value: "STARTING"

   .. py:attribute:: STOPPED
      :value: "STOPPED"

   .. py:attribute:: STOPPING
      :value: "STOPPING"

   .. py:attribute:: UPDATING
      :value: "UPDATING"

.. autoclass:: ComputeStatus
   :members:
   :undoc-members:

.. autoclass:: CustomTemplate
   :members:
   :undoc-members:

.. autoclass:: GetAppPermissionLevelsResponse
   :members:
   :undoc-members:

.. autoclass:: ListAppDeploymentsResponse
   :members:
   :undoc-members:

.. autoclass:: ListAppsResponse
   :members:
   :undoc-members:

.. autoclass:: ListCustomTemplatesResponse
   :members:
   :undoc-members:

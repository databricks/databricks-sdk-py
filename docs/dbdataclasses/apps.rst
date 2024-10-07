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

.. autoclass:: AppPermissionsRequest
   :members:
   :undoc-members:

.. autoclass:: AppResource
   :members:
   :undoc-members:

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

.. autoclass:: CreateAppDeploymentRequest
   :members:
   :undoc-members:

.. autoclass:: CreateAppRequest
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

.. autoclass:: StartAppRequest
   :members:
   :undoc-members:

.. autoclass:: StopAppRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateAppRequest
   :members:
   :undoc-members:

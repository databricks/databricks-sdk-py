Bundle
======

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.bundle`` module.

.. py:currentmodule:: databricks.sdk.service.bundle
.. autoclass:: Deployment
   :members:
   :undoc-members:

.. py:class:: DeploymentMode

   Bundle target deployment mode. Mirrors the `mode` field on a bundle target in `databricks.yml` (see https://docs.databricks.com/dev-tools/bundles/deployment-modes).

   .. py:attribute:: DEPLOYMENT_MODE_DEVELOPMENT
      :value: "DEPLOYMENT_MODE_DEVELOPMENT"

   .. py:attribute:: DEPLOYMENT_MODE_PRODUCTION
      :value: "DEPLOYMENT_MODE_PRODUCTION"

.. py:class:: DeploymentResourceType

   Type of a deployment resource.

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_ALERT
      :value: "DEPLOYMENT_RESOURCE_TYPE_ALERT"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_APP
      :value: "DEPLOYMENT_RESOURCE_TYPE_APP"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_CATALOG
      :value: "DEPLOYMENT_RESOURCE_TYPE_CATALOG"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_CLUSTER
      :value: "DEPLOYMENT_RESOURCE_TYPE_CLUSTER"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_DASHBOARD
      :value: "DEPLOYMENT_RESOURCE_TYPE_DASHBOARD"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_DATABASE_CATALOG
      :value: "DEPLOYMENT_RESOURCE_TYPE_DATABASE_CATALOG"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_DATABASE_INSTANCE
      :value: "DEPLOYMENT_RESOURCE_TYPE_DATABASE_INSTANCE"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_EXPERIMENT
      :value: "DEPLOYMENT_RESOURCE_TYPE_EXPERIMENT"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_EXTERNAL_LOCATION
      :value: "DEPLOYMENT_RESOURCE_TYPE_EXTERNAL_LOCATION"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_JOB
      :value: "DEPLOYMENT_RESOURCE_TYPE_JOB"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_MODEL
      :value: "DEPLOYMENT_RESOURCE_TYPE_MODEL"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_MODEL_SERVING_ENDPOINT
      :value: "DEPLOYMENT_RESOURCE_TYPE_MODEL_SERVING_ENDPOINT"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_PIPELINE
      :value: "DEPLOYMENT_RESOURCE_TYPE_PIPELINE"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_POSTGRES_BRANCH
      :value: "DEPLOYMENT_RESOURCE_TYPE_POSTGRES_BRANCH"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_POSTGRES_ENDPOINT
      :value: "DEPLOYMENT_RESOURCE_TYPE_POSTGRES_ENDPOINT"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_POSTGRES_PROJECT
      :value: "DEPLOYMENT_RESOURCE_TYPE_POSTGRES_PROJECT"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_QUALITY_MONITOR
      :value: "DEPLOYMENT_RESOURCE_TYPE_QUALITY_MONITOR"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_REGISTERED_MODEL
      :value: "DEPLOYMENT_RESOURCE_TYPE_REGISTERED_MODEL"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_SCHEMA
      :value: "DEPLOYMENT_RESOURCE_TYPE_SCHEMA"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_SECRET_SCOPE
      :value: "DEPLOYMENT_RESOURCE_TYPE_SECRET_SCOPE"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_SQL_WAREHOUSE
      :value: "DEPLOYMENT_RESOURCE_TYPE_SQL_WAREHOUSE"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_SYNCED_DATABASE_TABLE
      :value: "DEPLOYMENT_RESOURCE_TYPE_SYNCED_DATABASE_TABLE"

   .. py:attribute:: DEPLOYMENT_RESOURCE_TYPE_VOLUME
      :value: "DEPLOYMENT_RESOURCE_TYPE_VOLUME"

.. py:class:: DeploymentStatus

   Status of a deployment.

   .. py:attribute:: DEPLOYMENT_STATUS_ACTIVE
      :value: "DEPLOYMENT_STATUS_ACTIVE"

   .. py:attribute:: DEPLOYMENT_STATUS_DELETED
      :value: "DEPLOYMENT_STATUS_DELETED"

   .. py:attribute:: DEPLOYMENT_STATUS_FAILED
      :value: "DEPLOYMENT_STATUS_FAILED"

   .. py:attribute:: DEPLOYMENT_STATUS_IN_PROGRESS
      :value: "DEPLOYMENT_STATUS_IN_PROGRESS"

.. autoclass:: HeartbeatResponse
   :members:
   :undoc-members:

.. autoclass:: ListDeploymentsResponse
   :members:
   :undoc-members:

.. autoclass:: ListOperationsResponse
   :members:
   :undoc-members:

.. autoclass:: ListResourcesResponse
   :members:
   :undoc-members:

.. autoclass:: ListVersionsResponse
   :members:
   :undoc-members:

.. autoclass:: Operation
   :members:
   :undoc-members:

.. py:class:: OperationActionType

   Type of action performed on a resource during a deployment.

   .. py:attribute:: OPERATION_ACTION_TYPE_BIND
      :value: "OPERATION_ACTION_TYPE_BIND"

   .. py:attribute:: OPERATION_ACTION_TYPE_BIND_AND_UPDATE
      :value: "OPERATION_ACTION_TYPE_BIND_AND_UPDATE"

   .. py:attribute:: OPERATION_ACTION_TYPE_CREATE
      :value: "OPERATION_ACTION_TYPE_CREATE"

   .. py:attribute:: OPERATION_ACTION_TYPE_DELETE
      :value: "OPERATION_ACTION_TYPE_DELETE"

   .. py:attribute:: OPERATION_ACTION_TYPE_INITIAL_REGISTER
      :value: "OPERATION_ACTION_TYPE_INITIAL_REGISTER"

   .. py:attribute:: OPERATION_ACTION_TYPE_RECREATE
      :value: "OPERATION_ACTION_TYPE_RECREATE"

   .. py:attribute:: OPERATION_ACTION_TYPE_RESIZE
      :value: "OPERATION_ACTION_TYPE_RESIZE"

   .. py:attribute:: OPERATION_ACTION_TYPE_UPDATE
      :value: "OPERATION_ACTION_TYPE_UPDATE"

   .. py:attribute:: OPERATION_ACTION_TYPE_UPDATE_WITH_ID
      :value: "OPERATION_ACTION_TYPE_UPDATE_WITH_ID"

.. py:class:: OperationStatus

   Status of a resource operation.

   .. py:attribute:: OPERATION_STATUS_FAILED
      :value: "OPERATION_STATUS_FAILED"

   .. py:attribute:: OPERATION_STATUS_SUCCEEDED
      :value: "OPERATION_STATUS_SUCCEEDED"

.. autoclass:: Resource
   :members:
   :undoc-members:

.. autoclass:: Version
   :members:
   :undoc-members:

.. py:class:: VersionComplete

   Reason why a version was completed.

   .. py:attribute:: VERSION_COMPLETE_FAILURE
      :value: "VERSION_COMPLETE_FAILURE"

   .. py:attribute:: VERSION_COMPLETE_FORCE_ABORT
      :value: "VERSION_COMPLETE_FORCE_ABORT"

   .. py:attribute:: VERSION_COMPLETE_LEASE_EXPIRED
      :value: "VERSION_COMPLETE_LEASE_EXPIRED"

   .. py:attribute:: VERSION_COMPLETE_SUCCESS
      :value: "VERSION_COMPLETE_SUCCESS"

.. py:class:: VersionStatus

   Status of a version.

   .. py:attribute:: VERSION_STATUS_COMPLETED
      :value: "VERSION_STATUS_COMPLETED"

   .. py:attribute:: VERSION_STATUS_IN_PROGRESS
      :value: "VERSION_STATUS_IN_PROGRESS"

.. py:class:: VersionType

   Type of version.

   .. py:attribute:: VERSION_TYPE_DEPLOY
      :value: "VERSION_TYPE_DEPLOY"

   .. py:attribute:: VERSION_TYPE_DESTROY
      :value: "VERSION_TYPE_DESTROY"
